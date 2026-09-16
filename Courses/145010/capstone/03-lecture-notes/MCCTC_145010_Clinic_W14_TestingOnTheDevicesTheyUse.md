# Clinic · Testing on the Devices They Use
## 145010 Senior Capstone · Clinic · Week 14, Thursday

**The signal:** test plans whose platform cases say "passes the validator" with no output, or that
were only ever run on the student's own laptop in one browser. Today you run a practice pass of your
test plan against the release candidate, before Friday's recorded run.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The reports and measurements
below are real output from the build machine, on a small example page; file paths are shortened to
the file name. **Nothing was checked by hand there**: no phone, no zoom control, no screen reader.
Those steps are procedures for you, marked where they could not be verified.

**Competencies:** 6.5.11 (cross-platform and cross-browser compatibility and validation), 6.5.13
(integrate responsive design), 2.12.3 (test cases that include targeted platforms and device types),
2.7.4 (how browsers and devices, including screen readers and mobile versus desktop, affect a page)

**The example page belongs to the Northside Community Garden, an invented organization.**

---

## The idea in plain language

**Your stakeholder's users do not use your laptop.** They use a phone, an old office computer, a
different browser, a zoomed-in screen, or a keyboard instead of a mouse. Your test plan's section 2
names those platforms. Today you test on them, and write down which ones you could not reach.

There are two layers:

1. **The automated layer.** web-check at 360, 768, and 1280 wide. It catches invalid markup, many
   accessibility rule failures, and sideways overflow. How to read its report is in the Week 12
   clinic, [Reading a Web-Check Report](MCCTC_145010_Clinic_W12_ReadingAWebCheckReport.md).
2. **The human layer.** A keyboard-only pass, zoom to 200 percent, a real phone, a second browser,
   and a screen reader on one screen. These find what the tool cannot.

## Why it exists

A page tested in one browser at one width has been tested on one platform. **The example below passes
web-check at every width and still traps a keyboard user, hides text on a phone, and hides focus.**
Each of those would surface next week in front of a participant, or in Week 16 in front of your
stakeholder.

---

## Worked example 1 · a page that passes web-check

The garden's "log your hours" page. The parts that matter:

```html
<style>
  .notice { height: 4rem; overflow: hidden; border: 1px solid #233452; padding: 0.5rem; }
  button:focus { outline: none; }
</style>
...
<div class="notice" id="notice">
  <p>Log hours on the day you work. Hours count toward the spring plant sale discount.
  If you worked with a partner, each of you logs your own hours.
  Hours logged after Sunday night go into next week's total.
  Questions about your total go to the coordinator at the Saturday gate table.</p>
</div>
<form action="/hours" method="post">
  <p><label for="hours">Hours worked</label>
  <input type="text" id="hours" name="hours" inputmode="decimal"></p>
  <p><label for="bed">Bed number</label>
  <input type="text" id="bed" name="bed" inputmode="numeric"></p>
  <button type="submit" id="save">Save hours</button>
</form>
<script>
  // Keep the volunteer in the hours box until it holds a number.
  document.getElementById("hours").addEventListener("keydown", function (event) {
    if (event.key === "Tab" && isNaN(parseFloat(this.value))) {
      event.preventDefault();
    }
  });
</script>
```

```
node tools/web-check/check.js hours.html
```

```
PASS  hours.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

Exit code 0. Valid markup, every input labelled, no overflow. **On the automated layer, this page is
done.**

## Worked example 2 · what three browsers measured

A small puppeteer script, kept in the scratchpad and not shipped, loaded the same page and measured
three things web-check does not: lines of the notice cut off by the fixed height, where Tab goes, and
whether the focused button shows an outline. It ran headless in Chrome, in Edge, and in Firefox. The
Chrome output:

```
browser: chrome Chrome/153.0.8010.48
width 1280: notice has 2 lines of text, 0 cut off
width 640: notice has 4 lines of text, 1 cut off
width 360: notice has 7 lines of text, 4 cut off
Tab x4, empty hours box: hours -> hours -> hours -> hours
Tab x3, hours typed:  hours -> bed -> save -> BODY
focus outline on save button: none 3px
```

**Edge (`Edg/153.0.4234.32`) and Firefox (`firefox/156.0`) printed the same six lines.** Edge shares
Chrome's engine; Firefox does not, so its match means more.

**Read the output against real people:**

- **Width 360 is a phone.** Four of seven lines are cut off, including the late-hours rule.
  web-check looks for a page too wide, not text too tall for its box.
- **Width 640 approximates 200 percent zoom in a 1280-wide window**, because zoom doubles
  everything, so half as many CSS pixels fit across. One line is cut off. It is not the real zoom
  control, so the by-hand check below still matters.
- **Tab from an empty hours box goes nowhere.** Four presses, four times `hours`. A keyboard user who
  does not know the hours yet is trapped. A mouse user never notices.
- **`none 3px`** means the button's outline style is `none`. A keyboard user reaching Save cannot
  see that they are on it.

## Worked example 3 · the fix, measured the same way

Three changes: `min-height` instead of `height`, a visible focus style, and no keydown trap (the
number is checked when the form is submitted instead).

```css
.notice { min-height: 4rem; overflow: hidden; border: 1px solid #233452; padding: 0.5rem; }
button:focus-visible { outline: 3px solid #57A1EB; outline-offset: 2px; }
```

web-check still printed `PASS` with zero errors and zero violations at all three widths, exit 0. The
browser measurements changed. Chrome:

```
width 1280: notice has 2 lines of text, 0 cut off
width 640: notice has 4 lines of text, 0 cut off
width 360: notice has 7 lines of text, 0 cut off
Tab x4, empty hours box: hours -> bed -> save -> BODY
Tab x3, hours typed:  hours -> bed -> save -> BODY
focus outline on save button: solid 3px
```

Firefox printed the same, except for one line:

```
Tab x3, hours typed:  hours -> bed -> save -> save
```

**That difference is real, so record it.** It is about what the browser reports after Tab passes the
last control. Chrome reported the page body both times; Firefox reported the body once and the Save
button once. The reason was not investigated [VERIFY]. Every control was still reached in order in
both browsers. **This is what a second browser is for:** it shows where "the browser" really meant
one browser.

---

## The human checks, as procedures

Run these on your release candidate today. Record each one in test plan section 6, with what you
actually saw.

**1. Keyboard only.** Put the mouse away. Tab from the top of the page through the main task, using
Tab, Shift+Tab, Enter, Space, and arrows. At every stop, write where focus is and whether you can see
it. Fail it if focus disappears, gets stuck, or jumps out of screen order.

**2. Zoom to 200 percent.** Press Ctrl and plus until the browser shows 200 percent, and reload. No
text cut off or overlapping, no sideways scrolling to read a sentence, main task still works. Ctrl and
0 resets it. (Not done by hand on the build machine; the 640 measurement approximates it.)

**3. A real phone.** Open the deployed address in the phone's own browser and do the main task with
your thumb. Record the phone type and browser, never whose phone it is. (No phone was available on the
build machine. [VERIFY])

**4. A second browser.** Chrome, Edge, and Firefox are on the build machine, and the script ran in all
three. Do the main task by hand in a browser you did not build in. A browser your stakeholder uses and
you cannot reach is a written limit.

**5. A screen reader on one screen.** Windows Narrator is built in; the Windows logo key, Ctrl, and
Enter turn it on and off. Use Tab and the arrow keys without looking, and write what it reads for each
control. (Not verifiable on the build machine. Your instructor confirms the steps on a lab machine.
[VERIFY] the key commands for your version of Windows.)

---

## The wrong version, and what it produces

```
| T-11 | NF3 | P1-P4 | PASS | passes the validator |
```

**What it produces:** four platforms claimed from one check that tests none of them directly. For
the hours page, the line is true of the validator and false for the phone, the keyboard, and focus.
Next week those become usability findings you could have had today.

A useful set of rows:

```
| T-11 | NF5 | all   | PASS | web-check index.html, hours.html: 0 errors, 0 violations, no overflow at 360/768/1280, exit 0 |
| T-12 | NF3 | P3 kb | FAIL | Tab trapped in Hours when empty; fixed in 4e1c2a9, re-run PASS |
| T-13 | NF3 | P2 ph | FAIL | notice cut off on phone (4 of 7 lines); min-height in 4e1c2a9, re-run PASS |
| T-14 | NF3 | P4 sr | NOT RUN | Narrator walkthrough booked for lab machine, Week 14 Fri |
```

## Why the wrong version is tempting

The validator is fast and prints a clean result. Borrowing a phone and turning on a screen reader feel
slow and awkward. **The awkward checks find what your users will hit.** Twenty minutes today saves a
correction in Week 16.

---

## What to do in your project today

1. Open section 2 of your [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md). List every
   targeted platform, device, and input method.
2. Run web-check on every page at 360, 768, and 1280. Paste the real output into section 6.
3. Do human checks 1 to 4 above on your main task. Book check 5 on a lab machine if you cannot do it
   today.
4. Every platform gets its own row, with what you saw. A platform you could not reach is NOT RUN with
   a reason, never PASS.
5. Add at least three items to section 5, "what automated tools cannot tell you."
6. Fix what you found, re-run the whole practice pass, and commit before Friday's recorded
   release-candidate run.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Targeted platform** | A browser, device, or input method your requirements say the project must work on |
| **Cross-browser** | Working the same way in more than one browser, and knowing where it does not |
| **Responsive** | A layout that works at every width, including a phone |
| **Keyboard trap** | A place where Tab cannot move focus onward |
| **Visible focus** | An outline or other mark showing which control the keyboard is on |
| **Screen reader** | Software that reads the page aloud, such as Windows Narrator |

---

## Check yourself

1. Which check found the trapped hours box: web-check, the keyboard-only pass, or the second browser?
   Why did the other two not find it?
2. Your test plan names "volunteers' phones." You have no phone today. What do you record, and what do
   you do instead?
3. Chrome and Firefox disagree on one measurement, and your page works in both. Do you record the
   difference?

---

## Check your answers

**1.** The keyboard-only pass (in this note, the measurement script played that role). web-check
checks markup and accessibility rules, and pressing Tab is not one of its checks. A second browser
would show the same trap, because the trap is in the page's own script, not in the browser.

**2.** NOT RUN, with the reason and the day you will run it. Today, look at the 360 screenshot from
`--shots` and say it is not a real phone. Get a lab device or borrow a phone before Friday.

**3.** Yes. Write what each browser showed and why it does not affect users. A recorded difference is
evidence you tested more than one browser.
