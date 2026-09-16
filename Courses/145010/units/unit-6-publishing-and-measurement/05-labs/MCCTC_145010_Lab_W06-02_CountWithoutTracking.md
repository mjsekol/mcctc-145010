# Lab W06-02: Count Without Tracking
## 145010 Web Design · Unit 6 · Week 6, Tuesday

**Gate:** 3 (open). Full tooling, decision log entry required. **Duration:** Build 1 (40 minutes)
and Build 2 (55 minutes).
**Competencies:** 1.10.5 monitor customer expectations and determine satisfaction using measurement
tools · 6.5.3 standard web languages (markup and client-side script) in site development ·
6.4.7 scripting that talks to a data source, from Week 5, used here.

**Notes for this lab:** `03-lecture-notes/MCCTC_145010_Notes_MeasureAQuestionNotAPerson.md`.

---

## The scenario

On Friday you report whether anyone used your site and whether it helped them. The people visiting
are your classmates, many of them under 18, and a lot of ready-made analytics tools collect far more
about each visitor than that question needs. You are going to build the measurement tool yourself,
so you know exactly what it keeps.

## What you will build

A counter that records which pages load and whether visitors found them useful, and nothing that
could identify a single visitor.

---

## Starter files

From `05-labs/lab-w06-02-files/`:

| File | Copy it to | What it is |
|---|---|---|
| `serve.py` | `sitekit/` | Serves your site. Counts nothing yet. Logs the default way. |
| `count.js` | `sitekit/static/` | Comments only, plus a check for pages opened from disk |
| `test_counter.py` | `sitekit/` | 13 tests. Most fail until you finish. |
| `report.py` | `sitekit/` | Complete. Turns the counts into a table. |

**Port 8606, every time, for every server you start this week.** Stop your server with Ctrl+C
before you start another one. On the build machine, a second copy started on a port that was
already in use printed its "Serving" line and gave no error. You can end up testing the wrong one.

**Restart the server after every change to `serve.py`.** A running server keeps the old code.

---

## Part A · Build 1 · 40 minutes

**1. Start it and read the terminal.** In `sitekit/`:

```
python build.py
python serve.py --port 8606
```

Open `http://127.0.0.1:8606/` in your browser. Look at the terminal.
*You should see* a line like `127.0.0.1 - - [date and time] "GET / HTTP/1.1" 200 -`. Write one
sentence in your lab notes about what the first thing on that line is.

**2. Stop logging addresses.** In `SiteHandler`, where the step 2 comment is, add:

```python
def log_request(self, code="-", size="-"):
    status = code.value if isinstance(code, HTTPStatus) else code
    sys.stderr.write(f"{self.command} {self.path.split('?', 1)[0]} {status}\n")
```

Restart the server and reload the page.
*You should see* `GET / 200` with nothing in front of it.

**3. Take a baseline.** In a second terminal, in `sitekit/`, run `python test_counter.py`.
*You should see* `Ran 13 tests` and a `FAILED` line. Write down how many failures and errors.

**4. Accept a hit.** Replace the body of `_hit` so it follows its comment: parse the JSON, refuse
anything that is not JSON or has no `path` with a 400, `normalise()` the path, refuse any page
not in `self.known_pages` with a 400, then call `self.store.add_view(page)` and reply 204.

Restart. Open DevTools on your site, Console tab, and run:

```javascript
await fetch("/api/hit", { method: "POST", body: JSON.stringify({ path: "/nope.html" }) }).then(r => r.status)
```

*You should see* `400`. Now run it with `path: "/"`.
*You should see* the request fail, and a traceback in the server terminal ending
`NotImplementedError: add_view is step 5`. **Read the first line of that traceback report.** It
names something you stopped logging in step 2. Fill in `QuietServer` so a crash report prints the
traceback only:

```python
def handle_error(self, request, client_address):
    rule = "-" * 40
    print(rule, "A request could not be handled:", sep="\n", file=sys.stderr)
    traceback.print_exc()
    print(rule, file=sys.stderr)
```

Restart and repeat the `path: "/"` request.
*You should see* the traceback again, now with no address above it.

**5. Count it.** Write `add_view`: inside `with self.lock:`, add one to
`self.data["views"][page][today]`, creating the inner dictionaries when they are missing, then
call `self._save()`. Restart and repeat the `path: "/"` request.
*You should see* `204`, and a new file, `data/counts.json`, with your page and today's date in it.

**6. Send the hit from every page.** In `static/count.js`, where the step 6 comment is, send
`JSON.stringify({ path: location.pathname })` to `/api/hit` with `navigator.sendBeacon`, and
fall back to `fetch` with `method: "POST"` and `keepalive: true`, catching any failure. In
`template.html`, before `</head>`, add:

```html
<script src="count.js" defer></script>
```

Rebuild, restart, and click through every page of your site.
*You should see* a `POST /api/hit 204` line after each page's `GET` line, and matching counts in
`data/counts.json`.

### Acceptance criteria, Part A

- [ ] The server log shows no address on any line, including a crash report
- [ ] An unknown page and a non-JSON body each get a 400
- [ ] Every page load in the browser adds one to that page's count for today
- [ ] `data/counts.json` contains page addresses, dates, and numbers, and nothing else
- [ ] Committed. **Do not commit `data/`.** It is your traffic, not your code. Add a line that
      says `data/` to your repository's `.gitignore`.

---

## Part B · Build 2 · 55 minutes

**7. Ask the question on every page.** In `template.html`, between `</main>` and the footer, add:

```html
<aside class="helpful" aria-labelledby="helpful-heading">
  <h2 id="helpful-heading">Was this page useful?</h2>
  <form id="helpful-form" method="post" action="/api/helpful">
    <input type="hidden" name="page" value="{{page_path}}">
    <button type="submit" name="answer" value="yes">Yes</button>
    <button type="submit" name="answer" value="no">No</button>
  </form>
  <p id="helpful-status" role="status"></p>
  <p class="small">This site counts page loads and these answers. It sets no cookies and keeps no addresses. <a href="index.html#privacy">What is counted</a></p>
</aside>
```

Add a section with `id="privacy"` to your home page content that says, in plain words, exactly
what the site counts and what it does not. Rebuild.
*You should see* the question at the bottom of every page, and the "What is counted" link
landing on your privacy section.

**8. Count the answers.** Write `add_helpful` and `_helpful` from their comments. Refuse any page
not in your list and any answer that is not `yes` or `no`. Reply 204 when the request's `Accept`
header contains `application/json`. Otherwise reply `303` with a `Location` header set to the
**page from your own list**, never a value copied straight from the request.
Restart. **Turn JavaScript off** for the site (DevTools, Ctrl+Shift+P, type "Disable JavaScript")
and click Yes.
*You should see* the page reload, `POST /api/helpful 303` in the log, and the answer in
`data/counts.json`. Turn JavaScript back on.

**9. Answer without leaving the page.** In `count.js`, where the step 9 comment is, handle the
form's `submit` event: stop the normal submission, read `event.submitter.value`, and `fetch` the
form's action with `new URLSearchParams({ page: ..., answer: ... })` as the body and the header
`Accept: application/json`. On success, disable both buttons and write
`Thanks. Your answer was counted.` into `#helpful-status`. On failure, say the answer could not be
sent.
*You should see* the thank-you sentence appear without a page reload, and
`POST /api/helpful 204` in the log.

**10. Run the tests.** `python test_counter.py`.
*You should see* `Ran 13 tests` and `OK`. If a test fails, read its name: it says what it proves.

**11. Read your numbers.** `python report.py`.
*You should see* a table with every page you loaded, its views, and its answers, and two lines at
the bottom about what a view is.

**12. Write the measurement plan.** Create `measurement-plan.md` next to `sitekit/` with three
sections: the two questions you are measuring; the exact fields you store and why each one is
needed; and at least four things your numbers cannot tell you.
*You should see* a list of stored fields that matches `data/counts.json` exactly.

### Acceptance criteria, full lab

- [ ] Everything in Part A
- [ ] The question appears on every page, from the template
- [ ] The form works with JavaScript on and with JavaScript off
- [ ] `python test_counter.py` prints `Ran 13 tests` and `OK`
- [ ] Every page still passes web-check
- [ ] `measurement-plan.md` with all three sections
- [ ] A decision log entry: one thing you chose not to collect, and what it would have told you
- [ ] Committed and pushed, without `data/`

---

## If it breaks

**1. `serve.py: error: say which port: --port 8606`**
You ran `python serve.py` with no port. Every server this week takes one.

**2. `serve.py: error: ...\site\pages.json not found. Run python build.py first.`**
There is no built site yet, or you deleted `site/`. Build first. The server counts only the pages
`build.py` listed.

**3. `NotImplementedError: add_view is step 5` at the bottom of a traceback**
Your `_hit` works and is calling a store method you have not written yet. That is step 5. If the
line above the traceback shows an address, `QuietServer` is not done.

**4. `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` in a traceback**
Your `_hit` calls `json.loads` outside the `try`, so a bad body crashes the handler instead of
getting a 400. Move the parse inside the `try` and catch `ValueError`, which `JSONDecodeError` is a
kind of.

**5. You changed `serve.py` and nothing changed.**
The running server still has the old code. Ctrl+C, then start it again. If Ctrl+C does not stop
it, close that terminal, then check with `netstat -ano | findstr 8606`.

**6. The page loads but no `POST /api/hit` line ever appears.**
Open the page from `http://127.0.0.1:8606/`, not by double-clicking the file. `count.js` does
nothing on a `file://` page, on purpose. Then check DevTools, Network tab, for `hit`.

---

## Stretch goal

Add a `--no-count` switch to `serve.py` that serves the site but refuses every hit with a 403, so
you can test your published pages without adding your own visits to the numbers. Then explain in
two sentences why a switch on the server is a better fix for "my own visits are in the numbers"
than a cookie that marks your browser.

---

## Submission checklist

- [ ] `sitekit/serve.py`, `sitekit/static/count.js`, and `template.html` changes
- [ ] `python test_counter.py` output pasted into your lab notes
- [ ] `python report.py` output pasted into your lab notes
- [ ] `measurement-plan.md`
- [ ] Decision log entry
- [ ] Server stopped. `netstat -ano | findstr 8606` prints nothing.
- [ ] Committed and pushed, `data/` not committed

---

## Extended options

All four assess 1.10.5 and 6.5.3 and are graded on the same five-dimension scale.

| What you see in the first 15 minutes of Build 1 | Hand them |
|---|---|
| Server not started by minute 10, or starts it with no port twice | SCAFFOLDED |
| Step 2 done, reading step 4 carefully | STANDARD |
| Step 5 done by minute 25 and already asking how to exclude their own visits | EXTENDED |
| Asks why anyone would build this instead of using a free analytics service | APPLIED |

### SCAFFOLDED

Your instructor gives you `_hit` and `add_view` already written. You do steps 1, 2, 4 (the
`QuietServer` part only), 6, 7, and 11. The usefulness question is shown but counted only with
JavaScript on.

**Extra checkpoints:** show your instructor the terminal after step 2, and `data/counts.json` after
step 6.

**Then answer in writing:** point at the one line in `serve.py` that would have to change for the
server to start storing addresses again.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **views by day, drawn in text.** Change `report.py` so it prints, for
each day, a bar of `#` characters scaled so the busiest day is 40 characters wide.

Then answer the harder question in writing: your bar chart makes a busy day look important. Name
two things that could make one day busy that have nothing to do with the site being useful.

*Hint, not the answer:* the scaling is one division and one `round`. Read the documentation for
`max()` with a dictionary's values before you write a loop to find the biggest day.

### APPLIED

Same skill, no website. Pick something you or a group you belong to wants to measure: whether
people use the club's shared drive folder, whether a study guide helped, whether the new locker
room sign-in sheet is read.

Write a measurement plan for it with the same three sections: the question, the fields you would
collect and why each is needed, and four things the numbers could not tell you. Then name one field
somebody would be tempted to add, and argue for and against collecting it.
