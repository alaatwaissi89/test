"""Webhook service + dashboard for Dr. Alaa's WhatsApp assistant.

Run locally:  python -m app.server        (from the whatsapp-agent folder)
Production:   gunicorn -w 1 --threads 4 -b 0.0.0.0:$PORT app.server:app
"""

import hashlib
import hmac
import logging
import re
import threading
import time
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
ARABIC = re.compile(r"[؀-ۿ]")


# ---------------------------------------------------------------- busy mode

def is_busy() -> bool:
    return store.get_setting("busy") == "1"


def set_busy(on: bool) -> None:
    now = time.time()
    if on and not is_busy():
        store.set_setting("busy_since", now)
        store.set_setting("busy_until", None)
    elif not on and is_busy():
        store.set_setting("busy_until", now)
    store.set_setting("busy", "1" if on else "0")


def should_send(d: brain.Draft) -> bool:
    if not d.reply:
        return False
    if is_busy():
        # While busy, every reply goes out. Drafts that need the doctor are written as
        # holding replies ("the doctor will get back to you") and are listed on the summary page.
        return True
    return config.REPLY_MODE == "auto" and not d.needs_owner


# ---------------------------------------------------------------- AI notice

def with_ai_notice(wa_id: str, reply: str) -> str:
    """Prefix the 'this is an AI assistant' notice at the start of a conversation."""
    last = store.last_outgoing_at(wa_id)
    if last and time.time() - last < config.NOTICE_GAP_HOURS * 3600:
        return reply
    notice = config.AI_NOTICE_AR if ARABIC.search(reply) else config.AI_NOTICE_EN
    return f"{notice}\n\n{reply}"


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
            return store.add_draft(msg["wa_id"], msg["name"], in_id, "", False, d.reason,
                                   d.category, d.summary, status="skipped")
        reply = with_ai_notice(msg["wa_id"], d.reply) if d.reply else ""
        draft_id = store.add_draft(msg["wa_id"], msg["name"], in_id, reply, d.needs_owner, d.reason,
                                   d.category, d.summary)

    if should_send(d):
        send_draft(draft_id, reply)
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
textarea{{width:100%;min-height:90px;font:inherit;box-sizing:border-box;margin:8px 0}}
.flag{{color:#a40;font-weight:600}} .muted{{color:#666;font-size:.9em}}
.tag{{display:inline-block;padding:1px 8px;border-radius:9px;font-size:.8em;background:#e5e7eb}}
.patient{{background:#dbeafe}} .personal{{background:#fce7f3}}
button{{padding:6px 14px;margin-right:6px}} nav a{{margin-right:12px}}
.busy{{padding:10px 14px;border-radius:10px;margin:10px 0;background:{busy_bg}}}
pre{{white-space:pre-wrap;font:inherit}}
</style></head><body>
<h1>WhatsApp assistant</h1>
<form method="post" action="/busy" class="busy"><input type="hidden" name="csrf" value="{csrf}">
<b>{busy_text}</b> <button name="on" value="{busy_next}">{busy_button}</button></form>
<p class="muted">When not busy: <b>{mode}</b> · Dry run: <b>{dry}</b></p>
<nav><a href="/?category=patient">Patients</a><a href="/?category=personal">Personal</a>
<a href="/summary">Summary</a><a href="/?status=all">History</a></nav>
{body}
</body></html>"""


def _page(body: str) -> str:
    busy = is_busy()
    return PAGE.format(
        csrf=_csrf(),
        busy_bg="#fde68a" if busy else "#e5e7eb",
        busy_text="Busy: the assistant is replying on its own." if busy
        else "Not busy: replies wait for you here.",
        busy_next="0" if busy else "1",
        busy_button="I'm back" if busy else "I'm busy",
        mode=config.REPLY_MODE,
        dry="on (nothing is really sent)" if config.DRY_RUN else "off",
        body=body,
    )


def _card(d) -> str:
    incoming = escape(store.incoming_text(d["in_message_id"]))
    who = escape(d["contact_name"] or d["wa_id"])
    cat = escape(d["category"] or "personal")
    flag = ' · <span class="flag">Needs you</span>' if d["needs_owner"] else ""
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
    return f"""<div class="card"><div class="muted"><span class="tag {cat}">{cat}</span> {who} (+{escape(d['wa_id'])}){flag}</div>
<div class="in" dir="auto">{incoming}</div><p class="muted">{reason}</p>{err}{actions}</div>"""


@app.get("/")
@login_required
def dashboard():
    category = request.args.get("category") or "patient"
    if request.args.get("status") == "all":
        rows = store.drafts()
        title = "<h2>History</h2>"
    else:
        rows = [*store.drafts("pending", category), *store.drafts("error", category)]
        title = f"<h2>{'Patients' if category == 'patient' else 'Personal'}: waiting for you</h2>"
    body = title + ("".join(_card(d) for d in rows) or "<p>Nothing waiting. 🎉</p>")
    return _page(body)


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
    return redirect(f"/?category={draft['category']}")


@app.post("/busy")
@login_required
def busy_toggle():
    set_busy(request.form.get("on") == "1")
    return redirect("/summary" if not is_busy() else "/")


def summary_window() -> tuple[float, float, str]:
    """The busy period (current or last one), or the last 24 hours if there was none."""
    now = time.time()
    hours = request.args.get("hours")
    since = store.get_setting("busy_since")
    if hours:
        return now - float(hours) * 3600, now, f"the last {hours} hours"
    if is_busy() and since:
        return float(since), now, "since you went busy"
    until = store.get_setting("busy_until")
    if since and until:
        return float(since), float(until), "while you were busy"
    return now - 24 * 3600, now, "the last 24 hours"


def conversations_in(start: float, end: float) -> list[dict]:
    by_contact: dict[str, dict] = {}
    for d in store.drafts_between(start, end):
        c = by_contact.setdefault(d["wa_id"], {
            "wa_id": d["wa_id"], "name": d["contact_name"] or d["wa_id"], "category": d["category"],
            "flagged": False, "lines": [],
        })
        if d["category"] == "patient":
            c["category"] = "patient"
        c["flagged"] = c["flagged"] or bool(d["needs_owner"])
        if d["summary"]:
            c["lines"].append(d["summary"])
    for c in by_contact.values():
        c["messages"] = [(m["direction"], m["body"]) for m in store.messages_between(c["wa_id"], start, end)]
    return sorted(by_contact.values(), key=lambda c: (c["category"] != "patient", not c["flagged"]))


@app.route("/summary", methods=["GET", "POST"])
@login_required
def summary():
    start, end, label = summary_window()
    convs = conversations_in(start, end)
    parts = [f"<h2>Summary of {escape(label)}</h2>",
             f"<p class='muted'>{len(convs)} conversation(s). Patients and anything that needs you come first.</p>"]
    if request.method == "POST":
        try:
            parts.append(f"<div class='card'><pre dir='auto'>{escape(brain.summarize(convs))}</pre></div>")
        except Exception as exc:
            log.exception("summary failed")
            parts.append(f"<p class='flag'>Summary failed: {escape(str(exc))}</p>")
    elif convs:
        parts.append(f"""<form method="post"><input type="hidden" name="csrf" value="{_csrf()}">
<button>Write a short summary with Claude</button></form>""")
    for c in convs:
        flag = ' · <span class="flag">Needs you</span>' if c["flagged"] else ""
        items = "".join(f"<li>{escape(s)}</li>" for s in c["lines"]) or "<li>(no notes)</li>"
        parts.append(f"""<div class="card"><div class="muted"><span class="tag {escape(c['category'])}">{escape(c['category'])}</span>
{escape(c['name'])} (+{escape(c['wa_id'])}){flag}</div><ul>{items}</ul></div>""")
    return _page("".join(parts))


@app.get("/health")
def health():
    return {"ok": True, "busy": is_busy(), "mode": config.REPLY_MODE, "dry_run": config.DRY_RUN}


if __name__ == "__main__":
    import os

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
