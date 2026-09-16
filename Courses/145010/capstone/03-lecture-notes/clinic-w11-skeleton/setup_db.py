"""Create the skeleton's database with invented bins.

Run once before skeleton.py. Safe to run again: it only adds rows that are missing.
The database path comes from PARTS_DB, the same variable skeleton.py reads.
Every bin below is invented.
"""

import os
import pathlib
import sqlite3

HERE = pathlib.Path(__file__).resolve().parent
DB_PATH = pathlib.Path(os.environ.get("PARTS_DB", HERE / "parts-skeleton.db"))

BINS = [
    ("B-01", "Tubes, 26 inch"),
    ("B-02", "Brake pads, rim"),
    ("B-03", "Chains, 8 speed"),
]

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS bins (code TEXT PRIMARY KEY, name TEXT NOT NULL)")
    conn.executemany("INSERT OR IGNORE INTO bins (code, name) VALUES (?, ?)", BINS)
    total = conn.execute("SELECT COUNT(*) FROM bins").fetchone()[0]
conn.close()
print(f"database ready: {DB_PATH.name}, {total} bins")
