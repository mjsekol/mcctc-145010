"""The WRONG version of the skeleton, kept for the clinic.

Two mistakes that work on your own machine and fail somewhere else:
  1. The database path is relative, so it depends on the folder you start from.
     sqlite3.connect() then creates a new, empty file instead of failing.
  2. /health returns "ok" without touching the database, so the health log
     says the system is fine while every visitor sees an error.

Run it from a different folder to see both:

    cd ..
    python clinic-w11-skeleton\\skeleton_wrong.py

Port 5331, so it never collides with the correct skeleton on 5330.
"""

import sqlite3

from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    conn = sqlite3.connect("parts-skeleton.db")   # relative to wherever you started
    row = conn.execute("SELECT code, name FROM bins ORDER BY code LIMIT 1").fetchone()
    conn.close()
    return f"<p>First bin: {row[0]}, {row[1]}</p>"


@app.get("/health")
def health():
    return "ok"                                    # checks nothing


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5331)
