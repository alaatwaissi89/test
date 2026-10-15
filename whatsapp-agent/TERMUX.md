# Running the WhatsApp agent on Android with Termux

Install Termux from F-Droid or GitHub, not the Play Store, because the Play
Store version is outdated and its package installs fail.

## 1. Install the tools

```bash
pkg update && pkg upgrade -y
pkg install -y python git rust binutils cloudflared
```

`rust` is needed because two of the Claude SDK's libraries (pydantic-core and
jiter) have no ready-made Android builds, so pip compiles them. The first
install can take 10 to 20 minutes.

## 2. Get the code

```bash
cd ~
git clone -b claude/project-thread-4npwlw https://github.com/alaatwaissi89/test.git
cd test/whatsapp-agent
```

If the repository is private, git asks for a username and password. Use your
GitHub username, and for the password a personal access token from GitHub →
Settings → Developer settings → Personal access tokens. Your normal password
won't work there.

## 3. Install the Python packages

```bash
pip install -r requirements.txt pytest
python -m pytest -q        # should print "6 passed"
```

## 4. Add your settings

```bash
cp .env.example .env
nano .env                  # fill in the keys, keep DRY_RUN=true for now
```

Save with Ctrl+O, Enter, then exit with Ctrl+X. On the Termux extra-keys row,
Ctrl is the CTRL button.

## 5. Start the agent

```bash
termux-wake-lock           # stops Android from putting Termux to sleep
python -m app.server       # runs on http://localhost:8000
```

Open http://localhost:8000 in your phone's browser to see the dashboard. Log in
with any username and your DASHBOARD_PASSWORD.

## 6. Give Meta a public address

Meta can't reach your phone directly. In a second Termux session (swipe in from
the left edge → New session), run:

```bash
cloudflared tunnel --url http://localhost:8000
```

It prints a link like `https://something.trycloudflare.com`. In your Meta app
(WhatsApp → Configuration → Webhook), set:

- Callback URL: `https://something.trycloudflare.com/webhook`
- Verify token: the WHATSAPP_VERIFY_TOKEN from your .env

Then subscribe to **messages**.

## Things to know

- The address from the free cloudflared tunnel changes every time you restart
  it, so you'd have to update it in Meta each time. For a fixed address, set up
  a named Cloudflare tunnel, or move to a host like Render once it works.
- The agent only answers while Termux is running and the phone is online. In
  Android settings, turn off battery optimization for Termux so the system
  doesn't stop it.
- To start it again later: `cd ~/test/whatsapp-agent && python -m app.server`
- To get updates: `cd ~/test && git pull`
