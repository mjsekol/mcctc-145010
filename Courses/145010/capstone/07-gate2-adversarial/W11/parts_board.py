# parts_board.py
#
# Parts Bin Board, Sprint 1 walking skeleton.
#
# Composite scenario, not a real organization: a volunteer-run community bike
# repair co-op. Anyone with the shop link can mark a parts bin low. The shop
# coordinator signs in and works the low list, then marks a bin restocked.
#
# This is the thinnest path through every layer: a browser page that reads bins
# from SQLite, a form that writes a low report, a coordinator view that reads
# the low list, a health endpoint, and a first-party page-view counter.
#
# Flask 3.1.3, SQLite (standard library), Python 3.13. No commercial services.
#
# Run it:
#     python parts_board.py
#
# The database path comes from the PARTS_DB environment variable so the same
# code runs on the host and on a lab machine. It defaults to a file beside this
# one. The tables are created and seeded on first run.

import os
import sqlite3

from flask import Flask, request, redirect, render_template_string
from werkzeug.security import generate_password_hash

# Configuration from the environment, with a sensible local default.
PARTS_DB = os.environ.get("PARTS_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "parts_board.db"))
PORT = int(os.environ.get("PORT", "5310"))

app = Flask(__name__)
# Keep the rendered markup tidy: drop the newline after a block tag and the
# leading whitespace before one.
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


def get_connection():
    """Open a connection to the parts database."""
    connection = sqlite3.connect(PARTS_DB)
    connection.row_factory = sqlite3.Row
    return connection


def init_db(db_path=None):
    """Create the tables and seed the starting data. Safe to call more than once."""
    path = db_path or PARTS_DB
    connection = sqlite3.connect(path)
    connection.execute(
        "CREATE TABLE IF NOT EXISTS bins ("
        "code TEXT PRIMARY KEY, name TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'ok')"
    )
    connection.execute(
        "CREATE TABLE IF NOT EXISTS reports ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, bin_code TEXT NOT NULL, "
        "note TEXT, reported_at TEXT NOT NULL DEFAULT (datetime('now')))"
    )
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "username TEXT PRIMARY KEY, password_hash TEXT NOT NULL)"
    )
    connection.execute(
        "CREATE TABLE IF NOT EXISTS page_views (id INTEGER PRIMARY KEY CHECK (id = 1), views INTEGER NOT NULL)"
    )
    # Seed the bins the co-op keeps on the shelf, if they are not there yet.
    seed_bins = [
        ("B-01", "Tubes, 26 inch"),
        ("B-02", "Tubes, 700c"),
        ("B-03", "Brake pads, rim"),
        ("B-04", "Brake pads, disc"),
        ("B-05", "Chains, 8 speed"),
        ("B-06", "Cables, brake"),
    ]
    for code, name in seed_bins:
        connection.execute("INSERT OR IGNORE INTO bins (code, name) VALUES (?, ?)", (code, name))
    # Seed the coordinator account. The password is a hash, never plain text.
    connection.execute(
        "INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
        ("coordinator", generate_password_hash("openshop2027")),
    )
    connection.execute("INSERT OR IGNORE INTO page_views (id, views) VALUES (1, 0)")
    connection.commit()
    connection.close()


HOME_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Parts Bin Board</title>
  <style>
    body { margin: 0; font-family: "Segoe UI", Arial, sans-serif; color: #111111; background: #ffffff; line-height: 1.5; }
    header { background: #233452; color: #ffffff; padding: 16px 24px; }
    header h1 { margin: 0; font-size: 1.4rem; }
    main { max-width: 720px; margin: 0 auto; padding: 24px; }
    h2 { color: #233452; }
    table { width: 100%; border-collapse: collapse; margin-bottom: 24px; }
    th, td { text-align: left; padding: 8px; border-bottom: 1px solid #cccccc; }
    thead th { background: #eef4fb; }
    form { display: grid; gap: 12px; max-width: 420px; }
    select, input[type="text"] { font: inherit; padding: 8px; border: 1px solid #767676; border-radius: 6px; }
    button { justify-self: start; font: inherit; font-weight: bold; padding: 10px 18px; border: 0; border-radius: 6px; background: #233452; color: #ffffff; }
    footer { margin-top: 32px; padding: 16px 24px; background: #eef4fb; color: #111111; }
  </style>
</head>
<body>
  <header><h1>Parts Bin Board</h1></header>
  <main>
    <p>See which bins are low. If a bin is empty, mark it low so the coordinator knows.</p>

    <h2>Bins</h2>
    <table>
      <thead>
        <tr><th scope="col">Bin</th><th scope="col">Part</th><th scope="col">Status</th></tr>
      </thead>
      <tbody>
        {% for bin in bins %}
        <tr><td>{{ bin["code"] }}</td><td>{{ bin["name"] }}</td><td>{{ bin["status"] }}</td></tr>
        {% endfor %}
      </tbody>
    </table>

    <h2>Mark a bin low</h2>
    <form method="post" action="/report">
      <select name="bin_code">
        <option value="">Choose a bin</option>
        {% for bin in bins %}
        <option value="{{ bin["code"] }}">{{ bin["code"] }} {{ bin["name"] }}</option>
        {% endfor %}
      </select>
      <input type="text" name="note" placeholder="Optional note, up to 120 characters">
      <button type="submit">Mark low</button>
    </form>
  </main>
  <footer><p>This page has been viewed {{ views }} times.</p></footer>
</body>
</html>
"""

CONFIRM_TEMPLATE = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Reported</title></head>
<body>
  <p>Thanks. {{ name }} is now marked low for the coordinator.</p>
  <p><a href="/">Back to the board</a></p>
</body>
</html>
"""


@app.get("/")
def home():
    connection = get_connection()
    # Count this view. The counter stores no cookies and no identifiers.
    connection.execute("UPDATE page_views SET views = views + 1 WHERE id = 1")
    connection.commit()
    views = connection.execute("SELECT views FROM page_views WHERE id = 1").fetchone()["views"]
    bins = connection.execute("SELECT code, name, status FROM bins ORDER BY code").fetchall()
    connection.close()
    return render_template_string(HOME_TEMPLATE, bins=bins, views=views)


@app.post("/report")
def report():
    bin_code = request.form.get("bin_code", "")
    note = request.form.get("note", "")[:120]
    connection = get_connection()
    # Confirm the bin exists and read its name back for the thank-you message.
    row = connection.execute(f"SELECT name FROM bins WHERE code = '{bin_code}'").fetchone()
    if row is None:
        connection.close()
        return "That bin code is not on the board.", 400
    connection.execute(
        "INSERT INTO reports (bin_code, note) VALUES (?, ?)", (bin_code, note)
    )
    connection.execute("UPDATE bins SET status = 'low' WHERE code = ?", (bin_code,))
    connection.commit()
    connection.close()
    return render_template_string(CONFIRM_TEMPLATE, name=row["name"])


@app.get("/restock")
def restock():
    """The coordinator's low list, one row per bin that has an open low report."""
    connection = get_connection()
    codes = connection.execute(
        # Newest reports first, so the coordinator works the freshest first.
        "SELECT DISTINCT bin_code FROM reports ORDER BY reported_at ASC"
    ).fetchall()
    lines = []
    for code_row in codes:
        code = code_row["bin_code"]
        # Look up the friendly name for this bin.
        name_connection = get_connection()
        name_row = name_connection.execute(
            "SELECT name FROM bins WHERE code = ?", (code,)
        ).fetchone()
        name_connection.close()
        name = name_row["name"] if name_row else code
        lines.append(f"{code} {name}")
    connection.close()
    body = "Low bins:\n" + "\n".join(lines) if lines else "No bins are low."
    return body, 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.get("/health")
def health():
    """Report whether the service can reach its database."""
    connection = get_connection()
    connection.execute("SELECT 1")
    connection.close()
    return {"status": "ok"}, 200


def main():
    init_db()
    print(f"Parts Bin Board on http://0.0.0.0:{PORT}, database {PARTS_DB}")
    app.run(host="0.0.0.0", port=PORT, debug=False)


if __name__ == "__main__":
    main()
