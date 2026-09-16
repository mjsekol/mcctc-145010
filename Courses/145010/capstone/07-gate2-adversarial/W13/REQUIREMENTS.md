# Requirements · Volunteer shift sign-up

**Maple Street Food Pantry is an invented organization, a composite of small food pantries. No
real pantry is involved, and every name and email in the seed data is invented.**

The pantry coordinator needs volunteers to sign up for shifts online instead of on a paper
sheet by the door. The app was built from these requirements. Read them before you read a line
of code.

1. Show every upcoming shift with its week, day, start time, and task, soonest first.
2. Show how many spots are left on each shift, so a volunteer can see at a glance what still
   needs people.
3. A volunteer may sign up for a shift only while it has an open spot. **A shift must never hold
   more volunteers than its capacity.** A shift at capacity is full and takes no one else.
4. A volunteer can look up the shifts they signed up for, using the email they signed up with.
   **What a volunteer types is data, never part of the query.** No input a volunteer enters may
   return rows that are not their own or change what is stored.
5. Confirm each sign-up with a clear message, and show a clear message when a shift is full or
   the form is incomplete.
6. Build the shift list without querying the database once per shift. One query, or a small
   fixed number, serves the whole list no matter how many shifts there are.
7. **The sign-up form meets WCAG 2.1 AA and passes the course web-check with zero violations.**
   Every input has a label a screen reader can announce.
8. Names in the code say what each thing is, and every comment and docstring matches the code
   directly under it.

## How to run it

The seed script builds the database. The app reads an explicit port.

```
python seed.py
python app.py --port 8161
```

Open `http://127.0.0.1:8161` in Chrome. To watch every SQL statement the app runs, start it
with `--trace-sql`:

```
python app.py --port 8161 --trace-sql
```

Stop the server with Ctrl+C when you are done, and confirm the port is free before you move on.
