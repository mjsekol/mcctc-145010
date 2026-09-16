# Clinic · Estimating Hours
## 145010 Senior Capstone · Week 8, Monday · 15 minutes · Define

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 8, Monday, or any week the room shows this signal: task breakdowns
with no hours, or totals over fifty.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.9.5 (timeline, task breakdown, costs, and responsibilities), 2.9.3 (determine
the budget), 1.4.7 (productivity applications for lists and calendars), 1.6.11 (business
activities within a budget).

---

## Why this exists

**Your time is the budget.** Nobody in this project spends money, so the one resource that runs out
is hours. Tomorrow your instructor reads your proposal and answers one question first: will you
finish this? The task breakdown is where that answer comes from.

A task list with no hours cannot be checked. A task list with hours that add to more than fifty for
the build weeks has already answered the question, and the answer is no.

**This is the hardest arithmetic in Define, and it is not hard arithmetic.** The hard part is being
honest about what you do not know yet.

---

## The skill in plain language

**Step 1 · List every build task.** A task is something you can finish and show. "Sign-in" is a task.
"Backend" is not, because you cannot tell when it is done.

**Step 2 · Write your first guess next to each one.** Hours, whole numbers.

**Step 3 · Mark each task known or unknown.** A task is **known** if you have built the same thing
before, in a course or a project, and could do it again without looking anything up. Everything else
is **unknown**.

**Step 4 · Multiply every unknown task by four.** This program's rule of thumb is that unknown work
takes about four times the first guess. It is a planning rule, not a measured law. Your first guess
covers typing the code once you know how. It leaves out reading the documentation, the first attempt
that does not work, the debugging, and the redo.

**Step 5 · Add the tasks your first list forgot.** Almost every first list forgets three: fixing
accessibility and validation problems, writing tests, and fixing what each sprint demo turns up.

**Step 6 · Add the column, then check the sum a second way.** Compare the total with the fifty-hour
line.

### Where the fifty hours comes from

Your class block is about twelve hours a week. Not all of it is building. Here is the arithmetic for
one build week in Weeks 11-14:

```
Whole block:  149 minutes x 5 days            = 745 minutes, about 12.4 hours

Build time inside it:
  Monday to Thursday build  4 x 110 minutes   = 440 minutes
  Friday build, about half                    =  55 minutes
      (the other half is the sprint demo and your update)
  Period 8                  5 x 46 minutes    = 230 minutes
                                                ------------
                                                725 minutes
  725 / 60                                    = about 12.1 hours a week

Four sprints:  4 x 12.1                       = about 48 hours, call it fifty
```

Two honest adjustments:

- **If Period 8 goes to BPA or a credential**, a week is 495 minutes, about 8.25 hours, and four
  sprints are about 33 hours.
- **If you compete at BPA Nationals**, which usually falls in Week 14, you lose most of a sprint.
  Three sprints are 3 x 12.1, about 36 hours.

**The fifty-hour line is the Improve total** in section 11 of the
[Concept Proposal template](../05-labs/MCCTC_145010_Template_ConceptProposal.md). Define, Measure,
and Control hours are listed too, but they do not come out of the fifty.

---

## Worked example 1 · A task breakdown, estimated honestly

*Composite, not a real organization or person.* A shift sign-up application for the volunteer
coordinator of a youth recreation league. It is the finishable version from
[Scope Calibration](../09-project/MCCTC_145010_Capstone_ScopeCalibration.md).

**Before.** The student's first list, with first guesses:

```
Deploy it                     1
Sign-in                       2
Create shifts page            3
Claim a shift                 3
No double claims              1
Release a claim               1
Health check                  1
Page-view counter             2
Print the week                2
                            ----
                             16 hours
```

Sixteen hours looks like room for three more features. It is not.

**After.** Known or unknown marked, unknowns multiplied by four, forgotten tasks added:

| # | Task | First guess | Known? | Estimate |
|---|---|---|---|---|
| T1 | Walking skeleton deployed on the approved host | 1 | unknown: never used this host | 4 |
| T2 | Coordinator sign-in | 2 | unknown: never built sessions in this framework | 8 |
| T3 | Create shifts page, with validation | 3 | known: built a form like it in Week 5 | 3 |
| T4 | Open shifts list and claim form | 3 | known | 3 |
| T5 | A shift cannot be claimed twice, even by two people at once | 1 | unknown | 4 |
| T6 | Coordinator releases a claim | 1 | known | 1 |
| T7 | Health endpoint that checks the database | 1 | unknown | 4 |
| T8 | First-party page-view counter, no cookies | 2 | known: built one in Week 6 | 2 |
| T9 | Print the week's schedule from the browser | 2 | known | 2 |
| T10 | Accessibility and validation fixes on every page | not listed | forgotten | 4 |
| T11 | Automated tests for the claim rules | not listed | forgotten | 4 |
| T12 | Fixing what each sprint demo turns up | not listed | forgotten | 4 |
| | **Improve total** | | | **43** |

**Check the sum a second way.** The nine original first guesses add to 16. The four unknown tasks
had first guesses of 1 + 2 + 1 + 1 = 5, and multiplying by four adds 5 x 3 = 15 more hours. So the
original nine now total 16 + 15 = 31. The three forgotten tasks add 12. 31 + 12 = 43. Both ways
agree.

**43 is under 50, with 7 hours of margin.** That margin is not spare time for features. It is what
absorbs a sick day or a host that goes down.

---

## Worked example 2 · The same method, on a draft that will not finish

*Composite.* The same student adds two features the coordinator never named.

| # | Task | First guess | Known? | Estimate |
|---|---|---|---|---|
| T13 | Text message reminders to families | 3 | unknown | 12 |
| T14 | Family accounts with profiles | 4 | unknown | 16 |

43 + 12 + 16 = **71 hours.** That is 21 hours over the line, close to two sprints that do not
exist. The first guesses added only 7 hours, which is why the draft felt fine.

Text reminders also need an outside account and a credential, which this program does not use, and
family profiles store personal data the job does not need. The scope check would cut both anyway.
The arithmetic tells you before anyone has to.

---

## Worked example 3 · A total that does not match its rows

*Composite.* A draft proposal's section 11 ends like this:

```
| T1 | Walking skeleton     | Improve | 4  |    |
| T2 | Coordinator sign-in  | Improve | 8  | T1 |
| T3 | Create shifts page   | Improve | 3  | T2 |
| T4 | Claim form           | Improve | 3  | T3 |
| T5 | No double claims     | Improve | 4  | T4 |
| T6 | Release a claim      | Improve | 1  | T4 |
|    | Improve total        |         | 19 |    |
```

The rows add to 4 + 8 + 3 + 3 + 4 + 1 = 23, not 19. The student typed the total before adding T5,
which is exactly 4 hours. **Always
re-add the column after any change**, and let a spreadsheet or a short calculation do it. A total that
does not match its rows tells the reader the whole section cannot be trusted.

---

## The wrong version, and what it costs

A task breakdown with no hours, or with first guesses only. It passes your own reading, because
every task sounds small. On Tuesday the scope check says it will not finish, and you have to redo
section 11 and section 7 in one night before the proposal goes out Wednesday.

If nobody catches it, the cost arrives in Week 12. Sprint 2 ends with half the tasks done, the
thirty-day clock is not running, and every cut from then on needs a change request and the
stakeholder's written agreement.

---

## Why the wrong version is tempting

A first guess feels honest, because it is what you believe. The four-times rule feels like padding.
And a small total makes the proposal look ambitious for free.

The first guess is honest about the part you can picture. The multiplier is for the part you cannot
picture yet, which is the part that eats the week.

---

## Do this today

The first 40 minutes of today's build period is the Gate 2 critique. Finish your draft after it.

1. In `docs/define/concept-proposal.md`, section 11, list every build task with a first guess.
2. Mark each one known or unknown. Multiply the unknowns by four.
3. Add the three tasks most lists forget.
4. Add the Improve column. Check it a second way.
5. Put the same tasks in your task tracker, and name the tracker in section 11.
6. Fill section 15's labor row from your all-phases total. Cite the rate source. Never invent one.
7. The full draft is due at the end of the build period. Commit it. Your instructor reads it tonight.

---

## If you are ahead, if you are behind

**Ahead.** Write your stretch goals in section 7 with estimates too. They will not be built unless
every acceptance criterion passes, but an estimate tells you whether one is realistic.

**Behind.** Get section 7 and section 11 done before anything else. Those are the two sections the
scope check reads first.

---

## Words the WebXam uses

| Exam word | What it means in this skill |
|---|---|
| **Task breakdown** | The project split into tasks small enough to finish and show, each with an estimate |
| **Timeline** | When each task happens, by week |
| **Costs: labor** | The value of the hours worked, even when nobody is paid |
| **Budget** | The limit the work must fit inside. Here, about fifty build hours |
| **Responsibilities** | Who does each task, including the stakeholder's part |
| **Productivity application** | A tool that tracks tasks, such as a project board |

---

## Self-check

**1.** A student's first guess for "connect to the sensor" is 3 hours. They have never wired this
sensor. What is the estimate, and why?

**2.** A task list's rows are 4, 8, 3, 3, 4, 1, 4, 2, 2. The Improve total says 29. Is it right?

**3.** A student uses Period 8 every day for a credential. Roughly how many build hours do they have
across four sprints, and what does that mean for their proposal?

### Answers

**1.** 12 hours. It is unknown work, so the first guess is multiplied by four. The extra time covers
reading the documentation, the wiring attempt that does not read correctly, and the debugging.

**2.** No. 4 + 8 = 12, + 3 = 15, + 3 = 18, + 4 = 22, + 1 = 23, + 4 = 27, + 2 = 29, + 2 = 31. The rows add
to 31. The total is 2 short, which usually means a row was added after the total was typed.

**3.** About 33 hours: 495 build minutes a week is about 8.25 hours, and 4 x 8.25 = 33. Their Improve
total should fit under about 33, not 50, or they need to plan different time for the credential.
