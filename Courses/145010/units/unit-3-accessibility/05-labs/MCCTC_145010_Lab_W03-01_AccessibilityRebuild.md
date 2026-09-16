# Lab W03-01 · The Accessibility Rebuild
## 145010 Web Design & Senior Capstone · Week 3 · Tuesday through Friday

**Files:** `lab-w03-01-files/`
**Time:** Tuesday Build 2 (audit, first half). Wednesday Build 2 (audit, second half). Thursday Build 1
and Build 2 (rebuild, keyboard walk, partner test). Friday Build 2 (screen reader walkthrough and
recording).
**Grade:** the audit log is Lab & Practice. The rebuilt page and the walkthrough evidence are the Week 3
project, scored on the 100-point project rubric in
`09-project/MCCTC_145010_Project_W03_AccessibilityRebuild.md`.
**Competencies:** 6.1.2 (plan a page considering audience, devices, color, links, graphics, and ADA
requirements), 2.7.4 (how browsers and devices, text-to-speech, and screen readers affect a page),
6.5.10 (develop and execute usability tests for accessibility, ease of use, and navigation).

---

## About this page, before you start

**Lantern Street Community Pantry is invented.** The page, the people, and the shifts are made up for
this class, and any real pantry with a similar name is a coincidence. The situation is a composite of
a very common one: a small organization, a volunteer who built the site on a weekend, and a page that
looks finished.

Every problem in it was planted on purpose, and every one of them is checkable.

---

## The scenario

A community pantry recruits teen volunteers through this page, and a volunteer who uses a screen
reader told the coordinator she could not sign up. The coordinator looked at the page, saw nothing
wrong, and asked for help. Your job is to find out what that volunteer ran into, write it down in a
form someone else can check, and rebuild the page so she can sign up.

## What you will build

An audit log naming every problem you can find with the WCAG success criterion it fails, a rebuilt
page that passes `web-check` with zero errors at three widths, and a recorded keyboard and screen
reader walkthrough proving a person can use it.

---

## Why this is not optional

**This is a legal requirement, not a courtesy.** The Americans with Disabilities Act applies to the
services of state and local governments and of businesses open to the public, and the U.S. Department
of Justice says that includes what they offer on the web. Its own guidance names WCAG as a standard
to use. Monday's lecture notes explain this at the level you need, and where to look for the current
rules. Your instructor is not a lawyer and nothing in this lab is legal advice.

There is a second reason, and it is the one you will remember. The person who cannot use this page
is not hypothetical. Some of the people who will use every site you ever build navigate with a
keyboard, a screen reader, a magnifier, or voice control. If you only ever test with a mouse and your
own eyes, you are only testing for people like you.

---

## What is in the folder

| File | What it is |
|---|---|
| `index.html` | **The page you audit.** It looks fine. It is not |
| `thanks.html` | Where the form goes. It saves nothing |
| `logo.svg`, `calendar-icon.svg`, `hours.svg`, `entrance-map.svg` | The images the page uses |
| `shifts.ics` | A calendar file with one invented shift |
| `audit-log-template.md` | Copy it. It is your audit |
| `walkthrough-checklist.md` | Copy it. It is your Part D record |

**Copy the whole folder into your repository** as `week3-rebuild/`. Commit the untouched starter
first, with the message `Starter page before audit`. Your rebuild is graded partly on the diff between
that commit and your last one.

---

# Part A · The page

Open `index.html` in Chrome. Scroll it. Try the form with the mouse. It works. Nothing about it looks
wrong, and that is the point of the exercise.

**Do not start fixing anything yet.** An audit that fixes as it goes loses the record of what was
wrong, and the record is half of what you are graded on.

---

# Part B1 · The audit · Tuesday Build 2 and Wednesday Build 2

**Minimum: twelve problems logged, at least six of which web-check did not report.** There are more
than twenty in this page. Twelve is a passing audit. Eighteen is a strong one.

You work in four passes. **The order matters.** The tool pass comes first so you know what a machine
can see, and the three human passes come after so you find what it cannot.

## Pass 1 · The tool pass · 10 minutes

1. Run the checker on your copy from the repository root:

   ```
   node tools/web-check/check.js week3-rebuild/index.html
   ```

   **You see** `FAIL`, a list of validation errors, and a list of axe violations at 360, 768, and
   1280 pixels.

2. Paste the complete output into Pass 1 of your audit log.

   **You see** that the three widths report the same rules. Write down how many distinct axe rules
   there are, not how many lines.

3. Add a row to your log for each distinct problem the tool reported. Find the line in `index.html`
   that causes each one.

   **You see** some rows where one tool message points at several places. `color-contrast` lists
   three elements. That is one row with three line numbers.

**Warning.** One validation error in the list is about HTML structure and is not an accessibility
failure by itself. Decide which one and say so in its row.

## Pass 2 · The structure and names pass · 25 minutes

Open DevTools with F12. In the Elements panel, find the **Accessibility** pane. It shows what the
browser hands a screen reader for the element you have selected: its role, its name, and its state.
Chrome's documentation describes it as: Elements panel, select the element, then the **Accessibility**
tab, where a **Show accessibility tree** toggle shows the whole tree. **[VERIFY]** the exact location in
your version of Chrome; your instructor shows it on Tuesday.

4. Select every image. Read the name the accessibility tree gives it.

   **You see** four images. For each, ask: if this were read aloud and the image were gone, would I
   know what it showed? A name that exists is not the same as a name that helps.

5. Select every form field. Read its name.

   **You see** that some fields have a name even though they have no `<label>`. Find out where that
   name came from, and ask what a sighted person sees once they start typing.

6. Write down every heading on the page, in order, with its level. Then find every piece of text that
   **looks** like a heading.

   **You see** two lists that do not match.

7. Find the table. Select a data cell and read what the tree says about its column.

8. Find every link. Write down what each one says **with nothing around it**, the way a screen reader
   user hears it in a list of links.

9. Read the text on the page as if you could not see colour. Which sentences stop making sense?

10. Find the sentence that is not in English. Check what `lang` it is marked with.

## Pass 3 · The keyboard pass · Wednesday, 15 minutes

11. Put the mouse out of reach. Reload. Press Tab, slowly, and write down where focus goes each time.

    **You see** something unexpected on the very first press, and you may not be able to see where
    focus is at all. Write both down.

12. Keep pressing Tab until you reach the phone field. Type your area code and press Tab again.

    **You see** that you cannot leave. Write down exactly what happens. Do not refresh until you have
    tried Shift+Tab too. Then click away with the mouse to escape.

13. Click once in the Shift list to get past the trap, then keep pressing Tab. Try to reach the Sign up
    button with the keyboard.

    **You see** where focus goes after the Yes choice. Write down whether Sign up was ever in the order.

14. Read the viewport `<meta>` tag in the `<head>`. Write down, in plain words, what
    `maximum-scale=1, user-scalable=no` asks a phone browser to do, and who that hurts.

## Pass 4 · The reading pass · 10 minutes

15. Read the `<head>`. What would a person with twelve tabs open see for this page's title?

16. Read the `<style>` block top to bottom. Several lines in it are accessibility problems on their
    own, and at least one of them is something the tool never mentioned.

17. Read the `<script>` block. You have not studied JavaScript in this course yet. You do not need to.
    Read the comment, then read the line that says `preventDefault`, and connect it to step 12.

### Acceptance criteria, Part B1

- [ ] Pass 1 output pasted complete and unedited
- [ ] At least twelve problems logged, at least six marked `me`
- [ ] Every row has a line number, a person it stops, and a WCAG 2.2 criterion written as a number and
      a name, or `no WCAG criterion found` with a reason
- [ ] The summary answers all four questions
- [ ] Committed with the message `Audit complete` **before** you change `index.html`

---

# Part B2 · The rebuild · Thursday Build 1 and the first 20 minutes of Build 2

Now fix it. **The rules:**

- **Keep what it looks like.** The coordinator likes the design. Your rebuild should look like the
  same page to a sighted mouse user, with the colour changes that contrast forces on you.
- **Use the element that already does the job.** A real `<button>`, a real `<label>`, a real
  `<header>`. If you find yourself writing `role=` or `tabindex=`, stop and ask whether an HTML element
  already does it.
- **No JavaScript is required.** The rebuilt page needs no script at all. If you keep one, it must
  not touch the Tab key.
- **Every row in your audit log gets fixed or gets a written reason.**

18. Work through your log top to bottom. After every three or four fixes, rerun the checker.

    ```
    node tools/web-check/check.js week3-rebuild/index.html
    ```

19. When the checker passes, run it at the three required widths explicitly and save screenshots
    to a folder one level above your repository, so they never get committed:

    ```
    node tools/web-check/check.js week3-rebuild/index.html --widths 360,768,1280 --shots ../w03-shots
    ```

    **You see** `PASS`, `validation: 0 error(s)`, and `0 violation(s)` at all three widths, with no
    `OVERFLOWS` line. Open the three screenshots and look at them.

20. Commit with the message `Rebuild passes web-check`.

**Read this before you celebrate.** A pass from web-check means the tool found nothing it knows how
to look for. Most of your audit log is things it does not know how to look for. Parts D1 through D3
are how you find out whether the page works.

### Acceptance criteria, Part B2

- [ ] `web-check` exits 0 at 360, 768, and 1280
- [ ] Every audit row is fixed or carries a written reason
- [ ] The page looks like the same page
- [ ] No positive `tabindex`, no `outline: none` without a replacement, no script touching Tab

---

# Part D · The human component · Thursday Build 2 and Friday Build 2

Use `walkthrough-checklist.md`. **Part C is your instructor's key. You do not get it.**

## D1 · Keyboard only · Thursday, 15 minutes

21. Put the mouse out of reach. Work through checks K1 to K10 on your rebuilt page. Record the tab
    count to the Sign up button.

## D3 · Partner usability test · Thursday, 20 minutes

22. Swap with the person your instructor pairs you with. They do tasks T1 to T3 on **your** page with
    the keyboard only, while you read each task aloud once and then say nothing. Then you do theirs.

    **You see** at least one place where your partner hesitates on something you thought was
    obvious. Write it down. That hesitation is the finding.

23. Make the one change the test told you to make. Rerun web-check. Commit.

## D2 · Screen reader · Friday, after the quiz

24. Headphones on, volume low. Start Narrator with Ctrl + Windows key + Enter. Work through checks S1
    to S10.

25. Record the walkthrough described in the checklist. Browser window only. Two to four minutes.

26. Stop Narrator with Ctrl + Windows key + Enter. **Check that it has stopped** before you take the
    headphones off, or the next person at that machine gets a surprise.

27. Commit `audit/walkthrough.md` with the message `Walkthrough recorded`. Submit the video where your
    instructor says. Never commit it.

### Acceptance criteria, Part D

- [ ] K1 to K10 filled in, with a tab count
- [ ] S1 to S10 filled in, with what you heard
- [ ] T1 to T3 filled in **by your partner**, with times, and one change made because of it
- [ ] Recording submitted, or a listening log written by your partner, and the record says which

---

## If it breaks

**1. `label (critical, 1 node(s))  Form elements must have labels  e.g. #volunteer-email`**
You wrote a `<label>`, and the checker still says the field has none. The `for` on the label does not
match the `id` on the input, character for character. A label pointing at an id that does not exist
labels nothing.

**2. `wcag/h37  <img> is missing required "alt" attribute`**
You decided an image was decorative and deleted its `alt`. Decorative images keep the attribute and
leave it empty: `alt=""`. No attribute at all tells a screen reader nothing, and many will read the
file name instead.

**3. `axe at 360px: 0 violation(s), OVERFLOWS by 216px`**
Something is wider than a phone. In the rebuild it is almost always the table after you added a
column, or a cell with `white-space: nowrap`. Let the text wrap. The page is failing people on phones
even though every accessibility rule passed.

**4. `hidden-focusable  aria-hidden cannot be used on focusable elements (hidden by ancestor element)`**
You put `aria-hidden="true"` on something that contains links or fields. That hides them from a
screen reader while the keyboard can still land on them, so a screen reader user tabs into silence.
Remove `aria-hidden`. In this page you need it nowhere.

**And the one with no error message at all.** Narrator reads the Spanish sentence in an English voice
and it sounds like nonsense. Nothing fails. The checker cannot hear it. Check `lang` on that paragraph.

---

## Stretch goal

Open the rebuilt page at 400 percent zoom on a laptop. Can you still use the form without scrolling
sideways? Write down what you find. The success criterion is 1.4.10 Reflow. Look it up on the W3C
site and say whether your page meets it.

---

## Submission checklist

- [ ] `week3-rebuild/` in your repository, with the untouched starter as its first commit
- [ ] `audit/audit-log.md` committed before any fix, with the message `Audit complete`
- [ ] Rebuilt `index.html` passes `web-check` at 360, 768, and 1280
- [ ] `audit/walkthrough.md` with D1, D2, and D3 complete
- [ ] Recording submitted where your instructor said, not committed
- [ ] AI usage log entry if you used a model at any point. **Never paste the page or anyone's name
      into one to ask what is wrong with it.** The audit is the assignment
- [ ] Pushed at the end of every period this week

---

## Extended options

All four versions produce the same three things, an audit log, a page that passes web-check, and a
human walkthrough, and all four are graded on the same rubric.

### Choosing a version, three signals

| What you see by the end of Tuesday Build 2 | Version |
|---|---|
| Fewer than four rows logged, or the student is still reading the tool output line by line | SCAFFOLDED |
| Six or more rows, with WCAG numbers and names, and at least one row marked `me` | STANDARD |
| Ten or more rows before the keyboard pass, and asking about things the checklist does not mention | EXTENDED |
| The student asks where this shows up outside a school web page, or is on a team building a WPF panel or a kiosk | APPLIED |

### SCAFFOLDED

Same target, more structure, smaller scope. Your instructor gives you a list of the **ten line
numbers** to look at, without saying what is wrong at any of them. Log those ten. Then rebuild only
the header, the form, and the table; the rest of the page may stay as it was, as long as web-check
passes.

**Extra checkpoints.** Show your instructor your log after Pass 1, after Pass 2, and before you start
the rebuild. D1 and D2 are the same as STANDARD, because the human component is not optional for
anyone.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, and then two things this lab does not teach.

1. **Add a sign-up confirmation that a screen reader announces without the user moving focus.** The
   form stays on the page, and a message appears saying the sign-up was received. That needs a small
   script, which is Week 4 material, and an ARIA live region, which is not taught in this course.
   *Hint, not the answer:* read the MDN page on ARIA live regions, and find out why the region has to
   exist on the page **before** the message is put into it.
2. **Meet 1.4.10 Reflow and 1.4.12 Text Spacing** and prove both with a screenshot. Read the W3C
   Understanding document for each first. It says what the criterion requires and how to test it.

### APPLIED

Same skill, a different surface. Pick one interface **you did not build** and that you use every week:
the self-checkout at a store, a transit or school app, a game's settings menu, the WPF operator panel
you built in an earlier course. You do not need permission to use it, and you do not change anything in it.

Run passes 2, 3, and 4 on it as far as the platform allows: can you operate it without the pointer,
does it tell you where you are, does it rely on colour alone. Log at least eight findings with the
WCAG criterion each would fail **if the interface were a web page**, and write half a page on which
criteria translate to a non-web interface and which do not.

You still do Parts B2 and D on the Lantern Street page. The APPLIED audit replaces Part B1 only.
