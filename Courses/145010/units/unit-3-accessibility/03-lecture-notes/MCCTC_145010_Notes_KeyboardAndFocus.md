# Lecture Notes: Keyboard Access and Focus
## 145010 Web Design & Senior Capstone · Week 3 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W03_KeyboardAndFocus.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-3-accessibility/04-slides/MCCTC_145010_Slides_W03_KeyboardAndFocus.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome, a keyboard, and
`web-check`. **Put your mouse out of reach before you try any example.**

**Competencies:** 2.7.4 (how devices and assistive technology change how a page works), 6.1.2 (plan a
page for ADA requirements), 6.5.10 (test a site for ease of use and navigation).

---

## Why this exists

Screen reader users navigate with the keyboard. So do people with tremors, people who cannot hold a
mouse, people using a switch device that acts like a keyboard, and many developers who prefer it.

**If a mouse can do it and a keyboard cannot, the page has locked out every one of those people,** and
the page looks perfect while it does.

This is also the part of accessibility that automated tools are worst at. A tool reads the page at rest.
The keyboard problems only appear when someone presses keys.

---

## The concept in plain language

**Focus** is the browser's answer to "which element will receive what I type next?" Exactly one element
has focus at a time.

- **Tab** moves focus to the next focusable element. **Shift+Tab** moves it back.
- **Enter** activates a link or a button. **Space** activates a button and toggles a checkbox.
- **Arrow keys** move between radio buttons in a group and between options in a list.
- **Escape** often closes something that opened.

**What is focusable by default:** links with an `href`, buttons, form fields, and a few others. A `<div>`
is not, no matter what you attach to it.

**The focus order** is the order of those elements **in your HTML source**. Not their visual position.
If CSS moves something to the top visually, it is still where it is in the source for the keyboard.

**The focus indicator** is the ring or outline that shows where focus is. Browsers draw one by default.
Designers often remove it, because it appears when a mouse user clicks some elements. Modern CSS has an
answer: `:focus-visible` matches when the browser decides a ring is needed, which is mainly keyboard use.

### The four criteria for today

| WCAG 2.2 | Level | In plain words |
|---|---|---|
| 2.1.1 Keyboard | A | Everything works from a keyboard |
| 2.1.2 No Keyboard Trap | A | If focus can get in, it can get out with the keyboard |
| 2.4.3 Focus Order | A | Focus moves in an order that keeps the meaning |
| 2.4.7 Focus Visible | AA | You can always see where focus is |

And one from Monday worth rereading: **2.4.1 Bypass Blocks (A)**. A **skip link** as the first focusable
element lets a keyboard user jump past the header on every page.

### tabindex, the attribute to be careful with

| Value | Effect | Use it? |
|---|---|---|
| `tabindex="0"` | Adds a non-focusable element to the tab order in source position | Rarely. Only for custom widgets, which also need keyboard handling and a role. Prefer a real element |
| `tabindex="-1"` | Focusable by script, skipped by Tab | For moving focus on purpose, such as to an error message. Week 5 |
| `tabindex="1"` or higher | **Jumps the element ahead of everything else** | **No.** It breaks the order for the whole page |

---

## Worked example 1: walking a page with Tab

This is what a keyboard user experiences on the Lantern Street page before the rebuild. The walk was
recorded with a script that presses Tab and reads what has focus, which is what you do by hand.

```
   1  <input> textbox "Email"  focus ring: NONE
   2  <a> link "Shifts"  focus ring: NONE
   3  <a> link "Sign up"  focus ring: NONE
   4  <a> link "Visit"  focus ring: NONE
   5  <a> link ""  focus ring: NONE
   6  <a> link "Read more"  focus ring: NONE
   7  <a> link "Read more"  focus ring: NONE
   8  <input> textbox "Your name"  focus ring: NONE
   9  <input#phone> textbox ""  focus ring: NONE
  10  <input#phone> textbox ""  focus ring: NONE  <- did not move
  11  <input#phone> textbox ""  focus ring: NONE  <- did not move
  TRAP: Tab pressed three times and focus did not move.
```

Read it line by line. Four failures in eleven key presses:

- **Stop 1 is the Email field**, halfway down the page. `tabindex="1"` pushed it ahead of everything.
  2.4.3.
- **No stop has a visible ring.** One CSS rule, `*:focus { outline: none; }`, removed it. 2.4.7.
- **Stop 5 has no name.** That is Tuesday's problem showing up in a keyboard walk.
- **Stops 9, 10, and 11 are the same field.** A script cancels the Tab key there. 2.1.2.

`web-check` reported none of these four.

---

## Worked example 2: the same page after the rebuild

```
   1  <a> link "Skip to main content"  focus ring: visible
   2  <a> link "Shifts"  focus ring: visible
   3  <a> link "Sign up"  focus ring: visible
   4  <a> link "Finding us"  focus ring: visible
   5  <a> link "Add shifts to your calendar"  focus ring: visible
   6  <a> link "What to wear on a shift"  focus ring: visible
   7  <a> link "Getting your service hour form signed"  focus ring: visible
   8  <input#volunteer-name> textbox "Your name"  focus ring: visible
   9  <input#volunteer-email> textbox "Email"  focus ring: visible
  10  <input#volunteer-phone> textbox "Phone (optional)"  focus ring: visible
  11  <select#volunteer-shift> combobox "Shift"  focus ring: visible
  12  <input> radio "Yes"  focus ring: visible
  13  <button> button "Sign up"  focus ring: visible
  14  <a> link "Directions to the side door"  focus ring: visible
```

Three things to notice.

- **Stop 1 is a skip link.** It is hidden until it has focus, then it slides into view.
- **Stop 12 is one stop for two radio buttons.** A radio group is one Tab stop. Arrow keys move between
  Yes and No. Students often report this as a bug. It is how radio groups are meant to work.
- **Stop 13 is the Sign up button,** which did not appear in the first walk at all.

The CSS that makes the rings visible:

```css
:focus-visible { outline: 3px solid #1d4ed8; outline-offset: 2px; }
.site-header :focus-visible { outline-color: #f4c542; }
```

The second rule exists because a blue ring on the dark green header would be hard to see. Check your
focus ring against every background it can appear on.

---

## Worked example 3: the element that already does the job

A switch built from a div:

```html
<div class="toggle" onclick="this.classList.toggle('on')"></div>
<span>Text me when a new swap is posted</span>
```

It works with a mouse. With a keyboard it is never reached: the swap board's walk goes from the last
button straight to the search box. Now the replacement:

```html
<input type="checkbox" id="notify">
<label for="notify">Text me when a new swap is posted</label>
```

The walk after the change:

```
   5  <input#notify> checkbox "Text me when a new swap is posted"  focus ring: visible
```

Tab reaches it. Space toggles it. A screen reader announces "checkbox," the label, and whether it is
checked. **You wrote no script for any of that.** The browser did it because you used the element that
already does the job.

---

## The wrong version: adding tabindex to a div

A student is told the switch cannot be reached, and adds one attribute:

```html
<div class="toggle" tabindex="0" onclick="this.classList.toggle('on')"></div>
```

Now Tab reaches it. Press Space. Press Enter. **Nothing happens.** `onclick` on a div does not fire
from the keyboard. This was checked in Chrome on the build machine: focus reached the div, Space and
Enter changed nothing, and a mouse click toggled it. The accessibility tree gave it the role `generic`,
with no state at all, so a screen reader user cannot tell it is a switch or whether it is on.

The same idea with a role added, `<div role="button" tabindex="0">Save</div>`, got this from web-check's
validator on a test page:

```
    line 6:6  prefer-native-element  Prefer to use the native <button> element
```

And a real form whose submit control is a div got this:

```
    line 142:8  wcag/h32  <form> element must have a submit button
```

Neither message says "a keyboard user cannot use this." Both point in the right direction. Read them
that way.

---

## Why the wrong version is tempting

**One attribute feels like a fix.** Tab reaches the div, the checklist item "reachable by keyboard" is
ticked, and the tester moves on without pressing Space.

**Custom controls look better.** A styled div is quicker to make look like a design mockup than a
checkbox. Modern CSS can style real form controls far more than it once could, and `accent-color` alone
covers many cases.

**Removing the outline is a design request you will get.** The honest answer is `:focus-visible`, which
keeps the ring for keyboard users. Deleting the ring for everyone fails 2.4.7.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Focus** | Which element receives keyboard input right now |
| **Focusable** | Able to receive focus. Links, buttons, and form fields are by default |
| **Tab order** | The order Tab visits focusable elements. It follows the HTML source |
| **Focus indicator** | The visible ring that shows where focus is |
| **`:focus-visible`** | A CSS selector that matches when the browser decides a focus ring should show |
| **Keyboard trap** | A place focus can enter and not leave with the keyboard |
| **Skip link** | A link at the top of the page that jumps to the main content |
| **tabindex** | An attribute that changes whether and when an element is focusable. Never use a positive value |
| **Native element** | A built-in HTML element with behaviour already included, such as `<button>` |

---

## Self-check

**Question 1.** A page's source order is: logo link, nav links, a search box with `tabindex="2"`, main
content links, a footer link with `tabindex="1"`. Which two elements receive focus first, in order, and
which criterion does this fail?

**Question 2.** Stylesheet A contains only `*:focus { outline: none; }` for focus. Stylesheet B contains
only `:focus-visible { outline: 3px solid #1d4ed8; outline-offset: 2px; }`. Which fails 2.4.7, and why?

**Question 3.** A student's audit row says "phone field: keyboard trap, found by web-check." What is wrong
with the row, and how would you prove the trap?

---

### Answers

**1.** The footer link first, because `tabindex="1"` is the lowest positive value, then the search box
with `tabindex="2"`. Positive values go before everything with `0` or no tabindex, in increasing order.
Then the logo and the rest follow in source order. It fails 2.4.3 Focus Order (A).

**2.** A fails 2.4.7 Focus Visible (AA). It removes the ring on every element for everyone, including
keyboard users, and replaces it with nothing. The Lantern Street walk shows `focus ring: NONE` at every
stop. B passes: keyboard users get a thick ring, and the browser decides when a mouse click needs one.
Deleting A's rule and adding nothing also passes, because the browser's default ring returns, but B is
more visible.

**3.** web-check does not find keyboard traps. It never presses keys. The row claims a tool found
something it cannot find, so the found-by column is wrong. Prove it by hand: put the mouse away, Tab
into the phone field, press Tab and Shift+Tab, and record that focus did not move. Name 2.1.2 No
Keyboard Trap (A).
