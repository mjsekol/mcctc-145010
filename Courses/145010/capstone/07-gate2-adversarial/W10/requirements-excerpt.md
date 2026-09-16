# Requirements Specification · Parts Bin Board (excerpt)
Version 2.0   Written: Week 9, Wednesday   Revised: Week 10, Monday, after the coordinator's review
Supports: Concept Proposal version 2, Acceptance Agreement version 1

**Invented for a Gate 2 exercise.** The Parts Bin Board, the bike repair co-op, and its shop
coordinator are a composite, not a real organization or person. Every line here is invented.

**About the co-op.** A volunteer-run community bike repair shop. Volunteers fix donated bikes on
open-shop nights. They range from teenagers to retirees. Some have no smartphone and use the
co-op's one donated desktop computer by the door. The co-op has no other computers and no budget.
The stakeholder is the shop coordinator.

---

## 1. Functional requirements

### R1 · Mark a bin low
The system must let anyone with the shop link mark a parts bin low by choosing its bin code and,
if they want, adding a note of up to 120 characters. It must never ask for a name.
Traces to: need N1, proposal scope item "mark a bin low".

- AC-1.1 Given the board is open at the shop link, when a volunteer chooses bin B-04 and presses
  Mark low with no note, then B-04 appears on the coordinator's low list with the time it was marked.
- AC-1.2 Given the board is open, when a volunteer adds a note of exactly 120 characters, then the
  note is saved and shown in full on the low list.

### R2 · See and print the low list
The system must show the signed-in coordinator every bin currently marked low, newest first, and
must let the coordinator print the list to carry along the shelves.
Traces to: need N2, proposal scope item "coordinator low list".

- AC-2.1 Given a volunteer has marked a bin low, when the coordinator opens or reloads the low list
  within 60 seconds, then that bin is on it.
- AC-2.2 Given at least one bin is low, when the coordinator uses the browser's print command on
  the low list, then the list prints on one page with every bin code and note readable.

### R3 · Mark restocked
The system must let the signed-in coordinator mark a low bin restocked, which removes it from the
low list.
Traces to: need N2, proposal scope item "mark restocked".

- AC-3.1 Given B-04 is on the low list, when the coordinator presses Restocked beside it, then B-04
  is no longer on the list after the page reloads.

### R4 · Count board opens
The system must count how many times the board was opened each day and show the counts to the
coordinator. It must count without cookies and without storing any address.
Traces to: need N3, proposal scope item "page-view counter", and the Week 17 baseline comparison.

- AC-4.1 Given the board was opened 5 times today, when the coordinator opens the counts page, then
  today's row shows 5.

## 2. What happens when things go wrong

| ID | Situation | What the user sees | Criterion |
|---|---|---|---|
| E1 | The database cannot be reached | The board shows "The board cannot save right now. Please tell the coordinator in person." Nothing is reported as saved. `/health` answers 503. | AC-E1 |
| E2 | No bin chosen, or a note longer than 120 characters | A message next to the field that has the problem. Nothing is saved. | AC-E2 |
| E3 | Someone not signed in opens the low list or sends a restock | They are sent to the sign-in page. Nothing changes. | AC-E3 |

## 3. Non-functional requirements

| ID | Kind | Requirement | How it is measured |
|---|---|---|---|
| NF1 | Performance | The board page loads in under 3 seconds on the co-op desktop over the shop Wi-Fi | Browser developer tools, Network panel, cache disabled, three loads, the slowest reported |
| NF2 | Availability | Runs 30 consecutive days without manual intervention | Thirty-day survival record |
| NF3 | Accessibility | Zero automated accessibility violations at WCAG 2 A and AA on every page; every task possible by keyboard alone; headings, labels, and messages that make sense in Windows Narrator | Automated check with web-check, a keyboard-only walkthrough, a Narrator walkthrough |
| NF4 | Devices and browsers | The co-op desktop by the door: Windows, Microsoft Edge, 1280 pixels wide. Volunteers' own phones, 360 pixels wide, in the phone's own browser. Keyboard only. Windows Narrator | Test plan platform cases |
| NF5 | Validity | Zero HTML validation errors on every page | web-check validation |
| NF6 | Security | Only the signed-in coordinator can see the low list, mark restocked, or see the counts. The coordinator password is never in the repository | Test cases and review |
| NF7 | Privacy | Stores only bin code, note, time marked, time restocked, and daily open counts. No names, no addresses, no cookies | Data dictionary review, log search |

## 4. Acceptance criteria in the signed agreement, version 1

| AC | Short name | Requirements |
|---|---|---|
| AC-1 | Mark a bin low, no name asked | R1, E2 |
| AC-2 | See and print the low list | R2 |
| AC-3 | Mark restocked | R3, E3 |
| AC-4 | Count board opens | R4 |
| AC-5 | Works on the co-op desktop and on a phone | NF4, NF1 |
| AC-6 | Usable by keyboard alone and with Narrator, zero automated violations | NF3 |

## 8. Review and sign-off
- **Sent to stakeholder:** Week 9, Thursday
- **Their questions and changes:** AC-2.1 said "promptly". The coordinator asked for a number and
  chose 60 seconds. Meeting record `meetings/week-10-mon-requirements-review.md`.
- **Version after review:** 2.0
- **Stakeholder response:** agreed with changes, Week 10, Monday, by school email
