# Lecture Notes: The Page Waits for You
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W04_ThePageWaits.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-4-client-side-scripting/04-slides/MCCTC_145010_Slides_W04_ThePageWaits.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome and the
Lab W04-01 files. **If you were at BPA,** read this file, then follow Tuesday in
`10-resources/MCCTC_145010_CatchUp_W04.md`.

**Competency:** 6.3.2 insert client-side script into a web page, and manipulate page elements in
response to user events.

---

## Why this exists

Every Python program you have written runs from the first line to the last and then stops. A page
script does not work like that. It runs from top to bottom once, and almost everything it does in
that run is **leave instructions** for later. Then it waits, sometimes for an hour, for the person
to do something.

If you carry the Python picture into the browser, two things go wrong. You write code that expects
to run in order when it will actually run whenever the person acts. And you build controls that
work for you, with a mouse, and not for the person who uses a keyboard or a screen reader.

---

## The concept in plain language

**An event is something that happened.** A click, a key press, a change to a text box, the page
finishing loading. The browser creates an **event object** describing it.

**A listener is an instruction for later.** `addEventListener("click", handler)` says: when a click
happens on this element, call `handler` with the event object. It does not call `handler` now.

**The browser runs one thing at a time.** Events wait in a line. The browser takes the next one,
runs its handler to the end, draws any changes, and takes the next. This is the **event loop**, and
from the person's side it has one rule: **while a handler is running, the page cannot respond to
anything.**

**A `<button>` does keyboard work for you.** A button is in the tab order. When it has focus, Enter
and Space both fire a `click` event. So one click listener serves a mouse user, a keyboard user,
and a screen reader user. A `<div>` is not in the tab order and ignores Enter and Space. A click
listener on a div serves a mouse and nobody else.

---

## Worked example 1: one listener, three ways to trigger it

```html
<button type="button" id="ready">Mark order ready</button>
<p id="log" role="status">Nothing has happened yet.</p>
```

```js
const log = document.querySelector("#log");

document.querySelector("#ready").addEventListener("click", (event) => {
  log.textContent = `click from ${event.target.id}, detail ${event.detail}`;
});
```

Click it with the mouse, then Tab to it and press Enter, then press Space. The status line shows,
in turn:

```
click from ready, detail 1
click from ready, detail 0
click from ready, detail 0
```

Same event, same handler, three ways to cause it. `event.target` is the element the event happened
on. `event.detail` is the click count: 1 for a mouse click, 0 when the keyboard caused it. You will
rarely need `detail`. It is here to prove that the keyboard really did fire a click.

---

## Worked example 2: responding while the person types

```html
<label for="caption">Photo caption</label>
<textarea id="caption" rows="2"></textarea>
<p id="caption-count" aria-live="polite">0 of 80 characters</p>
```

```js
const caption = document.querySelector("#caption");
const captionCount = document.querySelector("#caption-count");

// "input" fires on every change to the box: typing, deleting, pasting.
caption.addEventListener("input", () => {
  captionCount.textContent = `${caption.value.length} of 80 characters`;
});
```

After typing `GG pit crew`:

```
11 of 80 characters
```

`input` fires on every change, including a paste. `change` fires only when the person leaves the
box. For a live counter you want `input`. `aria-live="polite"` asks a screen reader to announce the
new count when the person pauses.

---

## Worked example 3: the order things actually happen in

```js
console.log("order placed");
setTimeout(() => console.log("pizza ready"), 0);
for (let i = 0; i < 3; i++) {
  console.log("waiting", i);
}
console.log("done waiting");
```

Output:

```
order placed
waiting 0
waiting 1
waiting 2
done waiting
pizza ready
```

`setTimeout` with a delay of 0 does not mean "now." It means "put this in the line." The current
script has to finish before anything in the line runs. A click works the same way: it waits in the
line until the script in front of it is done.

---

## The wrong version, twice

### Wrong 1: the div that only a mouse can use

```html
<div id="cancel" class="fake-button">Cancel order</div>
```

```js
document.querySelector("#cancel").addEventListener("click", cancelOrder);
```

There is **no error**. Click it with a mouse and it works. Press Tab through the page and focus
never lands on it. A keyboard user cannot cancel the order. A screen reader announces "Cancel
order" as plain text, not as a control.

Now the part that surprises people. Run the checker on the instructor's demo page, which has
exactly this div, from the repository root:

```
node tools/web-check/check.js Courses/145010/units/unit-4-client-side-scripting/05-labs/instructor/live-demos-w04/tuesday.html
```

It reports, with the long path shortened here:

```
PASS  .../live-demos-w04/tuesday.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

The checker reads the tree. It sees a div with some text in it, which is valid. **It cannot see
that a listener is attached.** Only a person pressing Tab finds this bug.

**The fix is not to patch the div.** Adding `tabindex="0"`, `role="button"`, and a `keydown`
listener for Enter and Space can be made to work, and it is three things to get right where one
element gets them all:

```html
<button type="button" id="cancel">Cancel order</button>
```

### Wrong 2: the handler that freezes the page

```js
document.querySelector("#freeze").addEventListener("click", () => {
  log.textContent = "Recounting...";
  const stopAt = Date.now() + 3000;
  let laps = 0;
  while (Date.now() < stopAt) {
    laps += 1;
  }
  log.textContent = `Recount finished after ${laps.toLocaleString()} laps.`;
});
```

Click it, then click "Mark order ready" right away. For three seconds nothing happens. The ready
click runs only after the loop ends. On the build machine, the freeze ended at 3,072 milliseconds
and the waiting click ran at 3,081.

"Recounting..." never appears on screen. The browser draws between handlers, not during one, so it
never got the chance.

---

## Why the wrong versions are tempting

**The div** is tempting because it looks exactly the way you want with no CSS to undo, and it
works when you test it, because you test with a mouse. A button comes with a border, a background,
and a font you have to reset. That is five lines of CSS, and they are worth it.

**The freeze** is tempting because in Python a long loop is normal. Nobody is waiting on your
terminal. In a page, a person is waiting on every handler. Any work that takes more than a moment
belongs somewhere other than a click handler: done in smaller pieces, done ahead of time, or done
on a server.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Event** | Something that happened: a click, a key press, an input change, a page load |
| **Event object** | What the browser passes to your handler. `event.target` is where it happened. |
| **Listener, handler** | The function you register to run when the event happens |
| **`addEventListener`** | Registers a listener. It does not run it. |
| **`click`** | Fires for a mouse click, and for Enter or Space on a focused button |
| **`input`** | Fires on every change to a text box, including paste |
| **`change`** | Fires when the person commits a change, such as leaving a text box or choosing an option |
| **Event loop** | The browser runs one handler at a time, then draws, then runs the next |
| **Tab order** | The sequence focus moves through when the person presses Tab |

---

## Self-check

**Question 1.** The page has a button with `id="go"`, and nobody clicks. What does this print?

```js
console.log("1");
document.querySelector("#go").addEventListener("click", () => console.log("2"));
console.log("3");
```

**Question 2.** A teammate's "Delete" control is a `<span>` with a click listener, and the checker
passes. Name two people who cannot use it, and the one change that fixes it for both.

**Question 3.** A filter handler loops over 80,000 rows and takes two seconds. The person clicks
"Clear filter" during those two seconds. What do they see, and when?

---

### Answers

**1.** `1` then `3`. `2` never prints, because registering a listener does not run it and nobody
clicked.

**2.** A keyboard user, because the span is never in the tab order, and a screen reader user,
because the span has no role and is announced as text. Change it to `<button type="button">`. The
same click listener then works for both.

**3.** Nothing, for the rest of the two seconds. The page does not repaint or respond while the
handler runs. When it finishes, the clear click runs and the filter clears. To the person, the page
looked broken and then caught up.
