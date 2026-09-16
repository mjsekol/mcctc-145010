# Changing a Table That Already Holds Data
---
## Slide 1: You need one new column
- The skeleton went live last Friday
- Real reports are in the table now
- The coordinator needs a restocked button
- How do you add the column?
Speaker notes: Your skeleton has been live since last Friday, and real people have put real rows in it. This week you need a new column. The coordinator of the composite bike co-op wants to mark a report restocked, so the reports table needs a status. On every lab you have ever done, the answer was to delete the database and let the app build it again. Before you do that on a deployed system, watch what it costs.
Image: A clipboard of parts reports with a pencil hovering over a new blank column.
---
## Slide 2: Watch this
```
> python wrong_ways.py recreate wrong1.db
reports before: 5
reports after:  0
```
Speaker notes: This is a practice copy with five invented reports. The script drops the table and creates it again with the new column. Look at the output. No error. No warning. The program exited normally. And every report is gone. On the deployed system, that is the coordinator opening the board on open-shop night and seeing nothing, and it is manual intervention, so your thirty-day clock resets too.
Image: None. This slide is code.
---
## Slide 3: Why it is tempting, and what it costs
- Every lab database you built was test data
- This one holds someone else's work
- Deleting it resets your thirty-day clock
- There is no backup to go back to
Speaker notes: It is tempting because it has always worked. Every database you have built in this program held test data, and deleting it cost nothing. This is the first one that holds someone else's work. Deleting or hand-editing it is an intervention, which resets your clock. And if you did not take a backup first, there is nothing to go back to. Be direct with yourself. This is the most dangerous command you will run this capstone.
Image: A trash can next to a database cylinder, with a stopwatch resetting to zero.
---
## Slide 4: A migration, in five rules
- A numbered script for every schema change
- Never edit a script that already ran
- The database records its own version
- Back up, then test on a copy
- Release it as a planned release
Speaker notes: A migration changes the table in place. Each change is a numbered script. Once a script has run anywhere, you never edit it, you add the next number. The database keeps a schema version table, so the tool runs only the scripts above that number. You back up first and test on a copy. And you release it through your documented steps, with an events log line, which makes it a planned release and not an intervention.
Image: Numbered cards 001 and 002 stacked beside a database cylinder with a version tag.
---
## Slide 5: Migration 002
```sql
-- 002: the coordinator can mark a report restocked.
-- Existing rows get status 'open', so nothing already reported disappears.
ALTER TABLE low_reports ADD COLUMN status TEXT NOT NULL DEFAULT 'open';
ALTER TABLE low_reports ADD COLUMN restocked_at TEXT;
```
Speaker notes: Here is the whole change. Two statements. The status column is not null, so it needs a default, and every existing report gets open. On the build machine, SQLite refused a not null column with no default on a table that already had rows, with the message cannot add a not null column with default value null. The runner wraps both statements and the version record in one transaction, so they all commit or none do.
Image: None. This slide is code.
---
## Slide 6: On a copy
```
> python migrate.py parts-copy.db
database         parts-copy.db
current version  1
backup written   parts-copy.db.before-v2.bak
applied          002_add_status.sql
now at version   2
```
Speaker notes: Real output, on a copy of the practice database. It reads the current version, writes a backup before it changes anything, applies the one pending script, and reports the new version. Then I list the rows. Five before, five after, each one with status open. That row count is the check you run every single time.
Image: None. This slide is code.
---
## Slide 7: Run it again
```
> python migrate.py parts-copy.db
database         parts-copy.db
current version  2
nothing to apply
```
Speaker notes: Now I run exactly the same command again, the way a nervous person or a deploy script would. Nothing happens, and that is the point. The database already says it is at version two, so there is nothing to apply. Running it twice is safe. That property is what lets you put the migration step into your deployment steps without worrying about it.
Image: None. This slide is code.
---
## Slide 8: The other wrong way
```
> python wrong_ways.py twice wrong2.db
sqlite3.OperationalError: duplicate column name: status

> python migrate.py wrong2.db
FAILED           002_add_status.sql: duplicate column name: status
nothing from that migration was kept. The backup is untouched.
```
Speaker notes: The second wrong way is a bare alter table with no record that it ran. The first time it works. The second time it crashes with duplicate column name. And look what happens next. The real migration now fails on that copy, because somebody changed the table by hand. The rollback worked, so nothing half-finished was kept. The lesson: every schema change goes through a numbered script, or none do.
Image: None. This slide is code.
---
## Slide 9: Releasing it for real
- Back up the deployed database first [VERIFY]
- Migration first, new code second
- Check the old reports are still there
- Events log line: planned, the same day
Speaker notes: Once the copy is right, the real release follows your written deployment steps. Back up the deployed database, and how you do that depends on your host, so that step is marked verify. Run the migration before you deploy the code that uses the new column, or the new code asks for a column that is not there yet. Open the board and check the old reports. Then write the planned release in your events log that day. If your host will not let you run a command, do it on the lab machine copy and say what is unverified.
Image: A four-step checklist with a database, an arrow, a web page, and a logbook.
---
## Slide 10: What you are about to build
- src/migrations/001 matching what is deployed now
- A schema_version table and a migration runner
- Your Week 12 change as 002, with a default
- Test on a copy, twice, count the rows
- Commit the scripts, never the database
Speaker notes: Here is the build period. Write your current schema as migration one, so it matches what is deployed. Add the version table and a runner, and you may adapt the one in the clinic folder if you record where it came from. Write this week's change as migration two, with a default. Test it on a copy, run it twice, and count the rows before and after. Add the step to your architecture's deployment steps. Commit the scripts. Never commit the database file.
Image: A folder tree showing src, migrations, 001 and 002, with a database icon crossed out of the repository.
---
