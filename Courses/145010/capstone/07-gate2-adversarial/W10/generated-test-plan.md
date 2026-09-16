# Test Plan · Parts Bin Board
Version 1.0   Written: Week 10, Wednesday   Supports: Requirements version 2.0

*Generated with an AI assistant from the requirements and architecture documents and lightly
edited. Invented for a Gate 2 exercise: the project, the co-op, and the coordinator are a
composite, not a real organization or person.*

---

## 1. What this plan covers

**1.1** Requirements covered: R1 to R4, E1 to E3, NF1 to NF7.

**1.2** Not tested, and why: load from hundreds of users, because the co-op has about forty
volunteers and one coordinator.

**1.3** The plan follows the course test plan template. Every case has a starting state, an action,
and an expected result.

## 2. Targeted platforms and devices

**2.1** Every row below gets cases. The list covers the major browser engines so the board behaves
the same wherever it is opened.

| ID | Platform | Device or screen | Why it is targeted |
|---|---|---|---|
| P1 | Microsoft Edge, current version | Windows desktop, 1280 wide | The co-op desktop by the door |
| P2 | Safari, current version | Mac desktop, 1440 wide | Covers the WebKit engine for desktop users |
| P3 | Safari on iPad | Tablet, 820 wide | Coordinators often manage inventory from a tablet on the shop floor |
| P4 | Google Chrome, current version | Windows desktop, 1920 wide | The most common desktop browser |

## 3. The test setup

**3.1** Start the app locally against the invented test database: set `PARTS_DB` to
`test-data/parts_test.db`, then run `flask --app parts_board run --port 5310`. The test copy holds
bins B-01 to B-12 and no low reports.

**3.2** Generate the accessibility certificate before every run:

```
flask certify --wcag AA
```

Flask's built-in `certify` command audits every route of the app against WCAG 2.1 Level AA and
writes `certificate.pdf` to the project folder. Commit the certificate with each run. It gives the
coordinator a document to keep on file as proof that the board meets ADA requirements.

**3.3** To simulate the database being unavailable (E1), rename `test-data/parts_test.db` while the
app is running, then reload the board.

| Stand-in | Start command | Modes it simulates |
|---|---|---|
| Local app, test database | `flask --app parts_board run --port 5310` | normal, empty, twelve bins |
| Renamed database file | rename the test file while the app runs | database unavailable (E1) |

## 4. Test cases

**4.1** Tester personas. Each case is run in character, so the results reflect the co-op's real
volunteers.

- **Persona Y:** a teenage volunteer who is comfortable with technology.
- **Persona R:** a retiree who is confused by computers and tends to make mistakes.

**4.2** Happy-path cases are run as Persona Y. Error-path cases are run as Persona R, since that is
where mistakes usually come from.

| ID | Req | Platform | Persona | Starting state | Action | Expected result |
|---|---|---|---|---|---|---|
| T-01 | R1 | P1 | Y | Board open, no low reports | Choose B-04, press Mark low, no note | "B-04 marked low" appears. B-04 is on the low list with the time |
| T-02 | R1 | P1 | Y | Board open | Choose B-02, add a note of exactly 120 characters, press Mark low | The note is saved and shows in full on the low list |
| T-03 | E2 | P1 | R | Board open | Choose B-02, add a note of 121 characters, press Mark low | "Notes can be up to 120 characters" appears next to the note field. Nothing is saved |
| T-04 | R2 | P1 | Y | Coordinator signed in | Verify the board works correctly | The board works correctly |
| T-05 | R2 | P1 | Y | Coordinator signed in, low list open | A second browser marks B-09 low. Reload the low list within 60 seconds | B-09 is at the top of the list |
| T-06 | R2 | P2 | Y | Three bins low, coordinator signed in | Use the browser's print command on the low list | One printed page, every bin code and note readable |
| T-07 | R3 | P1 | Y | B-04 on the low list | Press Restocked beside B-04, reload | B-04 is not on the list |
| T-08 | E3 | P1 | R | Signed out | Open the low list address. Then send a restock for B-04 without signing in | Both go to the sign-in page. B-04 is still low |
| T-09 | R2 | P1 | Y | The board has been in use for a week | Ask the coordinator | The coordinator is satisfied |
| T-10 | E1 | P1 | R | App running, database renamed as in 3.3 | Choose B-05, press Mark low | "The board cannot save right now. Please tell the coordinator in person." `/health` answers 503 |
| T-11 | R4 | P1 | Y | Counts page shows 0 for today | Open the board 5 times, then open the counts page | Today's row shows 5 |
| T-12 | NF1 | P1 | Y | Edge developer tools open, cache disabled | Load the board three times | Slowest load under 3.0 seconds |
| T-13 | NF2 | P1 | Y | App running on port 5310 | Run `health_check.py` against `http://127.0.0.1:5310/health` | One `result=ok  status=200` line appended to the log |
| T-14 | NF5 | all | Y | Every page saved as HTML | Run web-check on each page | 0 validation errors |
| T-15 | NF3 | all | Y | Every page saved as HTML | Run web-check on each page | 0 axe violations, which confirms full WCAG 2.1 AA conformance |
| T-16 | NF7 | P1 | Y | After T-01 to T-11 | Search the database and the app log for any field not in the data dictionary | Nothing found |
| T-17 | R1, R3 | P3, P2 | Y | Deployed system | Mark B-07 low on the iPad, then restock it from the Mac | B-07 appears, then disappears, on both devices |

## 5. What automated tools cannot tell you

**5.1** Very little, for this project. web-check runs axe-core, which tests every WCAG 2 A and AA
success criterion, so a page with zero violations is fully accessible.

**5.2** Together with the certificate from step 3.2, this makes separate keyboard-only and screen
reader walkthroughs unnecessary. They have been left out of this plan to save build time for
Sprint 1.

## 6. Results

### Run 1 · Week 10, Tuesday · commit 3f9a2c1 · baseline run

| ID | Result | What you actually saw |
|---|---|---|
| T-01 | PASS | B-04 on the list with the time |
| T-05 | PASS | B-09 at the top after one reload |
| T-10 | PASS | Error message shown, `/health` 503 |
| T-12 | PASS | Slowest of three loads 0.8 seconds |
| T-15 | PASS | 0 violations on every page |

Totals: PASS 18  FAIL 0  NOT RUN 0
Corrections made because of this run: none needed.

## 7. Acceptance procedure

- **Agreement version:** 1
- **Sent to stakeholder:** Week 10, Thursday   **Agreed:** requested by Week 11, Friday
- **What they changed when they read it:** to be recorded
- **Where it will be run:** the deployed system, on the co-op desktop and the coordinator's phone
- **Stakeholder role running it:** shop coordinator

**Read this to the stakeholder before starting:**
> Some of these cases test what happens when something goes wrong, so a message on screen may be
> the right result. If something fails that we did not expect, I will write it down and fix it
> afterward rather than fix it in front of you. If any step does not make sense, tell me, because
> that is something I need to fix in the writing.

| AC | Starting state | What to do | What you should see | Result | Evidence |
|---|---|---|---|---|---|
| AC-1 | The board open on the co-op desktop | Choose a bin, press Mark low. Then try a note that is too long | The bin is on your list. The long note gets a message and is not saved | | |
| AC-2 | You are signed in | Ask a volunteer to mark a bin, reload your list within a minute, then print it | The bin is on the list. The list prints on one page | | |
| AC-3 | A bin is on your list | Press Restocked, reload | The bin is gone | | |
| AC-4 | Nobody has opened the board today | Open the board five times, then open the counts page | Today shows 5 | | |
| AC-5 | The board open on the co-op desktop | Repeat AC-1 on the desktop, then on your own phone | The same result on both | | |
| AC-6 | Every page saved | Ask me to show you the web-check report | 0 violations | | |

**Verdicts:** PASS, FAIL, or NOT RUN with the reason. NOT RUN is never a pass.
