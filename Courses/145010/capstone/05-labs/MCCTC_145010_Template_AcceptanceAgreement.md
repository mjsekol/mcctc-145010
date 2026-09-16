# Template · Acceptance Agreement
## 145010 Senior Capstone · Week 8

**Commit as:** `docs/define/acceptance-agreement.md`, **unsigned**.
**The signed copy goes to your instructor.** It never goes in your repository.
**Due:** sent with the final proposal Week 8, Wednesday. Signed by Week 8, Friday.

**Competencies this evidences:** 2.12.1 (a written procedure agreed by stakeholders and the
project team for determining acceptability), 2.9.6 (present a proposal to stakeholders), 1.2.11
(professional documents), 1.2.13 (stakeholders), 1.10.3 (communicate warranties), 1.7.13
(protect intellectual property).

---

## Why this exists

**"Done" means different things to different people**, and you find out how different on the
worst possible day. This page writes down, before any building starts, exactly what your
stakeholder will check and what counts as passing.

It protects both of you. The stakeholder knows what they will get. You know that a new wish in
Week 15 is a future improvement, not a failure.

**No signature, no build.** The capstone does not enter Measure & Analyze until this is signed.

---

## How to write acceptance criteria that work

An acceptance criterion is a test that someone who has never met you could run, and that could
come out either way.

**Shape:** Given <a starting situation>, when <someone does something>, then <an exact result
anyone can check>.

| Weak | Why it fails | Strong |
|---|---|---|
| The app works well. | Nobody can disagree, so it cannot fail. | Given a week with 12 open shifts, when a volunteer claims one, then that shift shows as taken on the coordinator's page within 5 seconds. |
| The panel is readable. | "Readable" is an opinion. | Given the panel on the shop-floor monitor, when the reading is above the alarm threshold, then the alarm banner is visible from 3 meters away, checked by the stakeholder. |
| The AI gives good answers. | "Good" is not checkable. | Given the 25 questions in the evaluation set, when each is asked, then at least 20 answers cite the correct manual and page, and every other answer says it could not find the information. |
| It is secure. | Too broad to run. | Given a visitor who is not signed in, when they open the shift editor address, then they are sent to the sign-in page and no shift data is shown. |

**The examples above come from composite projects.** Write your own.

**Include at least one criterion for each of these:** the main task, a failure (what happens when
something is unavailable or wrong), privacy or security, and the devices it must work on.

**Six to ten criteria is usual.** Fewer than six rarely covers a real project. More than ten is
usually scope creeping in.

---

```markdown
# Acceptance Agreement · <project name>
Version <1.0>   Written: Week 8, <day>
Supports: Concept Proposal version <n>

## Who this agreement is between
- **Stakeholder:** <role>, <organization>
- **Backup contact:** <role>, <organization>. Acts for the stakeholder if they are unavailable.
- **Student developer:** <first name and last initial>, senior, AI Automation & Software
  Development
- **Supervising instructor:** <instructor name>

## What will be delivered
<Two or three sentences, matching the proposal's scope and deliverables.>

## Acceptance criteria
The project is accepted when these pass in the acceptance run.

| ID | Given | When | Then |
|---|---|---|---|
| AC-1 | | | |
| AC-2 | | | |
| AC-3 | | | |
| AC-4 | | | |
| AC-5 | | | |
| AC-6 | | | |

**Devices and platforms these are checked on:** <list>

## How acceptance is decided
1. In Week 10, the student writes the detailed acceptance procedure from these criteria and sends
   it to the stakeholder. The stakeholder confirms it by Week 11, Friday.
2. In Week 16, the student and the stakeholder run the procedure together, in person at school with
   the instructor present or on an instructor-approved call.
3. Each criterion is recorded as **passed**, **not passed**, or **not run with a reason**.
4. The stakeholder decides, in writing: **accepted**, **accepted with agreed follow-up**, or **not
   accepted**, with the reason.
5. A criterion is never changed during the run. If a criterion turns out to be wrong, both parties
   agree any change in writing first.

## Changes to this agreement
- Changes are proposed in writing by either party and take effect only when both agree in writing.
- **After Week 12, the scope may be reduced and may not be expanded.** New requests are recorded
  as future improvements and delivered as a list at handoff.
- Every change raises the version number of this agreement.

## What the stakeholder agrees to
- Answer questions within <two> school days where possible.
- Review the requirements in Week 10 and the acceptance procedure by Week 11.
- Take part in the acceptance run in Week 16 and the handoff in Week 17, or name someone who will.
- Communicate with the student only through school email with the instructor copied, or in
  meetings the instructor has approved.

## What the student agrees to
- Send a written update every Friday.
- Report problems in the week they happen.
- Keep all contact within school channels.
- Hold no personal data beyond what the requirements name, and put no personal data into any AI tool.
- Deliver the user guide, training, rollout plan, and handoff package in Week 17.

## Support after handoff
<Plain words. For example: "The student will fix problems reported through the school until the
end of Week 18. After that, no support is promised unless agreed in writing through the school."
Do not promise support you cannot give.>

## Ownership
<Copied from the proposal's intellectual property section, as reviewed by the instructor.>

## Ending the project early
Either party may end the project by telling the other in writing, with the instructor copied. The
instructor decides how the student's capstone continues.

## Supervision
This is a school project supervised by the instructor. District policy applies to all contact
between the student and the stakeholder.

*Your instructor may replace any wording on this page with language the district prefers.*

## Signatures
*Signed copy kept by the instructor. Do not commit signatures.*

Stakeholder:        ______________________________   Week ___, ________
Student:            ______________________________   Week ___, ________
Instructor:         ______________________________   Week ___, ________
Parent or guardian, acknowledging they know who the stakeholder is:
                    ______________________________   Week ___, ________
```

---

## Before you send it · self-check

- [ ] Every criterion has a Given, a When, and a Then that could fail.
- [ ] At least one criterion covers a failure, one covers privacy or security, and one names the
      devices.
- [ ] Every criterion traces to something in the proposal's scope.
- [ ] Your instructor has read the ownership and support sections.
- [ ] No signatures, phone numbers, or personal addresses in the committed file.

## After it is signed

Add one line to `docs/communication/contact-log.md`:

```
Week 8, <day>   signed acceptance agreement version <n> received, on file with instructor
```
