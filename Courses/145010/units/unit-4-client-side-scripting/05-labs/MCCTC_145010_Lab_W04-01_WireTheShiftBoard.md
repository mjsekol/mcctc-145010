# Lab W04-01 · Wire the Shift Board
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Monday to Wednesday

**Competencies:** 6.3.1 select and apply scripting languages · 6.3.2 insert client-side script and
manipulate page elements in response to user events · 6.3.3 insert comments into client-side
scripts · 2.7.6 describe the characteristics and use of browser plug-ins (step 5 only)

**Time:** Monday Build 1 and Build 2, Tuesday Build 1 and Build 2, Wednesday Build 1. Due at the
end of Wednesday Build 1.

---

## The situation

The Scoop Shack is an ice cream shop that hires students for evening and weekend shifts. Every week
the shift lead posts open shifts, and every week somebody picks up eighteen hours by accident and
has to drop two shifts in the group chat. The page already lists the shifts and the rules. It does
nothing when you touch it.

*The Scoop Shack is invented for this lab. The problem is real at most places that hire teenagers.*

**What you will build:** a script that hides the rules behind a toggle, lets a person take or drop
each shift, and keeps a running total that warns past 12 hours, all usable with a keyboard alone.

---

## Before you start

Copy `lab-w04-01-files/` into your repository as `labs/w04-01/`. It has three files:

| File | What it is | Do you change it? |
|---|---|---|
| `index.html` | The page. Valid, accessible, and passes `web-check`. | One line in step 2 |
| `styles.css` | The styles, including the pressed-button style | No |
| `shift-board.js` | The starter script. It runs and does nothing useful. | Yes, most of the lab |

Create `labs/w04-01/lab-notes.md`. Every step that says **record** goes in there.

**If you missed Monday or Tuesday for BPA,** read the lecture note for each day you missed before
you start that day's steps. The catch-up guide in `10-resources/` lists them.

**Rules for this lab.** Gate 3 conditions: any tool, including an AI assistant, with an entry in
your AI usage log for each use. Two exceptions. **Step 3 and the keyboard tests are done by you,
with your own hands**, because the point is that you see the failure. And **no `innerHTML`**
anywhere in your script.

---

## Steps

### Part A · Monday · Where the script goes

**Step 1.** Open `index.html` in Chrome. Press F12 and choose the **Console** panel. Click every
button on the page.

*You should see:* nothing happens, and the Console is empty. The rules are visible. The page has no
script yet.

**Step 2.** In `index.html`, find the comment in the `<head>` that mentions step 2. Directly under
it, add the line that loads `shift-board.js` with the `defer` attribute. Save and reload.

*You should see:* `shift-board.js loaded` in the Console.

**Step 3. Break it on purpose.** At the very top of `shift-board.js`, above the `console.log`,
add this temporary line:

```js
document.querySelector("#rules-panel").hidden = true;
```

Reload. The rules disappear. Now **remove `defer`** from your script tag and reload again.

*You should see:* a red error in the Console, and the rules are visible again. **Record** the error
text exactly as Chrome shows it, and one sentence explaining why removing one word caused it.

Then put `defer` back, **delete the temporary line**, and reload. `shift-board.js loaded` is back
and there are no errors.

**Step 4.** In the Console, type each of these and press Enter. **Record** each result.

```js
document.querySelectorAll(".take").length
document.querySelector("#summary").textContent
document.querySelector(".take").dataset.hours
```

*You should see:* a number, a sentence in quotes, and a digit in quotes. **Record** one sentence on
why the third result has quotes around it, because it matters in step 10.

**Step 5. The plug-in note.** Monday, Build 2. Create `labs/w04-01/plugin-note.md`. Half a page,
in your own words, answering:

1. What was a browser plug-in? Name one and what it did.
2. Why did browsers remove plug-in support? Give at least two reasons.
3. How is an extension, such as an ad blocker, different from a plug-in?
4. Open `chrome://extensions` on your machine. List what is installed. Open the details of one and
   quote the permissions it asks for.

Every factual claim names where it came from: a page title and site is enough. **If you could not
confirm a claim, write [UNCONFIRMED] after it.** You may use an AI assistant to find sources. You
may not use one to write the note. Say which in your AI usage log.

*You should see:* a note of about 200 to 300 words, at least two named sources, and a quoted
permission list.

### Part B · Tuesday · Responding to the person

**Step 6.** In `shift-board.js`, under the step 6 comment, find the rules toggle button and the
rules panel with `document.querySelector` and store each in a `const`. Use the ids in
`index.html`.

*You should see:* no errors after reloading. Type `rulesToggle` in the Console. It shows the button.

**Step 7.** Write `setRulesOpen(isOpen)`. It does exactly two things: sets the panel's `hidden`
property to the opposite of `isOpen`, and sets the button's `aria-expanded` attribute to
`String(isOpen)`.

*You should see:* nothing yet. Test it from the Console: `setRulesOpen(false)` hides the rules,
`setRulesOpen(true)` shows them.

**Step 8.** Call `setRulesOpen(false)` once, so the rules start closed now that the script is
running. Then add a `click` listener to the toggle. Inside it, read the current state from the
button with `getAttribute("aria-expanded") === "true"` and call `setRulesOpen` with the opposite.

*You should see:* the rules start hidden, and each click opens or closes them. The chevron on the
button turns.

**Why the rules start visible in the HTML.** If your script fails to load, a person can still read
the rules. The script takes over only once it is running. That is **progressive enhancement**.

**Step 9. Keyboard test.** Take your hand off the mouse. Press Tab until the toggle has a focus
ring. Press Enter. Press Space. Then open the **Elements** panel, select the button, and watch its
`aria-expanded` attribute while you press Space twice more.

*You should see:* Enter and Space both toggle the rules, and `aria-expanded` changes between
`"true"` and `"false"` every time the panel changes. **Record** one sentence on why you did not
need a keyboard listener.

**Step 10.** Under the step 10 comment, find every "Take shift" button with
`document.querySelectorAll(".take")`. Then write `totalHours()`. It loops over the buttons, and for
each one whose `aria-pressed` is `"true"`, adds `Number(button.dataset.hours)` to a total. It
returns the total.

*You should see:* `totalHours()` in the Console returns `0`.

**Step 11.** Write `renderSummary()`. It writes one sentence into `#summary` with `textContent`:

| Picked | The sentence |
|---|---|
| none | `You have not picked any shifts yet.` |
| 12 hours or fewer | `You picked 3 shifts, 12 hours.` with the real numbers, and `1 shift` for one |
| more than 12 hours | `You picked 3 shifts, 13 hours. That is over the 12-hour limit. Drop a shift.` |

Then add the class `over-limit` to `#summary` when the total is more than 12, and remove it
otherwise. `classList.toggle("over-limit", condition)` does both in one line.

*You should see:* `renderSummary()` from the Console leaves the sentence as it was.

**Step 12.** Give each button a `click` listener. Inside it, flip the button's `aria-pressed`
between `"true"` and `"false"`, then call `renderSummary()`. **Do not change the button's text.**
A screen reader reads the name and the pressed state together. "Take shift, toggle button, pressed"
is clear. If you also change the text to "Drop shift", it reads "Drop shift, pressed", which says
the opposite of what happened.

Then run the **keyboard test** again, hand off the mouse: Tab to Wednesday, Saturday, and Sunday
and press Space on each.

*You should see:*

```
You picked 3 shifts, 12 hours.
```

with no red bar. Now Tab back to Monday and press Enter:

```
You picked 4 shifts, 16 hours. That is over the 12-hour limit. Drop a shift.
```

with a red left bar. Press Enter on Monday again and the warning goes away.

### Part C · Wednesday · Comments and submission

**Step 13. Comments pass.** Read every comment in your script against the line under it.

- The header block at the top says what the file does. Update it so it is true of your file.
- Delete every `TODO` comment you have finished.
- Add a comment above the `> HOUR_LIMIT` test saying why it is `>` and not `>=`.
- Add a comment above one other line whose reason is not obvious from the code.

*You should see:* no comment that only restates what the next line does, and no comment that is
no longer true.

**Step 14. Checks.** Search your script for `innerHTML`. There should be none. Then, from the
repository root, run the checker on your page:

```
node tools/web-check/check.js labs/w04-01/index.html
```

*You should see:* `PASS` and zero violations at all three widths. **Record** the output.

**Step 15. Submit.** Commit with a message that says what the script does. Push.

---

## Acceptance criteria

- [ ] The script loads from the `<head>` with `defer`, and the Console shows no errors
- [ ] `lab-notes.md` has the exact no-defer error and why it happened
- [ ] The rules start hidden once the script runs, and toggle by mouse, Enter, and Space
- [ ] `aria-expanded` always matches what is on screen
- [ ] Each shift toggles with `aria-pressed` by mouse, Enter, and Space, and its label never changes
- [ ] The summary sentence is correct for 0 shifts, for exactly 12 hours, and for more than 12
- [ ] The warning style appears only above 12 hours
- [ ] No `innerHTML` anywhere
- [ ] A header comment, a comment on the `>` test, and no false or finished-TODO comments
- [ ] `web-check` reports PASS, pasted in `lab-notes.md`
- [ ] `plugin-note.md` answers all four parts with named sources

---

## If it breaks

| What you see | What it means |
|---|---|
| `Uncaught TypeError: Cannot set properties of null (setting 'hidden')` | The panel query returned `null`. Either the script has no `defer`, or the selector does not match `#rules-panel`. |
| `Uncaught TypeError: Cannot read properties of null (reading 'setAttribute')` | The toggle query returned `null`, most often a typo such as `#rule-toggle`. Type your selector into the Console to check it. |
| `Uncaught ReferenceError: rulesToggle is not defined` | You used the name before creating it, spelled it differently, or created it inside a function where the rest of the file cannot see it. |
| The summary says `You picked 2 shifts, 043 hours.` and shows the warning | No error at all. `dataset.hours` is text, so `0 + "4" + "3"` joined into `"043"`. Wrap it in `Number()`. |
| The rules open on the first click and never close | No error. You compared `getAttribute(...)` to `true`. Attributes are always strings, so compare to `"true"`. |

---

## Stretch goal

Add an **Escape** key behaviour: when the rules are open and focus is anywhere inside the rules
section, Escape closes them and puts focus back on the toggle. Explain in `lab-notes.md` why a
`keydown` listener is the right tool here, when Tuesday said it was the wrong tool for making a div
into a button.

---

## Submission checklist

- [ ] `labs/w04-01/index.html` with the script tag
- [ ] `labs/w04-01/shift-board.js`, finished and commented
- [ ] `labs/w04-01/lab-notes.md` with every **record** item
- [ ] `labs/w04-01/plugin-note.md`
- [ ] AI usage log entry for any AI use this lab
- [ ] Committed and pushed by the end of Wednesday Build 1

---

## Extended options

Choose one with your instructor. All four assess the same competencies and are graded on the same
five-dimension scale.

### Three observable signals for choosing

| What you see by the end of Monday Build 1 | Give them |
|---|---|
| Step 3 took more than 15 minutes, or the student cannot say why the error happened | SCAFFOLDED |
| Steps 1 to 4 done, with a correct one-sentence explanation in `lab-notes.md` | STANDARD |
| Finished Part A early and asks how a framework would do this | EXTENDED |
| Says "I will never work at an ice cream shop" or asks what this is for | APPLIED |

### SCAFFOLDED

Same page, same target, more starting code. Your instructor gives you a version of
`shift-board.js` in which steps 6, 7, 10, and 11 are already written and commented. You write the
two listeners, steps 8 and 12, and run both keyboard tests.

**Extra checkpoints:** show your instructor after step 8 and after step 12.

**Then answer in writing:** the provided `totalHours()` reads the state from the buttons'
`aria-pressed` attributes. Name one advantage of keeping the state there instead of in a separate
array.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus the stretch goal, plus **one render for everything**. Rewrite your
script so the state lives in one object:

```js
const state = { rulesOpen: false, taken: new Set() };
```

and a single `render()` sets the panel, every button's `aria-pressed`, and the summary. The
listeners change `state` and call `render()`, and nothing else. Then write a paragraph comparing
the two versions: which one would you rather debug, and why.

*Hint, not the answer:* MDN's page on the `Set` object lists the methods you need. Search MDN for
"Set" and read the instance methods section.

### APPLIED

Same skills, a different page you design yourself: a **chore chart for a household**. Five chores,
each worth points, a toggle for "done" on each, a running point total, and a note that appears
once the week's goal is reached. Or pick your own: a playlist builder with a 30-minute cap, a
lunch order with a budget, a workout builder with a time limit.

It must meet every acceptance criterion above that applies: `defer`, a toggle panel with
`aria-expanded`, `aria-pressed` buttons whose labels do not change, a live `role="status"`
summary, no `innerHTML`, a header comment, and `web-check` passing.

**Then answer in writing:** name one place outside school where you have used a page that
behaved like this, and one thing it did that yours does not.
