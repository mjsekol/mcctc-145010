# Clinic · Requirements, Not Designs
## 145010 Senior Capstone · Week 9, Wednesday · 15 minutes · Measure

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 9, Wednesday, or any week the room shows this signal:
requirements that describe buttons and colors, or that trace to nothing.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.10.2 (determine the customer's needs and identify solutions), 2.12.1 (a
written procedure for determining acceptability, which starts here), 1.2.12 (technical writing),
6.1.2 (plan for devices, audience, and ADA requirements), 2.7.4 (how browsers and devices affect a
page)

---

## Why this exists

Your Requirements Fit score, 20 of the 100 points in the final code review, is judged against the
document you start today. A vague requirement is a risk to you, not only to your stakeholder.

Two failures show up in almost every first draft:

- **A requirement that is really a design.** "A big red button at the top." That is a decision
  about looks. It belongs in Monday's design brief. It also locks you in: if the button moves, the
  requirement fails, even though nothing the stakeholder needs has changed.
- **A requirement that traces to nothing.** It sounds useful, nobody asked for it, and it quietly
  grows your scope. In Weeks 9-12, a requirement with no source is a scope change and needs a
  change request.

## The skill in plain language

**A requirement says what must be possible. It does not say how it looks.**

Each functional requirement has four parts:

1. **An ID that never changes.** R1, R2, R3. A removed requirement is marked removed, not deleted.
2. **One sentence with "must" or "should."** "Must" is required and gets tested at acceptance.
   "Should" is wanted and does not.
3. **A trace line.** Which need (N1, N2) and which proposal scope item it comes from.
4. **At least one acceptance criterion** in Given, When, Then form that could fail.

Then two more sections that first drafts forget:

- **Failure behavior.** What the user sees when the database is down, the input is wrong, or
  someone without permission tries something. Each failure gets a criterion.
- **Non-functional requirements with numbers.** "Fast" is not a requirement. "Loads in under 3
  seconds on the co-op's desktop" is.

A test for any sentence you write: **could the design change completely and this still be true?**
If yes, it is a requirement. If no, it is a design.

## Worked example 1 · from design to requirement

*Composite, not a real organization.* The Parts Bin Board, for a bike repair co-op.

**Before:**

```
R1  A big red "BIN LOW" button at the top of the home page. When you click it a
    popup asks for the bin. It should be fast and easy to use.
```

Count the problems. "Big red," "top," and "popup" are design. `fast` and the phrase after it cannot
fail, because nobody can measure them. There is no trace and no criterion.

**After:**

```
R1 · Mark a bin low
The system must let anyone with the shop link mark a parts bin low by choosing
its bin code and, if they want, adding a note of up to 120 characters. It must
never ask for a name.
Traces to: need N1, proposal scope item "mark a bin low".

- AC-1.1 Given the board is open at the shop link, when a volunteer chooses
  bin B-03 and presses Mark low with no note, then B-03 appears on the
  coordinator's low list with the time it was marked.
- AC-1.2 Given the board is open, when a volunteer adds a note of exactly
  120 characters, then the note is saved and shown in full on the low list.
```

The button can be any color and anywhere. The requirement still holds.

## Worked example 2 · the failure table

*Composite.* The same project, section 2 of the
[Requirements Specification template](../05-labs/MCCTC_145010_Template_RequirementsSpecification.md).

| ID | Situation | What the user sees | Criterion |
|---|---|---|---|
| E1 | The database cannot be reached | "The board cannot save right now. Please tell the coordinator in person." Nothing is reported as saved. | AC-E1 |
| E2 | No bin chosen, or a note longer than 120 characters | A message next to the field that has the problem. Nothing is saved. | AC-E2 |
| E3 | Someone not signed in opens the low list or sends a restock | The sign-in page. Nothing changes. | AC-E3 |

E1 matters most for this stakeholder. A volunteer who is told a report was saved when it was not
trusts the board, and the repair stalls anyway. That is worse than no board.

## Worked example 3 · non-functional numbers and a "should"

*Composite.* A slice of section 3.

| ID | Kind | Requirement | How it is measured |
|---|---|---|---|
| NF1 | Performance | The board page loads in under 3 seconds on the co-op desktop over the shop Wi-Fi | Browser developer tools, Network panel, three loads, the slowest reported |
| NF3 | Accessibility | Zero automated violations at WCAG 2 A and AA; every task by keyboard alone; labels and messages that make sense in Windows Narrator | Automated check, keyboard walkthrough, Narrator walkthrough |
| NF4 | Devices | The co-op desktop: Windows, Edge, 1280 pixels wide. Volunteers' phones, 360 pixels wide. Keyboard only. Windows Narrator | Test plan platform cases |

And one "should":

```
R5 · Group the low list by shelf (should)
The low list should group bins by the shelf they sit on.
Traces to: need N2, proposal stretch list.
Not tested at acceptance.
```

Writing it as a "should" is honest. It is wanted. It is not promised.

## The wrong version, and what it costs

*Composite.* A student's version 1 contains this:

```
R7 · Volunteer accounts
The system must let each volunteer sign in and see the repairs they worked on.
```

Look for its trace line. There is none, because nobody asked for it. The signed scope says
volunteers mark bins with no name.

What it costs:

1. **Scope grows by a sign-in system and a repair history.** The Full-Stack track guide warns
   that authentication alone can eat three sprints.
2. **It stores personal data** the proposal never justified.
3. **If the stakeholder signs it without noticing,** you are now scored on a requirement you
   probably cannot finish.

The fix is to delete R7 before sending, or, if the stakeholder truly wants it, to raise a change
request that names what it replaces.

## Why the wrong version is tempting

You have spent two years designing screens, so you think in screens. Writing "a red button" feels
more concrete than "must let anyone mark a bin low." And extra requirements feel generous. They are
not. **Every requirement is a promise you will be scored on.** Promise what was agreed.

## Do this today

The Gate 2 critique takes the first 40 minutes of the build period. After it:

1. Open your signed acceptance agreement and your proposal side by side.
2. Write one R-number for each in-scope item. Each gets a trace line and at least one criterion.
3. Fill in section 2 with at least three failures.
4. Give every non-functional requirement a number and a way to measure it.
5. Run the self-check at the bottom of the template. Search your draft for these words and
   rewrite every hit: `color`, `button`, `top`, `fast`, `easy to use`, `user-friendly`.
6. Commit `docs/measure-analyze/requirements.md` as version 1.0. It goes to the stakeholder
   tomorrow.

## If you are ahead, if you are behind

**Ahead.** Fill in section 7, the traceability table. Every row should run from a need to a
proposal item to a requirement to a criterion. A gap in any column is a finding.

**Behind.** Get R1 complete with its trace and two criteria before the period ends. A short
version 1 that is precise is worth more than a long one that is vague. Tell your instructor at
standup what is left.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Requirement** | What the system must make possible, stated so it can be tested. |
| **Acceptance criterion** | A Given, When, Then check that could fail. |
| **Customer needs** | The N-numbers your requirements trace to. 1.10.2. |
| **Procedure for determining acceptability** | Where your criteria end up in Week 10. 2.12.1. |
| **ADA requirements** | The accessibility requirement, NF3. 6.1.2. |
| **Devices and browsers** | The platforms NF4 names. 2.7.4. |

## Self-check

**1.** Is this a requirement or a design? "The low list uses a table with the bin code in bold in
the first column."

**2.** Rewrite "The board must be fast" as a non-functional requirement.

**3.** A classmate's R6 reads "The system must send the coordinator a text when a bin is low."
The signed proposal lists text alerts as out of scope. What should happen to R6?

### Answers

**1.** A design. Bold, first column, and table are all about looks. The requirement underneath is
something like "The coordinator must be able to see which bins are low."

**2.** One good answer: "NF1: The report page loads in under 3 seconds on the co-op desktop,
measured with the browser's developer tools over three loads." Any version with a number, a place,
and a way to measure it earns the point.

**3.** Remove it before sending. It traces to nothing in scope. If the stakeholder wants it, it
goes through a change request that names what it replaces, and the stakeholder agrees in writing.
The Full-Stack track guide also lists sending text messages from the app as a change in risk, not
a stretch goal.
