# Gate 2 · Week 15 · The Findings That Wrote Themselves
## 145010 Senior Capstone · Week 15, Friday · first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool.** You may open any file in `W15/`. You may not ask
another student.

**Rubric this week: the AI Output Evaluation parameters.** Validity, Relevance, Authenticity,
Potential Bias, Hallucinations. This is a document week, so you are not using the Five-Dimension
Code Review.

**Competencies:** 6.5.10 (develop and execute usability tests, checking accessibility, ease of use,
and navigation), 2.12.4 (perform and document usability testing), 1.10.5 (determine satisfaction
with measurement tools), 1.5.5 (how bias influences who a product serves), 1.2.1 (extract valid
information and cite sources), 1.2.12 (technical writing to create reports).

**Grade category:** Written & Documentation.

---

## Why you are doing this today

This afternoon you write your own findings from your own five sessions. The fastest way to write
them is to hand your session notes to a chat tool. **You are not allowed to**, because nothing from
a session goes into an AI tool. But you will read documents written that way for the rest of your
working life, and some of them will be about your work.

So first you read one. It looks finished. It has counts, a table, severities, and a change list in
the right shape. **Your job is to find where it stopped being true.**

---

## The situation

**This is an invented composite.** The Northside Community Garden, its coordinator, the student,
the project, and the five participants do not exist. The kind of study is real. It is the one you
ran this week.

A student built Garden Watering Sign-Up, a small web app where garden members sign up for
watering slots. They ran five sessions in Week 15 and wrote each one up the same day. Then they
pasted the five records and the protocol into an AI assistant and asked for the findings. They made
a few edits and were about to commit it.

---

## What is in the folder

| File | Read it |
|---|---|
| `W15/protocol-tasks.md` | **First.** The requirements, who the users are, the five tasks, and the debrief questions |
| `W15/sessions/P1.md` to `P5.md` | The five session records. Lines are numbered, so you can cite `P3 L9` |
| `W15/findings-report.md` | The AI-written findings. The document you are evaluating. Sections are numbered |

**The folder is internally consistent.** Every claim in the findings can be settled by the
protocol and the five records. If a claim cannot be settled by them, that is information too.

---

## The five parameters

| Parameter | The question it asks here |
|---|---|
| **Validity** | Is it true, given the five records? |
| **Relevance** | Is it about what the tasks tested, and is it a finding rather than an opinion? |
| **Authenticity** | Is it this study's own work, or does it belong to somebody else? |
| **Potential Bias** | Whose experience does it count, and whose does it set aside? |
| **Hallucinations** | Does it state something that exists in none of the files? |

**There is one planted problem under each parameter, five in all.** There is also **one item that
is genuinely arguable**, where a careful person could go either way. It is not one of the five.

**The document is not all wrong.** Several sentences and table rows are correct. A sheet that marks
everything as a defect has not read the records either.

---

## What to hand in

Commit `gate2/w15.md` in your repository. Five findings, one per parameter, each with all six of
these:

```
Parameter         which of the five
The claim         quoted exactly, with its section number
Why it is wrong   in your own words
How you know      the file and line that settle it, for example "P4 L1 and P4 L6",
                  or the search you ran across all five records and what it returned
Who is harmed     a real person or group, and what they would do wrong because of it
The fix           what the corrected document should say instead
```

Then one more entry, for the arguable item:

```
The claim                 quoted, with its section number
The case that it is fine  the strongest version, not a straw man
The case that it is not   the strongest version
What would settle it      the one fact you would go and get, and from whom
```

**You are not scored on which side you pick.** You are scored on whether both cases are real.

---

## Scoring

| Item | Points |
|---|---|
| Validity finding | 1 |
| Relevance finding | 1 |
| Authenticity finding | 1 |
| Potential Bias finding | 1 |
| **Hallucinations finding** | **2. Missing it costs both points** |
| **Findings total** | **6** |
| The arguable item, scored on your reasoning | 3, separately |

**Partial credit on a finding:** the right problem under the wrong parameter, with real evidence,
earns half. The right problem with no evidence earns half.

**The arguable item, out of 3:**

| Points | What it looks like |
|---|---|
| 3 | Named as arguable, both cases stated fairly, and the deciding fact named |
| 2 | Named as arguable, one case stated well |
| 1 | Marked as plainly wrong, with a real reason |
| 0 | Marked as fine, or not mentioned |

**Why the hallucination carries double weight.** A number that nobody measured is the claim most
likely to leave the room. It goes into your weekly update, then into your presentation, then into
your stakeholder's report to their board. Once it has been repeated, it exists.

---

## Three habits that find these fastest

1. **Count it yourself.** Every count in the findings can be checked against five records in about
   ninety seconds. Make a tally before you read the table.
2. **For every number, ask which file it came from.** If you cannot point at the line, write down
   where you looked.
3. **For every sentence that sets something aside, ask what the requirements say.** Then check who
   the participant was on their record.

**The failure mode to name now:** you will read the change list, agree with it, and stop. A change
list can have the right shape and the wrong contents. Read it against the findings above it.

---

## Time

- 5 minutes: read `protocol-tasks.md`, then the findings once, without stopping
- 8 minutes: your own tally of the five records, task by task
- 17 minutes: the five findings
- 7 minutes: the arguable item
- 3 minutes: commit

---

## One rule for today

**Write nothing on your sheet that you cannot point at in one of the seven files.** That is the rule
the findings broke. Then, this afternoon, write your own findings the same way.
