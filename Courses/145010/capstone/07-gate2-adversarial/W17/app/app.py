"""Front Desk Checkout: shared-item lending for the Hillcrest Senior Center front desk.

The center, its groups, and every item here are invented for a Gate 2 exercise (a composite).

What it does: shows which shared items (folding tables, the projector, the coffee urn) are on
the shelf, which group has each one that is out, and when it is due back. It keeps a history
of every check-out and check-in.

Run it:     python app.py
Address:    http://127.0.0.1:8165
Database:   checkout.db next to this file, created on first start and seeded with invented
            items. Set the CHECKOUT_DB environment variable to keep it somewhere else.
"""
import os
import sqlite3
from datetime import datetime, timedelta

from flask import Flask, abort, flash, g, jsonify, redirect, render_template, request, url_for

PORT = 8165
LOAN_DAYS = 7
HISTORY_LIMIT = 50
DB_PATH = os.environ.get(
    "CHECKOUT_DB",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "checkout.db"),
)

GROUPS = ["Book Group", "Chair Yoga Class", "Front Desk", "Knitting Circle", "Tuesday Card Club"]

SEED_ITEMS = [
    "Card table set",
    "Coffee urn",
    "Extension cord, 25 feet",
    "Folding table A",
    "Folding table B",
    "Large-print puzzle box",
    "Portable projector",
    "Portable speaker",
]
# Two items start out checked out, so a new database never looks empty.
SEED_CHECKOUTS = [("Card table set", "Tuesday Card Club"), ("Coffee urn", "Book Group")]

SCHEMA = """
CREATE TABLE items (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL UNIQUE,
    group_name TEXT,
    due        TEXT
);
CREATE TABLE events (
    id         INTEGER PRIMARY KEY,
    item_id    INTEGER NOT NULL REFERENCES items(id),
    action     TEXT NOT NULL CHECK (action IN ('out', 'in')),
    group_name TEXT NOT NULL,
    at         TEXT NOT NULL
);
"""

app = Flask(__name__)
# Keep template tags from leaving blank, space-filled lines in the served HTML.
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
# A fresh key each start. Only used to carry the one-line message to the next page.
app.secret_key = os.urandom(16)


def now_text():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def init_db():
    """Create the database with invented seed data, but only if the file is missing."""
    if os.path.exists(DB_PATH):
        return
    con = sqlite3.connect(DB_PATH)
    try:
        con.executescript(SCHEMA)
        con.executemany("INSERT INTO items (name) VALUES (?)", [(n,) for n in SEED_ITEMS])
        due = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
        for name, group in SEED_CHECKOUTS:
            item_id = con.execute("SELECT id FROM items WHERE name = ?", (name,)).fetchone()[0]
            con.execute("UPDATE items SET group_name = ?, due = ? WHERE id = ?", (group, due, item_id))
            con.execute(
                "INSERT INTO events (item_id, action, group_name, at) VALUES (?, 'out', ?, ?)",
                (item_id, group, now_text()),
            )
        con.commit()
    finally:
        con.close()


def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    con = g.pop("db", None)
    if con is not None:
        con.close()


def find_item(item_id):
    row = db().execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if row is None:
        abort(404)
    return row


@app.get("/")
def index():
    items = db().execute("SELECT * FROM items ORDER BY name").fetchall()
    out_count = sum(1 for i in items if i["group_name"])
    return render_template("index.html", items=items, groups=GROUPS, out_count=out_count)


@app.post("/checkout/<int:item_id>")
def checkout(item_id):
    item = find_item(item_id)
    group = request.form.get("group", "")
    if group not in GROUPS:
        flash("Choose a group before checking an item out.")
    elif item["group_name"]:
        flash(f"{item['name']} is already checked out to {item['group_name']}.")
    else:
        due = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
        con = db()
        con.execute("UPDATE items SET group_name = ?, due = ? WHERE id = ?", (group, due, item_id))
        con.execute(
            "INSERT INTO events (item_id, action, group_name, at) VALUES (?, 'out', ?, ?)",
            (item_id, group, now_text()),
        )
        con.commit()
        flash(f"Checked out: {item['name']} to {group}. Due back {due}.")
    return redirect(url_for("index"))


@app.post("/checkin/<int:item_id>")
def checkin(item_id):
    item = find_item(item_id)
    if not item["group_name"]:
        flash(f"{item['name']} is already on the shelf.")
    else:
        con = db()
        con.execute("UPDATE items SET group_name = NULL, due = NULL WHERE id = ?", (item_id,))
        con.execute(
            "INSERT INTO events (item_id, action, group_name, at) VALUES (?, 'in', ?, ?)",
            (item_id, item["group_name"], now_text()),
        )
        con.commit()
        flash(f"Checked in: {item['name']}. It is back on the shelf.")
    return redirect(url_for("index"))


@app.get("/history")
def history():
    rows = db().execute(
        """SELECT events.action, events.group_name, events.at, items.name
           FROM events JOIN items ON items.id = events.item_id
           ORDER BY events.id DESC LIMIT ?""",
        (HISTORY_LIMIT,),
    ).fetchall()
    return render_template("history.html", rows=rows, limit=HISTORY_LIMIT)


@app.get("/health")
def health():
    con = db()
    items = con.execute("SELECT COUNT(*) FROM items").fetchone()[0]
    out = con.execute("SELECT COUNT(*) FROM items WHERE group_name IS NOT NULL").fetchone()[0]
    events = con.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    return jsonify(status="ok", items=items, checked_out=out, events=events)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=PORT, debug=False)
