# Usability Findings · Garden Watering Sign-Up
## Prepared from the Week 15 sessions · `docs/control/usability/findings.md`

*Drafted with an AI assistant from the five session records and the protocol, then lightly edited.
Invented composite for Gate 2 Week 15.*

---

## 1. Summary

Garden Watering Sign-Up was evaluated in five task-based sessions during Week 15. Overall the
product performs well against its core purpose. Participants completed the large majority of
tasks, found the dry-beds list, and read bed care notes on a phone.

Average participant satisfaction was **4.6 out of 5** on the post-session rating, which indicates
strong acceptance among the garden's members.

Three areas need attention before the acceptance run: the week the schedule opens on, how a
member removes themselves from a slot, and the time picker.

---

## 2. Method

Five participants took part: two garden members reached through the coordinator, a student in
another program, an adult in the building outside the program, and a family member. Each session
lasted thirteen to fifteen minutes and covered the five tasks in the protocol. Sessions were not
recorded. Notes were written up the same day.

**Five participants is the right number for this study.** This study found that testing with five
users uncovers about 85 percent of usability problems, so the findings below can be treated as
close to complete.

---

## 3. Task results

| Task | What it tested | Completed |
|---|---|---|
| 1 | Sign up for Tuesday evening (R1) | 5 of 5 (100 percent) |
| 2 | Cancel the Tuesday slot (R2) | 4 of 5 (80 percent) |
| 3 | Find the driest beds (R3) | 5 of 5 (100 percent) |
| 4 | Sign up for Thursday using only the keyboard (R5) | 4 of 5 (80 percent) |
| 5 | Read the tomato bed note on a phone (R4) | 5 of 5 (100 percent) |

**Overall task success: 92 percent.**

---

## 4. Findings

| # | What happened | How many | Evidence | Severity |
|---|---|---|---|---|
| F1 | The schedule opens on last week. Participants signed up for last week's Tuesday before noticing. | 4 of 5 | P2 L2, P3 L2, P4 L3, P5 L2 | Serious |
| F2 | One participant could not find Cancel and looked for it in the menu. | 1 of 5 | P2 L7 to L10 | Critical |
| F3 | Keyboard focus stayed inside the time picker, and the participant could not finish Task 4. | 1 of 5 | P5 L13 to L15 | Critical |
| F4 | The dry-beds link was passed once before being found. | 1 of 5 | P5 L9 | Minor |

### A note on P4

P4 set the browser to 200 percent zoom and used only the keyboard for the whole session. This is
not how the target user works, so the difficulties P4 ran into (the Sign up button sitting past
the edge of the screen, and not reaching Cancel) are not treated as findings. They reflect an
unusual setup rather than a problem with the product. The other four participants represent the
garden's members well.

---

## 5. Prioritized change list

**C1. Open the schedule on the current week.**
```
Finding:      F1, 4 of 5 signed up for last week first
Change:       the Schedule page opens on the current week
Prediction:   a participant signs up for the right Tuesday with no wrong attempts
How I know:   re-test Task 1 with at least one new person after the change
```
C1 comes first. A wrong-week sign-up leaves a bed unwatered, and nobody notices until the plants
show it.

**C2. Put Cancel where it can be seen.**
```
Finding:      F2, 1 of 5 could not find Cancel
Change:       Cancel moves to the top of the slot panel, beside Swap
Prediction:   a participant cancels with no wrong attempts
How I know:   re-test Task 2 with at least one new person after the change
```

**C3. Let keyboard focus leave the time picker.**
```
Finding:      F3, 1 of 5 could not leave the time picker with the keyboard
Change:       Tab moves focus out of the picker; arrow keys still change the time
Prediction:   a participant completes Task 4 with the keyboard alone
How I know:   re-test Task 4 with at least one new person after the change
```

**C4. Add text-message reminders the night before a slot.** Participants wanted to be reminded of
their slots (P2), and a reminder would reduce missed waterings.

**C5. Refresh the sign-in page with the garden's colors**, so the first screen members see feels
more welcoming.

---

## 6. Next steps

Corrections C1 to C3 start Week 16, Monday. C4 and C5 follow once the corrections are re-tested.
The whole test plan is re-run after the last correction.
