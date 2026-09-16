# Clinic · Changing a Table That Already Holds Data
## 145010 Senior Capstone · Week 12, Tuesday · 15 minutes · Improve

**Slides for this clinic:** [outline](../04-slides/MCCTC_145010_Slides_W12_DatabaseMigrations.md).
There is no exported deck yet. To generate one when Gamma credits are available, from the
repository root:
`node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W12_DatabaseMigrations.md --export pptx`

**When this clinic runs.** Week 12, Tuesday, or any week the room shows this signal: anyone about to
delete the deployed database to add a column.
**If you missed it,** you can learn the skill from this file alone. The code is in
[`clinic-w12-migrations/`](clinic-w12-migrations/).
**Competencies:** 1.4.6 (an electronic database for business and technical information), 6.4.7
(scripting that interacts with data sources), 2.11.5 (design a solution), 2.11.6 (test a
solution), 2.11.7 (implement a solution)

---

## Why this exists

**Your skeleton went live last Friday. Since then, real people have put real rows in it.** This
week you need a new column. On your laptop, the quick fix has always been to delete the database
and let the app build it again. On the deployed system, that deletes your stakeholder's data.

It also costs you the clock. Recreating or hand-editing the running system's data is manual
intervention, and it resets your thirty days.

**A migration changes a table in place**, in a numbered step, with a record of which steps have
run. It is written once, tested on a copy, and released through your documented steps, which makes
it a **planned release**, not an intervention.

**This is the most dangerous command you will run this capstone.** Treat it that way.

---

## The skill in plain language

1. **Never drop and recreate a table that holds real data.**
2. **Write each change as a numbered script**: `001_create_tables.sql`, `002_add_status.sql`. Never
   edit a script that has already run anywhere. Add a new one.
3. **Record the version in the database itself**, in a `schema_version` table. The migration tool
   runs only the scripts above that number, so running it twice is safe.
4. **Back up first.** A copy of the database file, taken before anything changes.
5. **Test on a copy** of the real database before touching the real one.
6. **Release it as a planned release**: your deployment steps, an events log line, a decision log
   entry.

Adding a column that existing rows need a value for? Give it a **default**. Every existing row gets
the default, and nothing already reported disappears.

---

## Worked example 1 · the migration files

**Composite project, not a real organization.** In Week 11 the Parts Bin Board shipped with
migration 001. Volunteers mark bins low; each report has a bin code, an optional note, and a time.
No names. In Week 12 the coordinator needs to mark reports restocked, so the table needs a status.

[`migrations/002_add_status.sql`](clinic-w12-migrations/migrations/002_add_status.sql):

```sql
-- 002: the coordinator can mark a report restocked.
-- Existing rows get status 'open', so nothing already reported disappears.
ALTER TABLE low_reports ADD COLUMN status TEXT NOT NULL DEFAULT 'open';
ALTER TABLE low_reports ADD COLUMN restocked_at TEXT;
```

[`migrate.py`](clinic-w12-migrations/migrate.py) does the rest. The part that makes it safe:

```python
def apply(conn, number, path):
    """Run one migration and record it, all in one transaction."""
    ...
    try:
        conn.execute("BEGIN")
        # ... run each statement in the file ...
        conn.execute(
            "INSERT INTO schema_version (version, name, applied_at) VALUES (?, ?, ?)",
            (number, path.name, stamp),
        )
        conn.execute("COMMIT")
    except sqlite3.Error:
        conn.execute("ROLLBACK")
        raise
```

The change and the version record commit together, or neither does.

---

## Worked example 2 · on a copy, then again

**On the build machine these commands ran in a scratch folder outside the repository**, so no
database file was left behind. Run them in any folder you like, then delete the practice files.
`make_week11_db.py` builds a practice database at version 1 with five invented reports.

```
python make_week11_db.py parts.db
```

```
database         parts.db
current version  0
applied          001_create_tables.sql
now at version   1
added 3 bins and 5 invented low reports
```

Make the copy, and look at it before changing anything:

```
Copy-Item parts.db parts-copy.db
python show_reports.py parts-copy.db
```

```
columns: id, bin_code, note, reported_at
rows: 5
   (1, 'B-01', 'last two on the hook', '2027-04-16T18:05:00')
   (2, 'B-03', None, '2027-04-16T18:40:00')
   (3, 'B-02', 'only the long ones left', '2027-04-17T10:15:00')
   (4, 'B-01', None, '2027-04-17T11:02:00')
   (5, 'B-02', None, '2027-04-17T11:30:00')
```

Migrate the copy:

```
python migrate.py parts-copy.db
```

```
database         parts-copy.db
current version  1
backup written   parts-copy.db.before-v2.bak
applied          002_add_status.sql
now at version   2
```

```
python show_reports.py parts-copy.db
```

```
columns: id, bin_code, note, reported_at, status, restocked_at
rows: 5
   (1, 'B-01', 'last two on the hook', '2027-04-16T18:05:00', 'open', None)
   (2, 'B-03', None, '2027-04-16T18:40:00', 'open', None)
   (3, 'B-02', 'only the long ones left', '2027-04-17T10:15:00', 'open', None)
   (4, 'B-01', None, '2027-04-17T11:02:00', 'open', None)
   (5, 'B-02', None, '2027-04-17T11:30:00', 'open', None)
```

Five rows before, five rows after, each with the default. **Now run it again**, the way a nervous
person or a deploy script would:

```
python migrate.py parts-copy.db
```

```
database         parts-copy.db
current version  2
nothing to apply
```

Exit code 0 both times. Re-running is safe because the version is stored in the database.

---

## Worked example 3 · releasing it for real

Once the copy is right, the real release follows your architecture's deployment steps, written down
before you start:

1. Back up the deployed database. `migrate.py` writes a `.bak` copy, and you also keep one off the
   host if your host allows it. [VERIFY how your host lets you copy files or run a command]
2. Run `migrate.py` against the deployed database.
3. Deploy the new code that uses the `status` column. **Migration first, code second**, or the new
   code asks for a column that does not exist yet.
4. Open the board and check the old reports are still there.
5. Add the line to `docs/control/survival/events-log.txt` the same day. An invented example:

```
2027-04-20T15:30:00  planned  released version 0.3.0: migration 002 and restock button, by the documented steps
```

**The local alternative.** If your host does not let you run a command against its storage, or is
not approved yet, do all of this on the approved lab machine's copy and write in your sprint review
what is still unverified on the host.

**Keep database files and backups out of git.** Add `*.db` and `*.bak` to `.gitignore`. If your
project's database holds anything personal, the practice copy stays on the approved machine and
never goes into a repository or an AI tool.

---

## The wrong version, and what it costs

[`wrong_ways.py`](clinic-w12-migrations/wrong_ways.py) shows two wrong ways, each on its own copy of
`parts.db`. Make the copies first:

```
Copy-Item parts.db wrong1.db
Copy-Item parts.db wrong2.db
```

**Wrong 1: drop the table and build it again with the new column.**

```
python wrong_ways.py recreate wrong1.db
```

```
reports before: 5
reports after:  0
```

No error. No warning. Every report is gone, and the program exited 0.

**Wrong 2: a bare `ALTER TABLE` with no record that it ran.** Run the same command two times. The
first run works:

```
python wrong_ways.py twice wrong2.db
```

```
reports before: 5
reports after:  5
```

The second run, the one a deploy script does next week, is the same command:

```
python wrong_ways.py twice wrong2.db
```

```
reports before: 5
Traceback (most recent call last):
  File "...\clinic-w12-migrations\wrong_ways.py", line 37, in <module>
    conn.execute("ALTER TABLE low_reports ADD COLUMN status TEXT NOT NULL DEFAULT 'open'")
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: duplicate column name: status
```

(The folder path in the second line is shortened here.) And on that hand-altered copy, the real
migration now refuses to finish:

```
python migrate.py wrong2.db
```

```
database         wrong2.db
current version  1
backup written   wrong2.db.before-v2.bak
FAILED           002_add_status.sql: duplicate column name: status
nothing from that migration was kept. The backup is untouched.
```

Exit code 1. The rollback worked: the table still had `status` from the hand edit and no
`restocked_at`. **A change made outside the migrations makes the migrations wrong.** Every schema
change goes through a numbered script, or none do.

**What wrong 1 costs:** the coordinator's list is empty on open-shop night, your thirty-day clock
resets, and there is no backup to go back to.

---

## Why the wrong version is tempting

**It has always worked before.** Every database you built in a lab was test data, and deleting it
cost nothing. This is the first one that holds someone else's work.

**A migration feels like ceremony for one column.** The runner is about a hundred lines, written
once, and it works for every column after this one.

---

## Do this today

1. Put your schema into `src/migrations/001_...sql`, matching what is deployed now.
2. Add a `schema_version` table and a migration runner. You may adapt `migrate.py`. Record where it
   came from in `LICENSING.md` and your AI usage log if an AI tool helped.
3. Write the Week 12 change as `002_...sql`, with a default for existing rows.
4. Test it on a copy. Run it twice. Check the row count before and after.
5. Add the migration step to `docs/measure-analyze/architecture.md`, section 10.
6. Record the release in the events log and the decision log the day it happens.
7. **Commit** the scripts, never the database.

---

## If you are ahead, if you are behind

**If you are ahead:** add a test case: "Given a copy of the deployed database at version 1, when
`migrate.py` runs twice, then the version is 2, the row count is unchanged, and the second run
applies nothing." Run it and record it.

**If you are behind:** you do not need a column change this week. Write `001` to match what is
deployed, add the version table, and stop there. The next change will be safe.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Electronic database** | The SQLite file that holds the reports (1.4.6) |
| **Interact with data sources** | Code that reads and changes the database (6.4.7) |
| **Design a solution** | The migration script and the order of release steps (2.11.5) |
| **Test a solution** | Running it on a copy, twice, and checking the rows (2.11.6) |
| **Implement a solution** | The planned release on the deployed system (2.11.7) |

---

## Self-check

**1.** Your new column is `NOT NULL`. Why does the migration need a `DEFAULT`?

**2.** You run the migration on the deployed database, and it prints `nothing to apply`. Is that a
problem?

**3.** You deploy the new code first and run the migration ten minutes later. What does a volunteer
see in those ten minutes?

### Answers

**1.** The rows already in the table have no value for the new column. Without a default, SQLite
refuses to add a `NOT NULL` column to a table that holds rows. On the build machine (SQLite 3.50.4)
it said `Cannot add a NOT NULL column with default value NULL`. The default gives every existing row
a value, here `'open'`.

**2.** Not by itself. It means the database is already at the latest version. Check the version it
printed. If you expected a change, the script may be missing from the migrations folder, or someone
already ran it, which the `schema_version` table will show.

**3.** Errors wherever the new code reads or writes `status`, because the column does not exist yet.
That is why the migration runs first and the code second.
