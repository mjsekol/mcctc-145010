# Clinic · Running the Acceptance Run
## 145010 Senior Capstone · Clinic · Week 16, Wednesday

**The signal:** acceptance runs booked for today or tomorrow. Anyone running one this week reads this
before the build period.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. You ran an acceptance procedure
in 145130. This one is with an adult who signed your criteria in Week 8, and their decision is most
of your Stakeholder Outcome score.

**Competencies:** 2.12.1 (a written procedure agreed by the stakeholders and the project team),
2.12.6 (seek stakeholder acceptance upon successful completion of the test plan), 2.12.3 (compare
with expected performance on targeted platforms), 1.2.13 (identify stakeholders and solicit their
opinions), 1.2.12 (technical writing to complete forms and reports)

**Every example below is a composite.** The Northside Community Garden is an invented organization,
and "the coordinator" is an invented role holder.

---

## The idea in plain language

**You and your stakeholder run the procedure you both agreed, case by case, on the deployed system.
Each case gets PASS, FAIL, or NOT RUN, with what was actually seen. Then the stakeholder decides, in
writing.** You record it in the [Acceptance Record](../05-labs/MCCTC_145010_Template_AcceptanceRecord.md).

## Why it exists

In Week 8 you and your stakeholder wrote down what "done" means, before either of you knew how the
build would go. Today you find out, together, whether it is done. The procedure was agreed in advance
so that nobody can move the finish line: not them, and not you.

**This is the moment most likely to make you nervous.** Something will probably fail. That is normal,
and the rules below exist so that a failure is recorded well instead of handled badly.

### The five rules, from the Control phase guide

1. **You run the procedure the stakeholder agreed**, the committed version. Not a newer one.
2. **You do not change a case because it is about to fail.** That is the whole reason the procedure
   exists.
3. **A surprise failure is written down, not fixed in front of them.** "That is a real failure. I
   will fix it and re-run it."
4. **If the stakeholder does not understand a case, that is a finding** about your writing.
5. **Something not accepted is recorded honestly** with what you agreed to do about it.

**A criterion is never quietly changed.** If a case turns out to be wrong, you say so before running
it, record it NOT RUN, and any change is agreed out loud and written into a change request. It never
happens quietly in a text editor. The rubric scores a quietly edited criterion at 0 for acceptance.

---

## Before the run

- [ ] The procedure is test plan section 7, **as committed when the stakeholder agreed it.** Write
      that commit hash in the record.
- [ ] You are testing the **deployed system**, not your laptop. Load it once ten minutes before, in
      case a free host is asleep.
- [ ] Your instructor is present, or the call is one your instructor approved.
- [ ] Invented test data is in place. No real names on screen.
- [ ] Your whole test plan was re-run after the last correction, and you know what to expect.
- [ ] A printed run sheet, one row per criterion, and a pen.

---

## Worked example 1 · the opening, read aloud

From section 7 of the [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md), word for word:

```
Some of these cases test what happens when something goes wrong, so a message
on screen may be the right result. If something fails that we did not expect,
I will write it down and fix it afterward rather than fix it in front of you.
If any step does not make sense, tell me, because that is something I need to
fix in the writing.
```

**The result:** the stakeholder knows an error message can be a pass, knows a failure will not turn
into a debugging session, and knows their confusion is useful. Rules 3 and 4 are set up before the
first case.

## Worked example 2 · the run sheet, filled in during the run

```
## 3. Results
| AC   | Verdict | What was actually seen                                                  |
| AC-1 | PASS    | Coordinator's phone: claimed bed 4 appeared on the coordinator page 3 s after reload |
| AC-2 | PASS    | Second browser: "This bed is already taken"; bed 4 lists one volunteer   |
| AC-3 | PASS    | Signed-out visitor opening /coordinator was sent to sign-in; no bed data shown |
| AC-4 | FAIL    | Database stopped by the student as the procedure says: page showed "Internal Server Error", not "Sign-up is down, try again in a few minutes" |
| AC-5 | PASS    | Keyboard only: whole sign-up completed, focus visible at every step     |
| AC-6 | NOT RUN | Coordinator's office tablet not available today; case needs it. Rebooked Thursday |

First run: PASS 4  FAIL 1  NOT RUN 1
What the stakeholder said (their opinion): "The phone part is what I care about most."
Cases the stakeholder did not understand: AC-3, "What is a signed-out visitor?"
  Finding about the writing: rename to "someone who has not logged in."
```

**Three habits make this record strong.** Every "what was seen" is a message, a time, or a count,
never "it worked." The FAIL says exactly what appeared. The NOT RUN has a reason and a plan, and it is
never counted as a pass.

## Worked example 3 · the surprise failure, handled

```
(AC-4 shows "Internal Server Error")

STUDENT       That is a real failure. The agreed result is a message saying
              sign-up is down. I am writing down exactly what we saw. I will fix
              it and re-run this case with you, or send you the re-run in
              writing. Can we go on to AC-5?
COORDINATOR   Sure. How long will that take?
STUDENT       I expect to have it fixed by Friday. I will tell you tomorrow if
              that changes.
```

**What the student did not do:** open the code, say "one second," restart anything, or explain why it
happened. The correction goes in section 4 of the record, with the file, the commit, and the re-run.

---

## If the stakeholder cannot attend

Send the procedure and your results in writing, and ask for their written decision. Record it as
decided in writing. **Never run it alone and record that they were there.** The
[Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#6-acceptance-request)
has the message.

---

## The wrong version, and what it produces

```
(AC-4 shows "Internal Server Error")

STUDENT       Oh, that's weird, hang on.
              (opens the code, edits a line, redeploys by hand)
              Okay, try it now. See, it works.
              (later, in the text editor, AC-4 is changed from "shows the message"
               to "shows an error")

## 3. Results
| AC-4 | PASS | worked |
```

**What it produces:** a false record. The case was changed after it failed, so the rubric scores
acceptance at 0 for this part. A redeploy by hand, outside your documented deployment steps, is a
manual intervention, which resets the thirty-day clock and has to go in the events log. The stakeholder watched a fix happen live and now
wonders what else was patched at the last minute. "Worked" is not evidence. If the panel asks about
AC-4, the honest answer contradicts the record.

## Why the wrong version is tempting

The fix looks like one line, the stakeholder is right there, and a FAIL feels like losing. **A FAIL
recorded honestly costs far less than a PASS that was manufactured.** The rubric says so in writing,
and so will any stakeholder who later learns what happened.

---

## What to do in your project today

1. Confirm the run's time and place in writing, with your instructor copied.
2. Print the run sheet from test plan section 7 and note the agreed commit hash.
3. Practice reading the opening paragraph aloud once.
4. After the run, fill in sections 1 to 3 of the Acceptance Record the same day.
5. Log the run in your contact log.
6. If anything failed, read the next clinic,
   [When a Criterion Fails](MCCTC_145010_Clinic_W16_WhenACriterionFails.md), before you touch the
   code.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Acceptance criterion** | A signed Given/When/Then test from Week 8 |
| **Acceptance procedure** | Test plan section 7: the agreed steps for each criterion |
| **Acceptance run** | Running the procedure with the stakeholder, recording each verdict |
| **Verdict** | PASS, FAIL, or NOT RUN with a reason |
| **Stakeholder acceptance** | The stakeholder's written decision after the run |

---

## Check yourself

1. Halfway through, you realize AC-6 was written wrongly: it names a report page you cut, by
   agreement, in Week 13. What do you do?
2. Why is NOT RUN never counted as a pass?
3. The stakeholder watches AC-2 pass and says, "That's all I need, you can skip the rest." What do
   you say?

---

## Check your answers

**1.** Say so before running it. Record AC-6 as NOT RUN with the reason, and point to the Week 13
change request. If that change request already updated the criterion, the committed procedure should
match it. If it did not, you and the stakeholder agree any change out loud, and it is written into a
change request. It is never edited quietly.

**2.** Because nobody saw the expected result. NOT RUN means the evidence does not exist yet.
Counting it as a pass would claim something nobody checked.

**3.** Thank them, and ask to finish, because the agreement says every criterion is run and some
cases check failures and privacy that matter when something goes wrong. If they still decline, record
the remaining cases as NOT RUN with "stakeholder chose to stop," and record their decision in their
words.
