"""WhatsApp Business Cloud API: parse incoming webhooks, verify signatures, send text."""

import hashlib
import hmac
import logging

import requests

from . import config

log = logging.getLogger(__name__)


def signature_ok(raw_body: bytes, header: str | None) -> bool:
    """Check Meta's X-Hub-Signature-256 header against META_APP_SECRET."""
    if not config.META_APP_SECRET:
        log.warning("META_APP_SECRET is not set; webhook signatures are NOT being checked")
        return True
    if not header or not header.startswith("sha256="):
        return False
    expected = hmac.new(config.META_APP_SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header.removeprefix("sha256="))


def parse_incoming(payload: dict) -> list[dict]:
    """Pull the incoming messages out of a webhook payload.

    Returns a list of {wa_id, name, text, message_id}. Status updates (sent,
    delivered, read) are ignored. Non-text messages get a short placeholder so
    the assistant knows something arrived.
    """
    out = []
    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            names = {c.get("wa_id"): c.get("profile", {}).get("name") for c in value.get("contacts", [])}
            for msg in value.get("messages", []):
                kind = msg.get("type")
                if kind == "text":
                    text = msg["text"]["body"]
                elif kind == "button":
                    text = msg["button"].get("text", "")
                elif kind == "interactive":
                    inter = msg["interactive"]
                    text = (inter.get("button_reply") or inter.get("list_reply") or {}).get("title", "")
                elif kind == "reaction":
                    continue
                else:
                    caption = (msg.get(kind) or {}).get("caption", "") if isinstance(msg.get(kind), dict) else ""
                    text = f"[{kind} received]" + (f" {caption}" if caption else "")
                out.append(
                    {
                        "wa_id": msg["from"],
                        "name": names.get(msg["from"]),
                        "text": text,
                        "message_id": msg.get("id"),
                    }
                )
    return out


def send_text(to: str, body: str) -> dict:
    """Send a text message. With DRY_RUN on, only logs it."""
    if config.DRY_RUN:
        log.info("DRY_RUN: would send to %s: %s", to, body)
        return {"dry_run": True}
    if not (config.WHATSAPP_TOKEN and config.WHATSAPP_PHONE_NUMBER_ID):
        raise RuntimeError("WHATSAPP_TOKEN and WHATSAPP_PHONE_NUMBER_ID must be set to send messages")
    url = f"https://graph.facebook.com/{config.GRAPH_API_VERSION}/{config.WHATSAPP_PHONE_NUMBER_ID}/messages"
    resp = requests.post(
        url,
        headers={"Authorization": f"Bearer {config.WHATSAPP_TOKEN}"},
        json={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {"preview_url": False, "body": body},
        },
        timeout=20,
    )
    if resp.status_code >= 400:
        raise RuntimeError(f"WhatsApp API error {resp.status_code}: {resp.text[:500]}")
    return resp.json()
