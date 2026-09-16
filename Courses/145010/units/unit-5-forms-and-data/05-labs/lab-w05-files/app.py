"""
app.py · Open Mic Night sign-ups · Labs W05-01 and W05-02 · STARTER

A small Flask application backed by SQLite. It serves the sign-up form,
receives it, checks it, stores it, and lists what is stored.

Run it from this folder, stating the port every time:

    python app.py --port 8405            start, creating openmic.db if missing
    python app.py --port 8405 --reset    rebuild openmic.db from schema.sql first

Stop it with Ctrl+C.

Routes:
    GET  /              the sign-up form
    GET  /echo          shows exactly what a GET form sent        (Monday)
    POST /echo          shows exactly what a POST form sent       (Tuesday)
    POST /signup        checks, stores, and redirects             (Tuesday to Thursday)
    GET  /signups       every stored sign-up                      (Tuesday)
    GET  /api/slots     the slots as JSON, a small web service    (Tuesday)
    POST /naive/signup  stores whatever arrives, unchecked        (Wednesday, DO NOT COPY)

Why Flask and SQLite: you used both in 145130, so this week is about the form
and the request, not about learning a server. Flask reads form data for you,
and its templates escape every value by default, which matters on Thursday.
"""

import argparse
import pathlib
import socket
import sqlite3
import sys
from contextlib import contextmanager

from flask import Flask, jsonify, redirect, render_template, request, url_for

from validation import validate_signup  # noqa: F401  (used from Wednesday)

HERE = pathlib.Path(__file__).parent
DB_PATH = HERE / "openmic.db"
SCHEMA_PATH = HERE / "schema.sql"

# Where each field's error message links to: the id of the control to focus.
# For a radio or checkbox group, that is the first control in the group.
FIELD_IDS = {
    "performer_name": "performer-name",
    "email": "email",
    "act_type": "act-music",
    "slot": "slot",
    "minutes": "minutes",
    "needs": "need-mic",
    "agree": "agree",
}

app = Flask(__name__)
# Drop the blank lines template tags would otherwise leave behind, so the
# HTML the browser receives is tidy and passes the course validator.
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

@contextmanager
def open_db():
    """One connection per request, committed if the block succeeds, rolled
    back if it fails, and always closed. SQLite connections are cheap, and a
    fresh one per request means no request sees another's half-finished work."""
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def reset_db():
    db = sqlite3.connect(DB_PATH)
    try:
        db.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    finally:
        db.close()


def slot_rows(db):
    """Every slot with the number of places still open.

    MAX(..., 0) because a slot can be over-filled by a route that skips the
    checks, and "-1 places left" helps nobody."""
    return db.execute(
        """
        SELECT s.id, s.label, s.capacity,
               MAX(s.capacity - COUNT(g.id), 0) AS places_left
        FROM slots AS s
        LEFT JOIN signups AS g ON g.slot_id = s.id
        GROUP BY s.id
        ORDER BY s.id
        """
    ).fetchall()


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

@app.get("/")
def form_page():
    with open_db() as db:
        slots = slot_rows(db)
    return render_template("signup.html", slots=slots, errors={}, values={},
                           field_ids=FIELD_IDS)


@app.route("/echo", methods=["GET", "POST"])
def echo():
    """Show exactly what arrived, so the form action is something you can see."""
    source = request.args if request.method == "GET" else request.form
    pairs = [(name, value) for name in source for value in source.getlist(name)]
    return render_template("echo.html", method=request.method,
                           content_type=request.content_type or "(none)",
                           query=request.query_string.decode("utf-8", "replace"),
                           pairs=pairs)


@app.post("/signup")
def signup():
    """Receive the form, check it, store it, and redirect to the list.

    TODO Lab W05-01, step 9 (Tuesday): store the sign-up.
        Open the database with `with open_db() as db:` and INSERT one row into
        signups using ? placeholders, never an f-string. Take the values from
        request.form. The needs checkboxes arrive as a list:
        request.form.getlist("needs"). Store them joined with commas.
        Then return redirect(url_for("list_signups", added=new_id), code=303),
        where new_id is cursor.lastrowid.

    TODO Lab W05-02, step 6 (Wednesday): check it first.
        Build open_slots = {row["id"]: row["places_left"] for row in slot_rows(db)}
        and call validate_signup(request.form, open_slots). Store clean values,
        not raw ones. If there are errors, do not store anything.

    TODO Lab W05-02, step 11 (Thursday): show the problems.
        If there are errors, return render_template("signup.html", ...) with
        errors, the person's values, slots, and field_ids=FIELD_IDS, and the
        status code 400.
    """
    return "The /signup route is not written yet. See Lab W05-01, step 9.", 501


@app.get("/signups")
def list_signups():
    with open_db() as db:
        rows = db.execute(
            """
            SELECT g.id, g.performer_name, g.act_type, s.label AS slot, g.minutes,
                   g.needs, g.source
            FROM signups AS g JOIN slots AS s ON s.id = g.slot_id
            ORDER BY g.id
            """
        ).fetchall()
    added = request.args.get("added", type=int)
    return render_template("signups.html", rows=rows, added=added)


@app.get("/api/slots")
def api_slots():
    """A web service: the same data the form uses, as JSON, for scripts."""
    with open_db() as db:
        return jsonify([
            {"id": r["id"], "label": r["label"], "capacity": r["capacity"],
             "places_left": r["places_left"]}
            for r in slot_rows(db)
        ])


@app.post("/naive/signup")
def naive_signup():
    """DO NOT COPY. This route trusts the browser completely.

    It exists so Lab W05-02 can show what reaches a database when the only
    checks are the ones in the page. It still uses ? placeholders, so the
    lesson is about validation, not injection.
    """
    with open_db() as db:
        db.execute(
            """
            INSERT INTO signups (performer_name, email, act_type, slot_id, minutes, needs, source)
            VALUES (?, ?, ?, ?, ?, ?, 'naive')
            """,
            (request.form.get("performer_name", ""), request.form.get("email", ""),
             request.form.get("act_type", ""), request.form.get("slot", "1"),
             request.form.get("minutes", ""), ",".join(request.form.getlist("needs"))),
        )
    return redirect(url_for("list_signups"), code=303)


# ---------------------------------------------------------------------------
# Start-up
# ---------------------------------------------------------------------------

def port_in_use(port):
    """True if something already answers on this port.

    On Windows, Flask's development server will start on a port another
    server is already using, without any error, and your browser keeps talking
    to the old one. Checking first turns that silent failure into a clear one.
    """
    with socket.socket() as probe:
        probe.settimeout(0.5)
        return probe.connect_ex(("127.0.0.1", port)) == 0


def main():
    parser = argparse.ArgumentParser(description="Open Mic Night sign-up server")
    parser.add_argument("--port", type=int, required=True,
                        help="the port to listen on. The labs use 8405.")
    parser.add_argument("--reset", action="store_true",
                        help="rebuild openmic.db from schema.sql before starting")
    args = parser.parse_args()

    if port_in_use(args.port):
        print(f"Port {args.port} is already in use. Stop the other server first "
              f"(find its terminal and press Ctrl+C).")
        sys.exit(1)

    if args.reset or not DB_PATH.exists():
        reset_db()
        print(f"Database rebuilt: {DB_PATH.name}")

    print(f"Open Mic sign-ups at http://127.0.0.1:{args.port}/  (Ctrl+C to stop)")
    # 127.0.0.1 only: nobody else on the network can reach this server.
    # debug=False: the debugger lets anyone who can reach the page run code.
    app.run(host="127.0.0.1", port=args.port, debug=False)
    print("Stopped.")


if __name__ == "__main__":
    main()
