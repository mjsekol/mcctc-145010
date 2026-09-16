# Lab W03-02 · The Shift Swap Board
## 145010 Web Design & Senior Capstone · Week 3 · Monday, Tuesday, and Wednesday, Build 1

**Files:** `lab-w03-02-files/`
**Time:** 40 minutes each day, after the Gate 1 rep. Part 1 Monday, Part 2 Tuesday, Part 3 Wednesday.
**Grade:** Lab & Practice.
**Competencies:** 6.1.2 (plan a page considering color, links, graphics, and ADA requirements), 2.7.4
(how devices, text-to-speech, and screen readers affect a page).

---

## The scenario

Scoop Street Creamery is an invented ice cream shop, and every name on its swap board is invented. The
teens who work there trade shifts on a small web page the owner's nephew built, and it works fine with
a mouse. This week you make it work for the coworker who navigates by keyboard, the one who uses a
screen reader, and the one who cannot tell red from green.

## What you will build

The same swap board, fixed one layer per day: what people see on Monday, what the browser tells a
screen reader on Tuesday, and what a keyboard can do on Wednesday.

**Why this lab comes before the Rebuild.** Each part practises exactly one day's concept on a page
small enough to finish in 40 minutes. On Tuesday and Wednesday afternoon you use the same moves on a
page five times the size.

---

## Setup, Monday only

1. Copy `lab-w03-02-files/` into your repository as `week3-swap/`. Commit it untouched with the message
   `Swap board starter`.

2. Open `swap-board.html` in Chrome. Click the green and red buttons, click the grey switch, type in
   the search box.

   **You see** a page that works. The switch turns green when you click it.

3. Run the checker from the repository root:

   ```
   node tools/web-check/check.js week3-swap/swap-board.html
   ```

   **You see** `FAIL`, eight validation errors, and two axe rules at every width:
   `button-name` on four buttons and `color-contrast` on two elements. **Write down the two axe rules.
   The tool found them. You find the rest.**

---

# Part 1 · Monday · What people see · 30 minutes

Monday's concept: a WCAG success criterion is a test you can pass or fail, and contrast and colour are
the two you can measure today.

4. Find the text the tool flagged for contrast. Open DevTools, select it, and find its colour in the
   Styles pane. Click the colour swatch.

   **You see** a contrast ratio in the colour picker. **[VERIFY]** where Chrome shows it in your
   version; your instructor shows it on Monday. Write the ratio down.

5. Change that colour until the ratio is at least 4.5:1. Keep it grey.

   **You see** the ratio climb as the colour darkens. Rerun web-check and confirm `color-contrast` is
   gone.

6. Read line 40: `Red bar means the shift is in less than 24 hours.` Cover the coloured bars with your
   hand, or turn on a greyscale view if your machine has one.

   **You see** two swap cards you cannot tell apart. The tool said nothing about this.

7. Fix it with **words**. Each card says whether it is urgent in text a screen reader will read. Keep
   the bars if you like them, as a second cue.

8. Rewrite line 40 so it no longer depends on colour.

9. Commit: `Part 1: contrast and colour`.

### Acceptance criteria, Part 1

- [ ] `color-contrast` no longer appears in web-check output
- [ ] Each card states its urgency in words
- [ ] No sentence on the page tells the reader to look for a colour
- [ ] Your commit message says which two success criteria you fixed, by number and name

---

# Part 2 · Tuesday · What the browser tells a screen reader · 40 minutes

Tuesday's concept: every element hands the browser a role, a name, and sometimes a state. A screen
reader reads those, not the pixels.

10. In DevTools, open the Accessibility pane and select the first green button.

    **You see** role `button` and an empty name. A screen reader says "button" and nothing else.
    Four of them.

11. Give each button a name that says **what it does and to which swap**. The image inside each button
    is the place to put it, in its `alt`.

    **You see** in the Accessibility pane: `Accept Maya R.'s Friday swap`. Not "check mark." Not
    "accept." Four buttons that all say "Accept" are four buttons nobody can tell apart in a list.

12. Add `type="button"` to all four. Rerun web-check.

    **You see** `button-name` gone, and the eight validation errors gone.

13. Select the search box. Read its name.

    **You see** a name, `Search by name`, taken from the placeholder. **web-check passed it.** Type one
    letter. The instruction disappears. Give it a visible `<label>` tied to it with `for` and `id`.

14. Select "Settings." Read its role.

    **You see** `generic`, or no role at all. It looks like a heading and it is not one. Make it an
    `<h2>`.

15. The two swap cards are a list of swaps. Make them one. `<ul>` and `<li>` work, and a screen reader
    will tell a listener how many there are.

16. Rerun web-check. Commit: `Part 2: names and roles`.

### Acceptance criteria, Part 2

- [ ] Every button has a name that says what it does and to which swap
- [ ] The search box has a visible label that stays visible while typing
- [ ] Settings is a real heading, one level below the h1
- [ ] web-check passes, which it will before Part 3 is done. Say in your commit message why that is
      not the same as finished

---

# Part 3 · Wednesday · What a keyboard can do · 40 minutes

Wednesday's concept: if a mouse can do it, a keyboard must be able to do it, and the person must be able
to see where they are.

17. Mouse out of reach. Reload. Press Tab slowly.

    **You see** focus land on the buttons, with no visible ring at all. Then the search box. **The
    switch is never reached.**

18. Find the line in the `<style>` block that hides focus. Delete it. Reload and Tab again.

    **You see** a ring on every button.

19. Replace the switch with a real checkbox and a real label:

    ```html
    <input type="checkbox" id="notify">
    <label for="notify">Text me when a new swap is posted</label>
    ```

    Delete the `.toggle` rules and the `onclick`.

20. Tab to the checkbox and press Space.

    **You see** it check and uncheck. Nobody wrote a script for that. The browser did it because you
    used the element that already does the job.

21. Rerun web-check. Walk the whole page with the keyboard once more, forward with Tab and back with
    Shift+Tab. Write the tab order in your commit message.

22. Commit: `Part 3: keyboard`.

### Acceptance criteria, Part 3

- [ ] Every control can be reached and used without a mouse
- [ ] A visible ring on every focused control
- [ ] The switch is a checkbox that Space toggles
- [ ] web-check exits 0 at 360, 768, and 1280

---

## If it breaks

**1. `button-name (critical, 4 node(s))  Buttons must have discernible text`**
still appears after you added names. You put the name somewhere a button does not read, such as a
`title` on the `<div>` around it. Put it in the `alt` of the image inside the button.

**2. `text-content  <button> must have accessible text`**
is the validator's version of the same problem. It goes away with the same fix.

**3. `label (critical, 1 node(s))  Form elements must have labels`**
appears after you added a label. The label's `for` does not match the input's `id`. Or you hid the label
with `display: none`, which removes it from the accessibility tree along with the screen.

**4. `no-implicit-button-type  <button> is missing recommended "type" attribute`**
A `<button>` inside a form submits the form unless told otherwise. This page has no form, but the
validator asks you to say what you mean. Add `type="button"`.

---

## Stretch goal

A real swap board would load swaps from a server and add new ones while the page is open. How would a
screen reader user find out a new swap arrived without reloading? Write three sentences. You build
something like it in Week 4.

---

## Submission checklist

- [ ] `week3-swap/swap-board.html` passes web-check
- [ ] Three commits, one per part, each message naming the success criteria fixed
- [ ] The tab order written in the Part 3 commit message
- [ ] Pushed at the end of each period

---

## Extended options

All four versions practise the same three moves, see, name, and reach, and are graded on the same
scale.

### Choosing a version, three signals

| What you see at the end of Monday's Part 1 | Version |
|---|---|
| Still hunting for the contrast ratio at minute 20 | SCAFFOLDED |
| Part 1 committed with both criteria named by number | STANDARD |
| Part 1 committed by minute 15, and asking why the tool missed the colour bars | EXTENDED |
| Asks what this has to do with an app, a game, or a job | APPLIED |

### SCAFFOLDED

Same page, one fix at a time. Your instructor gives you the exact line number for each step. Part 1 is
steps 4, 5, and 7 only. Part 2 is steps 10, 11, and 13. Part 3 is steps 17, 18, and 19. Show your
instructor web-check output at the end of each part before you commit.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, then turn the **Accept** buttons into something that remembers it was pressed.
A button that toggles on and off should announce its state, the way the checkbox does. That needs one
attribute this course does not teach and a few lines of script from Week 4.
*Hint, not the answer:* read the MDN page for the `aria-pressed` attribute, and read its warning about
when a toggle button's label should **not** change.

### APPLIED

Same moves, a different page. Pick one page you use weekly that you did not build: a school portal, a
game's news page, a shop's order page. Do not change it. Run Parts 1, 2, and 3 as an **audit**: one
contrast measurement, one colour-only message, one control with no name, one thing a keyboard cannot
reach. Write each as a finding with a WCAG 2.2 criterion number and name. Then fix the Scoop Street page
as STANDARD.
