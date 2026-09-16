# Requirements excerpt · Parts Bin Board · Sprint 1 walking skeleton

**This is a composite, not a real organization.** The Parts Bin Board is the capstone example
project that runs through the Define, Measure, and Improve materials: a volunteer-run community
bike repair co-op. Volunteers fix donated bikes on open-shop nights. Repairs stall when a parts
bin is empty and nobody tells the shop coordinator, who otherwise walks the shelves and texts a
list. No budget. No personal data about the people the co-op serves may leave the building.
Every line here is invented.

This excerpt is the part of the signed requirements the Sprint 1 walking skeleton has to reach.
The numbers match the full requirements specification, so a gap in the numbering below is work
planned for a later sprint, not a missing requirement.

## What the walking skeleton must do

The walking skeleton is the thinnest path through every layer, deployed where it will finally
run. For this project that path is: a browser page reads the bins from the database, a form
writes one low report, the coordinator view reads the low list, and a health endpoint reports
whether the service can reach its real data.

## Functional requirements in this sprint

### R1 · Mark a bin low
The system must let anyone with the shop link mark a bin low by choosing its bin code and, if they
want, adding a note of up to 120 characters. It must never ask for a name.

- AC-1.1 Given a bin code that is on the board, when a volunteer submits the low report, then the
  bin is recorded as low and the volunteer sees a confirmation naming the bin.
- AC-1.2 Given a bin code that is not on the board, when a volunteer submits the report, then the
  system rejects it and records nothing.

### R2 · See and print the low list
The system must show the coordinator every bin currently marked low, newest first. In this sprint
the skeleton shows the list as plain text. Sign-in and the printable view are Sprint 2 work.

- AC-2.1 Given one or more bins have been reported low, when the coordinator opens the low list,
  then every reported bin appears with its part name.

### R4 · Count board opens
The system must count how many times the board is opened, without cookies and without storing any
address. In this sprint the skeleton keeps one running total. The daily counts page is Sprint 2
work.

### R7 · Health endpoint
The system must provide a health address that reports whether the service can reach its real
data, so the scheduled check that feeds the thirty-day survival record can tell a working service
from a broken one. Reporting which version runs is added in Sprint 2.

- AC-7.1 Given the database is reachable and holds the bins table, when the health address is
  requested, then it reports ok.
- AC-7.2 Given the database file is missing, when the health address is requested, then it reports
  a failure, not ok.

## Not in this sprint

- **R3 · Mark restocked.** Sprint 2 work. This skeleton does not implement it.

## Non-functional requirements

| ID | Kind | Requirement | How it is measured |
|---|---|---|---|
| NF1 | Performance | The board page loads in under 3 seconds on the co-op desktop over the shop Wi-Fi | Browser developer tools, Network panel, cache disabled, three loads, the slowest reported |
| NF2 | Availability | Runs 30 consecutive days without manual intervention | Thirty-day survival record |
| NF3 | Accessibility | Zero automated accessibility violations at WCAG 2 A and AA on every page; every task possible by keyboard alone; headings, labels, and messages that make sense in Windows Narrator | Automated check with web-check, a keyboard-only walkthrough, a Narrator walkthrough |
| NF4 | Devices and browsers | The co-op desktop by the door: Windows, Microsoft Edge, 1280 pixels wide. Volunteers' own phones, 360 pixels wide. Keyboard only. Windows Narrator | Test plan platform cases |
| NF5 | Validity | Zero HTML validation errors on every page | web-check validation |
| NF6 | Security | Only the signed-in coordinator can see the low list, mark restocked, or see the counts (sign-in arrives in Sprint 2). The coordinator password is never in the repository. Every value that reaches a database query is passed as a bound parameter, so it cannot change the query | Test cases and code review |
| NF7 | Privacy | Stores only bin code, note, time marked, and board open counts. No names, no addresses, no cookies | Data dictionary review, log search |
| NF8 | Data size and speed | The low list does a fixed amount of database work however many bins are low | Code review, statement count |

## Constraints

- Flask and SQLite, deployed to a host the instructor approved, with a local fallback.
- Models, if any, run locally. No commercial AI developer account.
- Free tiers only. No payment details entered anywhere.
