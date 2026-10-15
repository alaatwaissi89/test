"""Settings, read from environment variables (or a .env file next to app/)."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
except ImportError:
    pass


def _bool(name: str, default: bool) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


# WhatsApp Business Cloud API (Meta)
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN", "")
WHATSAPP_PHONE_NUMBER_ID = os.environ.get("WHATSAPP_PHONE_NUMBER_ID", "")
WHATSAPP_VERIFY_TOKEN = os.environ.get("WHATSAPP_VERIFY_TOKEN", "")
META_APP_SECRET = os.environ.get("META_APP_SECRET", "")
GRAPH_API_VERSION = os.environ.get("GRAPH_API_VERSION", "v21.0")

# Claude
CLAUDE_MODEL = os.environ.get("AGENT_MODEL", "claude-opus-5-5")
CLAUDE_EFFORT = os.environ.get("AGENT_EFFORT", "low")

# Behaviour
# Busy mode (switched on the dashboard) sends every reply on its own while you're busy.
# When you're not busy, REPLY_MODE decides:
# approve: every draft waits for you on the dashboard (default)
# auto:    send drafts automatically, except ones flagged needs_owner
REPLY_MODE = os.environ.get("REPLY_MODE", "approve").strip().lower()

# Told to each contact at the start of a conversation (first reply, or after NOTICE_GAP_HOURS of quiet).
AI_NOTICE_AR = os.environ.get(
    "AI_NOTICE_AR", "🤖 معك المساعد الذكي (AI) تبع د. علاء. الدكتور بشوف الرسائل وبرد عليك بأقرب وقت إن شاء الله."
)
AI_NOTICE_EN = os.environ.get(
    "AI_NOTICE_EN", "🤖 This is Dr. Alaa's AI assistant. The doctor sees these messages and will follow up."
)
NOTICE_GAP_HOURS = float(os.environ.get("NOTICE_GAP_HOURS", "24"))
# DRY_RUN=true logs what would be sent instead of calling WhatsApp. On by default.
DRY_RUN = _bool("DRY_RUN", True)
HISTORY_MESSAGES = int(os.environ.get("HISTORY_MESSAGES", "20"))

# Dashboard login (Basic auth password; username is anything)
DASHBOARD_PASSWORD = os.environ.get("DASHBOARD_PASSWORD", "")

DB_PATH = os.environ.get("DB_PATH", str(ROOT / "data" / "whatsapp-agent.db"))
INSTRUCTIONS_PATH = ROOT / "agent" / "whatsapp-assistant.md"
KNOWLEDGE_PATH = ROOT / "agent" / "knowledge.md"
