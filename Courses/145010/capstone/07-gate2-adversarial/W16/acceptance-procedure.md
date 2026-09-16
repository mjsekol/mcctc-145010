# Test Plan, section 7 · Acceptance procedure · Kennel Care Log
## 145010 Senior Capstone · Gate 2 source file · Week 16 · invented composite

**Invented for a Gate 2 exercise.** An excerpt from the student's committed test plan,
`docs/measure/test-plan.md`, section 7, written from the
[Test Plan](../../05-labs/MCCTC_145010_Template_TestPlan.md) template.

---

```markdown
## 7. Acceptance procedure

- **Agreement version:** 1.0
- **Sent to stakeholder:** Week 10, Thursday   **Agreed:** Week 11, Friday, in writing
- **Committed at:** 4e7a2c1
- **What they changed when they read it:** nothing
- **Where it will be run:** the deployed system, on the front-desk tablet held upright, a phone
  360 pixels wide, and the coordinator's laptop
- **Stakeholder role running it:** the volunteer coordinator

**Read this to the stakeholder before starting:**
> Some of these cases test what happens when something goes wrong, so a message on screen may be
> the right result. If something fails that we did not expect, I will write it down and fix it
> afterward rather than fix it in front of you. If any step does not make sense, tell me, because
> that is something I need to fix in the writing.

| AC | Starting state | What to do | What you should see | Result | Evidence |
|---|---|---|---|---|---|
| AC-1 | Signed in as the test volunteer on the phone. Test animal **Biscuit** not walked today | Open Biscuit, press **Record walk** | Within 5 seconds the board on the laptop shows Biscuit as **Walked** with the time | | |
| AC-2 | Test clock set to 11:00. Test animals **Pepper**, **Juniper**, and **Moose** not walked | On the laptop, open **Board** | Pepper, Juniper, and Moose are the first three rows, under **Not walked yet** | | |
| AC-3 | A private browser window on the laptop, not signed in | Type the coordinator page address | The **Sign in** page. No animal names anywhere on screen | | |
| AC-4 | The student turns on the agreed test switch **Database offline** in the test settings, and says so before the case | On the tablet, open Biscuit, press **Record walk**. Then the student turns the switch off | The page says **Not saved. Write it on the paper sheet.** After the switch is off, Biscuit's walk is not on the board | | |
| AC-5 | Tablet held upright. Phone 360 pixels wide | On each device, open Juniper and record a walk | Every control is visible and works. No sideways scrolling on either device | | |
| AC-6 | A week of test records loaded | On the laptop, press **Export week** | A CSV file with one row per walk. Volunteers appear as first name and last initial only | | |

**Verdicts:** PASS (you saw the expected result), FAIL (you did not), NOT RUN (it could not be run,
with the reason). NOT RUN is never a pass.

**The rule:** a case is never changed because it is about to fail. A case that turns out to be
wrong is recorded as NOT RUN, and any change is agreed in writing by both of us.
```
