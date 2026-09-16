# Lab W01-01: Div Soup to Document
## 145010 Web Design & Senior Capstone · Week 1 · Monday, Tuesday, Wednesday

**Gate:** 3 (open), with the checkers as your reviewers. **Duration:** three Build 1 blocks,
40 minutes each. **Grade category:** Lab & Practice.
**Competencies:** 6.1.1, 6.1.3, 6.1.5, 6.2.1, 6.2.2, 6.2.3.

Files: [lab-w01-01-files/](lab-w01-01-files/). The checker you need for Parts 2 and 3 is
[structure-check/structure_check.py](structure-check/structure_check.py).

---

## The scenario

Harbor Lane Bike Kitchen is a volunteer-run repair shop, and its one volunteer who "does the
website" built the home page to look right. It does look right. A screen reader user hears no
headings and no navigation. Three links are placeholders that only jump to the top of the
page, and two more point at files that are not where the links say. **Harbor Lane is
invented.** The page is the kind of thing you will be handed at your first job.

## What you will build

The same page, looking almost the same, rebuilt so the browser has nothing to repair, every
piece of content is in the element made for it, and every link lands from where it lives.

**No CSS this week.** If the page starts to look worse, that is fine. Structure first.

---

## The starter

```
lab-w01-01-files/
  index.html              the home page, built by the volunteer
  pages/
    volunteer.html        a second page, one folder down
  files/
    tune-up-checklist.pdf the checklist people should download
```

`index.html` opens in any browser and reads fine. That is the point. Its header comment says
what each part of this lab does. Leave the comment in until Part 3 is done.

Copy the whole `lab-w01-01-files/` folder into your own repository as `lab-w01-01/` before
you change anything, and commit it untouched. Your first commit is the "before" picture.

---

## Before you start · set up the two checkers, once

**Why.** You will run both checkers after almost every change this week and next. Setting them
up takes about five minutes, once. Every command in this course runs **from the root of the
course repository**, the folder that contains `tools/` and `Courses/`.

**The page checker, `web-check`.** It needs Node.js and Chrome, which your instructor has
confirmed are on the lab machines. Its instructions are in
[tools/web-check/README.md](../../../../../tools/web-check/README.md). The setup is:

```
cd tools/web-check
npm install
cd ../..
node tools/web-check/check.js --widths 360
```

*You see:* `npm install` finishes and a `node_modules` folder appears inside `tools/web-check/`.
Never commit that folder. The last line, with no page named, prints a `usage:` line. That means
Node found the checker.

**The structure checker, `structure_check`.** It needs only Python, and there is nothing to
install:

```
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py
```

*You see:* the checker's description, starting with `structure_check.py: the checks web-check
does not make.`

**If `npm install` fails** because the network blocks it, write the exact message on the STUCK
board and do steps 1, 2, and 5 of Part 1, which need only Chrome. **If the page checker says
`No Chrome or Edge found`**, set `CHROME_PATH` as its README describes, or ask your instructor.

---

# Part 1 · Monday · What the browser built

**Why this part exists.** The browser never refuses a page. It repairs what you wrote and shows
the repair. If you only ever look at the rendered page, you never find out what it fixed, and
the next browser, the validator, and the screen reader may not fix it the same way.

1. **Copy and commit the starter.** From your repository: `git add lab-w01-01` and
   `git commit -m "Lab W01-01 starter, untouched"`.
   *You see:* `git status` reports a clean working tree.

2. **Open `lab-w01-01/index.html` in Chrome.**
   *You see:* a readable page with a title, a menu line, a bulleted list, and some paragraphs.
   Nothing looks broken.

3. **Run the validator and the audit.** From the repository root:
   `node tools/web-check/check.js <your path>/lab-w01-01/index.html`
   *You see:* `FAIL`, `validation: 21 error(s)`, and `axe at 360px: 0 violation(s)` at every
   width. Copy the first ten error lines into `notes.md`.

4. **Look at where the errors point.** Two of the 21 lines name lines 32 and 38. Two name
   lines 2 and 8, the `html` and `body` tags. Every other line names line 48 or a line after it.
   *You see:* a pattern. Write down which line you think is causing most of the list, before
   you look at it.

5. **Open DevTools on line 48's content.** Right-click "Helmets are required" and choose
   Inspect.
   *You see:* in the Elements panel, `<b><i>Helmets are required in the shop area.</i></b>`.
   Now press Ctrl+U for View Source and find line 48.
   *You see:* `<b><i>Helmets are required in the shop area.</b></i>`. The browser swapped the
   closing tags. The file did not.

6. **Fix line 48** so the tags close in the reverse order they opened. Save, rerun `web-check`.
   *You see:* `validation: 2 error(s)`. One misnested pair of tags produced 19 of the 21 errors.

7. **Inspect the Repair Night paragraph** ("Every Tuesday from 5:30...").
   *You see:* in Elements, `<p>Every Tuesday from 5:30 to 8:30 p.m. Bring:</p>`, then the
   `<ul>`, then an empty `<p></p>` that is nowhere in your file.

8. **Record what the browser built.** In `notes.md`, fill in this table for lines 32 to 38 and
   line 48:

   | Line | What the file says | What the browser built | Why |
   |---|---|---|---|

   *You see:* two rows, each with a difference you can point at.

9. **Fix lines 32 to 38.** A paragraph cannot contain a list. End the paragraph before the list
   starts, and remove the stray `</p>`. Rerun `web-check`.
   *You see:* `PASS`, `validation: 0 error(s)`, `0 violation(s)` at all three widths.

10. **Commit.** `git commit -am "Part 1: nothing for the browser to repair"`.
    *You see:* a second commit in `git log --oneline`.

### Acceptance criteria, Part 1

- [ ] `web-check` reports PASS on `index.html`
- [ ] `notes.md` has the what-the-browser-built table with at least two rows
- [ ] `notes.md` says, in one sentence, why fixing one line removed 19 errors

---

# Part 2 · Tuesday · The element that already exists

**Why this part exists.** `web-check` now says PASS. The page still has no headings, no
landmarks, and no lists, as far as any assistive technology can tell. A PASS from one checker
is not a finished page.

11. **Run the structure checker.** From the repository root:
    `python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your path>/lab-w01-01/index.html`
    *You see:* `FAIL`, `no headings at all`, `0 <main> elements`, and `7 fail, 22 warn`. Save
    the output: add `> <your path>/lab-w01-01/before-structure.txt` to the command.

12. **Replace the four landmark divs.** `div class="header"` becomes `header`,
    `div class="nav"` becomes `nav` with `aria-label="Main"`, `div class="main"` becomes
    `main`, `div class="footer"` becomes `footer`. Wrap the footer sentence in a `p`.
    *You see:* after a rerun, `LANDMARKS header x1, nav x1, main x1, footer x1`.

13. **Make the menu a list.** Inside `nav`, put the three links in a `ul`, one `li` each, and
    delete the `|` characters.
    *You see:* the menu is now a bulleted list. It looks worse. It is correct.

14. **Give the page its headings.** The big title becomes the one `h1`. Each
    `div class="section-title"` becomes an `h2`, and wrap each h2 with the content under it in
    a `section`. "What we can help you fix" becomes an `h3`, because it sits inside Repair
    Night. The site name in the header becomes a `p`, not a second `h1`.
    *You see:* the HEADINGS block shows `h1`, then four `h2`, with one `h3` indented under
    Repair Night, and no heading FAIL lines.

15. **Make the lists lists.** `div class="list"` and its items become a `ul` with `li` items.
    The three numbered steps under Donate a Bike become an `ol`. Delete the typed `1.`, `2.`,
    `3.`, because `ol` numbers them.
    *You see:* `DIVS 0 div, 0 span`.

16. **Choose between `b` and `strong`.** The helmet sentence is a rule, not a style. Change
    `<b><i>` to `<strong>` and delete the `i`.
    *You see:* the sentence is bold. Nothing else changed on screen.

17. **Check the accessibility tree.** In DevTools, open the Elements panel, then the
    Accessibility tab, and turn on **Show accessibility tree**. The Elements panel now shows the
    whole page as assistive technology receives it.
    *You see:* `banner`, `navigation "Main"`, `main`, and `heading ... level 1`. On the starter
    you would have seen only text.

18. **Run both checkers and commit.**
    *You see:* `web-check` PASS. `structure_check` still FAIL, now with `5 fail, 3 warn`, every
    one of them about links. `git commit -am "Part 2: landmarks, headings, lists"`.

### Acceptance criteria, Part 2

- [ ] `structure_check` reports no HEADINGS, LANDMARKS, or DIVS problems
- [ ] `web-check` still reports PASS
- [ ] `before-structure.txt` is committed
- [ ] Nothing on the page is a `div`

---

# Part 3 · Wednesday · Every link lands

**Why this part exists.** A relative link is resolved from the folder the page lives in, not
from where you are standing. A link that works on your machine can break the moment the file
moves, and a `#` link breaks without any error at all.

19. **Give the sections ids.** `repair-night`, `donate`, `before`, `questions`. Point the two
    `#` menu links at `#repair-night` and `#donate`.
    *You see:* clicking Repair Night in the menu scrolls to that section. Two ANCHORS failures
    are gone.

20. **Fix the Volunteer link.** The page is in `pages/`. Change the link to
    `pages/volunteer.html`.
    *You see:* clicking it opens the volunteer page. One FILES failure is gone.

21. **Fix the way back.** Open `pages/volunteer.html` and run `structure_check` on it.
    *You see:* `FAIL FILES line 33: <a href="index.html"> points at a file that is not there`.
    From inside `pages/`, the home page is one folder up. Change it to `../index.html`.

22. **Give the volunteer page a menu** in its header, with the same three destinations. From
    `pages/`, Repair Night is `../index.html#repair-night`, and the Volunteer link points at
    `volunteer.html`, the page itself. Add `aria-current="page"` to that link.
    *You see:* `structure_check` on `pages/volunteer.html` reports PASS. It checked that the
    `#repair-night` id exists inside `../index.html`.

23. **Fix the download.** The PDF is in `files/`. Point the link at
    `files/tune-up-checklist.pdf`, add the `download` attribute, and rewrite the sentence so the
    link text says what the file is, its type, and its size. Find the size with `dir files` in
    `cmd` or `ls -l files` in Git Bash.
    *You see:* the file is 2,153 bytes. `structure_check` prints
    `download link hands people a .pdf file` with your link text in it.

24. **Rewrite the two "click here" links.** The link text for the safety site is the name of
    the organization. The email link is next.
    *You see:* no `link text ... says nothing out of context` warnings.

25. **Make the email link.** `mailto:hello@harborlanebikes.example`, with the address itself as
    the link text.
    *You see:* `structure_check` prints `email link to hello@harborlanebikes.example`. Read the
    rest of that line out loud.

26. **Run both checkers on both pages, save the evidence, and commit.** Put the final output of
    each in `lab-w01-01/evidence/`.
    *You see:* four PASS lines. `git commit -am "Part 3: every link lands"`.

### Acceptance criteria, Part 3

- [ ] `web-check` PASS on both pages at 360, 768, and 1280
- [ ] `structure_check` PASS on both pages, zero FAIL lines, zero WARN lines on `index.html`
- [ ] The menu reaches every section it names, from both pages
- [ ] The download link names the file type and the size
- [ ] No link text says "here" or "click here"

---

## If it breaks

**1. "I fixed the first error and there are still 20."** The validator reports in file order,
not in order of importance. One unclosed tag makes everything after it look wrong. Look for the
line most errors point at or after, which here is line 48.

**2. The link opens a page that says `ERR_FILE_NOT_FOUND`.** Chrome shows that code when a
`file://` link points at a file that is not there. The path is resolved from the folder the
page is in. Count the folders: from `pages/volunteer.html`, `index.html` means
`pages/index.html`, which does not exist. You want `../index.html`.

**3. The menu link does nothing useful when you click it, and there is no error anywhere.**
If the link is `href="#"`, it is a placeholder that jumps to the top of the page, and
`structure_check` calls it one. Otherwise the `href`
after the `#` does not exactly match an `id`. `#repair-night` and `id="repairnight"` do not
match, and neither do `#Donate` and `id="donate"`. `structure_check` reports it as
`#... has no element with id="..." on this page`.

**4. `structure_check` says `h2 jumps to h4` or `the first heading is h2`.** You picked a
heading because of its size. Heading levels describe the outline. Size is next week's CSS. Go
back to one `h1`, sections at `h2`, and things inside a section at `h3`.

**If you serve the folder with a local server instead of opening the file,** a missing page
comes back as `Error code: 404` and `Message: File not found.` from Python's `http.server`.
Same cause, same fix. Always give the server a port: `python -m http.server 8150`, and stop it
with Ctrl+C when you are done.

---

## Stretch goal

Add a "Back to the top" link in the footer of `index.html` that works with no `id` added
anywhere. Then find out why it works, in the HTML specification or on MDN, and write the one
sentence of explanation in `notes.md` with the name of the page you read.

---

## Submission checklist

- [ ] `lab-w01-01/` has `index.html`, `pages/volunteer.html`, and `files/tune-up-checklist.pdf`
- [ ] `notes.md` with the what-the-browser-built table and the one-sentence explanation
- [ ] `before-structure.txt` from Part 2
- [ ] `evidence/` with the final output of both checkers
- [ ] Four commits: starter, Part 1, Part 2, Part 3
- [ ] Pushed
- [ ] An AI usage log entry if you used a model at any point

---

## Extended options

Choose one with your instructor. All four assess the same competencies and are graded on the
same scale.

### Three observable signals for choosing

| What you see in the first 15 minutes of Part 1 | Give them |
|---|---|
| Still trying to fix the first validator error in order, error by error | SCAFFOLDED |
| Found line 48 by reading where the errors point, and is filling in the table | STANDARD |
| Finished Part 1 and asks why Chrome swapped the tags rather than dropping one | EXTENDED |
| Says the bike page has nothing to do with anything they will build | APPLIED |

### SCAFFOLDED

Same page, same three parts, smaller steps. Your instructor marks the two misnested lines in
the starter before you start, so Part 1 is finding what the browser built for each, not
finding the lines.

In Part 2, do the landmarks first and run `structure_check`, then the headings and run it
again, then the lists and run it again. Three runs, three saved outputs, so you can see each
change do its job.

**Extra checkpoints:** show your instructor after step 9, step 14, and step 21.

**Then answer one question in writing:** `web-check` passed at the end of Part 1 and the page
still had no headings. What does a PASS from `web-check` actually tell you?

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **the browser's repair rules**. Browsers do not repair bad markup
by guessing. The HTML specification defines exactly what a parser does with misnested
formatting tags, and the procedure has a name.

Write three small test files of your own, each with a different misnesting you predict the
browser will repair differently: formatting tags crossed over each other, a block element
inside a paragraph, and a table row outside a table. Predict the repaired DOM for each in
`notes.md`, then check each prediction in the Elements panel and record where you were wrong.

*Hint, not the answer:* search the WHATWG HTML specification's parsing section for the
algorithm that handles formatting elements. The name of the algorithm is the thing to find.
The specification is at `https://html.spec.whatwg.org/multipage/`.

### APPLIED

Same skill, your own domain. Find a page you use: your job's schedule page, a club's page, a
game wiki, a school page. **Only a page you are allowed to save, and never one behind a login.**
Save a copy with Ctrl+S.

Run both checkers on your copy. Pick the five problems that would matter most to a person using
a screen reader or a phone, fix them in your copy, and write a `findings.md` with the before
and after output and one sentence per fix on who it helps. Do not publish your copy anywhere.
It is somebody else's work.

**Then answer the question this lab is really about:** the page you picked was built by
professionals, and it still had problems a free script found. Why do you think they are still
there?
