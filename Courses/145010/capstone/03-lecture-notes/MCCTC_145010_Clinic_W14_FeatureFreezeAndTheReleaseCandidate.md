# Clinic · Feature Freeze and the Release Candidate
## 145010 Senior Capstone · Clinic · Week 14, Monday

**The signal:** Sprint 4 plans that still list new features. Real users see your project next Tuesday,
and Friday is the release candidate.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 1.10.4 (procedures for initiating product and service improvements), 1.2.7
(problem solving and consensus building to determine next steps), 2.12.3 (test cases compared with
expected performance), 2.12.5 (make corrections indicated by test results), 1.4.7 (productivity
tools to optimize assigned tasks)

**Every example below is a composite** built for this note. The Northside Community Garden is an
invented organization.

---

## The idea in plain language

**A feature freeze means the list of what the project does stops growing.** You still fix, finish,
and test. You do not start anything new.

**A release candidate is the version you would hand over if nothing else changed.** Every in-scope
requirement is implemented, and your own test plan has been run against it with the results written
down. It is called a candidate because testing with real people next week may still change it.

## Why it exists

Scope locked in Week 12. That rule said nothing new gets promised. The freeze is its partner: nothing
new gets built. Next week five real people use your project, and the week after your stakeholder runs
the acceptance procedure. **Every hour spent on a new feature this week is an hour not spent making
the promised features work.**

**BPA Nationals usually falls this week**, so confirm this year's date. If you compete, your
release candidate and your Week 14 update are due before you leave, and Peer Code Review 2 happens
the first day you are back, no later than Week 15, Tuesday.

---

## Worked example 1 · a Sprint 4 plan that respects the freeze

```
Sprint 4 · Week 14

Sprint goal: The volunteer sign-up is finished and tested, ready for five real users.

| # | Task                                                   | Hours | Traces to        |
| 1 | Fix Review 1 must-fix #1 (empty-day crash)             | 1     | R4, review 1     |
| 2 | Fix Review 1 must-fix #4 (delete without sign-in)      | 2     | R6, NF4          |
| 3 | Finish R7: coordinator exports the week as a table     | 3     | R7, scope lock   |
| 4 | Keyboard-only walkthrough of every main task, fix      | 2     | NF3              |
| 5 | Run the whole test plan on the deployed system         | 2     | release candidate|
|   | Total                                                  | 10    |                  |

If I run out of time, I cut first: task 3's column sorting (R7 still passes without it).
```

**Read the last column.** Every task points at a signed requirement, a non-functional requirement, or
a review finding. The total fits a week that loses Tuesday to Review 2. The cut line is named before
it is needed. The shape comes from the [Sprint Plan template](../05-labs/MCCTC_145010_Template_SprintPlan.md).

## Worked example 2 · a good idea on Tuesday

The coordinator replies to the Week 13 update: "Could it also email volunteers a reminder the night
before?"

The student's reply, adapted from the [Change Request template](../05-labs/MCCTC_145010_Template_ChangeRequest.md):

```
That is a good idea, and I have added it to the list of future improvements I will
hand over with the project. The scope was locked in Week 12 so that what we agreed
will be finished and tested properly before the acceptance check in Week 16.
```

And the file gets one new row:

```
| FI-4 | Email reminder the night before a shift | garden coordinator | fewer no-shows |
  arrived after scope lock; also needs volunteer email addresses, which R2 does not store |
```

**The result:** nothing new to build, the idea is recorded with who asked, and the stakeholder hears
a reason instead of a no.

## Worked example 3 · the release candidate, recorded

Friday's block in section 6 of the [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md), with
most of the passing rows left out to save space:

```
### Run 4 · Week 14, Friday · commit 7d2e1b0 · release candidate
| ID   | Result | What you actually saw                                   |
| T-01 | PASS   | claim saved, coordinator page shows it after reload     |
| T-07 | PASS   | second browser shows "This shift was already taken"     |
| T-11 | FAIL   | at 360 wide the week table is 288 px wider than screen  |
| T-15 | PASS   | web-check: 0 errors, 0 violations at 360, 768, 1280     |
| T-18 | NOT RUN| screen reader walkthrough; lab machine booked, moved to Mon |

Totals: PASS 14  FAIL 1  NOT RUN 1
Corrections made because of this run: T-11, table given max-width, re-run Mon.
```

**A release candidate with a FAIL in it is still a release candidate**, as long as the failure is
written down and planned. What it cannot have is a feature that was never finished, or a test plan
that was never run.

---

## The wrong version, and what it produces

```
Sprint 4 · Week 14
Sprint goal: Add dark mode, a leaderboard for most shifts, and email reminders.
| 1 | Dark mode               | 4 |
| 2 | Volunteer leaderboard   | 5 |
| 3 | Email reminders         | 6 |
|   | Total                   | 15 |
```

**What it produces, by Friday:** three half-finished features, a Review 1 crash still in the code,
no test plan run, and 15 planned hours in a week with about 10. On Tuesday of Week 15, a participant
hits the empty-day crash in the first minute, and the session measures the crash instead of the
design. The leaderboard also ranks volunteers by name, which is personal data no requirement asked
for. None of these tasks trace to the scope lock statement, so each one is scope creep.

## Why the wrong version is tempting

New features are the fun part. Testing is not. It is also Week 14, and you finally know the code well
enough to build fast, so adding something feels cheap. And you tend to believe the promised
features are "basically done." **"Basically done" is the phrase the test plan exists to check.**

---

## What to do in your project today

1. Open your scope lock statement at the top of `docs/improve/change-requests.md`.
2. Write the Sprint 4 plan. Every task gets a "Traces to" note. Delete any task that traces to
   nothing.
3. List every Review 1 must-fix that is not fixed. They go first.
4. Book your usability participants now, using the
   [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md), part 1.
5. Put the release candidate test run on Friday in your plan, with the hours it takes.
6. Any new idea from anyone goes on the future improvements list today, not into the build.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Feature freeze** | No new features are started. Fixing, finishing, and testing continue |
| **Scope lock** | No new features are promised. Set Week 12, Friday |
| **Release candidate** | The version you would ship if nothing else changed, tested and recorded |
| **Future improvements list** | Ideas that were not built, with who asked and why not |
| **Cut line** | The task you drop first if time runs out, named in advance |

---

## Check yourself

1. What is the difference between the scope lock and the feature freeze?
2. On Wednesday you realize a signed requirement, R7, is only half built. Is finishing it a violation
   of the freeze? Why or why not?
3. Your release candidate run has one FAIL. Your friend says you cannot call it a release candidate.
   What do you say?

---

## Check your answers

**1.** The scope lock, Week 12, stops new promises. The feature freeze, Week 14, stops new building.
One is about the agreement and the other is about the work.

**2.** No. R7 is signed and in scope, so finishing it is exactly what Sprint 4 is for. The freeze
stops features that were not promised, not the ones that were.

**3.** A release candidate is the version with every in-scope requirement built and the test plan run
and recorded. A recorded FAIL with a planned correction and re-run meets that. What would not meet it
is an unfinished feature or a plan that was never run.
