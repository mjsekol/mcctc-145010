# Week 12 Update and Scope Lock Statement · AI draft

*Generated with an AI assistant on Thursday of Week 12, from the senior's prompt: "Write my Week 12
full-form update and my scope lock statement for the Parts Bin Board. Use the course templates. It
goes to the shop coordinator Friday." The senior pasted in three things: the Sprint 2 plan table, the six acceptance criteria, and the
future improvements list, which held one item, FI-1, text alerts. Invented for a
Gate 2 exercise: the project, the co-op, and the coordinator are a composite, not a real
organization or person. Paragraphs are numbered U1 to U13 and SL1 to SL10.*

---

## Part 1 · The weekly update

**Subject:** Parts Bin Board: week 12 update, at risk

**U1.** Hello,

**U2.** **Status: at risk.** A few finishing touches remain on the coordinator pages, and everything
else is on schedule.

**U3.** The system has run 7 days without manual intervention.

**What you can see or try this week**

**U4.** I refactored the app into Flask blueprints, which separates the volunteer code and the
coordinator code into their own modules and makes future features faster to add.

**U5.** All colors and spacing now come from CSS custom properties, so the whole theme can be
changed from one place.

**U6.** Test coverage for the database layer went up this week.

**Progress against what we agreed**

| Acceptance criterion | Status |
|---|---|
| AC-1 Mark a bin low, no name asked | working |
| AC-2 See and print the low list | in progress: the list works, printing is next week |
| AC-3 Mark restocked | working |
| AC-4 Count board opens | working |
| AC-5 Works on the co-op desktop and on a phone | in progress |
| AC-6 Keyboard and Narrator, zero automated violations | moved to future improvements, see Scope |

**Problems, and what I am doing about them**

**U7.** None this week. Some minor polish remains on the coordinator pages.

**What I need from you, and by when**

**U8.** Nothing this week.

**Next week**

**U9.** The printable low list.

**U10.** Text alerts when a bin is marked low.

**U11.** Final polish on the coordinator pages.

**Scope**

**U12.** My scope lock statement is below. One addition: text alerts are now in scope. The MCCTC
Capstone Handbook, section 4.2, allows one addition after scope lock with instructor sign-off, and I
will ask my instructor for that sign-off on Monday.

**U13.** Thank you,
[first name]
Senior, AI Automation and Software Development

---

## Part 2 · Scope Lock · Parts Bin Board

Locked: Week 12, Friday   Acceptance agreement version: 1

### In scope, final

**SL1.** Anyone with the shop link marks a bin low: bin code and an optional note of up to 120
characters, no name.

**SL2.** The signed-in coordinator sees the low list, newest first, and can print it.

**SL3.** The coordinator marks a bin restocked.

**SL4.** A count of board opens per day, with no cookies and no stored addresses.

**SL5.** A health address that checks the database, and the thirty-day health log.

**SL6.** Text alerts to the coordinator when a bin is marked low, added under Handbook section 4.2.

### Moved to stretch goals

**SL7.** A shelf map showing where each bin is. Unchanged from the proposal.

### Moved to future improvements

**SL8.** Keyboard-only and screen reader support (AC-6), since the co-op's volunteers are mostly
retirees who use a mouse. The automated check will still be run before handoff.

### Sent to the stakeholder

**SL9.** Week 12, Friday, with the weekly update. Their reply: Agreed by the shop coordinator, Week
12, Thursday.

**SL10.** From this point, scope may be reduced by agreement and is never expanded.
