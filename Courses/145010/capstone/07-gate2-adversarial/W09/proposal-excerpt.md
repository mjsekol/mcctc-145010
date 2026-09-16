# The signed scope · Parts Bin Board
## Gate 2 · Week 9 · folder file 1 of 3

**Everything in this folder is invented and composite.** The community bike repair co-op is a
composite, not a real organization. The shop coordinator and the student are not real people.

**What this file is.** Excerpts from the senior's committed Define documents, after the Week 8 scope
check: the concept proposal (version 2), the acceptance agreement the coordinator signed (version
1), and the contact log. The signed copy is on file with the instructor. Lines are numbered **L1 to
L44** so you can cite them.

---

## Part A · Concept Proposal, version 2, excerpts

**L1.** Version 2. Version 1 written: Week 8, Monday. Version 2, after the scope check: Week 8,
Tuesday. Presented: Week 8, Thursday, on an approved call. Track: Full-Stack.

### Section 3 · Target audience

**L2.** Primary users: volunteers on open-shop nights, from high school students to retirees, and
the shop coordinator.

**L3.** Devices: the donated desktop by the door, running Windows with Microsoft Edge at 1280 pixels
wide, which many older volunteers use because they do not carry a smartphone. Some younger
volunteers use their own phones, about 360 pixels wide, in the phone's own browser.

**L4.** Accessibility: at the presentation the coordinator said, "A couple of our regulars use the
big-text setting on that desktop." Nobody has asked the volunteers about any other needs. The
board is planned for keyboard use, text zoomed to 200 percent, and labels that make sense in
Windows Narrator.

### Section 4 · Client needs

**L5.** N1. A volunteer can report an empty bin the night it happens, without giving a name or
making an account. (Meeting record, Week 7, Friday.)

**L6.** N2. The coordinator knows which bins are empty before Sunday, and can carry the list along
the shelves. At the presentation the coordinator put it this way: "I need to hear about an empty
bin promptly. Before Sunday, not the second it happens." (Week 7, Friday, and Week 8, Thursday.)

**L7.** N3. The coordinator can see whether volunteers actually open the board, so the Week 17
comparison with the baseline means something. (Week 8, Thursday.)

**L8.** N4. It works on the donated desktop by the door and on volunteers' phones. Customer
information stays inside the co-op, and strangers cannot interfere with the board. (Week 7, Friday.)

### Section 7 · Scope

**L9.** S1. Mark a bin low: anyone with the shop link chooses a bin code from the co-op's list and
may add a note of up to 120 characters. No name, no account.

**L10.** S2. Coordinator low list: the coordinator signs in, sees every low bin newest first, prints
the list, and marks bins restocked.

**L11.** S3. Page-view counter: the board counts how many times it was opened each day, with no
cookies and no stored address, and shows the counts to the coordinator.

**L12.** S4. A health endpoint.

**L13.** S5. Flask and SQLite on an approved host, with a local fallback on the co-op desktop, to be
confirmed with the instructor in Week 10.

**L14.** How people reach it: the shop link is shared inside the co-op, on a card taped by the bins
and on the desktop's home page. The board is not advertised or listed publicly. The coordinator
said, "This is for our people, not for the internet." (Week 8, Thursday.)

**L15.** Out of scope: payments; ordering parts automatically; customer accounts and repair history;
donor tracking; an installable phone app; public listing or advertising of the board; anything that
reads the co-op's customer repair spreadsheet.

**L16.** Stretch: a count of low reports per bin.

### Section 18 · Data and privacy

**L17.** Data the project holds: bin codes and names of parts, low reports (bin code, optional
note, time marked), time restocked, daily open counts, and the coordinator's sign-in.

**L18.** Personal data: none about volunteers or customers. The note field says "Do not write
names" beside it.

**L19.** How long it is kept: a low report is deleted 90 days after it is marked restocked. The
coordinator asked for "about three months, so I can see what keeps running out." (Week 8,
Thursday.)

**L20.** No record from this project enters any AI tool.

---

## Part B · Acceptance Agreement, version 1, criteria

**L21.** Signed by the shop coordinator, Week 8, Friday. Signed copy on file with the instructor.

**L22.** Devices and platforms these are checked on: the co-op desktop, Windows, Microsoft Edge,
1280 wide; a phone at 360 wide; keyboard only; Windows Narrator.

**L23.** AC-1 · Mark a bin low, no name asked. Given the board open at the shop link, when a
volunteer chooses bin B-01 and presses Mark low with no note, then B-01 is on the coordinator's low
list, and no name or account was asked for. With no bin chosen, or a note over 120 characters, the
page says what to fix and nothing is saved.

**L24.** AC-2 · See and print the low list. Given a bin marked low, when the coordinator signs in
and opens the low list, then that bin appears with its note and the time it was marked, and the
list prints on one page.

**L25.** AC-3 · Mark restocked. Given B-01 on the low list, when the coordinator marks it
restocked, then it leaves the low list. Someone who is not signed in cannot open the low list or
mark anything restocked.

**L26.** AC-4 · Count board opens. Given the board was opened 5 times today, when the coordinator
opens the counts page, then today's row shows 5, and no cookie or address was stored.

**L27.** AC-5 · Works on the co-op desktop and on a phone. Given the co-op desktop and a phone at
360 wide, when a volunteer marks a bin low on each, then it works on both with no sideways
scrolling, and the board page loads in under 3 seconds on the desktop.

**L28.** AC-6 · Usable by keyboard alone and with Narrator, zero automated violations. Given the
co-op desktop with the keyboard only, when a volunteer marks a bin low, then every step can be done
without a mouse, Narrator reads each field's label, and the automated check reports zero
accessibility violations on every page.

**L29.** After Week 12, scope may be reduced and may not be expanded.

---

## Part C · Contact log, Weeks 8-9

| Line | Week and day | Direction | Channel | Purpose | Outcome |
|---|---|---|---|---|---|
| L30 | Week 8, Mon | sent | school email, instructor copied | reminder of Wednesday's proposal | acknowledged |
| L31 | Week 8, Wed | sent | school email, instructor copied | final proposal and agreement | received |
| L32 | Week 8, Thu | meeting | approved call, instructor on the call | proposal presented | see meeting record |
| L33 | Week 8, Thu | sent | school email, instructor copied | meeting summary | "That is right." |
| L34 | Week 8, Fri | received | school, via instructor | signed agreement version 1 | on file with instructor |
| L35 | Week 9, Mon | sent | school email, instructor copied | baseline request: counts only, names covered | coordinator agreed |
| L36 | Week 9, Tue | received | school email | baseline counts for six nights | see baseline record |
| L37 | Week 9, Tue | sent | school email, instructor copied | thank you for the counts | no reply needed |

**L38.** Planned: Week 9, Thursday. Send requirements version 1 for review, with the question "Is
anything here not what you meant, and is anything missing?"

**L39.** Planned: Week 9, Friday. Status note.

---

## Part D · What the senior committed on Week 9, Wednesday

**L40.** `docs/measure-analyze/baseline.md`: counts final, limits drafted.

**L41.** `docs/measure-analyze/requirements.md`: version 1.0, first draft, generated with the lab's
assistant from Parts A and B of this file and the baseline record. Not yet sent.

**L42.** `ai-usage-log.md`: one entry for the requirements draft.

**L43.** Nothing has been sent to the coordinator since L37.

**L44.** No message from the coordinator has arrived since L36.
