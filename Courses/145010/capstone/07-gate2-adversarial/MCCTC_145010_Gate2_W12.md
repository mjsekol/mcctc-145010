# Gate 2 · Week 12 · The Update That Said Everything Was Fine
## 145010 Senior Capstone · Week 12, Thursday · first 40 minutes of build

**40 minutes. Individual. Silent. No AI tool.** You may open every file in the folder, and you may
run the course survival report on the logs. **Grade category:** Written & Documentation.

**Rubric: AI Output Evaluation**, the same five parameters you used all through
Applications of AI.

**Competencies:** 1.2.5, 1.2.11, 1.10.4, 2.11.8, 1.2.1, 1.5.5

**Everything in the folder is invented and composite.** The Parts Bin Board, the bike repair co-op,
the shop coordinator, the logs, and every message are made up for this exercise. None of it is a
real organization, a real person, or a real system.

---

## Why you are doing this today

**Tomorrow you send Update 2 and your scope lock statement.** They are the two most consequential
messages of the build. The update is the picture your stakeholder has of the project. The scope
lock is the line nobody crosses for the rest of the capstone.

**Week 12 is the week students most want the picture to look better than it is.** An AI assistant
will happily help, because it writes what sounds finished. Today you read one of those drafts before
it goes out, so tomorrow you read your own the same way.

---

## The situation

The senior building the Parts Bin Board had a rough Sprint 2. On Thursday of Week 12 they asked an
AI assistant to draft the Friday update and the scope lock statement, and pasted in part of their
sprint file. The draft came back polished, on the right template, and calm.

**It goes to the shop coordinator tomorrow, with the instructor copied.** Your job is to read it
first.

---

## Your job

**Score the draft on the five AI Output Evaluation parameters.**

```
Validity        is what it says true, given the evidence
Relevance       is it about the thing that was asked
Authenticity    is it what it claims to be, from where it claims
Potential Bias  does it treat people or evidence unevenly
Hallucinations  does it contain things that are not there
```

**There is at least one real problem under every one of the five.** There is also **one item that is
genuinely arguable**, and it is not one of the five.

---

## What is in the folder

| File | Read it |
|---|---|
| [`W12/sprint-2-review.md`](W12/sprint-2-review.md) | **First.** What really happened this week. Review lines are S1 to S12 |
| [`W12/contact-log.md`](W12/contact-log.md) | **Second.** Every contact with the coordinator. Lines are L1 to L13 |
| `W12/health-log.txt` | Written by the health checker every 30 minutes, Week 11 Friday afternoon to Week 12 Thursday afternoon. Timestamps are invented program data |
| `W12/events-log.txt` | Written by the senior on the day of each event |
| [`W12/generated-update.md`](W12/generated-update.md) | The document you are scoring. Paragraphs are U1 to U13 and SL1 to SL10 |

**The folder is internally consistent.** Every problem in the draft is settled by a line in the
sprint review or the contact log, a rule in a course document, or the output of the survival report.

**Course files you may open:** [the Capstone Specification](../09-project/MCCTC_145010_Capstone_Specification.md)
(the scope rule and the thirty-day rule), [the Weekly Stakeholder Update template](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md)
(the status table), and [the Change Request template](../05-labs/MCCTC_145010_Template_ChangeRequest.md).

---

## What you may run

**From the repository root**, run the survival report on the two logs, the same way you run it on
your own:

```
python Courses/145010/capstone/05-labs/survival-files/survival_report.py --health Courses/145010/capstone/07-gate2-adversarial/W12/health-log.txt --events Courses/145010/capstone/07-gate2-adversarial/W12/events-log.txt --max-gap-minutes 75 --max-outage-minutes 60
```

Then run it again **without** the `--events` part, and compare the two outputs line by line.

**Write down the exit code as well as the text.** In PowerShell, `$LASTEXITCODE` holds it. In Git
Bash, `echo $?` does.

**Do the day arithmetic yourself too.** The report rounds to one decimal. You should be able to say
which day and time the longest run starts and ends.

---

## The 40 minutes

| Minutes | Do this |
|---|---|
| 0 to 8 | Read the sprint review and the contact log. Underline every fact a stakeholder would want to know |
| 8 to 14 | Run the report twice. Write down both "longest run" lines and both exit codes |
| 14 to 22 | Read the draft, paragraph by paragraph, against what you underlined |
| 22 to 34 | Write your five findings |
| 34 to 40 | Write the unsure-about entry. Reread your "what it costs" lines |

---

## What to submit

### Five findings, one per parameter

For each, all four of these:

```
Parameter        which of the five
The sentence     quoted, with its paragraph number (U3, SL9)
The evidence     the file and line that contradicts it, or the command and what it printed
What it costs    what the coordinator, the volunteers, or the senior would get wrong because of it
```

**"What it costs" separates a full finding from a half one.** Think about what the coordinator does
next if they believe the sentence.

### Plus one entry: the thing you are unsure about

```
The sentence            quoted, with its paragraph number
The case that it is fine
The case that it is not
What would settle it     the one thing you would check or change
```

**You are not scored on which side you land on.** You are scored on whether both cases are real.

---

## Before you start

**The draft is not all wrong.** Several rows in the progress table are accurate, and part of the
scope lock is exactly right. A student who marks every line as a defect has not read it.

**One problem is arithmetic.** It is settled by a command you are allowed to run.

**Two problems are about what is missing.** A sentence can be wrong because of what it leaves out,
and a reader who was not in the room cannot tell.

**This is the hardest Gate 2 of the build.** Every sentence in the draft sounds like something a
careful student would write.

---

## Scoring

| Item | Points |
|---|---|
| Validity finding | 1 |
| Relevance finding | 1 |
| Authenticity finding | 1 |
| Potential Bias finding | 1 |
| **Hallucination finding** | **1, and missing it costs 2** |
| The unsure-about entry, with both cases | 1 |
| **Total** | **6, and the lowest possible score is negative** |

**Why the hallucination carries the double penalty.** An invented rule is the most dangerous
sentence a stakeholder can receive, because it sounds like permission. It arrives in the coordinator's
inbox with the instructor copied, and it changes what the coordinator expects to get.

---

## One rule for today

**Write nothing on your sheet that you cannot point at in a file or in the report's output.**

**The reveal is the first 10 minutes of build tomorrow, Week 12, Friday**, before you write your own
Update 2 and scope lock statement.
