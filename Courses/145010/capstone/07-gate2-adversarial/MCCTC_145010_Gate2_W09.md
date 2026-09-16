# Gate 2 · Week 9 · The Requirements Nobody Could Fail
## 145010 Senior Capstone · Week 9, Wednesday · first 40 minutes of the build period · Measure

**40 minutes. Individual. Silent. No AI tool.** Read the folder on screen or on paper. Write your
answers on paper, or in a plain editor with every AI feature turned off.

**Rubric:** AI Output Evaluation. Validity, Relevance, Authenticity, Potential Bias,
Hallucinations.

**Slot:** Week 9, Wednesday, the first 40 minutes of the build period, before you write your own
requirements version 1. The reveal is the first 10 minutes of Thursday's build period, before you
send your requirements to your stakeholder.

**Competencies:** 1.10.2 (determine the customer's needs), 1.2.12 (technical writing), 2.12.1 (a
written procedure for determining acceptability), 6.1.2 (plan for devices, audience, and ADA
requirements), 1.5.5 (how bias shapes the way a product serves people), 1.2.1 (extract valid
information and cite its source).

---

## Why this exists

**Your Requirements Fit score is judged against the document you write today.** Every criterion in
it is something your stakeholder will check in Week 16. A criterion that cannot fail protects
nobody. A requirement that traces to nothing is scope creeping back in. A sentence that says the
stakeholder agreed, when they have not seen it, is a record you cannot take back.

**AI is very good at requirements that look finished.** The headings are right, the tables are
full, and the criteria have Given, When, and Then. That is why you check them line by line.

---

## The situation

The same composite project you saw in Week 8, after the scope check. A senior is building the
**Parts Bin Board** for the shop coordinator of a volunteer-run community bike repair co-op.
Volunteers mark a parts bin low from the shop link. The coordinator signs in, sees and prints the
low list, marks bins restocked, and sees how often the board is opened.

The coordinator signed the acceptance agreement on Week 8, Friday. The baseline counts arrived on
Week 9, Tuesday. On Week 9, Wednesday, the senior gave the signed scope and the baseline record to
the lab's local assistant and asked for requirements version 1. **The plan is to send it to the
coordinator on Thursday.**

---

## What is in the folder

| File | Read it |
|---|---|
| [proposal-excerpt.md](W09/proposal-excerpt.md) | **First.** The signed scope, needs N1 to N4, criteria AC-1 to AC-6, and the contact log. Lines are `L1` to `L44` |
| [baseline-record.md](W09/baseline-record.md) | **Second.** The six nights of counts. Lines are `B1` to `B24` |
| [generated-requirements.md](W09/generated-requirements.md) | The draft you are scoring. Every item has an ID (`G2`, `AC-2.1`, `NF3`, `V4`) |

**Everything in the folder is invented and composite**, including the co-op, the coordinator, the
senior, and the counts. Nothing in it describes a real organization or a real person. **It is
internally consistent**, so every claim in the draft can be settled by a line in the other two
files.

The template the draft follows is the
[Requirements Specification](../05-labs/MCCTC_145010_Template_RequirementsSpecification.md). Read
its "How to write one" list if you have not.

---

## Your job

**Score the draft on the five AI Output Evaluation parameters.**

| Parameter | The question it asks here |
|---|---|
| **Validity** | Is what it says true, given the baseline and the signed scope? |
| **Relevance** | Does every requirement serve the project that was signed? |
| **Authenticity** | Is the record of who reviewed and agreed what it claims to be? |
| **Potential Bias** | Does it assume something about the users that nobody measured? Who does that shut out? |
| **Hallucinations** | Does it rely on something that exists nowhere? |

**There is at least one real problem under every one of the five.** There is also **one item that
is genuinely arguable.** It is not one of the five.

**For every criterion you read, ask one question: could this fail?** A criterion that cannot fail
is not a test.

---

## What to hand in

### Five findings, one per parameter

For each finding, all four of these:

```
Parameter        which of the five
The sentence     quoted, with its ID (G2, R6, NF3, V4)
The evidence     the line that settles it (L or B), or your arithmetic
What it costs    what goes wrong in Week 10, Week 16, or at the defense
```

### Plus one entry: the sentence you are unsure about

```
The sentence              quoted, with its ID
The case that it is fine
The case that it is not
What would settle it      the one thing you would check or ask, or the fix
```

**You are not scored on which side you land on.** You are scored on whether both cases are real.

---

## The 40 minutes

| Minutes | What you do |
|---|---|
| 0 to 7 | Read the proposal excerpt and the baseline record. Then read the draft once |
| 7 to 28 | The five findings. Check every number, every trace, and every date against the other two files |
| 28 to 35 | The unsure-about entry. Then read every criterion and ask whether it could fail |
| 35 to 40 | Reread. Check that every finding cites a line |

---

## Two things worth saying before you start

**The draft is not all wrong.** Several requirements, the failure table, and most of the
non-functional rows are good, and some are better than what most first drafts contain. A sheet
that marks every section has not read the signed criteria.

**One of the problems is arithmetic.** The numbers are six lines long in `baseline-record.md`, and
it takes under a minute.

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

**Why the hallucination carries the double penalty.** A requirement built on something that does
not exist becomes a design decision, then a database setting, then a sentence in your handoff that
your stakeholder repeats to their board. Nobody checks it after today.

---

## One rule for today

**You may not write anything on your sheet that you cannot point at in the folder**, or show with
arithmetic. That is the same rule the draft broke.

**Then write your own version 1.** Before you commit it, ask of every criterion: could this fail?
And ask of every requirement: which line of my proposal does this trace to?
