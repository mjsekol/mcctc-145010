# Gate 2 · Week 16 · The Email That Reported Good News
## 145010 Senior Capstone · Week 16, Friday · first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool.** You may open any file in `W16/`. You may not ask
another student.

**Rubric this week: the AI Output Evaluation parameters.** Validity, Relevance, Authenticity,
Potential Bias, Hallucinations.

**Competencies:** 2.12.6 (seek stakeholder acceptance upon successful completion of the test
plan), 2.12.1 (the written acceptance procedure agreed by the stakeholder and the team), 1.2.11
(professional correspondence), 1.2.13 (stakeholders), 1.10.3 (communicate features, benefits, and
warranties).

**Grade category:** Written & Documentation.

---

## Why you are doing this today

This afternoon you finish your acceptance record and write to your stakeholder about it. Some of
you had a criterion fail this week. **The email after a failure is the hardest one you will write in
the capstone**, because every instinct pushes you to soften it.

An AI assistant will soften it for you, fluently, and add things that never happened. Today you
read one of those emails before it is sent, with the records beside it.

---

## The situation

**This is an invented composite.** Oak Hollow Animal Rescue, its volunteer coordinator, its
shelter manager, the animals, the project, and the student do not exist.

Marcus built the Kennel Care Log, a web app where shelter volunteers record dog walks. The
coordinator signed six acceptance criteria in Week 8. On Wednesday of Week 16 they ran the agreed
procedure together at school, with the instructor present, and Marcus wrote everything down.

Then he gave the run log to an AI assistant and asked it to write the results email. **It has not
been sent.** You are the last check.

---

## What is in the folder

| File | Read it |
|---|---|
| `W16/acceptance-agreement.md` | **First.** The six criteria, how acceptance is decided, how changes happen, and the support promise |
| `W16/acceptance-procedure.md` | The agreed procedure, test plan section 7, with the commit it was agreed at |
| `W16/run-log.md` | **Second.** What happened on Wednesday, line by line, plus the contact log |
| `W16/draft-email.md` | The AI-drafted email. The document you are evaluating. Paragraphs are numbered `[1]` to `[9]` |

**The records are honest and internally consistent.** Every claim in the email can be settled by
the agreement, the procedure, and the run log.

Keep the [Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md),
sections 3 and 6, open beside you. It says what a stakeholder needs to hear.

---

## The five parameters

| Parameter | The question it asks here |
|---|---|
| **Validity** | Is it true, given the run log? |
| **Relevance** | Does it deal with what the stakeholder needs from this email? |
| **Authenticity** | Did the student write this, and can the student stand behind it? |
| **Potential Bias** | Does it treat people and evidence unevenly, and who pays for that? |
| **Hallucinations** | Does it report something that exists in no record? |

**There is one planted problem under each parameter, five in all.** There is also **one item that
is genuinely arguable**. It is not one of the five.

---

## What to hand in

Commit `gate2/w16.md` in your repository. Five findings, one per parameter, each with all six of
these:

```
Parameter         which of the five
The claim         quoted exactly, with its paragraph number
Why it is wrong   in your own words
How you know      the file and line that settle it, for example "run-log.md L39"
Who is harmed     a real person or group, and what they would do wrong because of it
The fix           what the email should say instead
```

Then one more entry, for the arguable item:

```
The claim                 quoted, with its paragraph number
The case that it is fine  the strongest version
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

**Why the hallucination carries double weight here.** Acceptance is a person agreeing, in writing,
to something that was decided in advance. An email that reports an agreement nobody made puts words
in your stakeholder's mouth, in writing, with your instructor copied. **The capstone rubric scores a
criterion quietly changed after the fact at zero.**

---

## Three habits that find these fastest

1. **Tally the run log before you read the email.** PASS, FAIL, NOT RUN. Then compare.
2. **For every event the email mentions, find its line.** A conversation, a restart, a change.
   If it has no line, write down where you looked.
3. **Ask what the stakeholder has to do after reading this.** Then check whether the email asks
   them to do it.

**The failure mode to name now:** the email is polite, warm, and well organized, and you like the
person who wrote it. That is exactly when a reader stops checking.

---

## Time

- 6 minutes: the agreement and the run log, then the email once, without stopping
- 18 minutes: the five findings
- 10 minutes: the arguable item
- 6 minutes: re-read your fixes as if you were the coordinator, then commit

---

## One rule for today

**Nothing goes in an email to your stakeholder that you cannot point at in a record.** This
afternoon, write yours the same way.
