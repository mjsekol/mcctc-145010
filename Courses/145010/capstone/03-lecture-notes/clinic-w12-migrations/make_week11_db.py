"""Build a practice copy of the Week 11 database: migration 001 plus invented reports.

Usage:  python make_week11_db.py <new database file>

Everything in it is invented. The co-op is a composite, not a real organization.
Low reports carry a bin code and an optional note, never a name.
"""

import pathlib
import sqlite3
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent

BINS = [("B-01", "Tubes, 26 inch"), ("B-02", "Brake pads, rim"), ("B-03", "Chains, 8 speed")]
REPORTS = [
    ("B-01", "last two on the hook", "2027-04-16T18:05:00"),
    ("B-03", None, "2027-04-16T18:40:00"),
    ("B-02", "only the long ones left", "2027-04-17T10:15:00"),
    ("B-01", None, "2027-04-17T11:02:00"),
    ("B-02", None, "2027-04-17T11:30:00"),
]

if len(sys.argv) != 2:
    sys.exit("usage: python make_week11_db.py <new database file>")
db_path = pathlib.Path(sys.argv[1])
if db_path.exists():
    sys.exit(f"{db_path.name} already exists. This script only builds a new practice copy.")

subprocess.run([sys.executable, str(HERE / "migrate.py"), str(db_path), "--to", "1"], check=True)
with sqlite3.connect(db_path) as conn:
    conn.executemany("INSERT INTO bins (code, name) VALUES (?, ?)", BINS)
    conn.executemany(
        "INSERT INTO low_reports (bin_code, note, reported_at) VALUES (?, ?, ?)", REPORTS
    )
conn.close()
print(f"added {len(BINS)} bins and {len(REPORTS)} invented low reports")
