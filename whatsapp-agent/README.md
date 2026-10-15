# WhatsApp Assistant Agent

An agent that reads the WhatsApp messages people send you, drafts a reply with
Claude in your voice (Arabic or English), and sends it after you approve it.

```
Contact ──WhatsApp──▶ Meta Cloud API ──webhook──▶ this service ──▶ Claude drafts a reply
                                                       │
                                     you approve on the dashboard (or auto mode)
                                                       ▼
Contact ◀──WhatsApp── Meta Cloud API ◀──────────── send reply
```

## Important: which WhatsApp number this works with

- **Personal WhatsApp has no official API.** Tools that "log in" to a personal
  account by scanning a QR code break WhatsApp's terms and get numbers banned,
  so this agent does not use them.
- This agent uses the **official WhatsApp Business Cloud API** from Meta. It
  needs a phone number registered to the API. That can be a new number (best),
  or your existing number moved off the WhatsApp app. A number on the Cloud API
  can no longer be used in the normal WhatsApp or WhatsApp Business phone app.
- WhatsApp only allows free-form replies within **24 hours** of the contact's
  last message. That fits this agent, which only replies to incoming messages.

## Files

| Path | What it is |
|---|---|
| `agent/whatsapp-assistant.md` | The agent's instructions: tone, languages, what it may and must never do. Edit freely. |
| `agent/knowledge.md` | Facts about you the agent is allowed to use in replies. Fill this in. |
| `app/server.py` | Webhook that receives messages, plus the approval dashboard. |
| `app/brain.py` | Calls Claude to draft each reply. |
| `app/whatsapp.py` | Checks Meta's signature on webhooks and sends messages. |
| `app/store.py` | Small SQLite database of chats and drafts. |
| `tests/test_flow.py` | Tests with fake Claude and fake WhatsApp (nothing is sent). |
| `.env.example` | Every setting and credential, with where to find it. |

## Safety defaults

- `REPLY_MODE=approve`: every draft waits on the dashboard until you press
  **Send** (you can edit the text first) or **Don't send**.
- `DRY_RUN=true`: even approved replies are only logged, not sent. Turn it off
  when you're ready to go live.
- In `auto` mode, drafts the agent flags as needing you (money, meetings,
  commitments, anything it doesn't know) still wait for you.
- Verification codes, bank alerts and automated messages are skipped.
- Webhooks without a valid Meta signature are rejected; the dashboard is
  password protected.

## What you need (credentials)

| Setting | Where to get it |
|---|---|
| `ANTHROPIC_API_KEY` | platform.claude.com → API keys |
| Meta developer app | developers.facebook.com → Create app → type "Business" → add the **WhatsApp** product |
| `WHATSAPP_PHONE_NUMBER_ID` | Your app → WhatsApp → API Setup → "Phone number ID" |
| `WHATSAPP_TOKEN` | Temporary token on the API Setup page for testing; for real use, a permanent token from a **System User** in Meta Business Settings with `whatsapp_business_messaging` permission |
| `META_APP_SECRET` | Your app → App settings → Basic → App secret |
| `WHATSAPP_VERIFY_TOKEN` | Any random string you make up |
| `DASHBOARD_PASSWORD` | Any strong password you make up |
| Hosting | Any service that runs a Python web app on a public HTTPS URL (Render, Railway, Fly.io, a VPS). A `Procfile` is included. |

Put these in the hosting service's environment-variable settings, or in a
`.env` file copied from `.env.example` when running on your own machine. Never
commit `.env`.

## Setup, step by step

1. **Fill in the agent**: edit `agent/knowledge.md` with what the assistant may
   say about you, and adjust `agent/whatsapp-assistant.md` if you want a
   different tone or rules.
2. **Create the Meta app** and add WhatsApp (see the table above). Meta gives
   you a free test number; add your own phone as a test recipient to try it.
3. **Deploy this folder** to your host with the environment variables set
   (keep `DRY_RUN=true` at first). Start command:
   `gunicorn -w 1 --threads 4 -b 0.0.0.0:$PORT app.server:app`
4. **Register the webhook** in Meta: your app → WhatsApp → Configuration →
   Webhook. Callback URL `https://YOUR-HOST/webhook`, verify token =
   your `WHATSAPP_VERIFY_TOKEN`. Then subscribe to the **messages** field.
5. **Test**: send a WhatsApp message to the business number. Open
   `https://YOUR-HOST/` (log in with any username and your dashboard
   password) and you'll see the incoming message and Claude's draft.
6. **Go live**: when the drafts look right, set `DRY_RUN=false`. Later, if you
   trust it, set `REPLY_MODE=auto`.

## Run and test locally

```bash
cd whatsapp-agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt pytest
python -m pytest -q          # fake Claude + fake WhatsApp, nothing sent
cp .env.example .env         # fill in, then:
python -m app.server         # http://localhost:8000
```

To receive real webhooks on your own computer, expose port 8000 with a tunnel
such as `ngrok http 8000` and use that HTTPS URL in step 4.

## Cost

Each incoming message is one Claude call (`claude-opus-5-5`, low effort by
default). WhatsApp service conversations started by the customer are free on
Meta's current pricing; check Meta's pricing page for your country.
