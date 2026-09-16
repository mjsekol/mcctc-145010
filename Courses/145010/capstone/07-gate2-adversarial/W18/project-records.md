# Project records · Parts Counter Lookup
## 145010 Senior Capstone · Gate 2 source file · Week 18 · invented composite

**Everything in this folder is invented for a Gate 2 exercise.** Birchwood Auto Parts, its store
manager, its counter staff, the parts, the project, and the student do not exist. It is a composite
of the kind of capstone you finished this week.

These are extracts from the student's repository at the `capstone-final` tag, and from the records
the instructor holds. **This file lists every outcome the project's records contain.** Sections are
numbered so you can cite them.

---

## 1. The project

| | |
|---|---|
| Name | Parts Counter Lookup |
| Track | Full-Stack Application |
| Student | Tessa, senior |
| Stakeholder | the store manager, Birchwood Auto Parts |
| Users | the store's three counter staff |
| The problem, from the proposal | Customers bring old or superseded part numbers. Counter staff find the current part in a paper cross-reference binder of about 600 pages while the customer waits. |
| What was built | A web app on the store's internal network. Staff type an old or partial part number and see the current part, its shelf location, and whether it is in stock. |

## 2. Permission to share · meeting record MR-09, Week 17, Friday

The store manager's answers, recorded in the meeting record and confirmed by school email the same
day.

| Question | Answer |
|---|---|
| May the project be described in a portfolio, résumé, or interview? | Yes |
| May the business be named? | **No.** Describe it as "a local auto parts store" |
| May the store manager or any staff member be named or described? | **No** |
| May the store manager's words be quoted? | Yes, attributed to "the store manager" only |
| Screenshots? | Only with invented data |
| A link to the live tool? | No. It is internal to the store |
| May the repository be public? | Yes, after the instructor removes the store's parts data file, which belongs to the store |

## 3. Acceptance · `docs/control/acceptance-record.md`

```
Criteria in the signed agreement:     7
First run, Week 16, Wednesday:        PASS 5   FAIL 2   NOT RUN 0
  AC-4 FAIL  a partial old number (first five characters) returned no results
  AC-7 FAIL  on the counter's older tablet, the results table ran past the right edge
Correction for AC-4, Week 16, Thursday: re-run PASS
Whole procedure re-run, Week 16, Thursday: PASS 6   FAIL 1
Known and not fixed: AC-7, moved to future improvements, agreed with the store manager
Decision: accepted with agreed follow-up, Week 16, Friday, in writing
In the store manager's words: "It does what we agreed. The old-number search is the part we will
use most."
```

## 4. Usability · `docs/control/usability/findings.md`, Week 15

```
Participants: P1, P2, P3 counter staff (real users) · P4 adult in the building · P5 student in another program

T1  look up an old part number and read out the current one      5 of 5 completed
T2  the first match is out of stock; find one that is in stock   3 of 5 completed
      P2 and P4 chose the out-of-stock match
      P2, debrief, opinion: "I'd want the one we have on the shelf at the top."
T3  keyboard only: look up a partial number                       5 of 5 completed

Change: in-stock matches listed first (from T2)
Re-test of T2 with two new participants: 2 of 2 completed
```

## 5. Baseline and the repeated measurement · `docs/measure/baseline.md`

```
What was measured:  seconds from being handed an old part number to reading out the correct
                    current part, stopwatch, 10 prepared lookups, 2 counter staff
Week 9, the paper binder:     median 94 seconds
Week 17, Parts Counter Lookup: median 31 seconds
Limits, as written by the student:
  - two staff members and ten prepared lookups
  - the same ten lookups both times, so staff may have remembered some answers
  - measured at a quiet time, not during real customer traffic
```

## 6. Thirty-day record · `docs/control/thirty-day-record.md`

```
First clock:   started Week 11, Thursday. Reset Week 12, Monday.
  E-3  the host machine restarted for an update, and the app was not set to start again
       by itself. Fix: the start command now runs at startup. Recorded in the events log
       and the troubleshooting log.
Second clock:  started Week 12, Tuesday. Closed Week 17, Friday.
Unbroken run:  38 days, no manual intervention
Lookups recorded by the app's own events log, last 30 days of the run:  212
Busiest single day in that window:  19 lookups
```

## 7. Licensing statement, summary · `LICENSING.md`

*The student's file carries the line: "This is a record of the licenses in this project, written
by a student who is not a lawyer. It is not legal advice."*

| Part | Owner or source | License |
|---|---|---|
| The project's own code | Tessa | MIT, as agreed in the acceptance agreement |
| Flask 3.1 | the Pallets project | BSD-3-Clause |
| Jinja2 | the Pallets project | BSD-3-Clause |
| Werkzeug | the Pallets project | BSD-3-Clause |
| gunicorn | the gunicorn project | MIT |
| SQLite | the SQLite project | public domain |
| The cross-reference parts data | the store | used with written permission, internal use only, not published |
| Fonts and icons | none added; system fonts only | |

How the list was produced: from `requirements.txt`, and each license read from the license file that
shipped with the package.

## 8. AI usage, summary · `ai-usage-log.md`

```
Tool: a local model on the lab's own hardware. No commercial AI account.
Entries: 14

A1  Week 11  Generated the first draft of search_parts(), the main search function.
             What I changed: Peer Code Review 1 (Week 13) found it built SQL with string
             formatting. I rewrote the query with parameters.
             How I verified: test cases T-04 to T-09, all passing after the rewrite.
A2  Week 11  Generated the first draft of import_xref.py, the script that loads the store's
             cross-reference file.
             What I changed: added a check that rejects duplicate rows.
             How I verified: imported the invented 40-row test file and compared counts.
A3  Week 17  Drafted the first version of user-guide.md.
             What I changed: rewrote it in four passes, recorded in the decision log.
A4-A14       Explanations of error messages and of a CSS layout problem. No code copied.
```

## 9. Recognition and contact

```
Week 17, Friday   thank-you email from the store manager, through the school (MR-09)
Week 18, Friday   thank-you notes sent to the store manager and to all five participants
```
