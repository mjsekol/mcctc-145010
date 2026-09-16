# Lab W04-02 · Measure the Wait
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Thursday

**Competency:** 2.7.5 explain the relationship between data transmission volumes, bandwidth, and
latency.

**Time:** Thursday Build 1, 40 minutes. Due at the end of Build 1.

---

## The situation

A youth rec league posts game recaps and season badges on its site. Parents open it on their phones
at the field, where the signal is weak, and the league volunteer keeps hearing that "the site is
slow" while it loads instantly on her laptop at home. She needs to know what is slow and why before
she changes anything.

*The league is a composite, invented for this course.*

**What you will build:** a measured table of four pages under two network settings, and a written
explanation of which problem, bandwidth or latency, each pair of pages shows.

---

## Before you start

Copy `lab-w04-02-files/` into your repository as `labs/w04-02/`. Create
`labs/w04-02/measurements.md`. Everything you **record** goes there.

Read `03-lecture-notes/MCCTC_145010_Notes_VolumeBandwidthLatency.md` first if you missed Thursday's
instruction.

**The server takes its port every time.** This lab uses **8404**. If something else is already
using it, the server will say so and stop. Tell your instructor rather than picking another number.

**Rules.** Gate 3 conditions, any tool, AI usage logged. The numbers must be ones **you** measured.
A table copied from anywhere else, including the lecture notes, is a submission you cannot explain.

---

## Steps

**Step 1. Start the server.** In a terminal, in `labs/w04-02/`:

```
python serve.py --port 8404
```

*You should see:* a list of generated files and their sizes, then
`Serving site/ at http://127.0.0.1:8404/  (Ctrl+C to stop)`. **Record** the size of
`/img/field-full.png` and `/img/field-sized.png` in bytes. Leave this terminal open.

**Step 2. Open the lab page and set up dev tools.** In Chrome, go to `http://127.0.0.1:8404/`.
Press F12 and choose the **Network** panel. Tick **Disable cache**. Keep dev tools open for the
whole lab, because the tick does nothing once dev tools are closed.

Find the throttling menu at the top of the Network panel. It probably says **No throttling**.
Open it and **record** the names of the presets it lists.

*You should see:* four links on the page, and at least three presets in the menu, including one
with 4G in its name.

**Step 3. Your first measurement.** With **No throttling**, click **Recap, full photo**. Look at the
status bar along the bottom of the Network panel.

*You should see:* a number of requests, a number of kB transferred, and a **Load** time. **Record**
all three. Then press F5 to reload and record the three numbers again. They should be close.

**Step 4. Fill the table.** Measure all four pages under **No throttling** and under **Slow 4G**.
Reload each page twice under each setting and write the second reading. Slow 4G is slow on
purpose. The full photo takes a while.

| Page | Setting | Requests | Transferred | Load |
|---|---|---|---|---|
| Recap, full photo | No throttling | | | |
| Recap, full photo | Slow 4G | | | |
| Recap, sized photo | No throttling | | | |
| Recap, sized photo | Slow 4G | | | |
| Badges, thirty files | No throttling | | | |
| Badges, thirty files | Slow 4G | | | |
| Badges, one file | No throttling | | | |
| Badges, one file | Slow 4G | | | |

*You should see:* the two photo pages look the same on screen. The two badge pages look almost the
same. Their numbers do not.

If your menu has no Slow 4G, use the preset closest to it and write its name in the table.

**Step 5. Read the waterfall.** Load **Badges, thirty files** under Slow 4G. Look at the
**Waterfall** column on the right of the request list.

*You should see:* the badge rows starting in groups, one group after another, not all at once.
**Record** one or two sentences describing what the waterfall shows.

**Step 6. Check the arithmetic.** Slow 4G in current Chrome and puppeteer settings carries about
180,000 bytes per second. Using the size you recorded in step 1, work out how many seconds the full
photo should take to transfer at that speed. **Record** the working and compare it with your
measured Load time.

*You should see:* your calculation lands within a couple of seconds of your measurement. Write one
sentence on what makes up the difference.

**Step 7. Answer the two questions.** In `measurements.md`, answer each in three to five sentences,
using numbers from **your** table:

1. **The photos.** Which problem makes the full photo page slow, bandwidth or latency? How do you
   know? What would you tell the league volunteer to change?
2. **The badges.** The two badge pages transfer almost the same number of bytes. Why is one so much
   slower under Slow 4G, and why does the difference nearly vanish with no throttling?

**Step 8. Stop the server.** Click in the server terminal and press **Ctrl+C**.

*You should see:* `Stopped.` **Record** the last three lines of the terminal. Then reload any lab
page in Chrome to prove the server is gone.

**Step 9. Commit and push.**

---

## Acceptance criteria

- [ ] Step 1 file sizes and step 2 preset names recorded
- [ ] Eight table rows, every cell filled from your own measurement
- [ ] The waterfall description names the grouping
- [ ] The step 6 calculation shows its working and compares with the measurement
- [ ] Both questions answered using numbers from your table, and each names bandwidth or latency
- [ ] `Stopped.` recorded from your terminal
- [ ] Committed and pushed by the end of Build 1

---

## If it breaks

| What you see | What it means |
|---|---|
| `serve.py: error: the following arguments are required: --port` | You ran `python serve.py` without `--port 8404`. The server never guesses a port. |
| `OSError: [WinError 10048] Only one usage of each socket address ... is normally permitted` | Something is already listening on 8404, often your own server from earlier in another terminal. Find that terminal and press Ctrl+C. |
| Transferred shows almost nothing and the address bar starts with `file:///` | You opened the file by double-clicking it. Use `http://127.0.0.1:8404/`. |
| The second reload is very fast and shows `(memory cache)` or `(disk cache)` in the Size column | Disable cache is not ticked, or dev tools were closed. Tick it and reload. |
| `This site can't be reached` or `ERR_CONNECTION_REFUSED` | The server is not running. Check the terminal. After step 8, this is the result you want. |

---

## Stretch goal

Load `photo-full.html` under **Slow 4G** and, in the Network panel, click the image row and open its
**Timing** tab. **Record** how long the request spent waiting before the first byte arrived and how
long it spent downloading. Say which half of the rough model from the notes each one is.

---

## Submission checklist

- [ ] `labs/w04-02/measurements.md` with every record item, the table, and both answers
- [ ] The server stopped, with `Stopped.` recorded
- [ ] AI usage log entry if you used AI for anything
- [ ] Committed and pushed

---

## Extended options

All four assess 2.7.5 and are graded on the same scale.

### Three observable signals for choosing

| What you see in the first 10 minutes | Give them |
|---|---|
| Still hunting for the status bar or the throttling menu after step 2 | SCAFFOLDED |
| Step 3 recorded twice, with numbers that agree | STANDARD |
| Asks what the Slow 4G numbers actually are, or how to set their own | EXTENDED |
| Asks what this has to do with anything they will build | APPLIED |

### SCAFFOLDED

Measure only the two **photo** pages and the two **badge** pages under **Slow 4G**, four rows
instead of eight. Your instructor checks your step 3 reading with you before you go on. Skip step 6.
Answer both questions in step 7, and for each one, choose from this sentence starter and finish it
with a number from your table: "The slow page is slow mainly because of ___, and I know because ___."

### STANDARD

The lab as written.

### EXTENDED

Add a **custom throttling profile** in dev tools. [VERIFY] where Chrome keeps it on your version;
it is usually under dev tools Settings, in a section named Throttling, with an option to add a
profile. Name it **Field Wi-Fi**: 2,000 kbps down, 1,000 kbps up, 300 ms latency.

**Before you measure**, predict the Load time of all four pages under Field Wi-Fi using the rough
model and your step 1 sizes. Write the prediction down. Then measure, and explain in writing where
your prediction was furthest off and why.

*Hint, not the answer:* the model has two halves. Work out each half separately for each page, and
look at your step 5 waterfall to decide how many rounds of waiting the thirty-file page pays.

### APPLIED

Pick a public website you actually use: a game wiki, your favourite team's schedule, a restaurant's
menu. **Do not log in and do not use any page that shows your personal information.** Measure its
home page twice under No throttling and twice under Slow 4G. Record requests, transferred, and Load.

Then find the three largest rows in the Network panel by sorting on Size, and write half a page for
the site's owner: which of the three problems from Thursday's notes the page has, what one change
you would make first, and what number you would expect it to change.
