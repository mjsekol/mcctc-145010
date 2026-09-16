# Volunteer shift sign-up

An invented composite app for Gate 2, Week 13. **Maple Street Food Pantry is not a real
organization.** Every name and email in the seed data is invented, and `example.org` is a
domain reserved for examples, so no message could reach a real person.

## What it is

A small Flask 3.1 app backed by SQLite. Volunteers see the upcoming shifts, sign up for one,
and look up the shifts they are on. The pantry coordinator seeds the schedule.

## Run it on port 8161

```
python seed.py
python app.py --port 8161
```

Open `http://127.0.0.1:8161` in Chrome.

`seed.py` builds `pantry.db` in this folder. Run `seed.py` again at any time to reset the data
to its starting state. To watch every SQL statement, add `--trace-sql`:

```
python app.py --port 8161 --trace-sql
```

## Stop it

Press Ctrl+C to stop the server, then confirm nothing is still listening on port 8161 before
you move on. `pantry.db` is a local scratch file. Delete it when you are finished.

## Files

| File | What it is |
|---|---|
| `app.py` | The Flask app |
| `seed.py` | Builds and resets `pantry.db` |
| `templates/` | The pages the app renders |
| `REQUIREMENTS.md` | What the app was built from. Read it first |
