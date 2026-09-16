-- schema.sql · Open Mic Night sign-ups · Labs W05-01 and W05-02
--
-- Every name and address in the seed rows below is invented for this lab.
-- The database file is rebuilt from this script by: python app.py --port 8405 --reset

DROP TABLE IF EXISTS signups;
DROP TABLE IF EXISTS slots;

-- The time slots on the night, and how many acts fit in each.
CREATE TABLE slots (
    id       INTEGER PRIMARY KEY,
    label    TEXT    NOT NULL UNIQUE,
    capacity INTEGER NOT NULL
);

-- One row per sign-up. The columns are deliberately loose: no CHECK rules.
-- Lab W05-02 shows what gets stored when the server trusts the browser, and
-- the database would not stop it either.
CREATE TABLE signups (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    performer_name TEXT    NOT NULL,
    email          TEXT    NOT NULL,
    act_type       TEXT    NOT NULL,
    slot_id        INTEGER NOT NULL REFERENCES slots(id),
    minutes        TEXT    NOT NULL,
    needs          TEXT    NOT NULL DEFAULT '',
    source         TEXT    NOT NULL DEFAULT 'form'
);

INSERT INTO slots (id, label, capacity) VALUES
    (1, '7:00 pm', 2),
    (2, '7:20 pm', 2),
    (3, '7:40 pm', 2),
    (4, '8:00 pm', 2);

INSERT INTO signups (performer_name, email, act_type, slot_id, minutes, needs, source) VALUES
    ('Juniper Vale',  'juniper.vale@example.com', 'music',  1, '6', 'mic,amp', 'seed'),
    ('The Two Tims',  'twotims@example.com',      'comedy', 1, '5', 'mic',     'seed'),
    ('Rosa Okafor',   'rosa.okafor@example.com',  'poetry', 2, '4', '',        'seed');
