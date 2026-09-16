# Lab W06-03: Valid, Tested, Live
## 145010 Web Design · Unit 6 · Week 6, Wednesday and Thursday

**Gate:** 3 (open). Full tooling, decision log entry required. **Duration:** Wednesday Build 1
(Part A, 40 minutes) and Build 2 (Part B, 55 minutes). Thursday Build 1 after the quiz (Part C,
25 minutes) and Build 2 (Part D, 55 minutes).
**Competencies:** 6.5.1 web standards and protocols (W3C, HTML5) · 6.5.11 cross-platform and
cross-browser compatibility and validation · 6.5.5 selecting an IDE · 6.5.12 publish a site to a web
server · 6.5.14 search engine optimization · 1.4.8 electronic communication and network etiquette.

**Notes for this lab:** `03-lecture-notes/MCCTC_145010_Notes_TheBrowserForgives.md` (Parts A and
B) and `03-lecture-notes/MCCTC_145010_Notes_LiveAndFindable.md` (Parts C and D).

---

## The scenario

A club page that looks finished has nine problems a browser quietly repaired, and your own site
may have some too. Before anything goes public, it has to be valid, tested in more than one engine,
and checked the way a visitor and a crawler will meet it. Then it goes live, and you tell three
people where to find it, in a message you would be comfortable having forwarded.

## What you will build

A site with zero validation errors, a written cross-browser test, a published address that passes
a crawl check, and three launch messages.

---

## Starter files

From `05-labs/lab-w06-03-files/`:

| File | What it is |
|---|---|
| `looks-fine/club.html`, `club.css`, `shop.svg` | A page that looks finished and is not. Part A. |
| `crossbrowser-matrix.md` | The matrix you fill in by hand. Part B. |
| `check_site.py` | Copy into `sitekit/`. Checks a running site: links, sitemap, robots.txt, titles, descriptions. Parts C and D. |

---

## Part A · Wednesday Build 1 · 40 minutes · zero errors

**Set up your editor first, five minutes.** In VS Code: open the Problems panel (Ctrl+Shift+M),
turn on Format On Save in Settings, and, if your lab machine has an HTML validation extension,
turn it on. Write one sentence in your lab notes: which of these would have caught a mistake you
made in Weeks 1 to 5.

**1. Look before you check.** Open `looks-fine/club.html` in Chrome. Write down everything you think
is wrong with it.
*You should see* a page most people call finished. One card may look slightly off.

**2. Check it.** From the repository root:

```
node tools/web-check/check.js <path to>/looks-fine/club.html
```

*You should see* `FAIL`, `validation: 9 error(s)`, and one axe violation, `image-alt`, at each of
the three widths. Compare the list with what you wrote in step 1.

**3. Find the repairs.** Open DevTools, Elements panel. For each of these, write what the browser
built and how it differs from the file: the list under "Here is what happens every week", the first
card, the shop map link's `href`, and what `#roles` would scroll to.
*You should see* at least one empty `<p></p>` that is not in the file, and `href="shop"`.

**4. Fix the file, not the page.** Edit `club.html` until web-check passes. Keep the page looking
the way it looked. If you remove an element that was doing visual work, replace that work with CSS
in `club.css`. Give the image alt text that says what the floor plan shows.
*You should see* `PASS`, `validation: 0 error(s)`, and `0 violation(s)` at all three widths.

**5. Now your own site.** Rebuild your sitekit and run web-check on every page in `site/`. Fix
every error in `content/` or `template.html`, never in `site/`.
*You should see* `PASS` for every page.

### Acceptance criteria, Part A

- [ ] `club.html` passes web-check, and still looks the way it did
- [ ] Your lab notes have the step 1 guesses, the step 3 repairs, and the editor sentence
- [ ] Every page of your site passes web-check
- [ ] No file in `site/` was edited by hand
- [ ] Committed

---

## Part B · Wednesday Build 2 · 55 minutes · the cross-browser matrix

Copy `crossbrowser-matrix.md` next to your `sitekit/`. Serve your site:

```
python serve.py --port 8606
```

**6. Name your engines.** Open every browser on the lab machine. Find each one's version on its About
page. Fill in the engines table.
*You should see* at least two browsers. Count the **engines**, not the browsers, and write the
number.

**7. Test, by hand, in visible windows.** Fill at least eight rows. Rows 3 (keyboard only) and 6
(the usefulness question) are required in every browser you have. Use DevTools device mode, or
resize the window, for the widths.
*You should see* your own observations in every "What I saw" cell. "Looks good" is not an
observation. "Nav wraps to two lines, nothing cut off" is.

**8. Say what you could not test.** Safari's engine does not run on Windows. Name it, and anything
else you could not reach: a real phone, a screen reader, an older browser version.
*You should see* at least one item in that section.

**9. Find one difference.** Look for anything that behaves differently between your engines: a form
control, focus outlines, the video controls, font rendering. Write it down. If you find none, say
which check came closest and why you think it matched.

### Acceptance criteria, Part B

- [ ] Engines table complete, with the number of engines stated honestly
- [ ] At least eight rows, both required rows present for each browser
- [ ] "Could not test" section names Safari
- [ ] One difference, or an honest "closest" answer
- [ ] Server stopped. Committed.

---

## Part C · Thursday Build 1, after the quiz · 25 minutes · publish locally and check

**10. Serve it as a static host would.** From `sitekit/`:

```
python -m http.server 8606 --bind 127.0.0.1 --directory site
```

Visit `/`, `/Layout.html` with a capital L, and `/about.html`.
*You should see* 200, 200, and 404. Write one sentence on why the capital-L address might not work
once published.

Stop it. Then run your own server on the same port:

```
python serve.py --port 8606
```

**11. Write robots.txt.** Create `static/robots.txt`:

```
# Every crawler may read every page.
User-agent: *
Disallow:

Sitemap: https://portfolio.example/sitemap.xml
```

Rebuild and restart.
*You should see* `http://127.0.0.1:8606/robots.txt` in the browser, and `sitemap.xml` beside it.

**12. Check it like a crawler.** Copy `check_site.py` into `sitekit/`. In a second terminal:

```
python check_site.py http://127.0.0.1:8606 --as https://portfolio.example
```

*You should see* `No problems found.` Fix anything it reports, rebuild, restart, and run it again.

**13. Break it on purpose.** Change `Disallow:` to `Disallow: /`, rebuild, restart, and check again.
*You should see* `PROBLEM  robots.txt tells every crawler to stay out of the whole site (Disallow: /)`.
Put it back.

### Acceptance criteria, Part C

- [ ] `check_site.py` prints `No problems found.` for your running site
- [ ] Your lab notes have the step 10 sentence and the step 13 output
- [ ] Committed

---

## Part D · Thursday Build 2 · 55 minutes · publish for real

Your instructor tells you which route you are using. **Do not sign up for any service on your own.**

**14. Set your real address.** Put your published address in `site.json` as `base_url` and in the
`Sitemap:` line of `static/robots.txt`. Rebuild with `--strict`.
*You should see* your address in every `<loc>` in `site/sitemap.xml`.

**15. Publish.**

**Lab route (always available).** On your lab machine:

```
python serve.py --port 8606 --host 0.0.0.0
```

Your address is `http://<your lab machine's network address>:8606/`. Your instructor tells you how
to find that address on the lab network. **If Windows shows a firewall prompt, stop and call your
instructor.** That prompt is a security setting and it is not yours to decide. **[VERIFY]**

**Static host route: Cloudflare Pages. [VERIFY every step with your instructor.]** The general
shape: your instructor's account or a school-approved account creates a project, the contents of
`sitekit/site/` are uploaded or connected from your repository, and the host gives the site an
address. A static host runs none of your Python, so **your counter does not work there**. If you use
this route, run `serve.py` on the lab route as well for the counts, and say so in your report.

**Program host route: Render. [VERIFY every step with your instructor.]** The general shape: a web
service is created from your repository, with a start command that runs
`python serve.py --host 0.0.0.0` and a port the host supplies. `serve.py` reads the `PORT`
environment variable when it is set. Ask your instructor whether the service keeps files between
restarts. If it does not, your counts reset whenever it restarts, and your report must say so.

This lab does not state any host's prices, age rules, limits, or sign-up requirements, because
none of them could be checked when it was written. Your instructor confirms them.

*You should see* your home page open **on a classmate's machine**, at your address.

**16. Check the live site.**

```
python check_site.py <your published address> --as <your published address>
```

*You should see* `No problems found.`

**17. Send three launch messages.** Through the class channel your instructor names, to three
classmates. Each message says what the link is, what the site counts, one thing to try, and makes
"no" an acceptable answer. Paste all three into your lab notes.
*You should see* three different messages, each under 80 words, none of them a bare link.

**18. Watch for real traffic.** `python report.py --url <your address>`, or `python report.py` on
the machine running `serve.py`.
*You should see* at least one view that was not yours by the end of Period 8.

### Acceptance criteria, Part D

- [ ] A classmate opened your site from their own machine
- [ ] `check_site.py` passes against the live address
- [ ] Three launch messages in your lab notes
- [ ] At least one counted view that was not yours
- [ ] Decision log entry: which route you used, and what it cost
- [ ] Server running through Period 8, then stopped. Committed and pushed.

---

## If it breaks

**1. `Cannot reach http://127.0.0.1:8606. Is the server running on that port?`**
`check_site.py` found no server. Start `serve.py` in another terminal, on the same port.

**2. `PROBLEM  sitemap.xml: 'https://portfolio.example/' is not a full address under https://jordan.example`**
The address in `--as` and the one in `site.json` differ. Decide which is right, fix the other,
rebuild, restart.

**3. `PROBLEM  sitemap.xml: HTTP 404`**
`site.json` has no `base_url`, so `build.py` wrote no sitemap. It also printed a warning you
scrolled past.

**4. `PROBLEM  2 pages share the description '...': /document.html, /layout.html`**
Two content files have the same description. Fix one, rebuild, restart.

**5. `POST /api/hit` gives `501` and the message `Unsupported method ('POST').`**
You are running `python -m http.server`, which serves files and runs no code. Stop it and run
`serve.py`.

**6. A classmate cannot reach your lab address.**
Check you started with `--host 0.0.0.0`, not the default. Check the address and port you sent. If
both are right, the lab network or firewall is blocking it: tell your instructor, and do not change
security settings yourself.

---

## Stretch goal

Add a `404.html` page, generated from the template like every other page but left out of the nav
and the sitemap, and make `serve.py` send it with a 404 status for any address that does not exist.
Then explain why a 404 page should still have the nav on it.

---

## Submission checklist

- [ ] Fixed `club.html` and `club.css`
- [ ] `crossbrowser-matrix.md` complete
- [ ] `static/robots.txt`, `site.json` with your real address, and a `--strict` build
- [ ] Lab notes: step 1, step 3, editor sentence, step 10, step 13, three launch messages, `check_site.py` output against the live address
- [ ] Decision log entry
- [ ] Committed and pushed

---

## Extended options

All four assess 6.5.1, 6.5.11, 6.5.12, and 6.5.14 and are graded on the same five-dimension scale.

| What you see | Hand them |
|---|---|
| Part A step 4 still failing at minute 25 of Build 1, and fixing errors in a different order than the checker lists them | SCAFFOLDED |
| Step 4 passes by minute 25, step 5 under way | STANDARD |
| Everything in Part A passes by minute 20 and they are asking about Safari | EXTENDED |
| Says "our site is not going public, why does a crawler matter" | APPLIED |

### SCAFFOLDED

Part A: fix the nine errors in the order the checker lists them, one at a time, running web-check
after each fix. Your instructor gives you a card that names the rule for each error. Part B: five
rows instead of eight, keeping both required rows. Parts C and D as written.

**Extra checkpoints:** web-check after every fix in step 4, and `check_site.py` before step 14.

**Then answer in writing:** which of the nine errors would a visitor have noticed, and which would
never have been noticed by anyone?

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **a third engine.** Find a WebKit browser: a classmate's or family
member's iPhone, or a Mac. Have its owner open your published site and check rows 1, 3, and 6 while
you watch. Record what you saw. Do not install anything on anyone's device.

Then answer in writing: your site passed in Blink and Gecko. What made you confident, or not, that
it would pass in WebKit before you tried?

*Hint, not the answer:* MDN's reference pages for CSS properties end with a browser compatibility
table. Look up the three newest CSS features your stylesheet uses.

### APPLIED

Same skill, different setting. Your school's intranet, a club's shared page, or an internal tool at
a workplace is not meant for search engines. Write a one-page publishing checklist for a site that
**should not** be listed in search results, and explain what `robots.txt` does and does not do for
it. Then say what actually keeps a page private, if `robots.txt` does not.
