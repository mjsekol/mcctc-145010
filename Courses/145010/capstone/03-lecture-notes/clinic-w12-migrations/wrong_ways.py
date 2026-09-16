"""Two WRONG ways to add a column, kept for the clinic. Run them only on a practice copy.

Usage:
    python wrong_ways.py recreate <practice copy>   drops the table and builds it again
    python wrong_ways.py twice <practice copy>      runs a bare ALTER TABLE; run it two times to see it fail
"""

import pathlib
import sqlite3
import sys

if len(sys.argv) != 3 or sys.argv[1] not in ("recreate", "twice"):
    sys.exit(__doc__)
mode, db_path = sys.argv[1], pathlib.Path(sys.argv[2])
if not db_path.exists():
    sys.exit(f"{db_path.name} does not exist. Make a practice copy first.")

conn = sqlite3.connect(db_path)
before = conn.execute("SELECT COUNT(*) FROM low_reports").fetchone()[0]
print(f"reports before: {before}")

if mode == "recreate":
    # "I will rebuild the table with the new column. What could go wrong?"
    conn.executescript("""
        DROP TABLE low_reports;
        CREATE TABLE low_reports (
            id INTEGER PRIMARY KEY,
            bin_code TEXT NOT NULL REFERENCES bins(code),
            note TEXT,
            reported_at TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            restocked_at TEXT
        );
    """)
else:
    # A bare ALTER TABLE with no record that it already ran.
    conn.execute("ALTER TABLE low_reports ADD COLUMN status TEXT NOT NULL DEFAULT 'open'")
    conn.commit()

after = conn.execute("SELECT COUNT(*) FROM low_reports").fetchone()[0]
print(f"reports after:  {after}")
conn.close()
