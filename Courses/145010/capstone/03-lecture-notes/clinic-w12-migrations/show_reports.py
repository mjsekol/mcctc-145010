"""Print the low_reports columns and rows, so you can see a migration's effect.

Usage:  python show_reports.py <database file>
"""

import pathlib
import sqlite3
import sys

if len(sys.argv) != 2:
    sys.exit("usage: python show_reports.py <database file>")
db_path = pathlib.Path(sys.argv[1])
# mode=ro: open an existing file read-only, and never create an empty one.
conn = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
try:
    columns = [row[1] for row in conn.execute("PRAGMA table_info(low_reports)")]
    rows = conn.execute("SELECT * FROM low_reports ORDER BY id").fetchall()
finally:
    conn.close()
print("columns:", ", ".join(columns))
print(f"rows: {len(rows)}")
for row in rows:
    print("  ", row)
