# Sprint 2 · Week 12 · Parts Bin Board

**Invented for a Gate 2 exercise.** The Parts Bin Board, the bike repair co-op, and its shop
coordinator are a composite, not a real organization or person. This is the senior's own sprint
file, written through Thursday of Week 12. Lines in the review are numbered S1, S2, and so on.

---

## Plan · Monday

**Sprint goal:** You can sign in, see every bin marked low, mark bins restocked, and print the list,
on the deployed board.

**Acceptance criteria this sprint moves forward:** AC-2, AC-3, AC-4, AC-6

**Hours available this week:** 12 class hours plus 2 in Period 8 = 14

| # | Task | Hours | Done when | Status Thursday |
|---|---|---|---|---|
| 1 | Coordinator sign-in | 2 | Signed-out requests go to sign-in (T-10) | done |
| 2 | Low list page, newest first | 2 | T-06 passes on the deployed board | done |
| 3 | Mark restocked | 2 | T-08 passes on the deployed board | done |
| 4 | Board-open counter and counts page | 2 | T-12 passes | done |
| 5 | Printable low list | 3 | T-07 passes | not started |
| 6 | web-check clean on the coordinator pages | 3 | 0 violations on the low list page | not done |
| | **Total** | **14** | | |

**If I run out of time, I cut first:** task 5 from this sprint, moved to Sprint 3. Not from scope.

**Risks this week:** sign-in takes longer than planned.

## Daily standup

| Day | Finished | Working on | Blocked by |
|---|---|---|---|
| Mon | Sprint 2 plan | Sign-in | nothing |
| Tue | Nothing new. The board stopped answering before school. Restarted it by hand at 8:14. TS-3 opened | Finding why the database file was locked | the hang |
| Wed | TS-3 cause found. Sign-in, low list, restock. Released version 0.2.0 by the deployment steps at 3:20 | Counter | nothing |
| Thu | Counter and counts page | web-check on the low list page | 2 violations I do not understand yet |
| Fri | | | |

## Review · written Thursday, finished Friday

**S1. Goal met?** Partly. Sign-in, the low list, restock, and the counter work on the deployed
board. Printing is not started.

**S2. Tasks finished:** 4 of 6. **Hours planned:** 14. **Hours spent by Thursday:** 13, of which
about 4 went to TS-3.

**S3. What works now, that did not on Monday:** the coordinator can sign in at the shop link, see
the low list newest first, and press Restocked. The board counts how many times it was opened each
day.

**S4. What took longer than planned, and why:** TS-3. On Tuesday morning the board stopped
answering. The database file was locked by a copy of the app I had started by hand on Monday to
test sign-in and never stopped. I stopped it and restarted the service by hand at 8:14. That was a
manual intervention. It is in the events log and in `troubleshooting-log.md` as TS-3.

**S5. Test plan run this sprint:** web-check on the saved low list page: FAIL. 0 validation errors,
2 axe violations: `label` (the low list's filter box has a placeholder and no label) and
`color-contrast` (the grey time stamp). **NF3 is currently failing. AC-6 is not met yet.**

**S6. Thirty-day clock:** started Week 11, Friday, when the walking skeleton was deployed.
**Reset Week 12, Tuesday, 8:14, by the manual restart in S4.** Running again since then. The report
command and its output go in the Friday update.

**S7. Carried from Week 11:** at the Sprint 1 demo on Week 11, Friday, the coordinator asked whether
the board could send a text message when a bin is marked low. I said I would record it as a future
improvement. It is FI-1 in `change-requests.md`.

**S8. Stretch list, from the signed proposal, unchanged:** a shelf map showing where each bin is.

**S9. What moved:** task 5, printing, moves to Sprint 3. It stays in scope. It is part of AC-2.

**S10. Shown to:** a classmate, Thursday. The coordinator sees it at the Friday update.

**S11. One change to how I work next week:** stop every local test copy of the app before leaving,
and check for it at the start of each period.

**S12. Still to do Friday:** Update 2 and the scope lock statement, sent together, instructor copied.
