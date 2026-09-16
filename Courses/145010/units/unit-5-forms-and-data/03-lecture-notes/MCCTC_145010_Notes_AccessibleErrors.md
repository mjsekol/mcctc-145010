# Lecture Notes: Errors People Can Find, and tabindex
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W05_ErrorsPeopleCanFind.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-5-forms-and-data/04-slides/MCCTC_145010_Slides_W05_ErrorsPeopleCanFind.md --export pptx`

If you missed class, you can learn this concept from this file alone, with the lab app running on
port 8405.

**Competencies:** 6.4.6 format a completed form using HTML and CSS, including fieldset and tabindex
· 6.4.2 add a form to a web page. This day also carries Week 3's accessibility work into forms.

---

## Why this exists

Yesterday your server learned to say no. Today it learns to say no in a way every person can act
on. A form that refuses silently, or shows a red list at the top that a screen reader never reaches,
or throws away everything the person typed, is a form people give up on. The people who give up
first are the ones who navigate differently from you.

---

## The concept in plain language

**The accessible error pattern has six parts, and each does a different job.**

| Part | What it does | Who it helps most |
|---|---|---|
| 1. The page title starts with `Error:` | Announced first when a page loads | Screen reader users on a server-returned page |
| 2. A summary at the top, with a heading and one link per problem | Shows how many problems and where | Everyone, and keyboard users most |
| 3. Focus moves to the summary | The person starts from the problems, not from the top of the page | Keyboard and screen reader users |
| 4. Each message sits next to its field, tied with `aria-describedby` | The message is read with the field | Screen reader users |
| 5. `aria-invalid="true"` on each field with a problem | The field is announced as invalid | Screen reader users |
| 6. The person's answers are kept | They fix one thing instead of retyping eight | Everyone |

Red colour is never the only signal. Every error has words, and every summary has a heading.

**tabindex, the three values that matter:**

| Value | Effect | Use it for |
|---|---|---|
| `tabindex="0"` | Adds an element that is not normally focusable to the tab order, in source order | A scrolling box a keyboard user needs to scroll |
| `tabindex="-1"` | Focusable by script, never by Tab | The error summary, which focus is moved to |
| `tabindex="1"` or higher | Pulled ahead of **everything** else on the page, in number order | Almost nothing. It is usually a mistake. |

The real fix for a bad tab order is a better source order.

---

## Worked example 1: the server's error page

In the template, a macro writes the two attributes when a field has a problem:

```html
<input id="email" name="email" type="email" required maxlength="254"
       value="{{ values.get('email', '') }}"{{ described("email", "email-hint") }}>
```

For a request with a bad email, the server sends, verified on the build machine:

```html
<p class="field-error" id="email-error"><span class="visually-hidden">Error: </span>Enter an email address in the form name@example.com.</p>
<input id="email" name="email" type="email" autocomplete="email" required maxlength="254"
       value="not-an-email" aria-describedby="email-hint email-error" aria-invalid="true">
```

The value is kept. The field is described by its hint **and** its error, in that order. The hidden
"Error: " makes a screen reader say the word even though sighted users see the colour and position.

The summary at the top:

```html
<div class="error-summary" id="error-summary" tabindex="-1" aria-labelledby="error-summary-title">
  <h2 id="error-summary-title">There are 7 problems with your sign-up</h2>
  <ul>
    <li><a href="#performer-name">Enter a stage name between 2 and 40 characters.</a></li>
    <li><a href="#email">Enter an email address in the form name@example.com.</a></li>
    ...
  </ul>
</div>
```

And one line at the bottom of `signup.js` moves focus there when the page arrives:

```js
document.querySelector("#error-summary")?.focus();
```

Verified: after a bypassed submission, the page title was `Error: Sign up · Open Mic Night` and the
focused element was `error-summary`.

Everything in the template is escaped by Flask. A stage name of `<b>Loud</b>` came back into the
input as the literal text `<b>Loud</b>`, not as bold.

---

## Worked example 2: the same pattern in the browser, before sending

```js
form.noValidate = true;

form.addEventListener("submit", (event) => {
  const errors = checkForm();
  if (Object.keys(errors).length > 0) {
    event.preventDefault();
    showErrors(errors);
  }
});
```

`checkForm()` applies the same rules as the server and returns the same sentences. `showErrors()`
builds the same summary and messages with `createElement` and `textContent`, sets the same
attributes, and calls `summary.focus()`.

**Why `noValidate` is set in the script and not in the HTML.** With the script running, it replaces
the browser's one-at-a-time bubbles with the full summary. If the script fails to load, the HTML
still has no `novalidate`, so the browser's own checks still protect the person.

Verified with an empty submit: no request was sent, focus moved to the summary, six controls were
marked invalid, and every id in every `aria-describedby` existed on the page.

---

## Worked example 3: a summary link that lands on the field

```js
document.addEventListener("click", (event) => {
  const link = event.target.closest(".error-summary a");
  if (!link) {
    return;
  }
  const target = document.getElementById(link.getAttribute("href").slice(1));
  if (target) {
    event.preventDefault();
    target.focus();
    (target.closest(".field, fieldset") || target).scrollIntoView();
  }
});
```

Clicking "Enter a stage name..." puts focus in the stage name input and scrolls its label into view,
so the person sees the question, not only the box. Verified: the focused element after the click was
`performer-name`. For a radio group, the link points at the first radio.

---

## The wrong version, and what it does

### A positive tabindex

```html
<input type="checkbox" id="agree" name="agree" value="yes" tabindex="1">
```

Tab from the address bar. Verified order on the lab form:

```
agree > performer-name > email > act-music
```

The last question on the page is now the first stop. Nobody reading the page expects that, and
every new field anyone adds later falls in behind it.

### A red list and nothing else

```html
{% if errors %}
<div class="errors" role="alert">
  <h2>Please fix the following:</h2>
  <ul>{% for message in errors.values() %}<li>{{ message }}</li>{% endfor %}</ul>
</div>
{% endif %}
<input id="name" name="name" type="text" required>
```

It passes the automated checker. It fails five of the six parts: no title, the messages are not
links, nothing is tied to its field, no field is marked invalid, and the answers are gone. A
screen reader user who Tabs to the name field hears "Your name, edit text" and nothing about what is
wrong with it. That is the Gate 2 W05 Requirements Fit defect.

---

## Why the wrong versions are tempting

A positive tabindex feels like a quick fix for an order that looks wrong, and it works on the one
page you tested. The red list is what error handling looks like in most tutorials, it looks
finished, and the checker says nothing. The only test that finds either problem is a person using
the keyboard, or a screen reader, on the form.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Error summary** | The box at the top that lists every problem as a link |
| **`aria-describedby`** | Points at the ids of elements that describe this one, read after its name |
| **`aria-invalid="true"`** | Marks a control's current value as wrong |
| **`tabindex="-1"`** | Focusable by script, not by Tab |
| **`tabindex="0"`** | In the tab order, in source order |
| **Positive tabindex** | Pulled ahead of everything. Usually a mistake. |
| **`novalidate`** | Turns off the browser's built-in checks for one form |
| **`event.preventDefault()`** | Stops the browser's default action, here the sending |
| **Visually hidden** | Text a screen reader reads that is not shown on screen |

---

## Self-check

**Question 1.** The error summary has `tabindex="-1"`. What would change with `tabindex="0"`, and
why is that worse?

**Question 2.** A field has `aria-describedby="email-hint email-error"`. What does a screen reader
read when a person Tabs to it?

**Question 3.** Why does the page title start with `Error:` when the page already has a red summary?

---

### Answers

**1.** With `0`, the summary becomes a Tab stop every time the page shows it, before the first
field, so a keyboard user who has moved on has to Tab past it again. With `-1`, script can put focus
there once, and Tab never lands on it again.

**2.** The label, "Email for your confirmation (required)", then the field type and state, including
invalid, then the hint and then the error message. The exact words depend on the screen reader.

**3.** The title is the first thing a screen reader announces when a new page loads, before anyone
reaches the summary. It tells the person at once that the submission did not go through.
