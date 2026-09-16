# Lecture Notes: State, Render, and Comments That Tell the Truth
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W04_StateRenderComments.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-4-client-side-scripting/04-slides/MCCTC_145010_Slides_W04_StateRenderComments.md --export pptx`

If you missed class, you can learn this concept from this file alone. **If you were at BPA,** read
this file, then follow Wednesday in `10-resources/MCCTC_145010_CatchUp_W04.md`.

**Competencies:** 6.3.2 manipulate page elements in response to user events · 6.3.3 insert
comments into client-side scripts.

---

## Why this exists

Yesterday each handler changed the page directly. That works for one button. It stops working the
moment two parts of the page depend on the same fact. Take a shift, and the button, the total, and
the warning all have to change. Write three handlers that each update "their" part, and sooner or
later one of them forgets, and the page contradicts itself.

There is a second problem in how text gets onto the page. One way is safe. One way runs whatever
the person typed as code. They look almost identical.

And there is a third: the comments in your script are downloaded by every visitor.

---

## The concept in plain language

**State** is what is true right now: which shifts are taken, which filter is on, how many votes are
used. Keep it in one place.

**Render** is one function that reads the state and makes the page match it. Only render writes to
the page.

**Events** change the state and then call render. They never touch the page themselves.

```
person acts  ->  event handler changes state  ->  render()  ->  page matches state
```

This is the pattern every framework is built on. You are writing it by hand, so you know what a
framework is doing for you when you meet one.

**Text goes in with `textContent`.** `textContent` puts characters on the page. `innerHTML` hands a
string to the HTML parser, which builds elements from it, and some elements run code. **If a person
typed it, it is text.**

**Comments say why, agree with the code, and are public.** A comment that repeats the code is noise.
A comment that contradicts the code is a bug waiting for the next reader. And a comment in a `.js`
file is sent to every visitor, who can read it with View Source.

---

## Worked example 1: state, render, events

A playlist vote with a cap of two.

```js
// State: which playlists this person voted for. Voting is capped at two.
const MAX_VOTES = 2;
const votes = new Set();

const buttons = document.querySelectorAll(".vote");
const tally = document.querySelector("#tally");

// Render: reads the state, writes the page. Nothing else writes the page.
function render() {
  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(votes.has(button.textContent)));
  }
  if (votes.size === 0) {
    tally.textContent = "You have not voted yet.";
  } else {
    tally.textContent = `You voted ${votes.size} of ${MAX_VOTES} times.`;
  }
}

// Events: change the state, then render.
for (const button of buttons) {
  button.addEventListener("click", () => {
    const name = button.textContent;
    if (votes.has(name)) {
      votes.delete(name);
    } else if (votes.size < MAX_VOTES) {
      votes.add(name);
    }
    render();
  });
}

render();
```

Click all three playlists in order. The page shows:

```
You voted 2 of 2 times.
```

The first two buttons are pressed and the third is not. Click the first again, then the third. The
tally still reads 2 of 2, and now the second and third are pressed. At no point did any handler
decide what the tally says. Render did, every time, from the one place the truth lives.

**`aria-pressed`** is the attribute that makes a button a toggle. A screen reader says
"Vote: Warm-up mix, toggle button, pressed." Your CSS can style `[aria-pressed="true"]`, so what
people see and what a screen reader hears come from the same attribute and cannot disagree.

---

## Worked example 2: textContent against innerHTML

```html
<p id="panel"></p>
```

```js
const panel = document.querySelector("#panel");

panel.textContent = "<b>Closed</b> today";
console.log(panel.children.length, panel.textContent.length);

panel.innerHTML = "<b>Closed</b> today";
console.log(panel.children.length, panel.textContent.length);
```

Output:

```
0 19
1 12
```

With `textContent`, the page shows the angle brackets as characters. There are no child elements,
and all 19 characters are text. With `innerHTML`, the parser built a real `<b>` element. There is one
child, and the text is only the 12 visible characters.

When you wrote that string yourself, `innerHTML` is sometimes what you meant. When a person typed
it, it never is.

---

## Worked example 3: comments, three kinds

In a `.js` file:

```js
/*
 * shift-board.js
 * Lets a person take or drop shifts and keeps a running total.
 * Loaded with defer, so every element exists when this runs.
 */

// The most hours one person can pick in a week. One place to change it.
const HOUR_LIMIT = 12;

// Exactly 12 is allowed. Only more than 12 is over.
summary.classList.toggle("over-limit", hours > HOUR_LIMIT);
```

In an `.html` file:

```html
<!-- The rules panel starts visible, so the page still works if the script fails. -->
```

`//` runs to the end of the line. `/* ... */` can span lines, and the header block at the top of a
file is where you say what the file does and anything a reader needs before line one. `<!-- -->` is
HTML, and it does not work inside a `.js` file.

Each comment above answers a question the code cannot: why the number lives in a constant, why the
comparison is `>` and not `>=`, why the panel starts visible. That is the test for a useful comment.

**Now open View Source on the page and click the script's file name.** Every one of those comments
is there, readable by anyone. Never put a password, a key, an internal note about a person, or
"TODO: this check is fake, fix before launch" in client-side script.

---

## The wrong version, and what it does

A shout-out preview that shows what the person is typing:

```js
preview.innerHTML = `<p>${textBox.value}</p>`;
```

Type this into the box:

```
<img src="x" onerror="document.body.dataset.owned='yes'">
```

There is **no error**. The parser builds an `<img>`, the image at `x` fails to load, and the
browser runs the `onerror` attribute as JavaScript. On the build machine the preview contained 1
image element and the `onerror` code ran. That code could have done anything the page can do: read
what is on screen, change links, send data somewhere. This is **cross-site scripting**, usually
written XSS.

In this preview, only the person typing is affected, which sounds harmless. It stops being harmless
the moment the text is saved and shown to someone else, which is next week's form. It also is not
harmless when someone else supplies the text: "paste this into the shout-out box, it makes a cool
effect."

The fix is one word:

```js
preview.textContent = textBox.value;
```

---

## Why the wrong version is tempting

`innerHTML` is shorter, it lets you build a whole chunk of markup in one template string, and every
old tutorial uses it. It works perfectly with every test you think of, because you test with
ordinary words. The bug only appears for input you would never type.

**The comment version of the mistake** is tempting for a different reason. You write the comment
when you write the code, then you change the code. The comment still says what the old code did,
and the next reader believes it. When you change a line, read the comment above it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **State** | The facts that are true right now, kept in one place |
| **Render** | The one function that makes the page match the state |
| **`textContent`** | Reads or writes the text of an element. Never creates elements. |
| **`innerHTML`** | Reads or writes an element's content as HTML. Parses what you give it. |
| **`aria-pressed`** | Marks a button as a toggle and says whether it is on |
| **`setAttribute`** | Sets an attribute to a string. `String(true)` is `"true"`. |
| **XSS, cross-site scripting** | Getting a page to run code an attacker supplied, often through text inserted as HTML |
| **Header comment** | The block at the top of a file saying what it does and what a reader needs to know first |

---

## Self-check

**Question 1.** A handler adds a shift, updates the button, and updates the total. A different
handler removes a shift and updates only the button. What does the person see after removing one,
and how does the render pattern prevent it?

**Question 2.** Which of these is safe for a name someone typed into `nameBox`, and what does the
other one risk?

```js
item.innerHTML = nameBox.value;
item.textContent = nameBox.value;
```

**Question 3.** Rewrite this comment so it earns its place, and say what is wrong with the
original.

```js
// set disabled
addButton.disabled = length === 0 || length > MAX_LENGTH;
```

---

### Answers

**1.** The button shows the shift as dropped, and the total still counts it. The page contradicts
itself. With render, neither handler writes the total or the button. Both change the state and call
render, and render writes everything from the state every time, so they cannot drift.

**2.** `textContent` is safe: the name appears exactly as typed. `innerHTML` parses the name as HTML,
so a "name" containing an element with an event attribute runs code in the page. That is XSS.

**3.** The original repeats the code and says nothing a reader could not see. A comment that earns
its place says why: `// Empty shout-outs are pointless, and exactly MAX_LENGTH characters is still
allowed, so the test is > and not >=.`
