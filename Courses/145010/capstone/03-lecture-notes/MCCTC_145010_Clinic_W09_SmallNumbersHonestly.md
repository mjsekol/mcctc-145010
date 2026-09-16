# Clinic · Small Numbers, Honestly
## 145010 Senior Capstone · Week 9, Thursday · 15 minutes · Measure

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 9, Thursday, or any week the room shows this signal: baselines
reported as percentages, or with no limits.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.10.5 (determine satisfaction by using measurement tools), 2.11.4 (gather and
analyze data about the problem), 1.2.12 (technical writing to complete forms and reports), 1.2.1
(extract relevant, valid information and cite its source)

---

## Why this exists

Your baseline record is due today, and Grading Period 3 closes tomorrow. What you write today is
also what you compare against in Week 17 and report to a panel in Week 18.

Your sample is small. Six nights. Ten questions. Two months of a log. That is normal for a
capstone, and it is fine, as long as you report it as what it is.

The failure this clinic prevents is **a small count dressed up as a big finding.** "28.3 percent of
repairs stall" sounds like a study of hundreds of repairs. It came from six evenings. A panel
member who asks "out of how many?" will find that out in one question, and your credibility goes
with it.

## The skill in plain language

Report a baseline in four layers, in this order:

1. **Raw counts first.** Every number you collected, in a table, before any math.
2. **Arithmetic shown.** Write the sum and the division, so a reader can check them.
3. **A summary in counts, not percentages.** "17 stalled repairs in 6 nights." A rate per night is
   fine when you show where it came from.
4. **At least three honest limits.** What this measurement cannot tell you.

**Rounding rule.** Keep the full result in your working, then round once for the summary. One
decimal place is plenty for a rate from a small sample. More decimals suggest precision you do not
have.

**The percentage rule.** Do not turn a tiny sample into a percentage. "9 of 72 shifts" tells the
reader what you know. "12.5 percent" hides the 72.

## Worked example 1 · the Parts Bin Board baseline

*Composite, not a real organization.* The bike co-op's shop coordinator filled in the tally sheet
for the last six open-shop nights.

**Raw counts:**

| Night | Repairs stalled because a bin was empty |
|---|---|
| 1 | 4 |
| 2 | 2 |
| 3 | 3 |
| 4 | 0 |
| 5 | 5 |
| 6 | 3 |

**Arithmetic, shown:**

```
Total:     4 + 2 + 3 + 0 + 5 + 3 = 17
Per night: 17 / 6 = 2.833...
Rounded:   2.8 per night (one decimal place)
Range:     lowest 0 (night 4), highest 5 (night 5)
```

**Check it.** 2.8 times 6 is 16.8, and 2.833 times 6 is 17.0. The rounding lost nothing that
matters.

**The summary line:**

```
17 stalled repairs in 6 open-shop nights, an average of 2.8 per night
(17 / 6 = 2.83, rounded), ranging from 0 to 5.
```

The range matters. An average of 2.8 hides that one night had none and one had five.

## Worked example 2 · the same numbers, reported badly

*Composite.* The coordinator's sheet also recorded repairs started: 11, 9, 10, 8, 12, 10, which is
60 in total. A student wrote this:

```
Baseline: 28.3% of repairs stall due to empty bins.
Stalls fell 40% from night 5 to night 6, showing the problem is improving.
```

Both numbers are arithmetically right. 17 / 60 = 0.283. And (3 - 5) / 5 = -0.40. Both are
misleading.

- **28.3 percent** makes 60 repairs sound like a survey. The honest line is "17 of 60 repairs
  started stalled because a bin was empty."
- **"Fell 40 percent"** is two nights compared. Night 4 had zero and night 5 had five. That is
  ordinary variation, not a trend. Two points never make a trend.

**The rewrite:**

```
17 of the 60 repairs started across 6 open-shop nights stalled because a
bin was empty. Nights ranged from 0 to 5 stalls. Six nights is too few to
show a trend.
```

## Worked example 3 · three honest limits

*Composite.* Section 4 of the
[Baseline Measurement template](../05-labs/MCCTC_145010_Template_BaselineMeasurement.md) for the
Parts Bin Board:

```
- Six nights, counted once, by one person. A busier or quieter stretch
  could give a different number.
- The count depends on volunteers writing "waiting on part" in the log.
  A stall nobody wrote down is not counted, so the true number may be higher.
- The log records that a repair stalled, not for how long. This baseline
  cannot say how much time was lost.
```

Each limit names something specific to this method. "The sample might be small" alone is too
vague to be useful.

## The wrong version, and what it costs

A baseline section that reads only:

```
About 30% of repairs are delayed by missing parts.
```

What it costs:

1. **No raw counts,** so nobody can check it, including you in Week 17.
2. **"About 30%"** is a rounded percentage of a sample the reader cannot see.
3. **"Missing parts"** is broader than what was counted: bin items only.
4. **No limits.** Rubric part 3C asks for the comparison "reported with its limits stated." See
   the [Capstone rubric](../09-project/MCCTC_145010_Capstone_Rubric.md#3c-measured-change-from-the-baseline--5-points).

## Why the wrong version is tempting

Percentages look professional. Every chart you have seen online uses them. A limits section feels
like admitting the work is weak. It is the opposite. **A limit you name yourself is a strength. A
limit a panel member finds for you is a weakness.** The rubric scores a measured result for its
honesty, not its size.

## How the Week 17 comparison will look

*An invented illustration, not a result.* If the Week 17 repeat counts 9 stalls in 6 nights, the
comparison row reads:

| Measure | Week 9 | Week 17 | Change |
|---|---|---|---|
| Stalled repairs, bin empty, 6 nights | 17 (2.8 per night) | 9 (1.5 per night) | 8 fewer |

The arithmetic: 9 / 6 = 1.5, and 17 - 9 = 8. "8 fewer in 6 nights" is the honest headline. Not
"a 47 percent reduction."

## Do this today

1. Fill in section 3 of `docs/measure-analyze/baseline.md`: raw counts table, then arithmetic in a
   code block, then the summary line.
2. Check every division with a calculator, then check the reverse: multiply back.
3. Search the file for `%` and the word `percent`. Rewrite each as a count "of" a total.
4. Write at least three limits specific to your method.
5. Fill in section 7, the repeat plan, so Week 17 uses the same method.
6. Commit. Then send your requirements version 1 to the stakeholder, as the
   [phase guide](../05-labs/MCCTC_145010_PhaseGuide_MeasureAnalyze.md#thursday--finish-the-baseline-send-the-requirements)
   says. Grading Period 3 closes tomorrow. What is committed is what is graded.

## If you are ahead, if you are behind

**Ahead.** Write section 5, what you did not measure and why. Then ask a partner to repeat your
arithmetic from your raw counts without looking at your answer.

**Behind.** If your data has not arrived, commit the record anyway with the plan, the request you
sent, and "Results: not yet received, requested Week 9, Monday." That is honest and gradable. A
made-up number is neither. Tell your instructor at standup.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Baseline** | The "before" number, taken before your project exists. |
| **Measurement tool** | What produced the numbers: the log, the tally sheet, the timer. 1.10.5. |
| **Analyze data** | The arithmetic, the range, and what the numbers can and cannot show. 2.11.4. |
| **Valid information** | A number that measures what you say it measures, with its source cited. 1.2.1. |
| **Report** | A written record another person can check. 1.2.12. |

## Self-check

**1.** A classmate timed 8 manual lookups: 6, 9, 4, 12, 7, 5, 10, 3 minutes. Write the summary
line with the arithmetic shown.

**2.** What is wrong with "Empty shifts dropped 50% from week 2 to week 3" when week 2 had 4 and
week 3 had 2?

**3.** Name one limit that almost every capstone baseline shares.

### Answers

**1.** Total: 6 + 9 + 4 + 12 + 7 + 5 + 10 + 3 = 56. Average: 56 / 8 = 7.0. Summary: "8 lookups
took 56 minutes in total, an average of 7.0 minutes each (56 / 8), ranging from 3 to 12 minutes."

**2.** Two weeks cannot show a trend, and 50 percent makes a change of 2 shifts sound large. The
honest line is "4 empty shifts in week 2 and 2 in week 3."

**3.** It was measured once, over a short period, by one person, so a different period could give
a different number. Other good answers: the source only records what people remembered to write
down, or the sample is too small to show a trend.
