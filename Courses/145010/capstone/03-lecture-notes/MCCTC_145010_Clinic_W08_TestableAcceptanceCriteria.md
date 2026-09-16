# Clinic · Acceptance Criteria That Can Fail
## 145010 Senior Capstone · Week 8, Wednesday · 15 minutes · Define

**Slides for this clinic:** [outline](../04-slides/MCCTC_145010_Slides_W08_TestableAcceptanceCriteria.md).
There is no exported deck yet. To generate one when Gamma credits are available, from the
repository root: `node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W08_TestableAcceptanceCriteria.md --export pptx`

**When this clinic runs.** Week 8, Wednesday, or any week the room shows this signal: criteria like
"works well", "is secure", "is user-friendly".

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.12.1 (a written procedure agreed by stakeholders and the project team for
determining acceptability), 2.9.3 (expected outcomes and objectives), 2.12.3 (test cases that are
realistic and include targeted platforms and device types), 1.2.12 (technical writing).

---

## Why this exists

**In Week 16 you and your stakeholder sit down and run these criteria, one by one.** Each one is
recorded as passed, not passed, or not run with a reason. Then the stakeholder decides, in writing,
whether to accept the project. Ten points of your capstone grade come from that record.

A criterion that cannot fail cannot be checked. "The board works well" is true to you and maybe
false to the coordinator, and there is nothing either of you can do in the room to settle it. That is
an argument, scheduled for Week 16, and you signed up for it in Week 8.

**Today the agreement goes to your stakeholder with the final proposal.** It is the last day to
make every criterion one a stranger could run.

---

## The skill in plain language

**The shape.** Given a starting situation, when someone does something, then an exact result anyone
can check.

**Two tests for every criterion.** Answer both before you keep it.

1. **Could a stranger run it** from the words alone, without asking you anything?
2. **Could it come out "not passed"?** If no possible result fails it, it is not a criterion.

**Four habits that make criteria pass those tests.**

- **Numbers instead of adjectives.** Not "fast", but "within 3 seconds."
- **One idea per criterion.** If two results could pass or fail for unrelated reasons, split them.
  A half pass is an argument.
- **The stakeholder's words, not yours.** "The low list," not "the admin view."
- **What happens, not how you built it.** No table names, no routes, no framework words.

**The four you must have.** Include at least one criterion for each:

| Kind | What it checks |
|---|---|
| **Main task** | The thing the stakeholder named, working |
| **A failure** | What happens when something is unavailable or wrong |
| **Privacy or security** | What is not collected, or who cannot see what |
| **Devices** | The exact devices and ways of using them the criteria are checked on |

Six to ten criteria is usual. The full guidance is in the
[Acceptance Agreement template](../05-labs/MCCTC_145010_Template_AcceptanceAgreement.md#how-to-write-acceptance-criteria-that-work).

---

## Worked example 1 · Weak criteria, rewritten

*Composite, not a real organization or person.* The Parts Bin Board for a volunteer-run bike repair
co-op, after the Week 8 scope cut.

| Weak | Which test it fails | Strong |
|---|---|---|
| The board works well. | Cannot fail | Given the shop link open on the desktop by the door, when a volunteer selects bin B-04 and chooses Mark low, then the page says "B-04 marked low." |
| The board is secure. | A stranger cannot run it | Given a visitor who is not signed in, when they open the low list address, then they see the sign-in page and no bin information. |
| The board is user-friendly. | Cannot fail, and it is an opinion | Given a volunteer who has never used the board, when they are asked to mark a bin low with no help, then they finish within 2 minutes. |
| The list loads fast. | "Fast" is not a number | Given the desktop by the door, when the coordinator opens the low list, then the whole list is shown within 3 seconds, timed with a phone stopwatch. |
| It is accessible. | Too broad to run | Given the desktop by the door, when a volunteer marks a bin low using only the keyboard, then every step can be reached and completed without a mouse. |

---

## Worked example 2 · A full set of eight

*Composite.* This set covers all four kinds.

| ID | Kind | Given | When | Then |
|---|---|---|---|---|
| AC-1 | Main task | The shop link is open on the desktop by the door | A volunteer selects bin B-04 and chooses Mark low | The page says "B-04 marked low," and B-04 is on the coordinator's low list when the coordinator reloads it |
| AC-2 | Main task | Three bins are on the low list | The coordinator marks B-04 restocked | B-04 is no longer on the list, and the other two still are |
| AC-3 | Failure | The board is in its test mode with the database switched off | A volunteer chooses Mark low | The page says the report was not saved and to tell the coordinator. It never says the report was saved |
| AC-4 | Privacy | The mark-low form is open | A volunteer reads every field on it | No field asks for a name, phone number, or email address |
| AC-5 | Failure | The mark-low form is open | A volunteer types a note of 121 characters and submits | The note is refused with a message that says the limit is 120 characters |
| AC-6 | Security | A visitor is not signed in | They open the low list address | They see the sign-in page and no bin information |
| AC-7 | Devices | The desktop by the door (Windows, Edge, window 1280 pixels wide) and a phone 360 pixels wide | A volunteer marks a bin low on each | They complete the report on each without scrolling sideways |
| AC-8 | Devices | The desktop by the door with Windows Narrator on and no mouse | A volunteer marks a bin low using only the keyboard | They complete the report, and Narrator reads the name of every field they reach |

**Look at AC-3.** A failure criterion is the one students skip, and it is the one that shows whether
the system is honest. The test mode is something you build so the stakeholder can see the failure
safely, without anyone unplugging anything.

**Look at AC-1.** It joins two results with "and." They are the two ends of one action: the
volunteer's screen and the coordinator's list. If one passes and the other fails, a report was lost
somewhere, which is exactly the problem you want the run to catch. Some stakeholders would rather
see the two ends as separate criteria. Either choice is defensible, as long as each result could
fail on its own.

**Look at AC-7 and AC-8.** They name the exact devices and the exact way of using them. "Works on
phones" names none.

**This is a first draft, and drafts change.** When the co-op's coordinator read these eight in the
proposal meeting, they asked for the board-open counter to be checked and for fewer, larger
criteria. The signed agreement you will meet in later Gate 2 exercises has six: the no-name and
120-character checks folded into marking a bin low, the sign-in check folded into marking a bin
restocked, and the database-off failure kept as a requirement and a test case rather than a signed
criterion. Every change was agreed in writing before the signature. That is the process working.

---

## Worked example 3 · The criterion two people read differently

*Composite.* A draft said:

```
AC-2  Given a bin is marked low, when the coordinator is not in the shop,
      then the coordinator is notified.
```

The student meant "the bin appears on the low list." The coordinator read it aloud and said, "Good,
so I get a text." Same words, two meanings. In Week 16 one of them would have been disappointed.

This is why you ask your stakeholder to read each criterion aloud and say what it means. The rewrite
removes the word "notified":

```
AC-2  Given a bin is marked low, when the coordinator next opens the low
      list, then that bin is on it.
```

The proposal's out-of-scope list now says, in plain words, that the board sends no texts or emails.
The criterion stays one idea, and the expectation is written down where the coordinator will read it.

---

## The wrong version, and what it costs

*Composite.* An acceptance run in Week 16, recorded honestly:

```
AC-1  The board works well.            NOT RUN  no way to check it
AC-4  The board is user-friendly.      NOT RUN  stakeholder: "some volunteers
                                                 found it confusing"
                                                 student: "it is user-friendly"
Stakeholder decision: not accepted until AC-1 and AC-4 are rewritten
```

Rewriting a criterion after Week 8 needs a written change both of you agree to, before the run.
Changing it in the room is exactly what the agreement forbids. So the project reaches its acceptance
week with two criteria nobody can run, and the rubric's acceptance score is built from that record.

---

## Why the wrong version is tempting

"Works well" is what you mean, and it is quick to write. Specific criteria feel risky, because they
can fail, and you would rather not sign something you might not pass.

That instinct is backwards. A criterion that can fail is also the only kind that can pass in a way
nobody can dispute. "Works well" never passes. It only gets argued about.

---

## Do this today

1. Write six to ten criteria in `docs/define/acceptance-agreement.md`, from the
   [Acceptance Agreement template](../05-labs/MCCTC_145010_Template_AcceptanceAgreement.md).
2. Run both tests on every criterion. Rewrite any that fail.
3. Check you have the four kinds: main task, a failure, privacy or security, devices.
4. Check every criterion traces to something in section 7 of your proposal.
5. Your instructor reads the ownership and support sections.
6. Send the final proposal and the unsigned agreement to your stakeholder, from your school account
   with your instructor copied, and ask for a time to present. Log it in the contact log.
7. Commit. The signed copy, when it comes, goes to your instructor and never into the repository.

---

## If you are ahead, if you are behind

**Ahead.** For each criterion, write one line on how you would show it in the room. That line is the
seed of the Week 10 acceptance procedure.

**Behind.** Send the proposal and agreement today even if you are unsure about one criterion. Mark
it in your notes and raise it in tomorrow's presentation. A signature can come back even if the end
of the week is lost. A draft that never left cannot be signed.

---

## Words the WebXam uses

| Exam word | What it means in this skill |
|---|---|
| **Acceptance criteria** | The checks the stakeholder uses to decide whether the project is done |
| **Written acceptance procedure** | The agreed, written way acceptability is decided. Your criteria are its core |
| **Test case** | One check with a starting situation, an action, and an expected result |
| **Expected performance** | The exact result that counts as passing, such as "within 3 seconds" |
| **Targeted platforms and device types** | The exact devices and browsers the criteria are checked on |
| **Objectives** | Specific, measurable results. A criterion turns one into a check |

---

## Self-check

**1.** Rewrite this criterion so it can fail: "The coordinator page is clear."

**2.** A student's six criteria are all about marking and clearing bins. Which of the four kinds are
missing?

**3.** Why does changing a criterion during the Week 16 run break the agreement, even if the
stakeholder nods?

### Answers

**1.** One good version: "Given the low list with ten bins on it, on the desktop by the door, when the
coordinator stands at the door, then every bin code can be read aloud correctly by the coordinator."
Any version works if a stranger could run it and it could come out not passed.

**2.** A failure, privacy or security, and devices. All six are main-task criteria.

**3.** The agreement says a criterion is never changed during the run, and any change is agreed in
writing by both parties first. A change in the room has no written record, so the acceptance record
cannot show what was actually agreed.
