# The Senior Capstone · Specification
## 145010 Web Design & Senior Capstone · Weeks 7-18

**100 points on the Capstone rubric. This is the largest single body of work in the program.**
**Final presentations are in Week 18.**

---

## Why this project exists

For two years you have built things for a teacher. The teacher wrote the problem, the teacher
knew the answer, and the teacher was going to read your work whether it was good or not.

None of that is true in the next twelve weeks.

You are going to find a real person with a real problem. You are going to agree with that
person, in writing, what "finished" means. Then you are going to build it, put it where they can
reach it without you, and hand it over. At the end you stand in front of a panel and answer
questions about every part of it.

**This is what you show an employer, a college, or an internship interviewer.** A portfolio
piece is worth something because somebody outside this room depended on it. That is the whole
reason this project is shaped the way it is.

**Be clear about what gets graded.** Only 30 percent of this grade is the code. A working
project with no stakeholder, no documentation, and no defense is a failing capstone. A modest
project that a real person accepted, that you documented honestly, and that you can defend
line by line is an excellent one.

---

## The requirement, regardless of track

Every capstone meets all seven of these. They are not a menu.

| # | Requirement | What it means in practice |
|---|---|---|
| 1 | **It solves a real problem for a real person outside this classroom.** | The problem comes from your Problem Inventory, the list you wrote in Week 1 of junior year. You may update the list. You may not invent a user. |
| 2 | **It is deployed, running, and reachable by someone who is not you.** | The stakeholder, or the people they serve, can use it without you sitting next to them. Where it runs is decided in Week 10 and written in your architecture. |
| 3 | **It has a named external stakeholder who agreed to acceptance criteria in writing.** | A signed acceptance agreement exists by the end of Week 8. No signature, no build. |
| 4 | **It is documented.** | A README, a decision log, an AI usage log, and a user guide, at minimum. Every template in `05-labs/` that this spec names is part of the documentation. |
| 5 | **It runs the full DMAIC cycle with evidence at each phase, recorded by week.** | Every document says which week and day it was written. The commit history backs that up. |
| 6 | **It survives thirty days without manual intervention.** | A thirty-day record, with a health log the system writes by itself. See [the survival rule](#the-thirty-day-survival-rule). |
| 7 | **It is presented formally, and you can answer questions about anything in it.** | A presentation and a live defense in Week 18. |

**The one way to fail outright.** Submit work you cannot explain. That rule has been in every
course in this program and it matters most here, because a panel is going to ask. If the
defense shows you cannot explain a central part of the work you submitted, the capstone fails
regardless of every other score.

---

## The three tracks

The track sets the technical shape. **The problem is always yours.** Pick the track that fits
the problem, not the track that sounds best.

| Track | Typical build | Best for | Track guide |
|---|---|---|---|
| **Industrial / HMI** | A Raspberry Pi with sensors, a C# WPF operator panel, alarm handling, data logging, and a web dashboard | Manufacturing-bound students and employer internships | [Industrial / HMI](MCCTC_145010_TrackGuide_IndustrialHMI.md) |
| **Full-Stack Application** | A deployed web application with authentication, a database, real users, and analytics | College-bound and web-industry students | [Full-Stack](MCCTC_145010_TrackGuide_FullStack.md) |
| **AI-Integrated** | A locally hosted model wrapped as a service, a C# or web front end, and a written ethics and licensing analysis | Students targeting AI-adjacent work | [AI-Integrated](MCCTC_145010_TrackGuide_AIIntegrated.md) |

Each track guide says what the minimum viable version looks like, what a stretch looks like,
the technical risks that sink that track, and how that track proves it survived thirty days.
**Read yours before Week 8.** Read the other two if you are undecided.

**On frameworks.** The instruction phase was vanilla HTML, CSS, and script on purpose. In the
capstone the stack is your choice, including Blazor for C# students, provided you can explain
every part of it in the defense. A framework you cannot explain is a liability on the day it
matters.

---

## Who the capstone belongs to

**Each capstone belongs to one student.** The problem comes from your own inventory and you
defend it alone. The daily schedule talks about "teams" because that is how the shop runs, and
most teams in this phase are a team of one.

**A pair needs your instructor's approval in Week 7.** An approved pair writes down, in the
proposal, which part each person owns. Each partner must be able to demonstrate their own part
separately and answer questions about the whole. Each partner is scored separately.

---

## The twelve weeks

DMAIC is the framework. **The Agile ceremonies live inside Improve**: sprint plans, daily
standups, weekly demos, and reviews.

| Weeks | Phase | What you produce | Phase guide |
|---|---|---|---|
| 7-8 | **Define** | A stakeholder, a concept proposal presented to them, and a **signed acceptance agreement**. Signed agreement required to proceed. | [Define](../05-labs/MCCTC_145010_PhaseGuide_Define.md) |
| 9-10 | **Measure & Analyze** | Baseline data, requirements specification, conceptual model and design brief, wireframes, architecture, written test plan. **Grading Period 3 closes at the end of Week 9.** | [Measure & Analyze](../05-labs/MCCTC_145010_PhaseGuide_MeasureAnalyze.md) |
| 11-14 | **Improve** | Four one-week build sprints, weekly demos, weekly written stakeholder updates, two peer code reviews. **Scope locked after Week 12.** | [Improve](../05-labs/MCCTC_145010_PhaseGuide_Improve.md) |
| 15-16 | **Improve to Control** | Usability testing with real users, corrections, stakeholder acceptance against the agreed criteria. **WebXam post-test in Week 16.** | [Control](../05-labs/MCCTC_145010_PhaseGuide_Control.md) |
| 17-18 | **Control** | Rollout plan, support and training materials, final review and approval, handoff, formal presentation. | [Control](../05-labs/MCCTC_145010_PhaseGuide_Control.md) |

### The fixed milestones

These do not move. Everything else in the schedule can bend a day.

| When | Milestone | If you miss it |
|---|---|---|
| **Week 7, Friday** | **Stakeholder named.** A real, contactable person, approved by your instructor, who has replied in writing that they are willing to talk. | The project does not proceed. Your instructor helps you find one that day. |
| **Week 8, Friday** | **Acceptance agreement signed.** | You do not start building. You work on Define until it is signed. |
| **Week 9, Friday** | **Grading Period 3 closes.** What is committed is what is graded. | The grade is entered on what exists. |
| **Week 12, Friday** | **Scope locked.** From here, scope can shrink. It cannot grow. | Nothing is added. See [the scope rule](#the-scope-rule). |
| **Week 12, Friday** | **Thirty-day clock running.** Start it in Week 11 if you can. | Every day late is a day you do not get back. |
| **Week 16** | **WebXam 145010 post-test.** Your instructor confirms the day. | The survey at the end of it is how your college credit is triggered. Do not miss it. |
| **Week 17, Friday** | **Thirty-day record complete. Handoff and final approval.** | The rubric scores the record as it stands. |
| **Week 18** | **Final presentations.** Your repository is scored at the `capstone-final` tag you make before your slot. | There is no make-up week after Week 18. |

### Week by week

Friday is **stakeholder day** every week: client contact, feedback review, and the written
update. The Week 8 to Week 10 Friday notes are short status notes on the same template. The
full weekly update, the one scored in Improve, starts in Week 11.

| Week | Mon | Tue | Wed | Thu | Fri |
|---|---|---|---|---|---|
| 7 | Kickoff. Repository created. Stakeholder-finding worksheet | First contact message approved, then sent | Idea conference | Idea conference. Proposal drafting | **Stakeholder named.** Needs-discovery conversation |
| 8 | Concept proposal draft complete | Scope reality check conference | Final proposal and agreement sent to the stakeholder | Proposal presented to the stakeholder | **Agreement signed.** Status note |
| 9 | Baseline plan | Baseline collected | Requirements specification v1 | Baseline record complete. Requirements sent for review | Status note. **GP3 closes** |
| 10 | Design brief and wireframes | Architecture and data dictionary | Written test plan | Acceptance procedure sent to the stakeholder | Requirements signed off. Status note |
| 11 | Sprint 1 plan | Build | Build | Build | Sprint 1 demo. **Walking skeleton deployed.** Update 1. Acceptance procedure agreed |
| 12 | Sprint 2 plan | Build | Build | Build | Sprint 2 demo. **Scope locked. Thirty-day clock running.** Update 2 |
| 13 | Sprint 3 plan | Build | **Peer code review 1** | Build | Author response to review 1. Update 3 |
| 14 | Sprint 4 plan | **Peer code review 2** | Build | Build | **Release candidate.** Update 4 |
| 15 | Usability protocol, pilot | Sessions | Sessions | Sessions | Findings and change list. Update 5 |
| 16 | Corrections | Corrections | Acceptance run | Acceptance run | **Acceptance record.** Update 6 |
| 17 | Rollout plan | Rollout plan sent | User guide and training materials | Training with the stakeholder | **Handoff and final approval.** Thirty-day record closed. Update 7 |
| 18 | Rehearsal. Tag `capstone-final` | Presentations | Presentations | Presentations | Portfolio entry. Thank-you notes. Last commit |

**Milestone reviews** happen in Weeks 10, 12, 14, and 16. Your instructor reviews your
evidence, not your description of it: your commit history, your committed documents, and your
stakeholder contact record. Say what is true in standup and the review holds no surprises.

**Two weeks carry outside events.** BPA Nationals usually falls in Week 14, and competitors are
away. If you compete, do Peer Code Review 2 on the first day you are back, no later than Week 15,
Tuesday, and write your Week 14 update before you leave. A school break usually lands in Weeks
8-9. That is why the proposal and agreement go to your stakeholder on Wednesday of Week 8: a
signature can come back even if the end of that week is lost.

---

## Non-negotiables

Breaking one of these stops the work until it is fixed. They are not point deductions.

1. **No stakeholder, no project.** A named, contactable human, approved by your instructor, by
   the end of Week 7.
2. **No signature, no build.** The acceptance agreement is signed in Week 8.
3. **Scope is locked after Week 12.** It may be reduced. It is never expanded.
4. **Every period ends with a commit.** Work that is not committed is not submitted.
5. **Every contact with your stakeholder goes through school channels.** Your school email
   account, with your instructor copied, or a meeting your instructor has approved. Never a
   personal phone number, a personal account, or social media.
6. **You never meet a stakeholder alone.** Meetings happen at school, on an approved call, or at
   a site visit arranged through the school. Your parent or guardian knows who your stakeholder
   is.
7. **No personal information enters any AI tool.** Not yours, not your stakeholder's, not their
   customers'. No real names, no records, no photographs.
8. **Models run locally.** No part of any capstone requires a commercial AI developer account.
   Commercial developer APIs require users to be 18 or older.
9. **No money changes hands and no payment details are entered anywhere.** Free tiers only. If a
   stakeholder offers to pay you, stop and tell your instructor.
10. **An AI usage log and a licensing statement are part of every project.**
11. **Hardware work follows the Lab Acceptable Use and Safety Agreement you signed**, section 5,
    every time. See the Industrial / HMI track guide.

---

## The scope rule

**Oversized scope is the most common way a capstone fails, and it is only fixable early.** A
student picks something they cannot finish and spends twelve weeks at forty percent complete.

So scope is decided in three steps.

**Week 8: the scope reality check.** Your instructor reads your proposal and tells you, first,
whether you will finish it. Then they name the tasks that will take four times longer than you
think, and what to cut. You will not enjoy this conference. It is the most useful fifteen
minutes of the capstone. "Sounds great" in Week 8 is how a student fails in Week 16.

**Weeks 9-12: scope can change, in writing.** A change goes through a change request in your
decision log, and your stakeholder agrees to it in writing. A change that adds work names what
it replaces.

**After Week 12: scope is locked.** From Week 13 on, you may cut, and you may not add. A cut is
recorded as a change request, sent to your stakeholder, and reflected in the acceptance
criteria before the acceptance run. **An idea that arrives after Week 12 goes on the stretch
list or into the handoff notes as a future improvement.** It does not go into the build.

**Name your stretch goals in Week 8.** Ambition needs somewhere to go after the core is done.
A stretch goal is only started when every acceptance criterion already passes.

Three worked examples, one per track, each with an oversized version and a finishable version,
are in [Scope Calibration](MCCTC_145010_Capstone_ScopeCalibration.md). Read all three before
you write your proposal.

---

## The thirty-day survival rule

**Your project has to keep working when you are not looking at it.** A thing that works only
while you babysit it is a demo, not a deliverable.

**What counts as the thirty days.** Thirty consecutive calendar days in which the deployed
system runs without **manual intervention**.

**What counts as manual intervention.** A person restarting, repairing, clearing, or hand-editing
the running system or its data to keep it working. A reboot you did because it froze. A database
row you fixed by hand. A service you restarted because it stopped.

**What does not count.** A planned release of a new version through your documented deployment
steps, recorded in your deployment log, after which the system runs without help. Corrections
from usability testing are planned releases. A restart the system performs on its own, because
you designed it to, is not an intervention either. That is the point.

**What resets the clock.** Any manual intervention. Record it in your troubleshooting log with
the cause and the fix, then start counting again.

**When the clock should start.** The day your walking skeleton is deployed, **Week 11, Friday**.
Planned releases do not stop it, so there is no reason to wait for a finished product.

**When the clock must start.** By **Week 12, Friday**, at scope lock. Thirty days from there ends
as Week 16 ends, and the record is due **Week 17, Friday**.

**Do the arithmetic on resets before you need it.** Week 17, Friday is 42 days after Week 11,
Friday and 35 days after Week 12, Friday. So a clock started in Week 11 survives a reset in its
first 12 days, and a clock started in Week 12 survives one only in its first 5. **The latest start
that can still close by Week 17, Friday is Week 13, Wednesday, exactly 30 days before, and it
survives no reset at all.** If a late reset happens anyway, your record shows the longest unbroken
run and every reset, honestly, and the rubric scores what it shows.

**The evidence.** A health log the system writes by itself, a record of every release, and a
record of every intervention. The template is
[Thirty-Day Survival Record](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md). Each track
guide says what the health log looks like for that track. Timestamps inside the health log are
program data and belong there.

---

## Required repository structure

Your repository is the evidence. A reader should find any phase in under a minute.

```
capstone-<short-name>/
  README.md                         what it is, who it is for, how to run it, what is not finished
  decision-log.md                   every decision, written on the day
  ai-usage-log.md                   every AI interaction that changed something you submitted
  troubleshooting-log.md            every real problem, the method, and the verified fix
  LICENSING.md                      your licensing statement
  user-guide.md                     written for your stakeholder, not for you
  docs/
    define/
      stakeholder-finding.md
      concept-proposal.md
      acceptance-agreement.md       unsigned copy. The signed copy is kept by your instructor
      ethics-and-licensing.md       AI-Integrated track only
    measure-analyze/
      baseline.md
      requirements.md
      design-brief.md
      wireframes/
      architecture.md               includes the data dictionary
      test-plan.md                  includes the acceptance procedure
    improve/
      sprint-1.md ... sprint-4.md
      peer-review-1.md
      peer-review-2.md
      change-requests.md
    control/
      usability/
        protocol.md
        sessions/P1.md ... P5.md
        findings.md
      acceptance-record.md
      rollout-plan.md
      handoff-checklist.md
      thirty-day-record.md
    communication/
      contact-log.md                every contact, one line each
      updates/week-08.md ... week-17.md
      meetings/                     one meeting record per conversation
  presentation/
    outline.md
    portfolio-entry.md
  src/                              your code, shaped by your track
```

**Two things never go in the repository.** A signed document with a real person's signature on
it, and anything that identifies your stakeholder's customers or staff. Refer to your stakeholder
by role in every committed file unless they have told you in writing that you may use their name.
Your instructor keeps the signed originals.

---

## Where every template is

Every template is in `05-labs/`. Each one says which competencies it evidences.

| Phase | Templates |
|---|---|
| Define | [Stakeholder Finding and Contact Script](../05-labs/MCCTC_145010_Template_StakeholderFinding.md) · [Concept Proposal](../05-labs/MCCTC_145010_Template_ConceptProposal.md) · [Acceptance Agreement](../05-labs/MCCTC_145010_Template_AcceptanceAgreement.md) |
| Measure & Analyze | [Baseline Measurement](../05-labs/MCCTC_145010_Template_BaselineMeasurement.md) · [Requirements Specification](../05-labs/MCCTC_145010_Template_RequirementsSpecification.md) · [Design Brief](../05-labs/MCCTC_145010_Template_DesignBrief.md) · [Architecture and Data Dictionary](../05-labs/MCCTC_145010_Template_ArchitectureAndDataDictionary.md) · [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md) |
| Improve | [Sprint Plan](../05-labs/MCCTC_145010_Template_SprintPlan.md) · [Peer Code Review](../05-labs/MCCTC_145010_Template_PeerCodeReview.md) · [Change Request](../05-labs/MCCTC_145010_Template_ChangeRequest.md) |
| Control | [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md) · [Usability Observation Sheet](../05-labs/MCCTC_145010_Template_UsabilityObservationSheet.md) · [Acceptance Record](../05-labs/MCCTC_145010_Template_AcceptanceRecord.md) · [Rollout Plan](../05-labs/MCCTC_145010_Template_RolloutPlan.md) · [User Guide](../05-labs/MCCTC_145010_Template_UserGuide.md) · [Handoff Checklist](../05-labs/MCCTC_145010_Template_HandoffChecklist.md) · [Thirty-Day Survival Record](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md) |
| Every week | [Weekly Stakeholder Update](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md) · [Meeting Record](../05-labs/MCCTC_145010_Template_MeetingRecord.md) · [Decision Log](../05-labs/MCCTC_145010_Template_DecisionLog.md) · [AI Usage Log](../05-labs/MCCTC_145010_Template_AIUsageLog.md) · [Troubleshooting Log](../05-labs/MCCTC_145010_Template_TroubleshootingLog.md) · [Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md) |
| Documentation | [Project README](../05-labs/MCCTC_145010_Template_ProjectREADME.md) · [Licensing Statement](../05-labs/MCCTC_145010_Template_LicensingStatement.md) |
| Week 18 | [Final Presentation Outline](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md) · [Portfolio Entry](../05-labs/MCCTC_145010_Template_PortfolioEntry.md) · [Defense Question Bank](MCCTC_145010_Capstone_DefenseQuestionBank.md) |

---

## The three gates, in the capstone

The three gates run every week, the same as every unit you have taken.

- **Gate 3 (Open)** is the capstone itself. Full tooling. A decision log is required.
- **Gate 2 (Adversarial)** runs every week. You critique an AI-generated project artifact, such
  as a proposal with oversized scope or a status update that hides bad news, and score it on the
  AI Output Evaluation parameters: Validity, Relevance, Authenticity, Potential Bias,
  Hallucinations.
- **Gate 1 (Closed)** becomes WebXam review. More than half of the WebXam is web development, and
  you sit the post-test ten weeks after that instruction ended. Timed reps, no AI, no
  autocomplete. Do them.

---

## Grading · the Capstone rubric

| Dimension | Points |
|---|---|
| Process & Documentation | 30 |
| Technical Execution | 30 |
| Stakeholder Outcome | 20 |
| Presentation & Defense | 20 |
| **Total** | **100** |

**The full scoring guide, with the evidence for every band, is in
[the Capstone rubric](MCCTC_145010_Capstone_Rubric.md).** Read it in Week 7. It tells you exactly
what the documents you write are for.

What each dimension is looking for, in one paragraph each:

**Process & Documentation, 30.** DMAIC phase evidence recorded by week, a decision log with real
decisions in it, an AI usage log, meeting records, weekly updates, and a commit at the end of
every period. **The question it asks: could a stranger reconstruct how this project was made from
your repository alone?**

**Technical Execution, 30.** Scored on the Five-Dimension Code Review: Correctness, Security,
Readability, Performance, Requirements Fit. Plus the thirty-day record. **The question: does it
work, and does it stay working?**

**Stakeholder Outcome, 20.** Written acceptance from your external stakeholder against the
criteria you agreed in Week 8, a handoff they received, and a measured change from your baseline.
**The question: did the person you built it for get what you promised?**

**Presentation & Defense, 20.** A formal presentation, a live demonstration, and your answers to
unscripted questions. **The question: do you understand what you built?**

### How the capstone shows up in each grading period

The course weighting is the same as every course in the program: Projects 35 percent, Written &
Documentation 20 percent, Lab & Practice 20 percent, Quiz & Exam 15 percent,
BPA/Credential/Capstone 10 percent.

**Grading Period 3 closes at the end of Week 9**, in the middle of Measure. Your Define work and
your first Measure work are graded then, on what is committed at the close. The documents that
count are listed in the [Define phase guide](../05-labs/MCCTC_145010_PhaseGuide_Define.md#what-grading-period-3-sees).

**Grading Period 4** carries the milestone checkpoints and the final 100-point Capstone rubric
score from Week 18. Your instructor tells you in Week 7 which category each checkpoint is entered
under.

---

## What to do in the first hour

1. Open your Problem Inventory. Read all ten entries. Mark the three where you can name the person.
2. Create your repository with the structure above. Commit it empty.
3. Start `decision-log.md` with one entry: which three problems you are considering, and why.
4. Open the [Stakeholder Finding worksheet](../05-labs/MCCTC_145010_Template_StakeholderFinding.md).
5. Commit.
