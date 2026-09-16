# Clinic · Closing the Thirty-Day Record
## 145010 Senior Capstone · Clinic · Week 17, Tuesday

**The signal:** health logs that have been collecting for weeks and have never been run through the
report. The thirty-day record is due Friday.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. Every report below is real output
from `survival_report.py`, run on the build machine from inside
[`05-labs/survival-files/`](../05-labs/survival-files/README.md) on its **invented** sample logs.
Nothing in those files is a real system or a real organization.

**Competencies:** 2.13.5 (test the delivered application to assure it is fully functional), 2.11.4
(gather and analyze data about the problem), 2.11.8 (document the problem and the verified
solution), 2.12.3 (compare with expected performance), 1.4.4 (use system hardware to support
software applications)

---

## The idea in plain language

**You run the report on your real logs, paste its output exactly, and explain every break it lists.**
The report answers one question: what is the longest stretch your deployed system ran without a
person stepping in? The template is the
[Thirty-Day Survival Record](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md).

## Why it exists

**A project that works only while you watch it is a demo.** The record is the evidence that yours
kept working on nights and weekends. It has to be written by the system, not by you, and it has to
be honest, because the rubric drops part 2B to 0-1 if an intervention your events log left out shows
up in other evidence.

**The rule, exactly.** Thirty consecutive calendar days with no manual intervention. A planned
release through your documented steps does not count. A restart the system does on its own does not
count. A restart, repair, or hand edit by a person does, and it resets the clock.

---

## The command, and what the two limits mean

From inside `survival-files/`, standard library only:

```
python survival_report.py --health <health log> --events <events log> --max-gap-minutes <n> --max-outage-minutes <n>
```

- **`--max-gap-minutes`** is the longest silence you allow between health lines. A little more than
  twice your check interval is usual. Thirty-minute checks suggest 75.
- **`--max-outage-minutes`** is the longest stretch of failed checks **your requirements** allow.
  It comes from your non-functional requirements, not from whatever makes the report pass.

The report exits with 0 when thirty days were reached and 1 when they were not.

---

## Worked example 1 · a record that reaches thirty days

```
python survival_report.py --health sample-health-log.txt --events sample-events.txt --max-gap-minutes 75 --max-outage-minutes 60
```

```
health lines        1913  (2 failed)
observed            2027-04-16T15:00:02  to  2027-05-26T15:00:02
planned releases    2
interventions       1
run breaks          2
  2027-04-19T09:10:00  intervention: restarted the service by hand after it stopped answering
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         35.3 days  (2027-04-19T09:10:00  to  2027-05-24T16:00:02)
thirty days reached yes
```

Exit code 0. **Read it top to bottom.** Two failed checks in 1913. Two planned releases, which did
not break anything. One intervention three days in, which reset the clock. Then 35.3 days unbroken,
ended by a three-hour silence nobody explained.

**Section 4 of the record, "every break, explained," for this output:**

```
| When                 | What the report says        | What actually happened                              | Troubleshooting entry |
| 2027-04-19T09:10:00  | intervention                | service stopped answering; restarted by hand; auto-restart was not configured yet | TS-6 |
| 2027-05-24T16:00:02  | unexplained gap of 3:00:00  | <find out: the checking machine, the network, or the app?> | <write one> |
```

**The second row is the one people leave blank.** A gap means the health log went silent, which is
not the same as the app being down. The checking machine could have been off. Find out, write it
down, and say what you cannot know. The run still reached thirty days before the gap.

## Worked example 2 · one hand fix in the middle

The same health log, with one more line in the events log: rows deleted by hand because storage was
full.

```
python survival_report.py --health sample-health-log.txt --events sample-events-late-intervention.txt --max-gap-minutes 75 --max-outage-minutes 60
```

```
health lines        1913  (2 failed)
observed            2027-04-16T15:00:02  to  2027-05-26T15:00:02
planned releases    2
interventions       2
run breaks          3
  2027-04-19T09:10:00  intervention: restarted the service by hand after it stopped answering
  2027-05-07T10:45:00  intervention: deleted old rows by hand because storage was full
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         18.1 days  (2027-04-19T09:10:00  to  2027-05-07T10:45:00)
thirty days reached no
```

Exit code 1. **One hand fix cut the record in half.** The fix is not to leave that line out of the
events log. The fix is a retention rule in the code, so the system deletes old rows by itself. In the
record, section 6 says "no," gives the 18.1-day run, and says what changed and what the stakeholder
was told.

## Worked example 3 · the same log, without the events log

```
python survival_report.py --health sample-health-log.txt --max-gap-minutes 75 --max-outage-minutes 20
```

```
health lines        1913  (2 failed)
observed            2027-04-16T15:00:02  to  2027-05-26T15:00:02
planned releases    0
interventions       0
run breaks          3
  2027-04-24T17:00:02  unexplained gap of 2:00:00
  2027-04-28T18:00:02  failed checks for 1:00:00
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         25.9 days  (2027-04-28T19:00:02  to  2027-05-24T16:00:02)
thirty days reached no
```

**Look at the first break.** A two-hour gap starting at `2027-04-24T17:00:02`. In example 1 it was not a break, because
the events log records a planned release inside it. Without the events log, nothing says so. **A
release you did not record looks exactly like an outage.**

---

## The wrong version, and what it produces

A student's requirements say NF2: "the sign-up is unavailable for no more than 20 minutes at a
time." They run the report with the requirement's number:

```
python survival_report.py --health sample-health-log.txt --events sample-events.txt --max-gap-minutes 75 --max-outage-minutes 20
```

```
run breaks          3
  2027-04-19T09:10:00  intervention: restarted the service by hand after it stopped answering
  2027-04-28T18:00:02  failed checks for 1:00:00
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         25.9 days  (2027-04-28T19:00:02  to  2027-05-24T16:00:02)
thirty days reached no
```

(These are the last lines of the output. The first four lines match example 1.)

Then they change `--max-outage-minutes` to 60 and paste example 1's output, `thirty days reached yes`.

**What it produces:** a record that contradicts the requirements it sits next to. The hour of failed
checks starting at `2027-04-28T18:00:02` broke NF2, and the report said so. Changing the limit did not change what
happened to users. A reviewer who reads NF2 and then the command sees it in one line. The honest
record says "25.9 days, no," explains the hour-long outage, and names what changed.

## Why the wrong version is tempting

Both numbers look like settings, and "yes" is one flag away. It is also Week 17, and there is no time
left to earn thirty days again. **The rubric gives 4-5 points for a 21 to 29 day run with a complete,
honest record.** A manufactured "yes" risks the whole part.

---

## What to do in your project today

1. Practice first: run examples 1 and 2 yourself on the sample files and check you get the same
   output.
2. Copy your real health log and events log into `docs/control/survival/`.
3. Take `--max-outage-minutes` from your non-functional requirements. Write which one.
4. Run the report. Paste the output exactly, with the exact command, into section 3 of the record.
5. Fill in section 4: one row per break, each with what actually happened and a troubleshooting
   entry. See the [Troubleshooting Log template](../05-labs/MCCTC_145010_Template_TroubleshootingLog.md).
6. Section 5: at least one honest limit, such as where the checks came from.
7. Section 6: the longest run, yes or no, and if no, what changed. Tell your stakeholder in Friday's
   update. Commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Health log** | Lines the system writes by itself on a fixed interval: time and ok or fail |
| **Events log** | Lines you write on the day: each planned release and each intervention |
| **Manual intervention** | A person restarting, repairing, clearing, or hand-editing the running system |
| **Run break** | Anything that ends an unbroken run: an intervention, a long gap, or a long outage |
| **Unexplained gap** | A silence in the health log that no planned release covers |
| **Longest run** | The longest stretch with no break, the number the rubric scores |

---

## Check yourself

1. Your health log checks every 15 minutes. What `--max-gap-minutes` would you start with, and why?
2. The report shows an unexplained gap on a night you remember releasing a new version. What do you
   do, and what do you not do?
3. Why does the report treat a long gap as a break, even though the app might have been fine?

---

## Check your answers

**1.** About 35, a little more than twice the interval, so one missed check is tolerated and two in a
row is not. Write the reason in section 1 of the record.

**2.** Check your commits and deployment log for that night. If the release really happened through
your documented steps, it should have been in the events log, so section 4 says the release was not
logged on the day, gives the evidence, and the lesson. Do not add a back-dated events line and
present it as written on the day. The rubric depends on the events log being honest.

**3.** Because the health log is the only evidence, and a silence is missing evidence. The report
cannot tell a sleeping checker from a dead app. Treating the gap as a break keeps the record from
claiming time nobody observed. Your job is to explain the gap in section 4.
