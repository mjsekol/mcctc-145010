-- 001: the tables the walking skeleton shipped with in Week 11.
CREATE TABLE bins (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE low_reports (
    id          INTEGER PRIMARY KEY,
    bin_code    TEXT NOT NULL REFERENCES bins(code),
    note        TEXT CHECK (note IS NULL OR length(note) <= 120),
    reported_at TEXT NOT NULL
);
