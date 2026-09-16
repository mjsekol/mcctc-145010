# Clinic · Responding to a Review
## 145010 Senior Capstone · Clinic · Week 13, Thursday

**The signal:** authors arguing with their reviewer on Wednesday, or an author response section that
is still empty on Thursday. The author response is due Friday.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The code fix in example 1 was run
on the build machine with Python 3.13, and the output is pasted exactly.

**Competencies:** 1.1.9 (give and receive constructive feedback to improve work habits), 1.2.7
(problem solving and consensus building to determine next steps), 1.2.12 (technical writing to
complete forms and reports), 2.12.5 (make corrections indicated by test results)

**The examples use the Northside Community Garden, an invented organization.** It is a composite.

---

## The idea in plain language

**Every finding gets one of three answers, in writing: accepted, rejected, or deferred.** Each answer
has a reason. An accepted finding also has a commit and a re-run. That table is section 7 of the
[Peer Code Review template](../05-labs/MCCTC_145010_Template_PeerCodeReview.md).

## Why it exists

A review is only worth something if it changes the code or changes your mind on purpose. The response
is the record of which one happened for each finding.

**You are allowed to reject a finding.** Reviewers are wrong sometimes. What you are not allowed to do
is ignore one. The template says a finding rejected without a reason is scored as ignored.

**The hard part is not technical.** Being told your code crashes feels personal, even when the
reviewer wrote it kindly. That feeling is normal. It passes faster if you write the response the next
day rather than in the moment.

---

## Worked example 1 · accepted, fixed, and re-run

Finding 1 from Wednesday said `average_wait` crashes on an empty list. The author fixed it:

```python
def average_wait(minutes):
    """Average wait at the garden tool shed, in minutes, or None before the first visit."""
    if not minutes:
        return None
    return sum(minutes) / len(minutes)

print(average_wait([4, 6, 11]))
print(average_wait([]))
```

Output:

```
7.0
None
```

The row in section 7:

```
| 1 | accepted | Returns None for no visits; dashboard shows "No visits yet".
    Added test T-14 (empty day) to the test plan; re-run PASS. | a1c9e04 |
```

**Three things make this row strong.** It says what changed. It points to a test that would have
caught the problem. It names a commit, so anyone can check. The hash here is an example.

## Worked example 2 · rejected, with a reason

Finding 5 said: "Consider storing volunteer phone numbers so the coordinator can text reminders."

```
| 5 | rejected | The signed requirements store first names only (requirements R2,
    data dictionary). Storing phone numbers adds personal data the stakeholder did not
    ask for, and scope is locked after Week 12. Added as FI-3 on the future
    improvements list. | none |
```

**The reason points at a document, not a feeling.** "I do not want to" is not a reason. "The signed
requirements say otherwise, and scope is locked" is. The idea is not lost either. It goes on the
future improvements list in the [Change Request template](../05-labs/MCCTC_145010_Template_ChangeRequest.md).

## Worked example 3 · deferred, with a reason and a date

Finding 3 said the page reloads the whole bed list after every claim.

```
| 3 | deferred | True, and measured: about 0.4 s on the lab machine with 12 beds, which
    meets NF1 (under 2 s). Fixing it means restructuring the page script. Deferred to
    Sprint 4, Tuesday, after the must-fix items; if Sprint 4 runs short it goes to
    future improvements. Decision log D-19. | none |
```

**A deferral is a plan, not a shrug.** It says why not now, when, and what happens if "when" never
comes. (The 0.4 seconds is a made-up example of the kind of number to write. Write the number you
actually measured.)

---

## Talking about it on Wednesday, before you write anything

During minutes 45-55 of the review, **the author asks questions and does not argue yet.** Three
questions that always help:

```
"Can you show me the input that caused it?"
"What would you expect it to do instead?"
"Is this a must fix because of a requirement, or because of how it could break later?"
```

If you still disagree after you understand the finding, that is fine. Write it down on Friday, with
your reason.

---

## The wrong version, and what it produces

```
## 7. Author response
| Finding # | Accepted / rejected / deferred | What I did, or why not | Commit |
| 1 | rejected | it works on my machine | |
| 2 | rejected | the comment is fine | |
| 3 | accepted | will fix | |
| 4 | | | |
| 5 | accepted | ok | |
```

**What it produces:**

- Finding 1 is a real crash with a real input. "Works on my machine" means the author never ran the
  reviewer's input. The crash is still there in Week 18.
- Finding 3 says "will fix" with no commit. That is a promise, and Review 2 checks for the fix.
- Finding 4 is blank, so it is scored as ignored.
- Finding 5 is "accepted" for a feature that adds personal data after scope lock. Accepting
  everything is as careless as rejecting everything.

## Why the wrong version is tempting

Defending your code feels like defending yourself. It is also Thursday, and you would rather build.
A one-word response takes ten seconds. **But Review 2, next Tuesday, reads this table first**, and so
does your instructor at Milestone Review 3.

---

## What to do in your project today

1. Open `docs/improve/peer-review-1.md` in your own repository and read every finding once, slowly.
2. Fix every **must fix** first. For each one, re-run the case that failed and add a test case to
   your [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md) if one was missing.
3. Decide the rest: accepted, rejected with a reason that points at a document, or deferred with a
   week and day.
4. Anything that would add scope goes on the future improvements list, not into the build.
5. Write section 7 by Friday. Commit it, and mention the review in your
   [Weekly Stakeholder Update](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md) in the
   stakeholder's words: "A classmate reviewed the code and found a crash on empty days. It is fixed."
6. Update your [Sprint Plan](../05-labs/MCCTC_145010_Template_SprintPlan.md) review with the hours the
   fixes took.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Author response** | Section 7 of the review: one row per finding, written by the author |
| **Accepted** | You agree and you changed the code, with a commit and a re-run |
| **Rejected** | You disagree, with a reason that points at evidence |
| **Deferred** | You agree, and it waits, with when and what happens if it never happens |
| **Re-run** | Running the case that failed again after the fix, and recording the result |

---

## Check yourself

1. A reviewer marks "the color of the Save button is ugly" as must fix. How do you respond?
2. Why is "accepted, will fix" a weak row, even when the author means it?
3. A finding would take four hours to fix and you have six hours left in Sprint 3. It is a should fix.
   Write the decision you would make and the one thing that must appear in the row.

---

## Check your answers

**1.** Ask what requirement or real-user problem makes it must fix. If there is none, reject it or
record it as a preference, with the reason: no requirement covers the color, and the web-check
contrast check passes. If the color fails contrast, it is a real accessibility finding and you accept
it.

**2.** It has no commit and no re-run, so nobody can check that the fix happened. Review 2 looks for
evidence, and a promise is not evidence.

**3.** Either decision can be right. Fixing it uses most of what is left and risks the must-fix work.
Deferring it keeps the must-fix work safe. The row must give the reason and a specific week and day,
or say it moves to the future improvements list if Sprint 4 runs short.
