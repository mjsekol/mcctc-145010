# Clinic · Health Checks and the Thirty-Day Clock
## 145010 Senior Capstone · Week 11, Thursday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 11, Thursday, or any week the room shows this signal: health routes
that return "ok" without checking anything, and clocks not started.
**If you missed it,** you can learn the skill from this file alone. You need the skeleton from
[`clinic-w11-skeleton/`](clinic-w11-skeleton/) and the tools in
[`05-labs/survival-files/`](../05-labs/survival-files/).
**Competencies:** 2.13.5 (test the delivered application), 2.11.4 (gather and analyze data about a
problem), 2.11.8 (document the problem and the verified solution), 2.12.3 (compare with expected
performance), 1.4.4 (system hardware to support software applications)

---

## Why this exists

**Your capstone has to survive thirty days without you.** The only believable evidence is a log the
system writes by itself, a line every thirty minutes, for weeks. "I checked it most days" is a claim.
A health log is a record.

That log is only as honest as the thing it checks. **A health route that returns "ok" without
touching anything will log "ok" while every visitor sees an error.** Thirty days of that is thirty
days of nothing.

And the clock has a deadline. Started this Friday, Week 11, it has 42 days to reach Week 17, Friday,
so it survives a reset in its first 12 days. Started a week later, it survives one only in its first
5. **Every day you wait is margin you do not get back.**

---

## The skill in plain language

**A health endpoint answers one question: could this system do its job right now?**

- It **touches the real dependency**: the database table the main page reads, the model server, the
  sensor's latest reading.
- It answers **200** when the answer is yes and **an error status, such as 503**, when it is no.
- It says **which version** is running.
- It never returns personal data, secrets, file paths, or full error messages.

**`health_check.py` calls that endpoint once and appends one line** to a health log. A scheduler
runs it every thirty minutes. **`survival_report.py` reads the health log and your events log** and
reports the longest run without manual intervention. Both are in
[`05-labs/survival-files/`](../05-labs/survival-files/), with instructions in the
[Thirty-Day Survival Record](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md).

**The events log is yours to write, on the day.** One line for every planned release and every
intervention. An intervention is a person restarting, repairing, clearing, or hand-editing the
running system to keep it working. A planned release through your documented steps is not one. A
restart the system does by itself is not one.

---

## Worked example 1 · a health route that touches the database

From the skeleton, [`skeleton.py`](clinic-w11-skeleton/skeleton.py):

```python
@app.get("/health")
def health():
    """Touch the real dependency: the same table the home page reads."""
    try:
        with closing(connect()) as conn:
            count = conn.execute("SELECT COUNT(*) FROM bins").fetchone()[0]
    except sqlite3.Error as err:
        # Report the kind of failure, never the path or the full message.
        return {"status": "fail", "database": type(err).__name__, "version": VERSION}, 503
    return {"status": "ok", "database": "ok", "bins": count, "version": VERSION}
```

It reads **the same table the home page reads**. If the page would fail, health fails.

---

## Worked example 2 · running the check against three states

The skeleton was started on the health-demo port, 8160, from `05-labs/survival-files/` in
PowerShell (after `python setup_db.py` in the skeleton folder):

```
$env:PORT = "8160"
python ..\..\03-lecture-notes\clinic-w11-skeleton\skeleton.py
```

Then, in a second terminal in `05-labs/survival-files/`, the check ran three times. **The first field
of each line is your machine's date and time. It is written as `<time>` below.**

**State 1, healthy:**

```
python health_check.py --url http://127.0.0.1:8160/health --log health-log.txt
```

```
<time>  result=ok  status=200  ms=23
```

Exit code 0.

**State 2, database missing.** The server was stopped, `$env:PARTS_DB` was pointed at a folder that
does not exist, and the server was started again. Same command:

```
<time>  result=fail  status=503  ms=37
```

Exit code 1. The server answered, and it answered honestly.

**State 3, nothing listening.** The server was stopped. Same command:

```
<time>  result=fail  error=URLError
```

Exit code 1. `health-log.txt` now held all three lines, in order. The log file was deleted after the
run, and `netstat -ano | findstr LISTENING | findstr :8160` printed nothing: port free.

---

## Worked example 3 · starting the clock, and reading the report

**These logs are invented, for the composite Parts Bin Board.** They cover its first four days:
[`clinic-health-log.txt`](clinic-w11-skeleton/clinic-health-log.txt) and
[`clinic-events-log.txt`](clinic-w11-skeleton/clinic-events-log.txt). The events log:

```
2027-04-16T14:05:00  planned  self-recovery test: stopped the process on purpose, it restarted on its own
2027-04-19T08:12:00  intervention  restarted the service by hand after it stopped answering
```

The clock started at the first health line, on the Friday of Week 11. The self-recovery test is a
**planned** event: the student stopped the process on purpose to prove the host restarts it. On
Monday the service hung and the student restarted it by hand. That is an **intervention**, and it
went in the log that morning.

From `05-labs/survival-files/`:

```
python survival_report.py --health ../../03-lecture-notes/clinic-w11-skeleton/clinic-health-log.txt --events ../../03-lecture-notes/clinic-w11-skeleton/clinic-events-log.txt --max-gap-minutes 75 --max-outage-minutes 60
```

```
health lines        193  (4 failed)
observed            2027-04-16T13:30:02  to  2027-04-20T13:30:02
planned releases    1
interventions       1
run breaks          2
  2027-04-19T06:30:02  failed checks for 2:00:00
  2027-04-19T08:12:00  intervention: restarted the service by hand after it stopped answering
longest run         2.7 days  (2027-04-16T13:30:02  to  2027-04-19T06:30:02)
thirty days reached no
```

Exit code 1. **On day four, "no" is expected.** What matters is the arithmetic. The reset fell 3
days after the start, inside the 12-day margin. The new start is Week 12, Monday. Thirty days from
there is Week 16, Wednesday, 9 days before the record is due. The student also writes a
troubleshooting entry and fixes the cause, because a second reset eats most of that margin.

---

## The wrong version, and what it costs

**Wrong 1: a health route that checks nothing.**
[`skeleton_wrong.py`](clinic-w11-skeleton/skeleton_wrong.py) has `return "ok"` as its health route.
Started from `03-lecture-notes/` on port 5331, where its relative database path finds nothing:

```
python health_check.py --url http://127.0.0.1:5331/health --log health-log.txt
```

```
<time>  result=ok  status=200  ms=23
```

At the same moment the home page answered **500** with
`sqlite3.OperationalError: no such table: bins`. **The health log said the system was fine while it
served nobody.** Thirty days of those lines would be worth nothing.

**Wrong 2: leaving the intervention out of the events log.** The same invented week, with Monday's
restart missing ([`clinic-events-log-incomplete.txt`](clinic-w11-skeleton/clinic-events-log-incomplete.txt)).
The end of the report:

```
interventions       0
run breaks          1
  2027-04-19T06:30:02  failed checks for 2:00:00
longest run         2.7 days  (2027-04-16T13:30:02  to  2027-04-19T06:30:02)
thirty days reached no
```

The two hours of failed checks still break the run. The health log caught the outage anyway. Now
the events log says nobody touched the system while the evidence says somebody must have. The rubric
drops the survival score to 0-1 when an intervention the events log leaves out is revealed by other
evidence.

---

## Why the wrong version is tempting

**`return "ok"` is one line and it always passes.** A real check can fail, and a failing check
feels like a problem you created. It is a problem you found.

**Leaving out a restart feels harmless.** It was five minutes. But the clock rule is about honesty,
not about five minutes, and a record with one hidden restart is not a record.

---

## Do this today

1. Make your `/health` touch the real dependency and answer 503 when it cannot.
2. Run `health_check.py` against it locally on an explicit port, in all three states above.
3. Decide with your instructor what runs the check every thirty minutes: a scheduled task on an
   approved lab machine, or your host's scheduler. [VERIFY which is available and approved] Until it
   is set up, the clock has not started.
4. Start `docs/control/thirty-day-record.md` from the
   [template](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md). Fill in section 1. Put the
   logs in `docs/control/survival/`.
5. Start `docs/control/survival/events-log.txt` with your first planned event.
6. Plan your self-recovery test for Friday and record it as planned.
7. **Commit.** Tomorrow, Friday, the clock should be running.

---

## If you are ahead, if you are behind

**If you are ahead:** run the self-recovery test today. Stop the process on purpose, record it as a
planned event, and check the health log shows the system came back without you.

**If you are behind:** your skeleton is not deployed. Run the report on the invented clinic logs so
you know how to read it, and put deploying first in tomorrow's plan. The clock must start by Week 12,
Friday.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Test the delivered application** | A health check against the deployed system, every thirty minutes (2.13.5) |
| **Gather and analyze data** | The health log and the report built from it (2.11.4) |
| **Compare with expected performance** | The allowed outage from your requirements, set in `--max-outage-minutes` (2.12.3) |
| **Document the verified solution** | The troubleshooting entry for every intervention (2.11.8) |
| **Hardware to support software** | The machine or host that runs your service and your scheduled check (1.4.4) |

---

## Self-check

**1.** A classmate's health route runs `SELECT 1`. Their home page reads the `shifts` table. Name a
failure their health log would miss.

**2.** Your service stopped at 2 a.m. and your host's restart policy brought it back at 2:01. Is that
an intervention?

**3.** You start your clock on Week 12, Friday. You restart the service by hand on Week 13, Thursday.
Can the record still reach thirty days by Week 17, Friday?

### Answers

**1.** A missing or wrong `shifts` table, or a database path that points at a new empty file.
`SELECT 1` succeeds on any open connection, so health says ok while the page fails. The check should
read the table the page reads.

**2.** No. A restart the system performs by itself, because you designed it to, is not manual
intervention. Log it anyway, so the record explains the failed line.

**3.** No. Week 13, Thursday is 6 days after the start, past the 5-day margin. Thirty days from Week
13, Thursday is Week 17, Saturday, one day late. The record shows the longest unbroken run and the
reset, honestly, and the rubric scores what it shows.
