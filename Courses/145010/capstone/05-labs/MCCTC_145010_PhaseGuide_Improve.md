# Phase Guide · Improve
## 145010 Senior Capstone · Weeks 11-14

**Why this phase exists.** This is the build. Four one-week sprints, about fifty hours. It is the
part you have been waiting for, and it is the part where a plan meets reality.

**Why it is run in sprints.** A one-week sprint ends with something you can show. If Sprint 1 ends
with nothing to show, you find out in Week 11, when there is still time to cut. A single
four-week build finds out in Week 14, when there is not.

**This is the hardest phase to be honest in.** Every student in Week 12 believes they are about
to catch up. The weekly update, the demo, and the milestone review are there so that belief is
checked against evidence every Friday.

**What you are producing.** A working, deployed system that grows every week. Four sprint records,
four weekly updates, two peer code reviews, a scope lock, a running thirty-day clock, and a
release candidate at the end of Week 14.

**Competencies this phase evidences:** 2.11.1 to 2.11.8 (troubleshooting, continuously), 1.2.5
(communicate for an audience and purpose), 1.2.11 (professional correspondence), 1.2.7
(problem solving and consensus to decide next steps), 1.1.7 (problem solving on work-related
decisions), 1.1.9 (give and receive constructive feedback), 1.4.7 (productivity tools for tasks),
1.4.8 (electronic communication etiquette), 1.10.4 (procedures for initiating product
improvements), 6.5.3 (standard web languages), 6.5.11 (cross-browser compatibility and
validation), 6.5.12 (publish to a web server), 6.5.13 (responsive design), 6.4.7 (scripting that
interacts with data sources), 1.3.8 and 1.7.13 (licensing of what you add).

---

## What done looks like

At the end of Week 14:

- [ ] The system is deployed and reachable by the stakeholder, and has been since Week 11.
- [ ] The thirty-day clock has been running since Week 12, Friday, at the latest.
- [ ] `docs/improve/sprint-1.md` to `sprint-4.md`: a plan on Monday and a review on Friday, each.
- [ ] Weekly updates for Weeks 11-14 sent and committed.
- [ ] `docs/improve/peer-review-1.md` and `peer-review-2.md`, each with the author response.
- [ ] `docs/improve/change-requests.md` with the scope lock statement from Week 12.
- [ ] `troubleshooting-log.md` with real entries.
- [ ] `LICENSING.md` current for every dependency and asset you added.
- [ ] **A release candidate**: every requirement in scope implemented, and your own test plan run
      against it with results recorded.
- [ ] A commit at the end of every period.

---

## How a sprint week runs

| Day | What happens |
|---|---|
| **Monday** | Write the sprint plan: one goal, the tasks that reach it, hours for each, and what you cut if you run out. Commit it before the build period. |
| **Tuesday to Thursday** | Build. Standup every day: what you finished, what you are on, what is blocking you. Commit every period. |
| **Friday** | Sprint review in the sprint file. Demo what works. Weekly update to the stakeholder. Plan for next Monday. |

**The daily standup has three answers, and "blocked by" is the one that matters.** "Nothing" is a
fine answer when it is true. "Nothing" said three days in a row by a student who has not
committed is how a capstone disappears.

**The demo.** One student demos in the last fourteen minutes of each day, on a rotation. **Every
Friday you show your sprint result to someone**: your stakeholder if they can see it, live or in a
short screen recording with no personal data in it, and a classmate otherwise. Record who saw it
in the sprint review.

**Conferences.** Your instructor conferences with two students a day. **Come with your commit
history open and one question.** A conference is not a status report. Your status is in your
repository.

---

## Week 11 · Sprint 1

**The goal:** a walking skeleton, deployed.

A walking skeleton is the thinnest possible version of your system that goes through every layer
and runs where it will finally run. For Full-Stack: a page on your host that reads one row from
the real database. For Industrial: a reading from the sensor reaching the panel and the dashboard.
For AI-Integrated: a request from the front end reaching your service, the model or the stand-in,
and coming back labelled.

- [ ] Monday: [Sprint Plan](MCCTC_145010_Template_SprintPlan.md) for Sprint 1.
- [ ] By Friday: **walking skeleton deployed and reachable by the stakeholder.**
- [ ] By Friday: acceptance procedure agreed by the stakeholder.
- [ ] Friday: the health check running. **Start the thirty-day clock now if you can.** Planned
      releases do not stop it.
- [ ] Friday: **the first full [Weekly Stakeholder Update](MCCTC_145010_Template_WeeklyStakeholderUpdate.md).**

**Why deploy first.** Hosting, networks, environment settings, and device setup are the problems
that cannot be solved on your laptop. Finding them in Week 11 costs a sprint. Finding them in Week
15 costs the capstone.

---

## Week 12 · Sprint 2 · scope lock

**The goal:** the core feature working end to end, and a scope you can finish.

- [ ] Monday: Sprint 2 plan.
- [ ] Milestone Review 2 this week. Your instructor asks one question first: will this finish?
- [ ] Friday: **scope locked.** Write the scope lock statement at the top of
      `docs/improve/change-requests.md`: the final list of what is in, and the list of what moved
      to stretch or to future improvements. Send it to the stakeholder with the weekly update.
- [ ] Friday: **the thirty-day clock is running, no later than today.**

**After today, scope can shrink and cannot grow.** Every new idea from you, your stakeholder, or a
user goes on the future improvements list. See the
[Change Request template](MCCTC_145010_Template_ChangeRequest.md) and the
[Stakeholder Communication Guide](MCCTC_145010_Guide_StakeholderCommunication.md#4-scope-change-request).

**Cut now if you need to.** A cut in Week 12 is a decision. A cut in Week 15 is a failure you had
to admit. If your Sprint 2 review shows you are behind, the scope lock statement is the cheapest
place in the whole capstone to make the project smaller.

---

## Week 13 · Sprint 3 · Peer Code Review 1

**The goal:** the remaining in-scope features, and a first outside look at your code.

- [ ] Monday: Sprint 3 plan.
- [ ] Wednesday: **[Peer Code Review 1](MCCTC_145010_Template_PeerCodeReview.md).** You review a
      classmate's code and a classmate reviews yours, on the Five-Dimension Code Review.
- [ ] Friday: **author response** to every finding: accepted, rejected with a reason, or deferred
      with a reason. Must-fix findings are fixed or explained.
- [ ] Friday: weekly update.

**Why review now.** Week 13 is late enough that there is real code and early enough to fix what
the review finds. Review 1 looks at the whole project.

---

## Week 14 · Sprint 4 · Peer Code Review 2 · release candidate

**The goal:** a release candidate, finished and tested, ready for real users on Monday.

- [ ] Monday: Sprint 4 plan. **No new features in Sprint 4 that were not already in scope.**
- [ ] Tuesday: **Peer Code Review 2.** Different reviewer from Review 1. This review checks what
      changed since Review 1, whether Review 1's must-fix findings were fixed, and security.
- [ ] Milestone Review 3 this week.
- [ ] Friday: **release candidate.** Run your own test plan against it and record the results.
- [ ] Friday: weekly update, including when your usability sessions will happen next week.
- [ ] Recruit your five usability participants now. See the
      [Usability Test Protocol](MCCTC_145010_Template_UsabilityTestProtocol.md). A student who
      starts recruiting on Monday of Week 15 does not find five people.

**BPA Nationals usually falls this week.** If you compete, write your Week 14 update before you
leave, tell your stakeholder you are away, and complete Peer Code Review 2 on the first day you are
back, no later than Week 15, Tuesday.

---

## Troubleshooting, every week

Every real problem that takes you more than twenty minutes gets an entry in
[the Troubleshooting Log](MCCTC_145010_Template_TroubleshootingLog.md). **This is how 2.11 is
evidenced**, and it is a source of defense answers.

An entry names the problem, the **method** you chose, what you gathered, the fix, the test that
proved the fix, and what stops it happening again. The WebXam names four methods:

| Method | Use it when |
|---|---|
| **Top down** | You suspect the problem is in how the pieces are put together. Start at the user's view and work inward. |
| **Bottom up** | You suspect a low-level piece. Start at the device, the database, or the model server and work outward. |
| **Follow the path** | Data goes in one end and comes out wrong. Check it at each step along the way. |
| **Spot the differences** | It works in one place and not another. Compare the two, one difference at a time. |

---

## The two failures to catch this phase

**Scope.** The earliest signal is a Sprint 1 review that says "almost" about the walking skeleton.
A skeleton that is not deployed by Week 11 Friday means hosting or hardware is harder than planned,
and that is the week to cut. The second signal is a sprint plan whose hours add up to more than
the week has.

**Stakeholder.** The earliest signal is a weekly update with no reply for two weeks in a row. The
second is a student who stops sending updates because there is "nothing to report." There is
always something to report. See the
[Stakeholder Communication Guide](MCCTC_145010_Guide_StakeholderCommunication.md#3-bad-news-we-are-behind).

---

## The evidence this phase produces, and where it is scored

| Evidence | Rubric part |
|---|---|
| Sprint plans and reviews | 1A DMAIC evidence |
| Troubleshooting log | 1B · 4C failure questions |
| Decision log and AI usage log | 1B · 4C decision questions |
| Commit history | 1C |
| Weekly updates, scope lock statement, change requests | 1D · 3A (criteria changed only by agreed request) |
| Peer code reviews and author responses | 1A · practice for 2A, which uses the same standard |
| Deployed system and health log | 2B deployed and survived |
| The code itself | 2A Five-Dimension Code Review |
| Licensing statement | 1B |

---

## Words the WebXam uses for what you did this phase

| Exam word | In your project |
|---|---|
| **Identify the problem** | The symptom, stated precisely, in your troubleshooting entry. 2.11.1 |
| **Troubleshooting methodology** | Top down, bottom up, follow the path, spot the differences. 2.11.2 |
| **Gather and analyze data** | Logs, measurements, and comparisons in the entry. 2.11.4 |
| **Design, test, implement a solution** | The fix, the test that proved it, the release. 2.11.5 to 2.11.7 |
| **Document the problem and the verified solution** | The entry itself. 2.11.8 |
| **Publish to a web server** | Your deployment. 6.5.12 |
| **Cross-browser compatibility and validation** | Your test plan's platform cases and your validator runs. 6.5.11 |
| **Product improvement procedures** | Your change request process. 1.10.4 |
