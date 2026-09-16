"""Apply numbered migrations to a SQLite database that already holds data.

Why: the deployed database has real reports in it. Dropping a table and
creating it again deletes them. A migration changes the table in place, in a
numbered step, and records which steps have run, so running it twice is safe.

Usage (standard library only, from this folder):

    python migrate.py <database file>            apply every pending migration
    python migrate.py <database file> --to 1     stop after migration 1

Before applying anything, it writes a backup copy next to the database:
<name>.before-v<next>.bak. Test on a copy of the database first.
"""

import argparse
import datetime
import pathlib
import sqlite3
import sys

HERE = pathlib.Path(__file__).resolve().parent
MIGRATIONS = HERE / "migrations"


def migration_files():
    """Return [(number, path)] sorted by number, from files named 001_name.sql."""
    found = []
    for path in sorted(MIGRATIONS.glob("*.sql")):
        number = int(path.name.split("_", 1)[0])
        found.append((number, path))
    return found


def current_version(conn):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS schema_version ("
        " version INTEGER PRIMARY KEY, name TEXT NOT NULL, applied_at TEXT NOT NULL)"
    )
    row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
    return row[0] or 0


def backup(conn, db_path, next_version):
    target = db_path.with_name(f"{db_path.name}.before-v{next_version}.bak")
    with sqlite3.connect(target) as copy:
        conn.backup(copy)
    copy.close()
    return target


def apply(conn, number, path):
    """Run one migration and record it, all in one transaction."""
    sql = path.read_text(encoding="utf-8")
    stamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    try:
        conn.execute("BEGIN")
        for statement in sql.split(";"):
            if statement.strip() and not all(
                line.strip().startswith("--") or not line.strip()
                for line in statement.splitlines()
            ):
                conn.execute(statement)
        conn.execute(
            "INSERT INTO schema_version (version, name, applied_at) VALUES (?, ?, ?)",
            (number, path.name, stamp),
        )
        conn.execute("COMMIT")
    except sqlite3.Error:
        conn.execute("ROLLBACK")
        raise


def main():
    parser = argparse.ArgumentParser(description="Apply numbered SQLite migrations.")
    parser.add_argument("database", help="the SQLite file to migrate")
    parser.add_argument("--to", type=int, help="stop after this migration number")
    args = parser.parse_args()

    db_path = pathlib.Path(args.database)
    # isolation_level=None: this script opens and closes every transaction itself.
    conn = sqlite3.connect(db_path, isolation_level=None)
    try:
        version = current_version(conn)
        print(f"database         {db_path.name}")
        print(f"current version  {version}")
        pending = [(n, p) for n, p in migration_files()
                   if n > version and (args.to is None or n <= args.to)]
        if not pending:
            print("nothing to apply")
            return 0
        if version > 0:
            print(f"backup written   {backup(conn, db_path, pending[0][0]).name}")
        for number, path in pending:
            try:
                apply(conn, number, path)
            except sqlite3.Error as err:
                print(f"FAILED           {path.name}: {err}")
                print("nothing from that migration was kept. The backup is untouched.")
                return 1
            print(f"applied          {path.name}")
        print(f"now at version   {current_version(conn)}")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
