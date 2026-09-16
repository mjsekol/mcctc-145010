# Clinic · The Acceptance Procedure, in Plain Words
## 145010 Senior Capstone · Week 10, Thursday · 15 minutes · Analyze

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 10, Thursday, or any week the room shows this signal: procedures
that say "open DevTools" or "run pytest."
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 2.12.1 (create a written procedure agreed by the stakeholders and project team
for determining the acceptability of the project deliverables), 2.12.3 (realistic test cases that
include targeted platforms and device types), 2.12.6 (seek stakeholder acceptance upon successful
completion of the test plan), 1.2.5 (communicate directions for an intended audience and purpose)

---

## Why this exists

In Week 16 you and your stakeholder sit down and run a procedure together. Their answer decides
10 of your 20 Stakeholder Outcome points. The procedure you send today is what they will follow.

Your stakeholder is not a programmer. If a step says "open DevTools and check the network tab for
a 201," they cannot run it. So either you run it for them, which means they are watching you and
not checking anything, or it becomes NOT RUN. **NOT RUN is never a pass.**

There is a second reason to send it now. When the stakeholder reads the steps, they find the
places where "done" still means something different to them. Finding that in Week 10 costs an
email. Finding it in Week 16 costs the acceptance.

## The skill in plain language

The acceptance procedure is section 7 of your test plan. It has four parts.

1. **One row per signed acceptance criterion.** Nothing more, nothing less. Each row has a
   starting state, what to do, what you should see, a result, and the evidence.
2. **Every step in the stakeholder's words.** Name what they see on screen: the box labelled "Bin
   code," the button that says "Mark low." No tools they do not use. No code words.
3. **"What you should see" is exact.** The words on the screen, the item on the list. Something
   the stakeholder can compare with their own eyes.
4. **The read-aloud paragraph,** read before you start. It is already in the
   [Test Plan template](../05-labs/MCCTC_145010_Template_TestPlan.md), section 7.

Three verdicts only: **PASS** (you saw the expected result), **FAIL** (you did not), and **NOT
RUN** (it could not be run, with the reason). A case is never changed because it is about to fail.

Some criteria need you to set up a starting state the stakeholder cannot, like a database that is
unreachable. That is fine. You set it up before the row, you say what you did, and the stakeholder
checks the result.

## Worked example 1 · from programmer steps to plain words

*Composite, not a real organization.* The Parts Bin Board's agreement has six signed criteria,
AC-1 to AC-6. AC-1 says a volunteer can mark a bin low with no name asked, and that a bad entry is
refused.

**Before:**

```
AC-1  Open DevTools > Network. Submit the form with bin_id=3. Confirm
      POST /report returns 201. Run pytest tests/test_report.py. Query
      SELECT * FROM low_reports and confirm a new row. Then POST a
      121-character note and confirm a 400.
```

The coordinator cannot do any of that, and none of it is what they care about.

**After:**

| AC | Starting state | What to do | What you should see | Result | Evidence |
|---|---|---|---|---|---|
| AC-1 | The desktop by the door, with the shop link open. B-03 is not on your low list. | 1. Look at every box on the form. 2. In the list labelled "Bin," choose B-03. Leave "Note" empty. Press "Mark low." 3. Choose B-05. Copy the long note from the card I hand you into "Note." Press "Mark low." 4. On your laptop, signed in, reload "Low bins." | 1. No box asks for a name, phone, or email. 2. "Thanks. Bin B-03 is marked low." 3. A message beside "Note" saying notes can be up to 120 characters. 4. B-03 is on the list with the time. B-05 is not. | | |

The stakeholder does every step. You prepared the 121-character note on a card beforehand, so they
do not have to count. The evidence column gets what they saw, written during the meeting.

## Worked example 2 · the other rows

*Composite.*

| AC | Starting state | What to do | What you should see | Result | Evidence |
|---|---|---|---|---|---|
| AC-2 | You are signed in. A volunteer is at the desktop. | Ask the volunteer to mark B-11 low. Within a minute, reload "Low bins." Press "Print this list." | B-11 is on the list. The printout is one page and every code and note is readable. | | |
| AC-3 | B-03 is on your list. | Press "Restocked" beside B-03. Then press "Sign out" and type the low list address into the browser. | B-03 is gone after the page reloads. After signing out, you see the sign-in page and no bins. | | |
| AC-4 | You are signed in with "Counts" open. Read today's number aloud. | In a new tab, open the board 5 times. Go back and reload "Counts." | Today's number is 5 more than the one you read aloud. | | |
| AC-5 | The desktop by the door, and a volunteer's phone. | On each, mark B-07 low. I time the board opening on the desktop with a stopwatch and read the time aloud. | On both, the "Thanks" message, with no sideways scrolling to reach the button. The desktop time is under 3 seconds. | | |
| AC-6 | The desktop, mouse set aside. I turn on Narrator. | Using only Tab, the arrow keys, and Enter, mark B-02 low. Listen as you go. | You finish with no mouse and can always see where you are. Narrator reads each field's name and the message after "Mark low." | | |

Look at AC-6. Its signed wording also says "zero automated violations." You can show the checker's
summary as extra evidence, but the row is passed by the stakeholder doing the task. A report you
hand them is something they can only trust, not check.

**A failure that is not signed.** E1, "the database cannot be reached," is in the requirements but
not in this agreement. So it is not a row here. It lives in section 4 of your test plan, where you
test it with a stand-in. If your agreement does have a failure criterion like it, write the setup
into the starting state and say it aloud: "I have switched the board to its test copy with the
database turned off."

## Worked example 3 · sending it

*Composite.* Sent Week 10, Thursday, from the student's school account with the instructor
copied. The one required sentence comes from the
[Measure & Analyze phase guide](../05-labs/MCCTC_145010_PhaseGuide_MeasureAnalyze.md#thursday--send-the-acceptance-procedure).

```
Subject: Parts Bin Board: the tests we will run together in Week 16

Hello,

These are the tests we will run together in Week 16. Please tell me if
any of them is not what you meant.

There are six, one for each point in the agreement you signed. Each one
says where to start, what to do, and what you should see. You will do
the steps yourself, and I will write down what happens.

If you can reply by Friday of next week, I will have time to fix any
step that is unclear.

Thank you,
Jordan
```

Then a line in the contact log, and the date the reply is due in your plan.

## The wrong version, and what it costs

*Composite.* A student sends a procedure with rows like "Run the test suite, expected 12 passed"
and "Check the health endpoint returns JSON." The coordinator replies:

```
I'm sorry, I don't know what most of this means. I trust you.
```

What that costs:

1. **"I trust you" is not agreement.** The rubric scores written acceptance against criteria the
   stakeholder ran. A run done without the stakeholder, with their written response afterward,
   sits in the 3 to 5 band of 10. See the
   [Capstone rubric](../09-project/MCCTC_145010_Capstone_Rubric.md#3a-acceptance-against-the-agreed-criteria--10-points).
2. **In Week 16 the student runs everything** while the coordinator watches, which is a demo, not
   an acceptance.
3. **The rows the coordinator cares about are missing,** like what a volunteer sees when a report
   fails.

## Why the wrong version is tempting

Your test plan's sections 1 to 6 are written for you, and they should be. Section 7 is written for
someone else, and switching voices is hard. Code words also feel more precise. They are precise, to
you. **Precision the reader cannot use is not precision.** Keep the automated tests. They belong in
section 4, not here.

## Do this today

1. Open your signed acceptance agreement. Count its criteria. Section 7 gets exactly that many
   rows.
2. Write each row in plain words. Then give it to a partner who has never seen your project. They
   read each step aloud and say what they would do. Every place they hesitate is a rewrite.
3. Search the section for `DevTools`, `pytest`, `endpoint`, `JSON`, `POST`, `SQL`, `console`, and
   `terminal`. Rewrite every hit, or move that step into your own setup.
4. Paste the read-aloud paragraph from the template above the table.
5. Send it with the one required sentence, instructor copied. Ask for agreement by Week 11, Friday.
6. Log it in `docs/communication/contact-log.md` and commit `docs/measure-analyze/test-plan.md`.

## If you are ahead, if you are behind

**Ahead.** For each row, write what you will do if it fails in Week 16: which log you will check,
and how you will record it without fixing it in front of the stakeholder.

**Behind.** Send the rows for the main task and the failure case today, and say the rest follow
Friday. A partial procedure sent on time starts the stakeholder's review. Tell your instructor at
standup.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Acceptance procedure** | The written tests that decide whether the stakeholder accepts the work. 2.12.1. |
| **Agreed by the stakeholders and project team** | The stakeholder read it and said yes, in writing. |
| **Acceptance criterion** | One signed Given, When, Then check. One row each. |
| **Targeted platforms and device types** | The phone, the desktop, keyboard only, Narrator. 2.12.3. |
| **Stakeholder acceptance** | The written decision after the run: accepted, accepted with follow-up, or not accepted. 2.12.6. |
| **Intended audience** | Who the writing is for. Here, a non-programmer. 1.2.5. |

## Self-check

**1.** Rewrite this step for a non-programmer: "Verify POST /report returns 400 when bin_id is
missing."

**2.** In Week 16, AC-5 cannot be run because the co-op's phone is not there. What is recorded?

**3.** Why does section 7 have exactly one row per signed criterion, and no extra rows for the
things you tested yourself?

### Answers

**1.** One good answer: "Leave the list labelled 'Bin' on 'Choose a bin' and press 'Mark low.'
You should see a message beside 'Bin' asking you to choose one, and nothing new on your low list."

**2.** NOT RUN, with the reason: the phone was not available. It is not a pass. You and the
stakeholder agree in writing when and how it will be run, or what happens instead.

**3.** Because the procedure decides acceptance against what was signed. An extra row adds a
promise nobody agreed to. Your own tests belong in section 4 of the test plan.
