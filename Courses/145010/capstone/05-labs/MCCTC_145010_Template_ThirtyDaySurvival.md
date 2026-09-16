# Template · Thirty-Day Survival Record
## 145010 Senior Capstone · clock starts Week 11 or 12, record due Week 17, Friday

**Commit as:** `docs/control/thirty-day-record.md`, with the logs beside it in
`docs/control/survival/`.
**Due:** clock running by Week 12, Friday, at the latest. Events logged on the day they happen.
Record complete Week 17, Friday.
**Tools:** [`survival-files/`](survival-files/) has a one-shot health check, a report that reads
your logs, and invented sample logs to practice on.

**Competencies this evidences:** 2.13.5 (test the delivered application to assure it is fully
functional), 2.11.4 (gather and analyze data about a problem), 2.11.8 (document the problem and
the verified solution), 1.4.4 (hardware to support software), 2.12.3 (compare with expected
performance).

---

## Why this exists

**A project that works only while you watch it is a demo.** Your stakeholder needs one that works
on a Tuesday night when nobody is looking. Thirty days without a person stepping in is the
evidence that yours does.

**The evidence has to be written by the system, not by you.** "I checked it most days and it was
fine" is a claim. A log with a line every thirty minutes for five weeks is a record.

**The failure to avoid is starting late.** A clock started in Week 14 has no room for a single
problem.

---

## The rule, exactly

**Thirty consecutive calendar days** in which the deployed system runs without **manual
intervention**.

| Counts as manual intervention | Does not count |
|---|---|
| Restarting, rebooting, or replugging it because it stopped or froze | A planned release through your documented deployment steps, recorded on the day |
| Editing, deleting, or repairing data by hand to keep it working | A restart the system performs on its own because you designed it to |
| Recreating something that expired or disappeared | An idle free-tier service waking on a request within the time your requirements allow |
| Fixing the clock, the network settings, or a lost setting by hand | Corrections from usability testing, released through your documented steps |

**Any intervention resets the clock.** Record it in the events log the same day, write a
troubleshooting entry with the cause and the fix, and start counting again.

**The arithmetic.** Week 17, Friday is 42 days after Week 11, Friday and 35 days after Week 12,
Friday. A clock started in Week 11 survives a reset in its first 12 days. A clock started in Week
12 survives one only in its first 5. The latest start that can still close by Week 17, Friday is
Week 13, Wednesday, and it survives none.

---

## The three logs

### 1. The health log · written by the system

One line per check, on a fixed interval, in the shared format. Timestamps are program data.

```
2027-04-23T14:15:02  result=ok  status=200  ms=412
2027-04-23T14:45:02  result=fail  error=URLError
```

**The first two fields are required:** the timestamp and `result=ok` or `result=fail`. Anything
after that is yours to choose. Never write personal data, request contents, or secrets.

**How it gets written, by track:**
- **Full-Stack:** `health_check.py` run on a schedule against your health address, from an
  approved machine or a scheduler your host provides. [VERIFY which your instructor approves]
- **Industrial / HMI:** your logger service writes its own heartbeat line on its interval.
- **AI-Integrated:** your service writes its own line, or `health_check.py` checks its health
  address on a schedule.

### 2. The events log · written by you, on the day

One line per planned release or intervention.

```
2027-04-24T15:02:00  planned  released version 1.3.0 by the documented steps
2027-04-29T08:40:00  intervention  restarted the service by hand after it hung
```

**An intervention you leave out of this log is the most serious problem this record can have.**
If your health log shows a gap and your events log says nothing, the report counts it against
you. If your events log hides an intervention your commits reveal, the whole record loses its
value.

### 3. The troubleshooting log

Every intervention gets an entry in `troubleshooting-log.md`: the symptom, the method, the fix, and
what you changed so it does not happen again. See the
[Troubleshooting Log template](MCCTC_145010_Template_TroubleshootingLog.md).

---

## Running the report

From `survival-files/`, standard library only:

```
python survival_report.py --health <health log> --events <events log> --max-gap-minutes <n> --max-outage-minutes <n>
```

- **`--max-gap-minutes`** is the longest silence you allow between health lines. A little more
  than twice your check interval is usual. Thirty-minute checks suggest 75.
- **`--max-outage-minutes`** is the longest stretch of failed checks your requirements allow.
  Take it from your non-functional requirements, not from what makes the report pass.

**Practice on the invented samples first.** These are real outputs from the build machine:

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

The same health log with one more intervention, in the middle. The end of the output:

```
python survival_report.py --health sample-health-log.txt --events sample-events-late-intervention.txt --max-gap-minutes 75 --max-outage-minutes 60
```
```
run breaks          3
  2027-04-19T09:10:00  intervention: restarted the service by hand after it stopped answering
  2027-05-07T10:45:00  intervention: deleted old rows by hand because storage was full
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         18.1 days  (2027-04-19T09:10:00  to  2027-05-07T10:45:00)
thirty days reached no
```

**Read those two together.** One hand-deleted batch of rows in the middle of a good run cut the
record in half. The fix was not to leave it out of the log. The fix was a retention rule in the
code, designed in Week 10.

**And with no events log and a stricter outage limit.** The end of the output:

```
python survival_report.py --health sample-health-log.txt --max-gap-minutes 75 --max-outage-minutes 20
```
```
run breaks          3
  2027-04-24T17:00:02  unexplained gap of 2:00:00
  2027-04-28T18:00:02  failed checks for 1:00:00
  2027-05-24T16:00:02  unexplained gap of 3:00:00
longest run         25.9 days  (2027-04-28T19:00:02  to  2027-05-24T16:00:02)
thirty days reached no
```

The two-hour gap is a planned release, but without the events log nothing says so. **A release you
did not record looks exactly like an outage.**

The report exits with 0 when thirty days were reached and 1 when they were not.

---

```markdown
# Thirty-Day Survival Record · <project name>

## 1. Setup
- **Clock started:** Week <n>, <day>, at <the first health line's timestamp>
- **What writes the health log:** <health_check.py on a schedule / the service itself>
- **Check interval:** <minutes>
- **Where the logs live:** `docs/control/survival/`
- **Allowed gap:** <minutes>, because <reason>
- **Allowed outage:** <minutes>, from requirement NF<n>
- **How the system restarts itself:** <what you configured, and how you tested it>

## 2. Self-recovery test
*Proof that the system comes back without you. Planned and recorded as a planned event.*
- **What you did on purpose:** <pulled power / stopped the process / stopped the model server>
- **Week and day:** <...>
- **What the health log shows:** <the lines, pasted>
- **Came back without help:** <yes / no, and what you changed if no>

## 3. The report
*Pasted exactly, from the final run.*

    <survival_report.py output>

Command: `<the exact command>`   Run: Week 17, <day>

## 4. Every break, explained
| When | What the report says | What actually happened | Troubleshooting entry |
|---|---|---|---|
| | | | |

## 5. What this record does not show
- <for example: the checks came from the lab network, so they do not show whether the site was
  reachable from the stakeholder's building>
- <...>

## 6. Result
- **Longest unbroken run:** <days>
- **Thirty days reached:** <yes / no>
- **If no, what you changed, and what the stakeholder was told:** <...>
```

---

## Before you commit · self-check

- [ ] The clock started by Week 12, Friday.
- [ ] Every intervention is in the events log, with a troubleshooting entry.
- [ ] The allowed outage comes from your requirements, not from what passes.
- [ ] The report output is pasted exactly, with the command.
- [ ] Section 5 has at least one honest limit.
