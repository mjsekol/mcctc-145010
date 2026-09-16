"""Create pantry.db with two weeks of shifts and a few sign-ups.

Every name and email here is invented. example.org is a domain reserved
for examples, so no message could ever reach a real person.

    python seed.py

Run it again at any time to put the database back to this starting state.
"""

import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.environ.get("PANTRY_DB", os.path.join(HERE, "pantry.db"))

SCHEMA = """
DROP TABLE IF EXISTS signups;
DROP TABLE IF EXISTS shifts;

CREATE TABLE shifts (
    id         INTEGER PRIMARY KEY,
    week       INTEGER NOT NULL,
    day        TEXT    NOT NULL,
    day_index  INTEGER NOT NULL,
    start_time TEXT    NOT NULL,
    task       TEXT    NOT NULL,
    capacity   INTEGER NOT NULL CHECK (capacity > 0)
);

CREATE TABLE signups (
    id         INTEGER PRIMARY KEY,
    shift_id   INTEGER NOT NULL REFERENCES shifts (id),
    first_name TEXT    NOT NULL,
    email      TEXT    NOT NULL
);
"""

# (week, day, day_index, start_time, task, capacity)
SHIFTS = [
    (1, "Tuesday", 2, "17:30", "Sort donated food", 4),
    (1, "Thursday", 4, "17:30", "Stock shelves", 3),
    (1, "Saturday", 6, "09:00", "Distribution line", 4),
    (1, "Saturday", 6, "09:00", "Intake desk", 2),
    (2, "Tuesday", 2, "17:30", "Sort donated food", 4),
    (2, "Thursday", 4, "17:30", "Stock shelves", 3),
    (2, "Saturday", 6, "09:00", "Distribution line", 4),
    (2, "Saturday", 6, "09:00", "Intake desk", 2),
]

# (shift_id, first_name, email)
SIGNUPS = [
    (1, "Priya", "priya@example.org"),
    (1, "Marcus", "marcus@example.org"),
    (2, "Aubrey", "aubrey@example.org"),
    (3, "Jalen", "jalen@example.org"),
    (3, "Hana", "hana@example.org"),
    (3, "Luis", "luis@example.org"),
    (3, "Tessa", "tessa@example.org"),
    (4, "Deshawn", "deshawn@example.org"),
    (6, "Priya", "priya@example.org"),
    (6, "Marcus", "marcus@example.org"),
    (7, "Hana", "hana@example.org"),
]


def main():
    with sqlite3.connect(DATABASE) as db:
        db.executescript(SCHEMA)
        db.executemany(
            "INSERT INTO shifts (week, day, day_index, start_time, task, capacity) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            SHIFTS,
        )
        db.executemany(
            "INSERT INTO signups (shift_id, first_name, email) VALUES (?, ?, ?)",
            SIGNUPS,
        )
    db.close()
    print(f"Seeded {len(SHIFTS)} shifts and {len(SIGNUPS)} sign-ups into {DATABASE}")


if __name__ == "__main__":
    main()
