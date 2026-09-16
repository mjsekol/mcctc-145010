"""Walking skeleton for the composite Parts Bin Board.

The thinnest path through every layer: a browser asks Flask for a page, Flask
reads one row from SQLite, and the page shows it. A /health route touches the
same table, so it fails when the page would fail.

Everything in the database is invented. The co-op is a composite, not a real
organization.

Run it (Windows PowerShell, from this folder):

    python setup_db.py
    python skeleton.py

Then open http://127.0.0.1:5330/ and http://127.0.0.1:5330/health
Stop it with Ctrl+C.

Settings come from environment variables, with safe local defaults:
    PARTS_DB   path to the SQLite file   (default: parts-skeleton.db next to this file)
    PORT       port to listen on         (default: 5330)
"""

import os
import pathlib
import sqlite3
from contextlib import closing

from flask import Flask

VERSION = "0.1.0"
HERE = pathlib.Path(__file__).resolve().parent
DB_PATH = pathlib.Path(os.environ.get("PARTS_DB", HERE / "parts-skeleton.db"))
PORT = int(os.environ.get("PORT", "5330"))

app = Flask(__name__)


def connect():
    """Open the existing database. Never create an empty one by accident.

    sqlite3.connect() silently creates a new, empty file when the path is wrong.
    mode=rw refuses to do that, so a wrong path fails loudly here instead of
    failing later with "no such table".
    """
    return sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=rw", uri=True)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Parts Bin Board</title>
</head>
<body>
<main>
<h1>Parts Bin Board</h1>
<p>First bin on the shelf: <strong>{code}</strong>, {name}.</p>
<p>Version {version}. This is a walking skeleton.</p>
</main>
</body>
</html>
"""


@app.get("/")
def home():
    with closing(connect()) as conn:
        row = conn.execute("SELECT code, name FROM bins ORDER BY code LIMIT 1").fetchone()
    code, name = row
    return PAGE.format(code=code, name=name, version=VERSION)


@app.get("/health")
def health():
    """Touch the real dependency: the same table the home page reads."""
    try:
        with closing(connect()) as conn:
            count = conn.execute("SELECT COUNT(*) FROM bins").fetchone()[0]
    except sqlite3.Error as err:
        # Report the kind of failure, never the path or the full message.
        return {"status": "fail", "database": type(err).__name__, "version": VERSION}, 503
    return {"status": "ok", "database": "ok", "bins": count, "version": VERSION}


if __name__ == "__main__":
    # 127.0.0.1 keeps it on this machine. A host sets its own address and port.
    app.run(host="127.0.0.1", port=PORT)
