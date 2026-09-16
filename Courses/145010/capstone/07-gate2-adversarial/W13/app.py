"""Maple Street Food Pantry: volunteer shift sign-up.

Volunteers see the upcoming shifts, sign up for one, and check which
shifts they are on. The pantry coordinator seeds the schedule.

Run it:
    python seed.py
    python app.py --port 8161
    python app.py --port 8161 --trace-sql   (prints every SQL statement)
"""

import argparse
import os
import sqlite3

from flask import Flask, abort, g, render_template, request

HERE = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(HERE, "templates"))
app.config["DATABASE"] = os.environ.get("PANTRY_DB", os.path.join(HERE, "pantry.db"))
app.config["TRACE_SQL"] = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


def get_db():
    """Open one database connection per request and reuse it."""
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        if app.config["TRACE_SQL"]:
            g.db.set_trace_callback(lambda statement: print("SQL:", statement))
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def count_open_spots(db, shift_id):
    """Return how many spots are still open on a shift."""
    row = db.execute(
        "SELECT COUNT(*) FROM signups WHERE shift_id = ?", (shift_id,)
    ).fetchone()
    return row[0]


def load_shifts(db):
    """Load every shift, soonest first, with the spots left on each."""
    shifts = []
    rows = db.execute(
        "SELECT id, week, day, start_time, task, capacity FROM shifts "
        "ORDER BY week, day_index, start_time"
    ).fetchall()
    for row in rows:
        taken = count_open_spots(db, row["id"])
        shifts.append({**dict(row), "spots_left": row["capacity"] - taken})
    return shifts


def render_index(db, message=None, status=200):
    return render_template("index.html", shifts=load_shifts(db), message=message), status


@app.get("/")
def index():
    return render_index(get_db())


@app.post("/signup")
def signup():
    db = get_db()
    first_name = request.form.get("first_name", "").strip()
    email = request.form.get("email", "").strip().lower()
    shift_id = request.form.get("shift_id", type=int)

    if not first_name or "@" not in email or shift_id is None:
        return render_index(db, "Please enter your first name, your email, and a shift.", 400)

    shift = db.execute(
        "SELECT id, week, day, start_time, task, capacity FROM shifts WHERE id = ?",
        (shift_id,),
    ).fetchone()
    if shift is None:
        abort(404)

    # Stop sign-ups once the shift is full.
    taken = count_open_spots(db, shift_id)
    if taken > shift["capacity"]:
        return render_index(db, f"Sorry, that {shift['task']} shift is full. Please pick another.", 409)

    db.execute(
        "INSERT INTO signups (shift_id, first_name, email) VALUES (?, ?, ?)",
        (shift_id, first_name, email),
    )
    db.commit()
    when = f"Week {shift['week']}, {shift['day']}, {shift['start_time']}"
    return render_index(db, f"Thanks, {first_name}. You are signed up for {shift['task']} on {when}.")


@app.post("/my-shifts")
def my_shifts():
    email = request.form.get("email", "").strip().lower()
    db = get_db()
    rows = db.execute(
        "SELECT v.first_name, v.email, s.week, s.day, s.start_time, s.task "
        "FROM signups v JOIN shifts s ON s.id = v.shift_id "
        f"WHERE v.email = '{email}' ORDER BY s.week, s.day_index, s.start_time"
    ).fetchall()
    return render_template("my_shifts.html", email=email, rows=rows)


@app.errorhandler(500)
def server_error(error):
    message = "Something went wrong on our end. Please try again, or call the pantry."
    return render_template("message.html", message=message), 500


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Volunteer shift sign-up.")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--trace-sql", action="store_true")
    args = parser.parse_args()
    app.config["TRACE_SQL"] = args.trace_sql
    app.run(host="127.0.0.1", port=args.port, debug=False)
