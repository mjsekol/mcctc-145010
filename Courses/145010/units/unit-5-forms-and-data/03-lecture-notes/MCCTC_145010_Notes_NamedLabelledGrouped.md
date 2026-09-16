# Lecture Notes: A Form Is Named, Labelled, Grouped Controls
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W05_NamedControls.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-5-forms-and-data/04-slides/MCCTC_145010_Slides_W05_NamedControls.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need the Week 5 lab app
running: in `05-labs/lab-w05-files/`, `python app.py --port 8405 --reset`.

**Competencies:** 6.4.1 design a data entry form from specifications · 6.4.2 add a form to a web
page · 6.4.3 add text fields, radio buttons, check boxes, and drop-down menus · 6.4.5 add working
submit and reset buttons · 6.4.6 format a form with fieldset.

---

## Why this exists

Every sign-up, order, survey, and login you have ever used is a form. For three weeks your pages
showed information. From today they collect it, and collected information goes somewhere: a server,
a database, a person who acts on it.

Getting the markup right matters twice. A form with a mislabelled control is a form some people
cannot fill in. A form with a missing `name` is a form that loses data without telling anyone.

---

## The concept in plain language

**A form is a container with an address.** `<form action="/echo" method="get">` says where the
answers go and how. Tuesday is about that. Today is about what goes inside.

**Every control that should be sent needs a `name`.** When the form is submitted, the browser walks
its controls and, for each one that has a `name` and a value, adds `name=value` to the request.
Nothing else is sent.

**Every control needs a label.** `<label for="email">` points at `<input id="email">`. Clicking the
label focuses the control, and a screen reader reads the label with it. `id` is for the label.
`name` is for the server. Most controls need both.

**Related controls are grouped.** `<fieldset>` wraps them and `<legend>` names the group. A screen
reader reads the legend with each control inside, which is what makes "Music" make sense as an
answer to "Kind of act."

**The control types, and what each sends:**

| Control | Markup | What it sends |
|---|---|---|
| Text | `<input type="text" name="performer_name">` | `performer_name=` whatever was typed |
| Email | `<input type="email" name="email">` | The text typed. The type adds a format check and a phone keyboard with `@`. |
| Number | `<input type="number" name="minutes" min="1" max="8">` | The number. If what was typed is not a number, the name is sent with an empty value. |
| Radio group | several `<input type="radio" name="act_type" value="...">` with **one shared name** | The one chosen value, or nothing if none is chosen |
| Checkbox group | several `<input type="checkbox" name="needs" value="...">` with one shared name | One pair per ticked box, so the name can arrive several times |
| Single checkbox | `<input type="checkbox" name="agree" value="yes">` | `agree=yes` if ticked, **nothing at all** if not |
| Drop-down | `<select name="slot">` with `<option value="1">7:00 pm</option>` | The chosen option's `value`, not its text |
| Text area | `<textarea name="notes"></textarea>` | Whatever was typed |
| Submit | `<button type="submit">Sign up</button>` | Sends the form |
| Reset | `<button type="reset">Reset the form</button>` | Returns every control to the value the page loaded with. Sends nothing. |

---

## Worked example 1: the smallest honest form

```html
<form action="/echo" method="get">
  <label for="performer-name">Stage name (required)</label>
  <input id="performer-name" name="performer_name" type="text" required maxlength="40">
  <button type="submit">Sign up</button>
</form>
```

Type `Nova Park` and press Enter. The browser goes to:

```
/echo?performer_name=Nova+Park
```

The lab app's echo page shows one row: `performer_name` and `Nova Park`. A space in a value is
written as `+` in the address. Pressing Enter in a text field submits the form too, so test with
the keyboard as well as the button.

---

## Worked example 2: a radio group and a checkbox group in fieldsets

```html
<fieldset>
  <legend>Kind of act (required)</legend>
  <div class="choice">
    <input type="radio" id="act-music" name="act_type" value="music" required>
    <label for="act-music">Music</label>
  </div>
  <div class="choice">
    <input type="radio" id="act-poetry" name="act_type" value="poetry" required>
    <label for="act-poetry">Poetry</label>
  </div>
</fieldset>

<fieldset>
  <legend>What you need from us (optional)</legend>
  <div class="choice">
    <input type="checkbox" id="need-mic" name="needs" value="mic">
    <label for="need-mic">A microphone</label>
  </div>
  <div class="choice">
    <input type="checkbox" id="need-amp" name="needs" value="amp">
    <label for="need-amp">An amplifier</label>
  </div>
</fieldset>
```

Choose Poetry and tick both boxes. The address part after `?` is:

```
act_type=poetry&needs=mic&needs=amp
```

`needs` arrives twice. In Flask, `request.form.getlist("needs")` returns both, as a list.
`request.form.get("needs")` returns only the first, which is a real bug when you forget.

Inside a radio group, Tab lands on the group once and the arrow keys move between the choices.
That is how every browser does it, and it is why a radio group needs its shared name.

---

## Worked example 3: a drop-down whose value is not its text

```html
<label for="slot">Time slot (required)</label>
<select id="slot" name="slot" required>
  <option value="">Choose a time</option>
  <option value="1">7:00 pm</option>
  <option value="2">7:20 pm</option>
</select>
```

Choose 7:20 pm. The request carries `slot=2`. The person reads the text. The server reads the
value, which here is the slot's id in the database. The first option has an empty value, so with
`required`, a person who never chose gets stopped by the browser.

---

## The wrong version, twice

### The input with no name

```html
<label for="email">Email</label>
<input id="email" type="email" value="nova@example.com">
```

Submit, and the address is `/echo?performer_name=Nova+Park`. The email is not there. **There is no
error anywhere.** The person typed it, the page showed it, and the server never received it. Verified
on the build machine: the echo page listed every named control and no email.

### Radio buttons with different names

```html
<input type="radio" id="size-s" name="size_s" value="S">
<input type="radio" id="size-m" name="size_m" value="M">
```

Both can be checked at once. Verified in Chrome: after clicking both, both stayed checked. The
browser saw two groups of one.

---

## Why the wrong versions are tempting

You write `id` for the label and for CSS, and the form looks and works in the browser. Nothing tells
you that the server sees something different. The habit that prevents it: **submit to the echo page
before you write any server code**, and read every row.

Different radio names happen when people copy one radio button and change everything on the copy,
including the name. Being in the same fieldset feels like being in the same group. It is not.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Form** | A container of controls with an `action` and a `method` |
| **Control** | Anything a person fills in or chooses: input, select, textarea, button |
| **`name`** | The key the server receives. No name, not sent. |
| **`value`** | What is sent for that name. For a radio or checkbox, fixed in the markup. |
| **Label** | Text tied to a control with `for` and `id` |
| **Fieldset and legend** | A group of related controls, and the group's name, read with each control |
| **Radio group** | Radios sharing one name. One can be chosen. |
| **Submit button** | Sends the form. Enter in a text field does the same. |
| **Reset button** | Returns controls to the values the page loaded with |

---

## Self-check

**Question 1.** A checkbox `<input type="checkbox" name="agree" value="yes">` is not ticked. What
does the server receive for `agree`?

**Question 2.** Why does a drop-down send `slot=2` when the person chose "7:20 pm"?

**Question 3.** A form has a text input with `id="nickname"` and a label, and the server says the
nickname is always empty. What is the most likely cause, and how do you confirm it in ten seconds?

---

### Answers

**1.** Nothing. An unticked checkbox is not sent at all, so `request.form.get("agree")` is `None`.

**2.** A select sends the chosen option's `value` attribute, and that option was written as
`<option value="2">7:20 pm</option>`. The text is for the person.

**3.** The input has no `name`. Submit the form to `/echo` with GET and read the address: if
`nickname` is not in it, the browser never sent it.
