# Template · Baseline Measurement Record
## 145010 Senior Capstone · Week 9, and again in Week 17

**Commit as:** `docs/measure-analyze/baseline.md`
**Due:** plan Week 9, Monday. Record complete Week 9, Thursday. Repeat measurement and comparison
Week 17, Wednesday and Thursday.

**Competencies this evidences:** 1.10.5 (monitor customer expectations and determine
satisfaction by using measurement tools), 1.10.2 (determine the customer's needs), 2.11.4 (gather
and analyze data about a problem), 1.2.12 (technical writing to complete forms and reports),
1.2.1 (extract relevant, valid information and cite its source).

---

## Why this exists

**Without a "before," you cannot show an "after."** In Week 18 you will say what changed for your
stakeholder. If the only evidence is that they said they liked it, you have an opinion. If you
counted something in Week 9 and counted it again the same way in Week 17, you have a result.

**This is the only week you can take it.** Once your project is in use, the old process is gone.

**The failure to avoid.** Measuring something convenient instead of something that matters. The number
of clicks in your own app is convenient to count. The number of empty shifts the stakeholder complained about is
what matters.

---

## Choosing what to measure

Go back to your needs-discovery meeting record and find the sentence where the stakeholder said
what hurts. Then pick one of these shapes.

| Shape | Good when | Composite example |
|---|---|---|
| **Time a task** | The pain is that something takes too long | Minutes to find the right manual page for a counter question, timed on 10 questions |
| **Count errors in existing records** | The pain is mistakes | Shifts double-filled or empty, counted from the last six weekly schedules |
| **Count occurrences in a period** | The pain is how often something happens | Compressor heat shutdowns noticed late, from the maintenance log for the last two months |
| **Count steps or handoffs** | The pain is a clumsy process | Messages sent per week to arrange shifts |

**Count things. Do not copy people.** You never need a name to count an empty shift. If the
records have names in them, count with the stakeholder, or ask them to remove names before you see
the records.

---

```markdown
# Baseline Measurement · <project name>
Planned: Week 9, <day>   Measured: Week 9, <day>   Repeated: Week 17, <day>

## 1. The question
*One question, in the stakeholder's terms.*
<For example: "How many shifts per week are empty or double-filled?">

**Where it came from:** meeting record, Week <n>, <day>, line <n>.
**Objective it supports:** proposal section 6, objective <n>.

## 2. The method
*Precise enough that you could repeat it exactly in Week 17, or that someone else could.*

- **What is counted or timed:**
- **The source:** <records, direct observation, a timed trial>
- **The sample:** <which records, which period, how many>
- **Who took the measurement, and where:** <role, not name>
- **Tools used:** <stopwatch, spreadsheet, a script, with the file name>
- **How personal data was kept out:**

## 3. The results
*Raw counts first. Averages second, with the arithmetic shown.*

| Item | Count or time |
|---|---|
| | |
| | |

**Summary:** <for example: 9 problem shifts in 72, across 6 weeks: 9 / 6 = 1.5 per week>

## 4. The limits
*What this measurement cannot tell you. At least three entries.*
- <for example: six weeks in the fall may not be typical of the spring>
- <for example: measured once, by one person>
- <...>

## 5. What I did not measure, and why
- <...>

## 6. Why a simpler fix might not be enough
*One paragraph. What would a non-software fix do, and what would it miss? AI-Integrated track:
what would a version with no model do?*

## 7. Repeat plan for Week 17
- **Same source and sample size:** <how you will get it>
- **What will be different, honestly:** <for example: a shorter period, because the project has
  only been in use since Week 11>

---

## 8. The comparison · Week 17
*Filled in Week 17. Same method. Report the limits with the result.*

| Measure | Week 9 | Week 17 | Change |
|---|---|---|---|
| | | | |

**What changed, in one sentence:**
**What this does not prove:**
**What the stakeholder said about it** (quoted, from a meeting record, labelled as their opinion):
```

---

## Before you commit · self-check

- [ ] The question is about the stakeholder's problem, not about your software.
- [ ] Someone else could repeat section 2 and get comparable numbers.
- [ ] No names, no personal data, anywhere.
- [ ] Section 4 has at least three honest limits.
- [ ] **No percentages from tiny samples.** "9 of 72 shifts" says what you know. "12.5 percent" makes
      a small sample sound like a survey.
