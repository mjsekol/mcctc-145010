# Clinic · A Sprint Plan With a Cut Line
## 145010 Senior Capstone · Week 11, Monday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 11, Monday, or any week the room shows this signal: sprint plans
with more hours than the week has.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.4.7 (productivity tools to optimize assigned tasks), 1.2.7 (problem solving to
determine next steps), 1.1.7 (critical thinking when making decisions), 2.9.5 (timeline and task
breakdown)

---

## Why this exists

**A sprint plan that does not fit the week is a plan to be behind by Wednesday.** Nobody writes one
on purpose. You list what you want done, each task sounds like an afternoon, and the total never
gets added up.

Then Friday arrives. The review says "almost." The weekly update says "going well." And the one
thing your stakeholder needed this week is the task you never reached, because you did the
interesting ones first.

**The cut line fixes that before it happens.** You put the tasks in order of importance, add up
the hours, and draw a line where the week runs out. Everything under the line is the first thing
cut. You decide it on Monday, calmly, instead of on Thursday night in a panic.

This is the first sprint of four. **Sprint 1 has one goal: a walking skeleton, deployed.** Every
line of your plan either serves that goal or waits.

---

## The skill in plain language

A Monday sprint plan has five parts. The template is the
[Sprint Plan](../05-labs/MCCTC_145010_Template_SprintPlan.md).

1. **One goal**, in a sentence your stakeholder would understand.
2. **Hours available**, worked out from the real week, not guessed.
3. **Tasks in priority order**, each with hours and a "done when" someone else could check.
4. **The cut line**: the running total crosses the hours available, and you draw a line there.
5. **The first cut**, named: the task you drop first if the week goes badly.

**Work out the hours from the timetable.** This is the arithmetic for a normal week. Your own
week may be shorter.

```
Build period, Mon to Thu    110 min x 4 = 440 min
Build period, Fri           about 50 min after the review and the update
Period 8, Mon to Fri         46 min x 5 = 230 min
                                          -------
                                          720 min = 12 hours
```

Twelve hours is the ceiling. Subtract anything you already know about: a BPA practice, an
appointment, a conference with your instructor. **Then plan to about ten**, because something
always goes wrong in a build week, and the plan needs room for it.

**Estimate the unknown parts at four times your first guess.** You met this rule in Week 8. In
Week 11 the unknown part is almost always the host: the first deploy, the environment settings, the
database on a machine that is not yours.

---

## Worked example 1 · the plan that does not fit

**This is a composite project, not a real organization.** The Parts Bin Board is for a volunteer-run
community bike repair co-op. Volunteers mark a parts bin low. The shop coordinator sees the low list
and marks items restocked.

A student's first Sprint 1 plan:

| # | Task | Hours |
|---|---|---|
| 1 | Coordinator sign-in with hashed passwords | 4 |
| 2 | Low-report form with bin code and note | 3 |
| 3 | Coordinator low list with restock button | 3 |
| 4 | Styling for phone and the desktop by the door | 3 |
| 5 | Deploy to the host | 1 |
| 6 | Health route | 0.5 |
| 7 | Page-view counter | 2 |
| 8 | Sprint review and Update 1 | 1 |
| | **Total** | **17.5** |

Read it the way your instructor will.

- **17.5 hours in a 12-hour week.** It was behind before it started.
- **The deploy is 1 hour and it is task 5.** It is the least known task on the list, so it is the
  one most likely to take four times longer. It sits behind 13 hours of features.
- **No "done when" column.** On Friday nobody can say whether task 2 is done or almost done.
- **No cut named.** When Thursday goes wrong, the student decides under pressure.

---

## Worked example 2 · the same sprint, with a cut line

**Sprint goal:** You can open the shop link and see the first parts bin on the board.

**Hours available:** 12, minus 1 for a BPA practice on Tuesday in Period 8 = 11. Planned to 10.

| # | Task | Hours | Done when |
|---|---|---|---|
| 1 | Skeleton: one page reads one bin row from SQLite, locally | 1 | The page shows B-01 at 127.0.0.1:5330 |
| 2 | Health route that reads the bins table | 1 | `/health` answers 503 when the database is missing |
| 3 | Deploy to the approved host by the architecture steps | 4 | The stakeholder's link shows the page from outside the lab |
| 4 | Settings from environment variables, nothing secret committed | 1 | The app refuses to start without `PARTS_DB` |
| 5 | Health check scheduled, thirty-day clock started | 1.5 | Two health log lines, thirty minutes apart |
| 6 | Sprint review and Update 1 | 1 | Both committed and the update sent |
| | **Subtotal above the line** | **9.5** | |
| **CUT LINE** | | | |
| 7 | Low-report form, bin code and note only | 3 | A report appears in the table |
| | **Total if everything fits** | **12.5** | |

**If I run out of time, I cut first:** task 7. It moves to Sprint 2.

What changed, and why each change matters:

- **The deploy moved to task 3 and grew to 4 hours.** It is the riskiest task, so it goes early,
  while there is still a week to recover.
- **Sign-in, the restock list, styling, and the counter left this sprint.** They are real
  requirements. They are Sprint 2 and Sprint 3 work, and none of them serves this week's goal.
- **Task 7 sits under the line on purpose.** If the deploy goes smoothly, the student builds it. If
  it does not, nobody is surprised on Friday.
- **Every "done when" is observable.** A classmate could check each one without asking.

---

## Worked example 3 · Friday, with the line doing its job

The deploy took 6 hours instead of 4. The host's first build failed on a missing package, and the
database path was different on the host. (That is exactly what a walking skeleton is for.)

The Friday review, in the template's words:

```
Goal met? yes
Hours planned: 9.5   Hours spent: 11.5   Tasks finished: 6 of 7
What took longer than planned, and why: the deploy, 6 hours against 4.
  The host's build needed a requirements file, and PARTS_DB had to
  point at the host's storage path. TS-1 in the troubleshooting log.
What moved to next sprint: task 7, the low-report form, as planned
  on Monday (D-9).
```

The update to the coordinator says "on track," and it is true. The goal was met. The cut was
decided on Monday and written down, so it is a plan working, not a failure.

---

## The wrong version, and what it costs

The wrong version is example 1, sent to the build period unchanged. By Thursday the student has a
sign-in page and half a form on their laptop, nothing deployed, and a Sprint 1 review that says
"almost."

**What it costs:** the walking skeleton is late, so every hosting problem is still unknown. The
thirty-day clock cannot start. Milestone Review 2 in Week 12 opens with "nothing deployed," which is
the first red flag your instructor looks for. And the student now has a week less to
find out whether the host works at all.

---

## Why the wrong version is tempting

**Features feel like progress. Deploying feels like paperwork.** A sign-in page is something you
can look at. A deploy that fails three times looks like nothing on your screen. So students build
the visible things first and leave the deploy for "once there is something worth deploying."

**Adding up hours is uncomfortable.** The total tells you, on Monday, that you cannot do everything
you wanted. It is tempting not to look. Look anyway. The number is true whether you add it up or
not.

---

## Do this today

1. Open `docs/improve/sprint-1.md` in your repository, from the
   [Sprint Plan](../05-labs/MCCTC_145010_Template_SprintPlan.md) template.
2. Write the goal in one sentence your stakeholder would understand.
3. Work out your hours from the timetable above, minus what you already know about.
4. List tasks in priority order. The deploy is in the top three.
5. Give every task hours and a "done when." Estimate anything on the host at four times your guess.
6. Draw the cut line where the running total crosses your hours. Name the first cut.
7. Add a decision log entry for anything you moved out of this sprint.
8. **Commit the plan before the build period starts.**

---

## If you are ahead, if you are behind

**If you are ahead:** your plan fits with room left. Check that every task traces to an acceptance
criterion in your signed agreement. Then put a stretch task under the cut line, not above it.

**If you are behind:** your requirements or architecture are not finished from Week 10. Your
Sprint 1 plan still gets written today, and its first task is the missing Week 10 document with its
own hours. Tell your instructor at standup, not on Friday.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Task breakdown** | The numbered tasks in your plan, each small enough to finish and check (2.9.5) |
| **Timeline** | When each piece happens: this week's plan inside the four-sprint schedule (2.9.5) |
| **Deliverables** | What exists on Friday that did not on Monday: the "done when" column |
| **Productivity applications** | The task board or list you track the sprint in (1.4.7) |
| **Determine next steps** | The cut line and the first cut, decided before they are needed (1.2.7) |

---

## Self-check

**1.** Your tasks add up to 15 hours. Your week has 12, and you have a dentist appointment during
Wednesday's build period. What do you do before you commit the plan?

**2.** Why does the deploy go near the top of a Sprint 1 plan, when it is only one line?

**3.** A classmate's "done when" for the form task says "form works." Rewrite it so someone else
could check it.

### Answers

**1.** Subtract the appointment first: 12 minus about 2 is 10 hours available. Then keep the tasks
in priority order, draw the cut line where the running total crosses 10, and name the first task to
cut. Everything under the line moves to Sprint 2 unless the week goes better than planned, and the
move is recorded in the decision log.

**2.** Because it is the task you know least about, so it is the one most likely to take far longer
than planned. Doing it early leaves the rest of the week to recover. Doing it last leaves nothing.

**3.** Any observable result works. For example: "Submitting bin B-02 with the note 'two left'
adds one row to the low_reports table, and the page shows 'Thanks, the coordinator will see it.'"
It names an action and a result that could come out wrong.
