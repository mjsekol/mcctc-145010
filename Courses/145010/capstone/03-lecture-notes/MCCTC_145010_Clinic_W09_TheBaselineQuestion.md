# Clinic · The Baseline Question
## 145010 Senior Capstone · Week 9, Monday · 15 minutes · Measure

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 9, Monday, or any week the room shows this signal: baseline plans
that measure the student's own app, or measure a feeling.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.10.5 (monitor customer expectations and determine satisfaction by using
measurement tools), 1.10.2 (determine the customer's needs), 2.11.4 (gather and analyze data about
the problem), 1.2.12 (technical writing to complete forms and reports)

---

## Why this exists

In Week 18 you will stand up and say what changed for your stakeholder. You need a number for
that. A number needs a "before," and this week is the only time you can take it. Once your project
is in use, the old way of doing things is gone.

The failure this clinic prevents is a baseline that measures the wrong thing. It usually looks
like one of two plans:

- **Measuring your own software.** "Clicks to report a bin in my app." Your app does not exist yet,
  so there is nothing to count. Even later, it tells you about your app, not about the problem.
- **Measuring a feeling.** "Do volunteers feel frustrated?" A feeling can matter. It is also hard
  to count the same way twice, and your stakeholder never asked you to change it.

Both are tempting because they feel measurable. Neither can show that the problem got smaller.

## The skill in plain language

You turn the stakeholder's complaint into **one measurable question** and **one repeatable method**.

1. Open your needs-discovery meeting record. Find the sentence where the stakeholder said what
   hurts. Copy it word for word.
2. Ask: what would I count or time to see that pain on paper?
3. Write one question in the stakeholder's words. It must be about their problem, not your build.
4. Write the method so exactly that you could repeat it in Week 17, or a classmate could do it
   without asking you.

The method has six parts, the same six the
[Baseline Measurement template](../05-labs/MCCTC_145010_Template_BaselineMeasurement.md) asks for:
what is counted or timed, the source, the sample, who measures and where, the tools, and how
personal data stays out.

There are four shapes a baseline usually takes: time a task, count errors in existing records,
count occurrences in a period, or count steps and handoffs. Pick the one that matches the pain.

## Worked example 1 · the Parts Bin Board

*Composite, not a real organization.* A volunteer-run community bike repair co-op fixes donated
bikes on open-shop nights. The shop coordinator told the student this, recorded in the Week 7
meeting record:

> "A repair stops dead because the tube bin is empty, and nobody tells me. I find out when I walk
> the shelves and text myself a list."

**The first draft of the question:**

```
How many clicks does it take a volunteer to report a low bin?
```

That measures a product that does not exist. It is the wrong question.

**The rewrite:**

```
On an open-shop night, how many repairs stall because a needed part's bin is empty?
```

**The method, written to be repeated:**

```
What is counted:  repairs the paper repair log marks "waiting on part", where the
                  part is a bin item (tubes, brake pads, chains, cables)
The source:       the co-op's paper repair log
The sample:       the last six open-shop nights before Week 9, Tuesday
Who, and where:   the shop coordinator counts at the co-op; the student records
                  the totals the coordinator reads out
Tools:            a paper tally sheet with one row per night
Personal data:    none leaves the log; the coordinator counts, the student never
                  sees a name (see the Week 9, Tuesday clinic)
```

The question uses the coordinator's words: "repair," "stall," "bin." It is about the co-op's
problem. The method is specific enough that a stranger could do it again in Week 17.

## Worked example 2 · one question, not three

*Composite.* A student working with the same co-op wrote three questions:

```
1. How many repairs stall because a bin is empty?
2. How long does the coordinator's shelf walk take?
3. How many texts does the coordinator send about parts each week?
```

All three connect to the pain. Only one can be the baseline. The student picked the first,
because the coordinator's complaint was about stalled repairs, and because the paper log already
records it. The other two went into section 5 of the template, "What I did not measure, and why,"
with the reason written down. That is a decision, so it also goes in the decision log.

## Worked example 3 · the same move on other tracks

*Composite examples, drawn from the template.*

| Complaint, in the stakeholder's words | Wrong question | Measurable question and shape |
|---|---|---|
| "The compressor overheats and we find out too late." | How fast does my panel refresh? | How many heat shutdowns in the last two months were noticed late, from the maintenance log? Count occurrences in a period. |
| "The new counter staff take forever to find the right manual page." | Would staff like an AI helper? | How many minutes does it take to find the right page for 10 typical questions? Time a task. |
| "We double-book shifts every week." | How many shifts can my app hold? | How many shifts were empty or double-filled in the last six weekly schedules? Count errors in existing records. |

## The wrong version, and what it costs

A plan that measures a feeling looks like this:

```
Question: Are volunteers frustrated by empty bins?
Method:   Ask a few volunteers how they feel.
```

What it costs, in order:

1. **It cannot be repeated.** "A few volunteers" in Week 9 and a different few in Week 17 are not
   the same measurement.
2. **It collects opinions from people who did not agree to be studied.** Asking volunteers about
   themselves drifts toward personal data.
3. **Rubric part 3C, measured change from the baseline, is worth 5 points.** The rubric says a
   satisfaction statement with no measurement behind it earns 1 to 2 of those points. See the
   [Capstone rubric](../09-project/MCCTC_145010_Capstone_Rubric.md#3c-measured-change-from-the-baseline--5-points).

## Why the wrong version is tempting

Your app is the thing you are excited about, so counting inside it feels natural. A feeling is
the first word a stakeholder uses, so it feels faithful. The fix is one question: **could I take
this measurement today, before I build anything?** If the answer is no, you are measuring your
build, not the problem.

## Do this today

In the build period:

1. Copy the stakeholder's complaint from your meeting record into section 1 of the template,
   with the week, day, and line it came from.
2. Write the question. Read it aloud to a partner. Ask: "Is this about their problem or my app?"
3. Write all six method lines.
4. Send the stakeholder your request for the data today, through your school email with your
   instructor copied. Say exactly what you need them to count. Log it in
   `docs/communication/contact-log.md`.
5. Add a decision log entry for the question you picked and the ones you did not.
6. Commit `docs/measure-analyze/baseline.md` with sections 1 and 2 filled in.

The day-by-day plan is in the
[Measure & Analyze phase guide](../05-labs/MCCTC_145010_PhaseGuide_MeasureAnalyze.md#week-9--measure).

## If you are ahead, if you are behind

**Ahead.** Write section 6 of the template: what a non-software fix would do and what it would
miss. For the co-op, a clipboard by the bins is a real option. Say honestly why it might not be
enough. AI-Integrated track: write the "why a model" comparison in your decision log.

**Behind.** If your stakeholder has not given you a complaint you can quote, you cannot write
this yet. Tell your instructor at standup tomorrow. Draft a two-question message asking "Walk me
through the last time this went wrong" and "Is there a record I could count, with no names in it?"

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Baseline** | The measurement of the current process before your project exists. |
| **Measurement tool** | What you use to count or time: a log, a tally sheet, a stopwatch, a script. 1.10.5. |
| **Customer needs** | The problem as the stakeholder describes it, before any solution. 1.10.2. |
| **Gather and analyze data** | Collect records about the problem and work out what they show. 2.11.4. |
| **Objective** | A result the project aims for, which the baseline lets you check. |

## Self-check

**1.** A student writes: "Baseline question: how long does my sign-in page take to load?" Name
what is wrong with it in one sentence.

**2.** Why must the method be written so precisely?

**3.** A stakeholder at an animal shelter says, "Volunteers show up for walks and there is nobody
to hand them a dog." Write one measurable question, and name its shape.

### Answers

**1.** It measures the student's own software, which does not exist yet and says nothing about
the stakeholder's problem.

**2.** Because in Week 17 you, or someone else, must take the same measurement the same way.
If the method changes, the two numbers cannot be compared, and rubric part 3C scores that lower.

**3.** One good answer: "In the last four weeks of the shelter's walk schedule, how many walk
slots had a volunteer arrive with no dog assigned?" The shelter staff count it, so no volunteer
names leave the schedule. Its shape is counting errors in existing
records. Any question works if it is countable from something that exists today, uses the
stakeholder's words, and needs no names.
