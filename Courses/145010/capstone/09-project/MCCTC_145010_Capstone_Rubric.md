# The Capstone Rubric · Scoring Guide
## 145010 Web Design & Senior Capstone · Weeks 7-18

**Why you are reading this in Week 7.** Every document you write in the next twelve weeks is
evidence for one of four scores. If you know what a score needs, you write the document once. If
you do not, you rewrite it in Week 17.

This file is public on purpose. Nothing in it is a secret, and nothing in it is an answer. The
work is yours.

---

## The rubric

| Dimension | Points |
|---|---|
| Process & Documentation | 30 |
| Technical Execution | 30 |
| Stakeholder Outcome | 20 |
| Presentation & Defense | 20 |
| **Total** | **100** |

**The rule above the rubric.** The only way to fail outright is submitting work you cannot
explain. If the defense shows you cannot explain a central part of the work you submitted, the
capstone fails regardless of the scores below.

**How to read the bands.** Every dimension is split into parts. Every part has bands. Each band
names the **evidence** that earns it, and the scorer looks for that evidence in your repository,
your signed records, and the defense. **A band is earned by evidence, never by effort described.**
When the evidence sits between two bands, the scorer gives the lower band and writes one sentence
saying what would have earned the higher one.

---

## 1. Process & Documentation · 30 points

**The question:** could a stranger reconstruct how this project was made from your repository
alone?

### 1A. DMAIC phase evidence, recorded by week · 10 points

| Points | Evidence |
|---|---|
| **9-10** | Every phase has its documents, each dated by week and day. Every phase guide's "done" list is met. The commit history agrees with the dates. Each phase's documents refer to the one before: requirements cite the proposal, the test plan cites the requirements, the acceptance record cites the test plan. |
| **6-8** | Every phase has its documents. One phase is thin, or a document was plainly written after the fact and says so honestly. |
| **3-5** | One phase is missing a required document, or several documents were written in the last two weeks and dated as if they were not. |
| **0-2** | Two or more phases have no evidence. |

**How to check it fast.** Open the phase guides' "done" lists beside the repository. Then run
`git log --format="%ad %s" --date=short -- docs/` and compare the commit dates with the week each
document claims.

### 1B. Decision log, AI usage log, troubleshooting log, licensing statement · 8 points

| Points | Evidence |
|---|---|
| **7-8** | At least ten decisions with alternatives considered and a reason, written on the day. At least three troubleshooting entries with a named method and a verified fix. An AI usage log where the "what I changed" and "how I verified" fields have real content. A licensing statement covering every dependency, asset, and model. |
| **5-6** | All four exist and are current. Decisions record what, but often not the alternative. |
| **2-4** | One of the four is missing, or the decision log is a diary rather than a record of choices. |
| **0-1** | Two or more missing, or an AI usage log that contradicts the work. |

**A log that says "no AI used" on a project that plainly used it scores 0 on this part** and
becomes a defense question.

### 1C. Commit history · 4 points

| Points | Evidence |
|---|---|
| **4** | A commit at the end of essentially every period from Week 7 to Week 18. Messages say what changed. |
| **3** | A handful of gaps, each explained by an absence. |
| **1-2** | Long gaps, or large commits that bundle a week of work. |
| **0** | The history was built in the last week, or the work was committed by someone else. |

### 1D. Stakeholder communication record · 5 points

| Points | Evidence |
|---|---|
| **5** | A contact log with every contact. A meeting record for every conversation. A status note every Friday in Weeks 8-10 and a full update every Friday in Weeks 11-17. Bad news appears in the update of the week it happened. |
| **3-4** | Every update exists. One or two meeting records are missing, or an update softened a problem that the next update had to correct. |
| **1-2** | Several updates missing, or updates that describe activity without progress against the agreed criteria. |
| **0** | No record of regular contact. |

### 1E. README, user guide, and support documents · 3 points

| Points | Evidence |
|---|---|
| **3** | A README a stranger can follow from a clean machine. A user guide written for the stakeholder, proofread, with no step that depends on knowing the code. A rollout plan and handoff checklist complete. |
| **2** | All exist. One has a step that fails or a section written for a developer rather than a user. |
| **0-1** | Missing or unusable. |

---

## 2. Technical Execution · 30 points

**The question:** does it work, and does it stay working?

### 2A. The Five-Dimension Code Review · 24 points

The instructor scores the final submitted commit on the Five-Dimension Code Review, the same
standard as every review you have done.

| Dimension | Points |
|---|---|
| Correctness | 20 |
| Security | 20 |
| Readability | 20 |
| Performance | 20 |
| Requirements Fit | 20 |

**The review total, out of 100, converts to this part:** multiply by 0.24 and round to the nearest
whole point. A review of 85 scores 20. A review of 62 scores 15.

**The per-dimension bands are the same ones your peer reviews use:**

| Score | Meaning, for any dimension |
|---|---|
| **18-20** | No finding above **consider**. The reviewer looked hard and can say where. |
| **14-17** | One **should fix**, or several **consider** findings. |
| **10-13** | One **must fix**, or several **should fix** findings. |
| **0-9** | More than one **must fix**, or the dimension could not be checked because it does not run. |

**Security is capped at 9 by any must-fix security finding.** In the capstone that includes a
credential in the repository or its history, personal data stored that the requirements did not
need, an endpoint that changes data without authentication, or input that reaches a database
query unparameterized.

**Requirements Fit is scored against your signed requirements**, not against what the project
could have been. A project that does less than you hoped and exactly what was agreed scores well
here. A project that does more than was agreed and misses a signed requirement does not.

### 2B. Deployed and survived · 6 points

| Points | Evidence |
|---|---|
| **6** | Deployed and reachable by someone other than the student. An unbroken run of at least thirty days with no manual intervention, backed by a health log the system wrote itself and an events log. Any earlier reset is recorded with its cause, its fix, and the change that stops it recurring. |
| **4-5** | Deployed and reachable. An unbroken run of 21 to 29 days with a complete, honest record. Or thirty days of operation with one or two interventions inside them, each fully recorded in the events log and the troubleshooting log. |
| **2-3** | Deployed and reachable. An unbroken run shorter than 21 days, or a health log with gaps nobody explained. |
| **0-1** | Not reachable by anyone else, or no survival evidence. |

**An intervention the events log leaves out, revealed by other evidence, drops this part to 0-1.**
The record is only worth something if it is honest.

**A project that is not deployed and reachable by someone other than the student scores no more
than 15 of the 30 points in this dimension**, whatever the review says. Requirement 2 is not
optional.

---

## 3. Stakeholder Outcome · 20 points

**The question:** did the person you built it for get what you promised?

**This dimension scores written evidence from the stakeholder, never whether they were nice about
it.** A stakeholder who says "it is great" and signs nothing has given you nothing to score.

### 3A. Acceptance against the agreed criteria · 10 points

Scored from the signed acceptance record and the acceptance agreement it refers to.

| Points | Evidence |
|---|---|
| **9-10** | Every acceptance criterion was run with the stakeholder. All criteria accepted, or all but one with an agreed plan in the record. Any criteria changed after Week 8 were changed by a recorded change request the stakeholder agreed to. |
| **6-8** | Most criteria accepted. The rest are recorded as not accepted, with the reason and what was agreed. |
| **3-5** | Fewer than half accepted, or the run was done without the stakeholder and their written response came afterward. |
| **0-2** | No acceptance record, or criteria changed after the fact without the stakeholder's agreement. |

**A criterion quietly edited so that it passes scores 0 on this part.** A criterion that failed
and is recorded honestly costs far less.

### 3B. Handoff received · 5 points

| Points | Evidence |
|---|---|
| **5** | The rollout plan was sent to the stakeholder before the handoff. Training happened, or the stakeholder confirmed in writing that they worked through the user guide. The handoff checklist is signed off. The final review and approval is recorded. |
| **3-4** | Handoff happened, and one of those pieces is missing. |
| **1-2** | Materials were sent, and nothing confirms the stakeholder received or used them. |
| **0** | No handoff. |

### 3C. Measured change from the baseline · 5 points

| Points | Evidence |
|---|---|
| **5** | The same measurement taken in Week 9 was taken again after handoff, the same way, and the comparison is reported with its limits stated. Usability findings are counts out of the number of people watched, never percentages. |
| **3-4** | A second measurement exists and was taken differently, and the report says so. |
| **1-2** | A satisfaction statement from the stakeholder with no measurement behind it. |
| **0** | No comparison. |

**No improvement is not zero.** A second measurement that shows no change, reported honestly with
a reason, earns this part's evidence. A measured result is scored for its honesty, not its size.

### When a stakeholder disappears

If your contact log shows you did your part and the stakeholder stopped responding, your
instructor applies the procedure in the Control phase guide. **You are not scored down for a
stakeholder's silence that your record documents.** You are scored down for silence of your own.

---

## 4. Presentation & Defense · 20 points

**The question:** do you understand what you built?

### 4A. The presentation · 8 points

| Points | Evidence |
|---|---|
| **7-8** | Follows the structure: problem, stakeholder, what you built, what you rejected and why, what the stakeholder accepted, what you would do next. Within time. Every claim about results matches the records. Speaks to the audience, not to the slides. |
| **5-6** | Structure complete. Over or under time by more than two minutes, or one claim the records do not support. |
| **3-4** | A tour of features rather than an account of a problem solved. |
| **0-2** | Unprepared, or claims the records contradict. |

### 4B. The live demonstration · 4 points

| Points | Evidence |
|---|---|
| **4** | Shows the deployed system, not a local copy, doing the thing the stakeholder needed. If something breaks, the student names what broke and moves to the recorded fallback without panic. |
| **2-3** | Runs a local copy with an explanation, or recovers from a failure awkwardly. |
| **0-1** | No demonstration, or a failure the student cannot explain. |

**A demo that breaks and is handled well can score 4.** The plan for that moment is in the
[Final Presentation Outline](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md).

### 4C. The defense · 8 points

The panel asks unscripted questions of four kinds: technical, decision, failure, and honest. The
[Defense Question Bank](MCCTC_145010_Capstone_DefenseQuestionBank.md) shows what each kind looks
like and what a strong answer contains.

| Points | Evidence |
|---|---|
| **7-8** | Answers name the actual file, function, table, or decision. Answers to failure questions describe what the system does, not what it should do. "I do not know" is said plainly when true, followed by how the student would find out. |
| **5-6** | Most answers specific. One or two general where a specific answer existed. |
| **3-4** | Answers describe the technology in general rather than this project in particular. |
| **0-2** | Cannot answer questions about central parts of the work. **See the rule above the rubric.** |

---

## Score sheet

```
Student: ____________________   Track: ____________________   Final commit: ________

1  PROCESS & DOCUMENTATION                                     ____ / 30
   1A DMAIC evidence by week                    ____ / 10
   1B Decision, AI usage, troubleshooting, licensing  ____ / 8
   1C Commit history                            ____ / 4
   1D Stakeholder communication record          ____ / 5
   1E README, user guide, support documents     ____ / 3

2  TECHNICAL EXECUTION                                         ____ / 30
   2A Five-Dimension Code Review
      Correctness ___/20  Security ___/20  Readability ___/20
      Performance ___/20  Requirements Fit ___/20
      Review total ___/100  x 0.24 =            ____ / 24
   2B Deployed and survived                     ____ / 6
   Not reachable by anyone else? Cap at 15      [ ] applied

3  STAKEHOLDER OUTCOME                                         ____ / 20
   3A Acceptance against agreed criteria        ____ / 10
   3B Handoff received                          ____ / 5
   3C Measured change from baseline             ____ / 5

4  PRESENTATION & DEFENSE                                      ____ / 20
   4A Presentation                              ____ / 8
   4B Live demonstration                        ____ / 4
   4C Defense                                   ____ / 8

TOTAL                                                          ____ / 100

Could the student explain every central part of the submitted work?   [ ] yes  [ ] no
One sentence on what would have raised the lowest part:
_____________________________________________________________________________
```
