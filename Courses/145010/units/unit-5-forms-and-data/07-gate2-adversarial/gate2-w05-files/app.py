"""
Car Wash Volunteer Sign-Up

A Flask + SQLite app for the robotics club's car wash fundraiser.
Volunteers pick a shift, get a confirmation code, and can look up
their sign-up later with that code.

Usage:
    python app.py --port 8415
"""

import argparse
import secrets
import socket
import sqlite3
import sys
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

DB_PATH = Path(__file__).parent / "carwash.db"

SHIFTS = ["9:00 am", "11:00 am", "1:00 pm"]
GRADES = ["9", "10", "11", "12"]
SHIFT_CAPACITY = 4  # volunteers per shift

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def init_db():
    """Create the table and sample data if they do not exist yet."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS volunteers (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            grade TEXT NOT NULL,
            shift TEXT NOT NULL,
            code  TEXT NOT NULL UNIQUE
        )
        """
    )
    if conn.execute("SELECT COUNT(*) FROM volunteers").fetchone()[0] == 0:
        conn.executemany(
            "INSERT INTO volunteers (name, grade, shift, code) VALUES (?, ?, ?, ?)",
            [
                ("Dana Whitfield", "11", "9:00 am", "a1b2c3"),
                ("Marco Ruiz", "10", "9:00 am", "d4e5f6"),
                ("Priya Natarajan", "12", "11:00 am", "0718aa"),
            ],
        )
    conn.commit()
    conn.close()


def get_db():
    """Open a connection, making sure the database is ready first."""
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def count_for_shift(shift):
    """Return how many volunteers are signed up for the given shift."""
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM volunteers").fetchone()[0]
    conn.close()
    return count


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def is_valid_name(name):
    """Check the volunteer's name."""
    if not name:
        return "Enter your name."
    if len(name) > 50:
        return "Enter a name of 50 characters or fewer."
    return None


def validate(form):
    """Validate the submitted form. Returns a dict of field -> error message."""
    errors = {}

    name = form.get("name", "").strip()
    if is_valid_name(name):
        errors["name"] = is_valid_name(name)

    if form.get("grade") not in GRADES:
        errors["grade"] = "Choose your grade."

    shift = form.get("shift")
    if shift not in SHIFTS:
        errors["shift"] = "Choose a shift."
    elif count_for_shift(shift) >= SHIFT_CAPACITY:
        errors["shift"] = "That shift is full. Choose another one."

    return errors


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
def form_page():
    spots = {shift: SHIFT_CAPACITY - count_for_shift(shift) for shift in SHIFTS}
    return render_template("volunteer.html", shifts=SHIFTS, grades=GRADES,
                           spots=spots, errors={})


@app.post("/signup")
def signup():
    errors = validate(request.form)
    if errors:
        spots = {shift: SHIFT_CAPACITY - count_for_shift(shift) for shift in SHIFTS}
        return render_template("volunteer.html", shifts=SHIFTS, grades=GRADES,
                               spots=spots, errors=errors), 400

    code = secrets.token_hex(3)
    conn = get_db()
    conn.execute(
        "INSERT INTO volunteers (name, grade, shift, code) VALUES (?, ?, ?, ?)",
        (request.form["name"].strip(), request.form["grade"], request.form["shift"], code),
    )
    conn.commit()
    conn.close()
    return redirect(url_for("thanks", code=code), code=303)


@app.get("/thanks")
def thanks():
    return render_template("thanks.html", code=request.args.get("code", ""))


@app.get("/lookup")
def lookup():
    code = request.args.get("code", "").strip()
    rows = []
    if code:
        conn = get_db()
        rows = conn.execute(
            f"SELECT name, grade, shift FROM volunteers WHERE code = '{code}'"
        ).fetchall()
        conn.close()
    return render_template("lookup.html", code=code, rows=rows)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    with socket.socket() as probe:
        if probe.connect_ex(("127.0.0.1", args.port)) == 0:
            sys.exit(f"Port {args.port} is already in use.")

    app.run(host="127.0.0.1", port=args.port, debug=False)


if __name__ == "__main__":
    main()
