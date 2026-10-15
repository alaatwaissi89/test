"""SQLite storage for messages and reply drafts."""

import sqlite3
import time
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wa_id TEXT NOT NULL,              -- contact's WhatsApp number
    contact_name TEXT,
    direction TEXT NOT NULL,          -- 'in' or 'out'
    body TEXT NOT NULL,
    wa_message_id TEXT UNIQUE,        -- WhatsApp's id, used to ignore duplicate webhooks
    created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS drafts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wa_id TEXT NOT NULL,
    contact_name TEXT,
    in_message_id INTEGER NOT NULL,
    reply TEXT NOT NULL,
    needs_owner INTEGER NOT NULL DEFAULT 0,
    reason TEXT,
    status TEXT NOT NULL DEFAULT 'pending',  -- pending | sent | rejected | skipped | error
    error TEXT,
    created_at REAL NOT NULL,
    updated_at REAL NOT NULL
);
"""


class Store:
    def __init__(self, path: str):
        if path != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    def add_message(self, wa_id, contact_name, direction, body, wa_message_id=None):
        """Insert a message. Returns its row id, or None if it was a duplicate."""
        try:
            cur = self.db.execute(
                "INSERT INTO messages (wa_id, contact_name, direction, body, wa_message_id, created_at)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                (wa_id, contact_name, direction, body, wa_message_id, time.time()),
            )
        except sqlite3.IntegrityError:
            return None
        self.db.commit()
        return cur.lastrowid

    def history(self, wa_id, limit):
        rows = self.db.execute(
            "SELECT direction, body FROM messages WHERE wa_id = ? ORDER BY id DESC LIMIT ?",
            (wa_id, limit),
        ).fetchall()
        return list(reversed(rows))

    def add_draft(self, wa_id, contact_name, in_message_id, reply, needs_owner, reason, status="pending"):
        now = time.time()
        cur = self.db.execute(
            "INSERT INTO drafts (wa_id, contact_name, in_message_id, reply, needs_owner, reason, status,"
            " created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (wa_id, contact_name, in_message_id, reply, int(needs_owner), reason, status, now, now),
        )
        self.db.commit()
        return cur.lastrowid

    def get_draft(self, draft_id):
        return self.db.execute("SELECT * FROM drafts WHERE id = ?", (draft_id,)).fetchone()

    def update_draft(self, draft_id, **fields):
        fields["updated_at"] = time.time()
        cols = ", ".join(f"{k} = ?" for k in fields)
        self.db.execute(f"UPDATE drafts SET {cols} WHERE id = ?", (*fields.values(), draft_id))
        self.db.commit()

    def drafts(self, status=None, limit=100):
        if status:
            q, args = "SELECT * FROM drafts WHERE status = ? ORDER BY id DESC LIMIT ?", (status, limit)
        else:
            q, args = "SELECT * FROM drafts ORDER BY id DESC LIMIT ?", (limit,)
        return self.db.execute(q, args).fetchall()

    def incoming_text(self, message_id):
        row = self.db.execute("SELECT body FROM messages WHERE id = ?", (message_id,)).fetchone()
        return row["body"] if row else ""
