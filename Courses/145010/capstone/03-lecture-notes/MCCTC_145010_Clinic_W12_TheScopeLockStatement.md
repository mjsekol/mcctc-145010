# Clinic · The Scope Lock Statement
## 145010 Senior Capstone · Week 12, Thursday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 12, Thursday, or any week the room shows this signal: Sprint 2
reviews that show the plan will not finish.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.10.4 (procedures for initiating product and service improvements), 1.2.11
(professional correspondence), 1.2.7 (problem solving and consensus building to determine next
steps), 2.12.1 (a written acceptance procedure agreed by stakeholders and the team)

---

## Why this exists

**Tomorrow, scope locks.** From Week 13 on, scope can shrink and never grow. The scope lock
statement is the written list of what you will deliver, and it goes to your stakeholder with
tomorrow's update.

**This is the cheapest place in the whole capstone to make the project smaller.** A cut today is a
decision, with two sprints left to finish what remains. A cut in Week 15 is a failure you have to
explain in the middle of usability testing.

The statement fails in two directions. **It keeps everything**, and the plan quietly does not
finish. Or **it changes the agreement quietly**, and Week 16 becomes an argument about what "done"
means. This clinic is about writing one that does neither.

The template is the
[Change Request and Scope Lock Statement](../05-labs/MCCTC_145010_Template_ChangeRequest.md).

---

## The skill in plain language

A scope lock statement has four parts, and each has a rule.

| Part | The rule |
|---|---|
| **In scope, final** | Every item traces to an acceptance criterion in your signed agreement. If it traces to nothing, it is not in scope. |
| **Moved to stretch goals** | Only items from your Week 8 stretch list. Started only after every acceptance criterion passes. |
| **Moved to future improvements** | Every idea that will not be built, with who asked. Delivered as a list at handoff. |
| **Sent to the stakeholder** | Sent with Update 2. Their reply is recorded when it arrives, not before. |

**Three rules sit above the parts.**

1. **Nothing new goes in.** An idea that arrived after the agreement goes to future improvements,
   however good it is.
2. **A cut to a signed criterion needs a change request and the stakeholder's written agreement.**
   Until they agree, the criterion stays in the agreement. A criterion never changes quietly.
3. **Decide with arithmetic, not hope.** Hours left against hours needed.

---

## Worked example 1 · the Sprint 2 review that will not finish

**This is a composite, not a real organization.** A Full-Stack student is building a shift sign-up
app for the volunteer coordinator of a youth recreation league's concession stand. The signed
criteria:

| AC | Criterion, short form |
|---|---|
| AC-1 | Volunteers see open shifts on a phone |
| AC-2 | A volunteer claims a shift with a first name and last initial |
| AC-3 | Two claims on one shift: the second sees "already taken" |
| AC-4 | The coordinator creates next week's shifts |
| AC-5 | Every main task works by keyboard alone and with Windows Narrator |
| AC-6 | A printable weekly view |

The Sprint 2 review, Week 12 Friday draft:

```
Goal met? partly
Working on the deployed system: AC-1, AC-2, AC-3
AC-4 coordinator page: started, about 6 hours left
AC-5 keyboard and Narrator: 3 fixes found, about 3 hours
AC-6 printable view: not started, estimated 6 hours
New request, Week 11 meeting: a season volunteer-hours report
  for the league's board, asked through the coordinator
```

**Now the arithmetic.** Sprint 3 has about 12 hours, minus about 2 for Peer Code Review 1 on
Wednesday, so 10. Sprint 4 has no new features. Say 3 hours of it can go to finishing in-scope work,
because the rest belongs to review fixes and the full test plan.

```
Hours left:    10 (Sprint 3) + 3 (Sprint 4)          = 13
Hours needed:  6 (AC-4) + 3 (AC-5) + 6 (AC-6)        = 15
```

**15 is more than 13, before anything goes wrong.** Something has to move, and it should be decided
today.

---

## Worked example 2 · choosing the cut

Ask the question from the Define phase: **what did the stakeholder say matters most?** In the
needs-discovery record, the coordinator said the pain is Sunday evenings spent building next week's
schedule. That is AC-4. The printable view was their idea for posting at the stand, and they called
it "nice to have."

| Candidate | Cut it? | Why |
|---|---|---|
| AC-4 coordinator page | No | It is the reason the project exists |
| AC-5 keyboard and Narrator | No | It is about people who cannot use the app otherwise. Three hours |
| AC-6 printable view | **Propose cutting** | Six hours, the least important to the coordinator, and a phone screenshot covers most of the need for now |
| Volunteer-hours report | Not in scope | It arrived after the agreement. Future improvements |

After the proposed cut: 6 + 3 = 9 hours needed, against 13. Four hours of margin for the week that
goes wrong.

---

## Worked example 3 · the statement, and the change request with it

```markdown
# Scope Lock · Snack Stand Shifts
Locked: Week 12, Friday   Acceptance agreement version: 2

## In scope, final
- Open shifts visible on a phone (AC-1). Done.
- Claim a shift with first name and last initial (AC-2). Done.
- Second claim on a taken shift shows "already taken" (AC-3). Done.
- Coordinator creates next week's shifts (AC-4). Sprint 3.
- Keyboard-only and Narrator use of every main task (AC-5). Sprint 3.
- Printable weekly view (AC-6). Proposed for removal in CR-3.
  Stays in scope until the coordinator replies.

## Moved to stretch goals
*Started only if every acceptance criterion passes.*
- Export of the shift list for a spreadsheet (Week 8 stretch list).

## Moved to future improvements
*Delivered as a list at handoff. Not built.*
- FI-1 Season volunteer-hours report. Asked by the league's board
  through the coordinator, Week 11. Arrived after the agreement.
- FI-2 Printable weekly view, if CR-3 is agreed.

## Sent to the stakeholder
Week 12, Friday, with the weekly update. Their reply: not yet received.

From this point, scope may be reduced by agreement and is never expanded.
```

And CR-3, below it in the same file, from the template:

```markdown
## CR-3 · Remove the printable weekly view
**Raised:** Week 12, Thursday   **By:** me
**Type:** reduce scope
**What is asked for:** remove AC-6, the printable weekly view, and record
it as a future improvement.
**Why:** Sprint 2 review: 15 hours of work left against 13 hours available.
AC-6 is 6 of them and the coordinator called it "nice to have" (meeting
record, Week 7 Friday).
| Affected | Change |
|---|---|
| Acceptance criteria | AC-6 removed |
| Hours | 6 saved |
**Decision:** waiting for the coordinator's written reply
**Agreed by:**
**Acceptance agreement version after this change:** 3, if agreed
**Decision log entry:** D-17
```

The update that goes with it uses the words in the
[Stakeholder Communication Guide, section 4](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#4-scope-change-request).
The volunteer-hours report gets the second draft in that section: heard, recorded, not built now,
and why that protects the coordinator.

Notice what the statement does **not** do. It does not add the report because the board asked. It
does not drop AC-6 before the coordinator replies. It does not say "agreed" before anyone agreed.

---

## The wrong version, and what it costs

```markdown
# Scope Lock
## In scope, final
- Everything in the proposal
## Moved to stretch goals
- Anything else
## Moved to future improvements
- (none)
```

It changes nothing, so it decides nothing. It traces to no criterion. It does not mention the
volunteer-hours request, so that request is still floating, and the student will be tempted to build
it. **What it costs:** Sprint 3 ends with AC-4 half done because the printable view took the hours.
In Week 16 the coordinator runs the acceptance procedure and AC-4, the reason the project exists,
fails. That is the scope failure, arriving two weeks after the last cheap moment to prevent it.

---

## Why the wrong version is tempting

**Cutting feels like losing.** The printable view was in your proposal. Removing it feels like
admitting you could not do it. What you are actually doing is protecting the part your stakeholder
cares about most.

**"Everything" sounds confident.** It is the one answer the arithmetic has already ruled out.

**Saying no to a request feels rude.** Recording it as a future improvement is not no. It is "not in
this project," with a reason that protects them.

---

## Do this today

1. Open your Sprint 2 review draft. Add up the hours left against the hours needed.
2. Draft the scope lock statement at the top of `docs/improve/change-requests.md`.
3. Trace every in-scope item to an AC number.
4. For any cut to a signed criterion, write the change request below the statement.
5. Put every idea that will not be built on the future improvements list, with who asked.
6. Add a decision log entry for each choice.
7. Draft the paragraph for tomorrow's update that sends the statement.
8. **Commit.** Tomorrow the statement is final, sent, and committed as sent.

---

## If you are ahead, if you are behind

**If you are ahead:** your hours fit with margin. Write the statement anyway, with every item
traced. Put your Week 8 stretch goals under "stretch," and nothing new.

**If you are behind:** your arithmetic does not fit even after one cut. Cut to the minimum viable
version from your Week 8 proposal, and bring the statement to your instructor before the end of
Period 8 today.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Procedures for initiating product improvements** | The change request, and the future improvements list delivered at handoff (1.10.4) |
| **Consensus building to determine next steps** | Proposing the cut and waiting for the stakeholder's written agreement (1.2.7) |
| **Written procedure agreed by the stakeholders** | The acceptance agreement and procedure, changed only by agreement (2.12.1) |
| **Professional correspondence** | The update that sends the statement and asks for a decision (1.2.11) |

---

## Self-check

**1.** On Week 13, Tuesday, your stakeholder asks for one small extra field on a form. It would take
twenty minutes. What do you do?

**2.** Your change request removes AC-6. The stakeholder has not replied by Week 14. Is AC-6 still
in the acceptance procedure?

**3.** Your in-scope list has an item that traces to no acceptance criterion. What does that tell
you, and what are your two honest options?

### Answers

**1.** Scope is locked, so it is not built, however small. Thank them, add it to the future
improvements list with who asked, and say that the scope was locked so that what was agreed is
finished and tested properly. Record it in the change request file.

**2.** Yes. A criterion changes only with the stakeholder's written agreement. Keep following up
using the communication guide's quiet-stakeholder steps, and tell your instructor. Until they agree,
AC-6 is run in the acceptance procedure, and if it is not built, the record says so honestly.

**3.** It is scope nobody signed for. Either remove it from the in-scope list and put it on the
stretch or future improvements list, or, if it is needed to deliver a signed criterion, write down
which criterion it serves and fix the trace.
