"""Drafts WhatsApp replies and conversation summaries with Claude."""

import json
import logging
from dataclasses import dataclass

import anthropic

from . import config

log = logging.getLogger(__name__)

REPLY_SCHEMA = {
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["patient", "personal"]},
        "reply": {"type": "string"},
        "needs_owner": {"type": "boolean"},
        "skip": {"type": "boolean"},
        "reason": {"type": "string"},
        "summary": {"type": "string"},
    },
    "required": ["category", "reply", "needs_owner", "skip", "reason", "summary"],
    "additionalProperties": False,
}

SUMMARY_SYSTEM = (
    "You summarize WhatsApp conversations that Dr. Alaa's AI assistant handled while the doctor, "
    "an orthopaedic surgeon in Jordan, was busy. Write in English for the doctor. Keep two sections, "
    "'Patients' and 'Personal'. For each contact give one or two short lines: what they wanted, what the "
    "assistant replied, and what the doctor still needs to do. Put anything urgent or flagged first and "
    "mark it URGENT. No medical advice, no extra commentary."
)


@dataclass
class Draft:
    reply: str
    needs_owner: bool
    skip: bool
    reason: str
    category: str = "personal"
    summary: str = ""


_client = None


def client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    return _client


def system_prompt() -> str:
    # Read on every call so edits to the agent files apply without a restart.
    instructions = config.INSTRUCTIONS_PATH.read_text(encoding="utf-8")
    knowledge = config.KNOWLEDGE_PATH.read_text(encoding="utf-8") if config.KNOWLEDGE_PATH.exists() else ""
    return f"{instructions}\n\n---\n\n{knowledge}"


def build_messages(contact_name, history) -> list[dict]:
    """Turn the chat history into one user turn.

    The whole chat goes in as a transcript rather than alternating roles, so the
    contact's words are clearly data to respond to, not instructions to Claude.
    """
    who = contact_name or "the contact"
    lines = []
    for row in history:
        speaker = "Dr. Alaa's side" if row["direction"] == "out" else who
        lines.append(f"{speaker}: {row['body']}")
    transcript = "\n".join(lines)
    return [
        {
            "role": "user",
            "content": (
                f"WhatsApp chat with {who}. The last line is the newest message.\n\n"
                f"<chat>\n{transcript}\n</chat>\n\n"
                "Classify the newest message and draft the reply, following your instructions."
            ),
        }
    ]


def _create(**kwargs):
    return client().beta.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=16000,
        # If a safety classifier declines, Anthropic retries on a recommended fallback model.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        **kwargs,
    )


def draft_reply(contact_name, history) -> Draft:
    response = _create(
        system=system_prompt(),
        messages=build_messages(contact_name, history),
        output_config={
            "effort": config.CLAUDE_EFFORT,
            "format": {"type": "json_schema", "schema": REPLY_SCHEMA},
        },
    )
    if response.stop_reason == "refusal":
        return Draft("", True, False, "Claude declined to draft this one; please reply yourself.")
    if response.stop_reason == "max_tokens":
        return Draft("", True, False, "The draft was cut off; please reply yourself.")
    text = next((b.text for b in response.content if b.type == "text"), "")
    data = json.loads(text)
    return Draft(
        data["reply"].strip(),
        bool(data["needs_owner"]),
        bool(data["skip"]),
        data["reason"].strip(),
        data["category"],
        data["summary"].strip(),
    )


def summarize(conversations: list[dict]) -> str:
    """conversations: [{name, category, flagged, messages: [(direction, body), ...]}, ...]"""
    if not conversations:
        return "No conversations in this period."
    blocks = []
    for c in conversations:
        lines = "\n".join(
            f"{'Assistant' if d == 'out' else c['name']}: {b}" for d, b in c["messages"]
        )
        flag = " (flagged for the doctor)" if c["flagged"] else ""
        blocks.append(f"<conversation contact=\"{c['name']}\" category=\"{c['category']}\"{flag}>\n{lines}\n</conversation>")
    response = _create(
        system=SUMMARY_SYSTEM,
        messages=[{"role": "user", "content": "\n\n".join(blocks) + "\n\nSummarize these conversations."}],
        output_config={"effort": config.CLAUDE_EFFORT},
    )
    if response.stop_reason == "refusal":
        return "Claude declined to summarize these conversations."
    return "".join(b.text for b in response.content if b.type == "text").strip()
