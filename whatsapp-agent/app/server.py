"""Webhook service + approval dashboard for the WhatsApp assistant.

Run locally:  python -m app.server        (from the whatsapp-agent folder)
Production:   gunicorn -w 1 -b 0.0.0.0:$PORT app.server:app
"""

import hashlib
import hmac
import logging
import threading
from functools import wraps
from html import escape

from flask import Flask, Response, abort, redirect, request

from . import brain, config, whatsapp
from .store import Store

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("whatsapp-agent")

app = Flask(__name__)
store = Store(config.DB_PATH)
_lock = threading.Lock()


# ---------------------------------------------------------------- webhook

@app.get("/webhook")
def verify():
    """Meta calls this once when you register the webhook URL."""
    if (
        request.args.get("hub.mode") == "subscribe"
        and config.WHATSAPP_VERIFY_TOKEN
        and request.args.get("hub.verify_token") == config.WHATSAPP_VERIFY_TOKEN
    ):
        return request.args.get("hub.challenge", "")
    abort(403)


@app.post("/webhook")
def incoming():
    raw = request.get_data()
    if not whatsapp.signature_ok(raw, request.headers.get("X-Hub-Signature-256")):
        abort(401)
    for msg in whatsapp.parse_incoming(request.get_json(silent=True) or {}):
        # Answer Meta quickly; draft in the background.
        threading.Thread(target=handle_message, args=(msg,), daemon=True).start()
    return "ok"


def handle_message(msg: dict) -> int | None:
    """Store an incoming message, draft a reply, and send or queue it. Returns the draft id."""
    with _lock:
        in_id = store.add_message(msg["wa_id"], msg["name"], "in", msg["text"], msg["message_id"])
        if in_id is None:
            return None  # duplicate webhook delivery
        history = store.history(msg["wa_id"], config.HISTORY_MESSAGES)
    try:
        d = brain.draft_reply(msg["name"], history)
    except Exception as exc:  # keep the service up; show the failure on the dashboard
        log.exception("drafting failed")
        d = brain.Draft("", True, False, f"Drafting failed: {exc}")

    with _lock:
        if d.skip:
            return store.add_draft(msg["wa_id"], msg["name"], in_id, "", False, d.reason, status="skipped")
        draft_id = store.add_draft(msg["wa_id"], msg["name"], in_id, d.reply, d.needs_owner, d.reason)

    if config.REPLY_MODE == "auto" and not d.needs_owner and d.reply:
        send_draft(draft_id, d.reply)
    return draft_id


def send_draft(draft_id: int, text: str) -> None:
    draft = store.get_draft(draft_id)
    try:
        whatsapp.send_text(draft["wa_id"], text)
    except Exception as exc:
        log.exception("send failed")
        store.update_draft(draft_id, status="error", error=str(exc), reply=text)
        return
    with _lock:
        store.add_message(draft["wa_id"], draft["contact_name"], "out", text)
        store.update_draft(draft_id, status="sent", reply=text, error=None)


# ---------------------------------------------------------------- dashboard

def _csrf() -> str:
    return hmac.new(config.DASHBOARD_PASSWORD.encode(), b"csrf", hashlib.sha256).hexdigest()


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if not config.DASHBOARD_PASSWORD:
            return Response("Set DASHBOARD_PASSWORD to use the dashboard.", 503)
        auth = request.authorization
        if not auth or not hmac.compare_digest(auth.password or "", config.DASHBOARD_PASSWORD):
            return Response("Login required", 401, {"WWW-Authenticate": 'Basic realm="WhatsApp assistant"'})
        if request.method == "POST" and not hmac.compare_digest(request.form.get("csrf", ""), _csrf()):
            abort(403)
        return view(*args, **kwargs)

    return wrapper


PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WhatsApp assistant</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:760px;margin:0 auto;padding:16px;background:#f6f7f8;color:#111}}
.card{{background:#fff;border-radius:10px;padding:14px;margin:12px 0;box-shadow:0 1px 3px #0002}}
.in{{background:#eef;padding:8px;border-radius:8px;white-space:pre-wrap}}
textarea{{width:100%;min-height:70px;font:inherit;box-sizing:border-box;margin:8px 0}}
.flag{{color:#a40;font-weight:600}} .muted{{color:#666;font-size:.9em}}
button{{padding:6px 14px;margin-right:6px}} nav a{{margin-right:12px}}
</style></head><body>
<h1>WhatsApp assistant</h1>
<p class="muted">Mode: <b>{mode}</b> · Dry run: <b>{dry}</b></p>
<nav><a href="/">Waiting for you</a><a href="/?status=all">History</a></nav>
{body}
</body></html>"""


def _card(d) -> str:
    incoming = escape(store.incoming_text(d["in_message_id"]))
    who = escape(d["contact_name"] or d["wa_id"])
    flag = '<span class="flag">Needs you</span> · ' if d["needs_owner"] else ""
    reason = escape(d["reason"] or "")
    err = f'<p class="flag">Error: {escape(d["error"])}</p>' if d["error"] else ""
    if d["status"] in ("pending", "error"):
        actions = f"""<form method="post" action="/drafts/{d['id']}">
<input type="hidden" name="csrf" value="{_csrf()}">
<textarea name="reply" dir="auto">{escape(d['reply'])}</textarea>
<button name="action" value="send">Send</button><button name="action" value="reject">Don't send</button>
</form>"""
    else:
        actions = f'<p dir="auto"><b>{escape(d["status"])}</b>: {escape(d["reply"])}</p>'
    return f"""<div class="card"><div class="muted">{flag}{who} (+{escape(d['wa_id'])})</div>
<div class="in" dir="auto">{incoming}</div><p class="muted">{reason}</p>{err}{actions}</div>"""


@app.get("/")
@login_required
def dashboard():
    if request.args.get("status") == "all":
        rows = store.drafts()
    else:
        rows = [*store.drafts("pending"), *store.drafts("error")]
    body = "".join(_card(d) for d in rows) or "<p>Nothing waiting. 🎉</p>"
    return PAGE.format(mode=config.REPLY_MODE, dry="on" if config.DRY_RUN else "off", body=body)


@app.post("/drafts/<int:draft_id>")
@login_required
def act(draft_id: int):
    draft = store.get_draft(draft_id)
    if not draft or draft["status"] not in ("pending", "error"):
        abort(404)
    if request.form.get("action") == "send":
        text = request.form.get("reply", "").strip()
        if text:
            send_draft(draft_id, text)
    else:
        store.update_draft(draft_id, status="rejected")
    return redirect("/")


@app.get("/health")
def health():
    return {"ok": True, "mode": config.REPLY_MODE, "dry_run": config.DRY_RUN}


if __name__ == "__main__":
    import os

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
