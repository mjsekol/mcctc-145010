# The AI's draft · Requirements Specification
## Gate 2 · Week 9 · folder file 3 of 3

**Everything in this folder is invented and composite.** The co-op, the coordinator, and the
student are not real.

**What this file is.** The draft the lab's assistant returned when the senior gave it Parts A and B
of `proposal-excerpt.md` and the whole of `baseline-record.md` and asked for version 1 of the
requirements specification. It is unedited. Every item has an ID (G1, R2, AC-2.1, E1, NF3, D2) so
you can cite it.

---

# Requirements Specification · Parts Bin Board
Version 1.0   Written: Week 9, Wednesday   Supports: Concept Proposal version 2, Acceptance
Agreement version 1

## 0. Background

**G1.** The co-op's volunteers repair donated bikes on open-shop nights. When a parts bin is empty,
the repair stalls until the bin is restocked.

**G2.** The Week 9 baseline found that the co-op averages 4.5 stalled repairs per night because of
empty bins. The Parts Bin Board exists to bring that number down by telling the coordinator about
empty bins before Sunday.

## 1. Functional requirements

### R1 · Mark a bin low
The system must let anyone with the shop link mark a parts bin low by choosing its bin code and, if
they want, adding a note of up to 120 characters. It must never ask for a name.
Traces to: need N1, proposal scope item S1.

- **AC-1.1** Given the board is open at the shop link, when a volunteer chooses bin B-01 and presses
  Mark low with no note, then B-01 appears on the coordinator's low list with the time it was
  marked.
- **AC-1.2** Given the board is open, when a volunteer adds a note of exactly 120 characters, then
  the note is saved and shown in full on the low list.

### R2 · See and print the low list
The system must show the signed-in coordinator every bin currently marked low, newest first, and
must let the coordinator print the list to carry along the shelves.
Traces to: need N2, proposal scope item S2.

- **AC-2.1** Given a bin marked low, when the coordinator opens the low list, then the
  coordinator's list shows it promptly.
- **AC-2.2** Given at least one bin is low, when the coordinator uses the browser's print command on
  the low list, then the list prints on one page with every bin code and note readable.

### R3 · Mark restocked
The system must let the signed-in coordinator mark a low bin restocked, which removes it from the
low list.
Traces to: need N2, proposal scope item S2.

- **AC-3.1** Given B-01 is on the low list, when the coordinator presses Restocked beside it, then
  B-01 is no longer on the list after the page reloads.

### R4 · Count board opens
The system must count how many times the board was opened each day and show the counts to the
coordinator. It must count without cookies and without storing any address.
Traces to: need N3, proposal scope item S3.

- **AC-4.1** Given the board was opened 5 times today, when the coordinator opens the counts page,
  then today's row shows 5.

### R5 · Ease of use
The system must be user-friendly.
Traces to: need N4.

- **AC-5.1** Given any user, when they use the system, then they find it user-friendly.

### R6 · Search engine visibility
The system must rank on the first page of search engine results for "bike repair parts" in the
region. Every page must have a unique title, a meta description, keywords, and an entry in a
sitemap submitted to the major search engines.
Traces to: need N4, proposal scope item S1.

- **AC-6.1** Given a search for "bike repair parts" in the region, when the results load, then the
  Parts Bin Board appears on the first page.

### R7 · Health endpoint
The system must provide a health address that reports whether the database can be read.
Traces to: proposal scope item S4.

- **AC-7.1** Given the database file is missing, when the health address is requested, then it
  reports a failure, not "ok".

## 2. What happens when things go wrong

| ID | Situation | What the user sees | Criterion |
|---|---|---|---|
| E1 | The database cannot be read | "The board cannot save right now. Please tell the coordinator in person." Nothing is reported as saved | AC-E1: Given the database is unavailable, when a volunteer presses Mark low, then that message is shown and the page does not claim the bin was marked |
| E2 | No bin chosen, or a note over 120 characters | A message next to the field that has the problem. Nothing is saved | AC-E2: Given a 121-character note, when submitted, then the page names the note field and the low list does not change |
| E3 | Someone not signed in opens the low list or sends a restock | They are sent to the sign-in page and nothing changes | AC-E3: Given no sign-in, when a restock request is sent for B-01, then B-01 stays on the low list |

## 3. Non-functional requirements

| ID | Kind | Requirement | How it is measured |
|---|---|---|---|
| NF1 | Performance | The board page loads in under 3 seconds on the co-op desktop over the shop Wi-Fi | Browser developer tools, Network panel, cache disabled, three loads, the slowest reported |
| NF2 | Availability | Runs 30 consecutive days without manual intervention | Thirty-day survival record |
| NF3 | Accessibility | Not required, because the co-op's volunteers have no disabilities. Automated accessibility checks and keyboard and screen reader walkthroughs are skipped to save build time | None |
| NF4 | Devices and browsers | The co-op desktop by the door: Windows, Microsoft Edge, 1280 pixels wide. Volunteers' own phones, 360 pixels wide, in the phone's own browser | Test plan platform cases |
| NF5 | Validity | Zero HTML validation errors on every page | Validator run |
| NF6 | Security | Only the signed-in coordinator can see the low list, mark restocked, or see the counts. The coordinator password is never in the repository | Test cases E3 and review |
| NF7 | Privacy | Stores only bin code, note, time marked, time restocked, and daily open counts. No names, no addresses, no cookies. No record enters any AI tool | Data dictionary review, log search |
| NF8 | Data size and speed | A mark-low request sends under 2 kilobytes and gets a reply in under 1 second on the shop Wi-Fi | Developer tools, five requests |
| NF9 | Retention | Low reports and restock records are kept for seven years, because Ohio rules require community repair shops to keep digital parts records for seven years | Database review |

## 4. Data requirements

| ID | Data | Why it is needed | Personal? | Kept for |
|---|---|---|---|---|
| D1 | Bin code and part name | To choose a bin and show the list | No | While the bin exists |
| D2 | Low report: bin code, optional note, time marked | The coordinator's list | No, if the note has no names | Seven years (NF9) |
| D3 | Time restocked | To remove a bin from the list | No | Seven years (NF9) |
| D4 | Daily open counts | R4 | No | Seven years (NF9) |
| D5 | The coordinator's sign-in | To protect the list and the counts | Yes, one adult, with their agreement | While the coordinator uses the board |

## 5. Constraints

- **C1.** No model is part of this project. No commercial AI developer account.
- **C2.** Free tiers only. No payment details entered anywhere.
- **C3.** All stakeholder contact through school channels.
- **C4.** It must work on the donated desktop by the door, which the co-op already owns.

## 6. Out of scope

- **O1.** Payments; ordering parts automatically; customer accounts and repair history; donor
  tracking; an installable phone app; anything that reads the co-op's customer repair spreadsheet.

## 7. Traceability

| Need | Proposal scope item | Requirements | Signed criterion |
|---|---|---|---|
| N1 | S1 | R1, E2 | AC-1 |
| N2 | S2 | R2, R3, E3 | AC-2, AC-3 |
| N3 | S3 | R4 | AC-4 |
| N4 | S1 | R5, R6, NF1, NF4, NF7 | AC-5 |
| | S4 | R7 | none |

## 8. Review and sign-off

- **V1.** Sent to stakeholder: Week 9, Tuesday.
- **V2.** Their questions and changes: none.
- **V3.** Version after review: 1.0.
- **V4.** Stakeholder response: Reviewed and agreed by the shop coordinator, Week 9, Tuesday.

## 9. Change history

| Version | Week and day | What changed | Why | Change request |
|---|---|---|---|---|
| 1.0 | Week 9, Wednesday | First version | | |
