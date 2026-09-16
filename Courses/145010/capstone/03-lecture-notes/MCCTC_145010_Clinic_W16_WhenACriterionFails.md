# Clinic · When a Criterion Fails
## 145010 Senior Capstone · Clinic · Week 16, Thursday

**The signal:** a Wednesday acceptance run with a FAIL in it, or a student who wants to "fix it quickly
and change the record." The acceptance record is due tomorrow.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The code in example 1 was run on
the build machine with Python 3.13 and Flask 3.1, using Flask's test client, and the output is pasted
exactly.

**Competencies:** 2.12.5 (make corrections indicated by test results), 2.12.6 (seek stakeholder
acceptance upon successful completion of the test plan), 2.12.1 (the agreed procedure, used as
agreed), 1.10.4 (procedures for initiating product and service improvements), 2.11.1 (identify the
problem)

**Every example below is a composite.** The Northside Community Garden is an invented organization.

---

## The idea in plain language

**A failed criterion has three honest outcomes, and one dishonest one.** You fix it and re-run it.
You agree with the stakeholder, in writing, to accept it with a follow-up. Or it stays not accepted,
recorded with the reason. **The dishonest outcome is changing the criterion so that it passes.** It
is never an option.

## Why it exists

Something failing in the acceptance run is normal. It is the reason the run exists. What your
Stakeholder Outcome score measures is what you did next.

**The rubric is blunt about this.** A criterion quietly edited so that it passes scores 0 on
acceptance. A criterion that failed and is recorded honestly costs far less. See
[the Capstone Rubric, part 3A](../09-project/MCCTC_145010_Capstone_Rubric.md#3a-acceptance-against-the-agreed-criteria--10-points).

**Remember the surprise-failure rule from yesterday.** A failure is written down, not fixed in front
of the stakeholder. Today is the "afterward."

---

## Worked example 1 · fix, re-run, record

AC-4 said: given the database is unavailable, when a volunteer opens the sign-up page, then the page
says "Sign-up is down, try again in a few minutes." On Wednesday the page showed a server error
instead.

**Identify the problem first (2.11.1).** The route opened the database with no handling for failure.
Here is the route as it was, reduced to the part that matters, with the database made unreachable on
purpose:

```python
@app.get("/beds")
def beds():
    rows = open_beds()
    return {"open": [r[0] for r in rows]}
```

Flask's test client, first lines of the response body:

```
500 <!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
```

The fix adds a handler for that one kind of failure:

```python
@app.errorhandler(sqlite3.OperationalError)
def database_down(error):
    app.logger.error("database unavailable: %s", error)
    return "Sign-up is down, try again in a few minutes.", 503
```

The same request after the fix, with the log line first:

```
ERROR database unavailable: unable to open database file
503 Sign-up is down, try again in a few minutes.
```

**The record, section 4 of the [Acceptance Record](../05-labs/MCCTC_145010_Template_AcceptanceRecord.md):**

```
### Correction for AC-4
- What failed: with the database stopped, the page showed "Internal Server Error"
- What I changed: app.py, added database_down handler, commit 3be90a1
- Re-run: Week 16, Thursday, PASS, page showed "Sign-up is down, try again in a
  few minutes." with status 503; log line has no volunteer data

Whole procedure re-run after the last correction: Week 16, Thursday, commit 3be90a1
After corrections: PASS 5  FAIL 0  NOT RUN 1   (AC-6 still to run, see example 2)
```

**Two details matter.** The re-run was with the stakeholder or sent to them in writing, not run alone
and recorded as if they watched. And the correction was released through your documented deployment
steps and logged as a planned release, so the thirty-day clock keeps running.

## Worked example 2 · a fix that cannot land by Friday

AC-6 needs a coordinator export in the format the garden's printer software reads. When AC-6 was
finally run on Thursday, it failed, and the student found that the format needs a library the lab
machines do not allow.

```
## 5. Known and not fixed
| Item | Why it is not fixed | What was agreed |
| AC-6 export format | Needs a library not approved for lab machines; found Week 16 Thu | Accepted with follow-up: a plain table export by Week 17 Fri, which the coordinator prints by hand; the printer format goes to future improvements FI-7 |

## 6. The stakeholder's decision
- Decision: accepted with agreed follow-up
- In their words: "The table is fine for now. The sign-up is the part we need."
- Follow-up agreed: plain table export, Week 17, Friday
- Given: Week 16, Friday, in writing
```

**The result:** an honest record with a known issue in it. The Control phase guide says it plainly: a
record with a known issue in it is an honest record, not a weak one. The rubric's top band allows
"all but one with an agreed plan in the record."

## Worked example 3 · the criterion itself was wrong

AC-2 said the coordinator page updates "within 1 second." During the run the stakeholder said, "I
meant when I reload it, not while I'm watching." The case was recorded as NOT RUN before anyone ran
it, and the change went through a change request:

```
## CR-5 · AC-2 timing means "after reload"
Raised: Week 16, Wednesday   By: stakeholder, during the acceptance run
Type: change a criterion
What is asked for: AC-2's "within 1 second" means the claim shows after the
coordinator reloads, not live.
Why: the stakeholder's words during the run, recorded in the acceptance record section 3
Acceptance criteria: AC-2 before: "...within 1 second." After: "...when the
coordinator reloads the page."
Decision: agreed   Agreed by: garden coordinator, Week 16, Thursday, by school email
Acceptance agreement version after this change: 1.2
```

**Then AC-2 is run against the new wording**, and the record shows both the NOT RUN and the later
result. Nothing was changed quietly, and both parties agreed in writing first. The
[Change Request template](../05-labs/MCCTC_145010_Template_ChangeRequest.md) has the form.

---

## The wrong version, and what it produces

```
test-plan.md, section 7, edited Thursday night:
  before: AC-4 | ... | What you should see: "Sign-up is down, try again in a few minutes"
  after:  AC-4 | ... | What you should see: an error page

acceptance-record.md:
| AC-4 | PASS | error page shown |
First run: PASS 5  FAIL 0  NOT RUN 1
```

**What it produces:** a record that disagrees with the committed procedure the stakeholder agreed,
which your commit history shows. The rubric scores acceptance at 0 for a criterion edited after the
fact. The volunteer who meets a server error on a real Saturday is the person the criterion was
written to protect. And the panel question "Did anything fail in acceptance?" now has only bad
answers.

## Why the wrong version is tempting

The deadline is tomorrow, the failure feels like a mark against you, and the edit is one line. It
also feels harmless, because an error page is "sort of" an error message. **It is not the message the
stakeholder signed for, and the commit history keeps the original.** Honest failure is scored.
Hidden failure is found.

---

## What to do in your project today

1. List every FAIL and NOT RUN from your run sheet.
2. For each FAIL, identify the problem and write a troubleshooting entry with the
   [Troubleshooting Log template](../05-labs/MCCTC_145010_Template_TroubleshootingLog.md).
3. Fix what can be fixed today. Release through your documented steps. Log the release as planned.
4. Re-run each fixed case with the stakeholder or in writing, then re-run the whole procedure.
5. Anything that cannot be fixed by Friday goes in section 5 with what you and the stakeholder agreed.
6. Any wrong criterion goes through a change request, agreed in writing, before it is run again.
7. Tell the stakeholder in plain words, using the bad-news section of the
   [Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#3-bad-news-we-are-behind).
8. Complete sections 4 to 6 of the record. The signed copy goes to your instructor.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Correction** | A change made because a test failed, with a re-run under it |
| **Re-run** | Running the failed case again after the correction |
| **Known and not fixed** | Section 5 of the record: what still fails and what was agreed |
| **Accepted with agreed follow-up** | The stakeholder accepts, with a specific promise and date |
| **Change request** | The written, agreed way a criterion changes |

---

## Check yourself

1. Your correction works on your laptop. Is the correction done?
2. The stakeholder says, "Do not worry about AC-6, mark it passed." What do you record?
3. Which of these is allowed after a FAIL: editing the criterion, recording NOT RUN, fixing and
   re-running, or accepted with follow-up? Explain the one that is not.

---

## Check your answers

**1.** No. It is done when it is released to the deployed system through your documented steps, the
failed case is re-run there with the stakeholder or in writing, the whole procedure is re-run, and all
of it is in section 4.

**2.** You record what was seen, FAIL, and their decision in their own words, for example "accepted
with AC-6 not passed, stakeholder says it is not needed." You never write PASS for a case that did not
pass. If they want AC-6 removed, that is a change request, agreed in writing.

**3.** Recording NOT RUN (when the case could not be run or is wrong), fixing and re-running, and
accepted with follow-up are all allowed. Editing the criterion so it passes is not, because it
changes the agreement one party signed without that party's written agreement.
