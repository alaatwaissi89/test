"""Drafts a WhatsApp reply with Claude."""

import json
import logging
from dataclasses import dataclass

import anthropic

from . import config

log = logging.getLogger(__name__)

REPLY_SCHEMA = {
    "type": "object",
    "properties": {
        "reply": {"type": "string"},
        "needs_owner": {"type": "boolean"},
        "skip": {"type": "boolean"},
        "reason": {"type": "string"},
    },
    "required": ["reply", "needs_owner", "skip", "reason"],
    "additionalProperties": False,
}


@dataclass
class Draft:
    reply: str
    needs_owner: bool
    skip: bool
    reason: str


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
        speaker = "Alaa" if row["direction"] == "out" else who
        lines.append(f"{speaker}: {row['body']}")
    transcript = "\n".join(lines)
    return [
        {
            "role": "user",
            "content": (
                f"WhatsApp chat with {who}. The last line is the newest message.\n\n"
                f"<chat>\n{transcript}\n</chat>\n\n"
                "Draft Alaa's reply to the newest message, following your instructions."
            ),
        }
    ]


def draft_reply(contact_name, history) -> Draft:
    response = client().beta.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=16000,
        system=system_prompt(),
        messages=build_messages(contact_name, history),
        output_config={
            "effort": config.CLAUDE_EFFORT,
            "format": {"type": "json_schema", "schema": REPLY_SCHEMA},
        },
        # If a safety classifier declines, Anthropic retries on a recommended fallback model.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        return Draft("", True, False, "Claude declined to draft this one; please reply yourself.")
    if response.stop_reason == "max_tokens":
        return Draft("", True, False, "The draft was cut off; please reply yourself.")
    text = next((b.text for b in response.content if b.type == "text"), "")
    data = json.loads(text)
    return Draft(data["reply"].strip(), bool(data["needs_owner"]), bool(data["skip"]), data["reason"].strip())
