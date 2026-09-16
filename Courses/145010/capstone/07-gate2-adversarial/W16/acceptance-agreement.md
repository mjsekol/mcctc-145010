# Acceptance Agreement · Kennel Care Log
## 145010 Senior Capstone · Gate 2 source file · Week 16 · invented composite

**Everything in this folder is invented for a Gate 2 exercise.** Oak Hollow Animal Rescue, its
volunteer coordinator, its shelter manager, the animals, the project, and the student do not exist.

This is the committed, unsigned copy, `docs/define/acceptance-agreement.md`, written from the
[Acceptance Agreement](../../05-labs/MCCTC_145010_Template_AcceptanceAgreement.md) template. The
signed copy is with the instructor.

---

```markdown
# Acceptance Agreement · Kennel Care Log
Version 1.0   Written: Week 8, Tuesday
Supports: Concept Proposal version 2

## Version history
| Version | What changed | Agreed in writing by both |
|---|---|---|
| 1.0 | First signed version | Week 8, Friday |

Change requests since version 1.0: none.

## Who this agreement is between
- **Stakeholder:** the volunteer coordinator, Oak Hollow Animal Rescue
- **Backup contact:** the shelter manager, Oak Hollow Animal Rescue. Acts for the stakeholder if
  they are unavailable.
- **Student developer:** Marcus, senior, AI Automation & Software Development
- **Supervising instructor:** the program instructor

## What will be delivered
A web app where volunteers record each dog's walks and feedings on a phone or the front-desk
tablet, and the coordinator sees at a glance which animals have not been walked yet today. It
replaces the clipboard at the front desk. The paper sheet stays as the backup.

## Acceptance criteria
The project is accepted when these pass in the acceptance run.

| ID | Given | When | Then |
|---|---|---|---|
| AC-1 | the kennel board with the test animals | a volunteer records a walk for one animal | the board shows that animal as walked, with the time, within 5 seconds |
| AC-2 | three test animals not walked by 11:00 on the test clock | the coordinator opens the board | those three animals are listed first, under **Not walked yet** |
| AC-3 | a browser that is not signed in | someone opens the coordinator page address | they are sent to the sign-in page and no animal records are shown |
| AC-4 | the database is unavailable | a volunteer records a walk | the page shows **Not saved. Write it on the paper sheet.** and the walk is not shown as recorded anywhere |
| AC-5 | the front-desk tablet held upright, and a phone 360 pixels wide | a volunteer records a walk | every control is visible and usable with no sideways scrolling, on both devices |
| AC-6 | a week of test records | the coordinator presses **Export week** | a CSV file opens with one row per walk, and volunteers appear by first name and last initial only |

**Devices and platforms these are checked on:** the front-desk tablet (held upright, its own
browser), a phone 360 pixels wide, and the coordinator's laptop.

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
- After Week 12, the scope may be reduced and may not be expanded. New requests are recorded as
  future improvements and delivered as a list at handoff.
- Every change raises the version number of this agreement.

## What the stakeholder agrees to
- Answer questions within two school days where possible.
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
The student will fix problems reported through the school until the end of Week 18. After that, no
support is promised unless agreed in writing through the school.

## Ownership
The student holds the copyright in the code. Oak Hollow Animal Rescue may use, copy, and change it
for its own work, at no cost, for as long as it wants. No money changes hands under this agreement.

## Supervision
This is a school project supervised by the instructor. District policy applies to all contact
between the student and the stakeholder.

## Signatures
*Signed copy kept by the instructor. Do not commit signatures.*
```
