# Architecture · Parts Bin Board (excerpt)
Version 1.0   Written: Week 10, Tuesday   Supports: Requirements version 2.0

**Invented for a Gate 2 exercise.** The project, the co-op, and the coordinator are a composite,
not a real organization or person.

**Status on the day this was written.** Nothing is built yet. Sprint 1, the walking skeleton,
starts Week 11, Monday. The repository holds documents only.

---

## 1. The picture

    co-op desktop (Edge) or a volunteer's phone
            |
            | HTTPS, the shop link
            v
    web app: Flask 3.1.3 (Python)  --->  SQLite file: parts_board.db
            |
            +--> /health   (opens the database and reads one row)

## 2. Components

| Component | What it does | Language or product | Runs on | Port or address |
|---|---|---|---|---|
| Web app | The board, the low list, sign-in, the counts page | Python 3.13, Flask 3.1.3 | Approved host, to be confirmed | Local runs: 127.0.0.1 port 5310 |
| Database | Bins, low reports, daily counts | SQLite, one file | Same machine as the web app | File path from the setting `PARTS_DB` |
| Health route | Reports whether the database answers | Part of the web app | Same | `/health` |
| Health checker | Writes the thirty-day health log | `health_check.py`, every 30 minutes | A lab machine the instructor approves | Calls the deployed `/health` |

## 3. Where it runs, and who can reach it
- **Decision:** approved host, to be confirmed. The host choice is on the agenda for this week's
  conference. Until it is confirmed, every run is local on a lab machine.
- **Approved by:** not yet. Conference booked for Week 10, Thursday.
- **Who can reach it, and how:** volunteers open the shop link on the co-op desktop or their own
  phone. The coordinator signs in from the same link.
- **What it needs that you do not control:** the host's free tier, and the shop Wi-Fi.
- **Static or dynamic, and why:** dynamic, because the low list changes every time someone marks a
  bin.

## 4. Hardware
| Component | Needs | Has | Checked how |
|---|---|---|---|
| Co-op desktop | A current browser | Windows, Microsoft Edge, screen 1280 wide. No other computer at the co-op. No tablet. | Coordinator's answer in the needs-discovery meeting, Week 7, Friday |

## 8. Logging and health
- **What is logged:** start and stop, errors by type. Never a note's text, never a password.
- **The health check:** `GET /health` answers 200 with `{"database": "ok"}` after reading one row,
  and 503 when the read fails.
- **The health log:** `health_check.py` on a schedule, every 30 minutes, from the approved machine.

## 9. The test setup

| Real piece | Stand-in | How to start it | What it can simulate |
|---|---|---|---|
| Hosted web app | The same app run locally | `flask --app parts_board run --port 5310` | normal |
| Hosted database | A local copy with invented bins B-01 to B-12 | set `PARTS_DB` to `test-data/parts_test.db`, then the start command above | empty, twelve bins, missing file |
| Database unavailable | The test copy renamed while the app runs | rename `test-data/parts_test.db`, then reload | E1 |

## 11. Tools

| Tool | Version | Why this one |
|---|---|---|
| Python | 3.13.7 | Installed on every lab machine |
| Flask | 3.1.3 | Used in 145130; its command line has `run`, `routes`, and `shell` |
| web-check | course copy, `tools/web-check/check.js` | Validation and automated accessibility audit, NF3 and NF5 |
| Microsoft Edge developer tools | with the browser | NF1 load time |
| Windows Narrator | with Windows | NF3 screen reader walkthrough |
