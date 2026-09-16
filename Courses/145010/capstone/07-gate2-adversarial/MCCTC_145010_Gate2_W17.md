# Gate 2 · Week 17 · The Guide That Would Erase the Desk
## 145010 Senior Capstone · Week 17, Wednesday · first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool.** You may open any file in `W17/`, and **you may
and should run the app.** You may not ask another student.

**Rubric this week: the AI Output Evaluation parameters.** Validity, Relevance, Authenticity,
Potential Bias, Hallucinations. The document is a user guide, so the parameters apply to what it
tells a person to do.

**Competencies:** 2.13.6 (deliver support and training materials), 6.1.4 (drafting, revising,
editing, and proofreading), 1.2.5 (communicate directions for an intended audience), 1.10.3
(communicate features, benefits, and warranties), 1.3.8 (intellectual property compliance),
1.2.1 (extract valid information and cite sources).

**Grade category:** Written & Documentation.

---

## Why you are doing this today

Your own user guide is due today. The [User Guide](../05-labs/MCCTC_145010_Template_UserGuide.md)
template says the test of a guide is whether your stakeholder can use the project with nothing
else. **A guide is also the one document a stranger will follow exactly, step by step, on the worst
day.** A wrong sentence in a README costs a developer ten minutes. A wrong sentence in a user guide
can cost the stakeholder every record they have.

An AI assistant writes guides quickly and confidently. Today you check one against the app it
describes, by running the app.

---

## The situation

**This is an invented composite.** The Hillcrest Senior Center, its front desk, its front office
manager, its groups, and its items do not exist.

A student built Front Desk Checkout, a small web app the center's front desk uses to lend shared
items such as folding tables and the projector to the center's groups. The student asked an AI
assistant to write the user guide from the README and the app, made a few edits, and planned to
deliver it on Thursday at training.

---

## What is in the folder

| Path | What it is |
|---|---|
| `W17/app/README.md` | **First.** Developer notes: what the app does, how to run it, its addresses |
| `W17/app/app.py` | The program |
| `W17/app/templates/` | The three page templates |
| `W17/app/start-checkout.bat` | The start file the front desk computer uses |
| `W17/user-guide.md` | The AI-written guide. The document you are evaluating. Sections are numbered |

## How to run it

**Port 8165.** Use a database in your temp folder so nothing you try can damage your repository.

PowerShell:

```
cd W17/app
$env:CHECKOUT_DB = "$env:TEMP\checkout-gate2.db"
python app.py
```

Then open `http://127.0.0.1:8165`. **You may try any step the guide gives, on this copy.** Stop the
app with Ctrl+C when you finish, and delete any `checkout.db` that appears inside the `app` folder.

**The failure mode to name now:** you read a step, it sounds sensible, and you move on without
trying it. **A recovery step is the kind you only find out about by doing it.** If a step says
something will happen, make it happen and count what is there before and after.

---

## The five parameters

| Parameter | The question it asks here |
|---|---|
| **Validity** | If the stakeholder does exactly what a step says, does the promised result happen? |
| **Relevance** | Is it written for the person who will use it, about what they will do? |
| **Authenticity** | Is it written by the student, about this project? |
| **Potential Bias** | Who can follow it, and who does it leave out? |
| **Hallucinations** | Does it describe something that does not exist in the app? |

**There is one planted problem under each parameter, five in all.** There is also **one item that
is genuinely arguable**. It is not one of the five.

**The guide is not all wrong.** Several sections are correct, and one of them is quoted word for
word from the app.

---

## What to hand in

Commit `gate2/w17.md` in your repository. Five findings, one per parameter, each with all six of
these:

```
Parameter         which of the five
The claim         quoted exactly, with its section number
Why it is wrong   in your own words
How you know      what you ran, what you searched, or what you read in the app, and what came back.
                  For a step you tested, the counts before and after
Who is harmed     a real person or group, and what they would lose or be unable to do
The fix           what the guide should say instead
```

Then one more entry, for the arguable item:

```
The claim                 quoted, with its section number
The case that it is fine  the strongest version
The case that it is not   the strongest version
What would settle it      the one fact you would go and get, and from whom
```

**You are not scored on which side you pick.** You are scored on whether both cases are real.

---

## Scoring

| Item | Points |
|---|---|
| **Validity finding** | **2. Missing it costs both points** |
| Relevance finding | 1 |
| Authenticity finding | 1 |
| Potential Bias finding | 1 |
| Hallucinations finding | 1 |
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

**Why Validity carries double weight this week.** A guide is trusted because the reader cannot
check it. When a step promises one result and delivers another, the reader follows it anyway, and
some results cannot be undone by any later step.

---

## Time

- 5 minutes: README, then start the app
- 5 minutes: read the guide once, without stopping
- 18 minutes: test the steps and write the five findings
- 8 minutes: the arguable item
- 4 minutes: stop the app, delete any test database, commit

---

## One rule for today

**Do not write "this step is wrong" until you have run it.** Then, this afternoon, run every step in
your own guide the same way before you deliver it.
