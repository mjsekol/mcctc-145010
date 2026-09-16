# Catch-Up Guide · Week 4
## 145010 Web Design & Senior Capstone · Unit 4 · for students at BPA State

**You were competing. This week was built so you can catch up on your own.** Nobody expects you to
have been in two places. Everyone expects you to catch up by the dates below.

**Print this before you leave.** Start with the first day you missed, and do the days in order,
because each one builds on the last.

---

## Your deadlines

| What | Normal deadline | Your deadline if you missed two or more days |
|---|---|---|
| Lab W04-01 Wire the Shift Board | Week 4 Wed, Build 1 | Week 4 Fri, end of Period 8 |
| Plug-in note | Week 4 Mon, Build 2 | Week 4 Fri, end of Period 8 |
| Lab W04-02 Measure the Wait | Week 4 Thu, Build 1 | Week 5 Mon, end of Period 8 |
| Gate 2 W04 | Week 4 Fri, Build 1 | Taken when you are in the room, same conditions |
| Quiz W04 | Week 4 Fri, Build 2 | Week 5 Mon, Period 8 |
| Project: The Interactive Component | Week 4 Fri, commit window | Week 5 Tue, end of Period 8 |

**Confirm your deadline with your instructor on your first day back.** It goes in the gradebook
comment, and it is not a penalty.

---

## If you missed Monday · Where script lives

**Read:** [Where Script Lives](../03-lecture-notes/MCCTC_145010_Notes_WhereScriptLives.md). Answer
its three self-check questions on paper before looking at the answers.

**Build:** Lab W04-01, Part A, steps 1 to 4, then step 5, the plug-in note.

**Gate 1 rep:** rep 01, ten minutes, no tools. Ask your instructor for it.

**Minimum evidence to commit:** `lab-notes.md` with the exact error from step 3 and your three
Console results from step 4, and `plugin-note.md` with at least two named sources.

**The one idea to leave with:** a script runs when the parser reaches it, so every script tag gets
`defer`.

---

## If you missed Tuesday · The page waits for you

**Read:** [The Page Waits for You](../03-lecture-notes/MCCTC_145010_Notes_ThePageWaitsForYou.md).

**Build:** Lab W04-01, Part B, steps 6 to 12.

**Gate 1 rep:** rep 02 or 06.

**Minimum evidence to commit:** the rules toggle and the shift buttons working, and your step 9
sentence on why no keyboard listener was needed.

**The one idea to leave with:** a `<button>` turns Enter and Space into a click. A `<div>` does not,
and the checker will not tell you.

**Test yourself:** hands off the mouse. If you cannot use your shift board with Tab, Enter, and
Space, you are not finished.

---

## If you missed Wednesday · State, render, and comments

**Read:** [State, Render, and Comments](../03-lecture-notes/MCCTC_145010_Notes_StateRenderAndComments.md).

**Build:** Lab W04-01, Part C, steps 13 to 15, and submit. Then the project's Define checkpoint:
open the [project spec](../09-project/MCCTC_145010_Project_W04_InteractiveComponent.md), pick a scope
using its calibration table, and write the Define section of `decision-log.md`.

**Minimum evidence to commit:** Lab W04-01 submitted with `web-check` output, and the Define
checkpoint.

**The one idea to leave with:** if a person typed it, it is text, so it goes in with `textContent`.

**Scope advice.** If you missed two or more days, choose the **Small** scope. A finished accordion
that passes every check scores higher than an unfinished finder.

---

## If you missed Thursday · What a page costs

**Read:** [What a Page Costs to Deliver](../03-lecture-notes/MCCTC_145010_Notes_VolumeBandwidthLatency.md).

**Build:** Lab W04-02, all of it. It takes about 40 minutes. **Start the server with
`python serve.py --port 8404` and stop it with Ctrl+C when you finish.** Then measure your own
project page, as the project spec's R11 describes, using port 8414, and stop that server too.

**Minimum evidence to commit:** the eight-row table, both answers, `Stopped.` from your terminal, and
your project README's page weight line.

**The one idea to leave with:** big files suffer on low bandwidth. Many files suffer on high latency.

---

## If you missed Friday · Gate 2, quiz, demos

**No new content was taught.** Your instructor gives you Gate 2 W04 under the same conditions:
40 minutes, silent, no AI tool. You take the quiz in Period 8 of Week 5, Monday.

**Before the quiz,** redo the self-check questions in all four notes and gate 1 reps 02, 04, and 09.
Those three cover the ideas the quiz leans on hardest.

**Your demo** happens when your instructor schedules it, in the first days of Week 5, keyboard only,
three minutes. The script is in the project spec.

---

## If you are stuck

1. Reread the "If it breaks" table in the lab. Most problems this week are one of four errors.
2. Type your selector into the Console. If it says `null`, the selector or the timing is wrong.
3. Ask a classmate who was here that day to show you their step, not their code.
4. Write the question in your decision log with your best guess, and keep going on the next step.
5. Bring it to your instructor on your first day back. Say which step and what you tried.
