# Clinic · From Observations to a Change List
## 145010 Senior Capstone · Clinic · Week 15, Friday

**The signal:** draft findings that report what people said ("P2 thought it was confusing") instead
of what they did. Findings and the change list are due today, and corrections start Monday.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.12.4 (develop, perform, and document usability testing), 2.12.5 (make
corrections indicated by test results), 1.10.4 (procedures for initiating product and service
improvements), 1.2.7 (problem solving and consensus building to determine next steps), 2.11.6 (test
a solution)

**Every example below is a composite**, built from invented sessions. The Northside Community Garden
is an invented organization.

---

## The idea in plain language

**Five session records become one findings table, one row per problem.** Each row says what people
did, how many of the five did it, and the line numbers that prove it. Then each finding you act on
becomes a change with a prediction and a re-test. **Every correction gets a re-test. After the last
correction, you re-run the whole test plan.**

## Why it exists

You have five records and about forty lines of notes each. Your stakeholder has ten minutes. The
findings table is how two hundred lines become five decisions somebody can check.

**The change list is where usability testing turns into corrections**, which is what 2.12.5 asks
for. A finding with no decision is a report. A change with no re-test is a guess.

---

## Step 1 · group lines into problems

Read all five write-ups with your scratch list beside you. Every time two lines describe the same
problem, they go in the same group, even if the people said different things.

```
Focus goes to page top after Claim        P1 L9, P3 L7, P4 L11
Clicked Sunday first when asked Saturday  P1 L2, P2 L3, P5 L2
Could not find own shifts                 P2 L14, P3 L12
"The green is nice"                       P4 L6 (opinion, not a problem)
Missed the export button                  P5 L18
```

## Step 2 · the findings table

```markdown
## Findings
| #  | What happened                                         | How many of the 5 | Evidence               | Severity | Decision |
| F1 | Could not find their own shifts; one moved on at 3 min | 2 of 5           | P2 L14, P3 L12         | Critical | change   |
| F2 | After Claim, keyboard focus went to the top of the page | 3 of the 3 who tried it keyboard only | P1 L9, P3 L7, P4 L11 | Serious | change |
| F3 | Chose the wrong day tab first                          | 3 of 5           | P1 L2, P2 L3, P5 L2    | Serious  | change   |
| F4 | Did not see the export button                          | 1 of 5           | P5 L18                 | Minor    | no change: coordinator-only, covered in training |
```

**Severity, from the protocol.** Critical: could not complete a task a requirement depends on.
Serious: completed it with a wrong attempt or a long delay. Minor: hesitation or a comment, no effect
on completion.

**Prioritize by severity first, then count.** F1 is seen twice and is first, because two people could
not finish a task R5 depends on. F3 is seen three times and is third.

**Read F2's count carefully.** Only three people tried a keyboard task, and all three hit it. Say so.
The honest count is out of the people who tried.

## Step 3 · four lines per change

```
Finding:      F1, 2 of 5 could not find their own shifts
Change:       a "My garden days" link at the top of every page (P3's word, P3 debrief)
Prediction:   a participant finds their shifts with no wrong attempts, under 30 s
How I know:   re-test Task 3 with at least one new person after the change

Finding:      F2, 3 of 3 keyboard users lost focus after Claim
Change:       after Claim, focus moves to the confirmation message
Prediction:   pressing Tab after Claim reaches the next open bed
How I know:   keyboard-only test case T-16 re-run, then re-test Task 2 with a new person

Finding:      F3, 3 of 5 chose the wrong day first
Change:       the next upcoming day is selected when the page opens
Prediction:   a participant reaches the right day with no wrong attempts
How I know:   re-test Task 1 with at least one new person after the change
```

**The prediction is the part people skip, and it is the part that makes the re-test mean
something.** Without it, any result looks like success.

## Step 4 · preferences, separately

```markdown
## Preferences (not findings)
- Make the header green like the garden sign. No finding supports this. Asked the coordinator.
```

A change with no finding above it is a preference. Preferences are allowed. They are labelled.

---

## Monday and Tuesday of Week 16 · corrections with re-tests

**Every correction gets a re-test**, recorded in section 6 of your
[Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md), with the case, the change, and the
re-run.

```
Corrections made because of the usability findings:
F2 · T-16 keyboard after Claim · focus moved to message · re-run Week 16 Mon: PASS
F3 · T-02 day selected on open · default is next upcoming day · re-run Week 16 Mon: PASS
F1 · Task 3 re-test, one new building adult, Week 16 Tue: found shifts in 12 s, 0 wrong attempts
```

**Then re-run the whole test plan, not only the fixed cases.** A change to what opens by default can
break a test nobody was thinking about. The full re-run is what lets you walk into the acceptance run
on Wednesday knowing what will happen. Release the corrections through your documented deployment
steps and record each release in your events log, so the thirty-day clock does not reset.

---

## The wrong version, and what it produces

```markdown
## Findings
- P2 thought the calendar was confusing.
- P4 loved the colors.
- 60% of users had trouble with the tabs.
- Several people said it was pretty intuitive overall.

## Changes
- Redesign the calendar
- Add dark mode
```

**What it produces:** nothing a reader can check. "Thought it was confusing" is an opinion. "60% of
users" turns three of five people into a claim about everyone. "Several people said" hides the fact
that two of them failed a task. "Redesign the calendar" has no prediction and no re-test, so Monday's
work cannot be shown to have helped. "Add dark mode" traces to no finding and adds scope after the
lock. At the acceptance run, the stakeholder hears that users found it intuitive, and then watches
it fail the way P2 did.

## Why the wrong version is tempting

What people say sticks in your memory longer than what they did, and it is usually kinder. A redesign
feels more satisfying than three small changes. **But what they did is the data. Your reasons are not,
and neither are their compliments.** Three small, re-tested changes are what move the acceptance
result.

---

## What to do in your project today

1. Group your lines into problems (step 1). Every group cites line numbers.
2. Write `docs/control/usability/findings.md` with the table (step 2). Counts out of five, or out of
   the number who tried.
3. Four lines for every change (step 3). A separate preferences list (step 4).
4. Add the limits: who your five do not represent, any session with a facilitator slip, and what
   five sessions cannot tell you.
5. Put the corrections into your Week 16 plan, highest priority first, each with its re-test.
6. Tell your stakeholder the top finding in today's
   [Weekly Stakeholder Update](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md), in
   their words.
7. Anything that is not a correction goes to the future improvements list in the
   [Change Request](../05-labs/MCCTC_145010_Template_ChangeRequest.md) file.
8. Part 7 of the [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md)
   is the reference for all of this. Commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Finding** | One problem, what people did, with a count and line-number evidence |
| **Severity** | Critical, serious, or minor, by effect on completing a task |
| **Change list** | The findings you act on, each with a change, prediction, and re-test |
| **Prediction** | What should happen after the change, written before you test it |
| **Re-test** | Running the task again after the change, ideally with a new person |
| **Full re-run** | Running the whole test plan after the last correction |

---

## Check yourself

1. F5 was seen once and was critical. F6 was seen five times and was minor. Which is first?
2. Write the prediction line for this change: "The Claim button text becomes Sign me up."
3. You corrected F2 and its test passes. Why run the whole test plan again?

---

## Check your answers

**1.** F5. Severity comes first. One person who could not complete a required task outranks five who
hesitated.

**2.** Something like: "A participant finds and presses the sign-up button with no hesitation longer
than 5 seconds." It must be something a re-test could show to be false.

**3.** Because a correction can break something else. Changing where focus goes, or what opens by
default, can change the result of cases that were passing. The full re-run shows the whole project
still does what the acceptance procedure expects.
