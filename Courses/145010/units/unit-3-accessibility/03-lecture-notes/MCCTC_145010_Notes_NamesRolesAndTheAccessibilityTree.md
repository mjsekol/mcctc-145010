# Lecture Notes: Names, Roles, and the Accessibility Tree
## 145010 Web Design & Senior Capstone · Week 3 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W03_NamesAndRoles.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-3-accessibility/04-slides/MCCTC_145010_Slides_W03_NamesAndRoles.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome and `web-check`.

**Competencies:** 2.7.4 (how screen readers and text-to-speech change the function of a page), 6.1.2
(plan a page's layout, links, and graphics for ADA requirements).

---

## Why this exists

A screen reader does not look at your page. It never sees a pixel. It asks the browser a question about
every element, and the browser answers with three things:

- a **role**: what kind of thing this is, such as heading, link, button, textbox, image, list
- a **name**: what this particular one is called, such as "Sign up" or "Email"
- sometimes a **state**: checked, expanded, required, disabled

The browser builds all of those answers into a structure called the **accessibility tree**. It is a
second version of your page, built from your HTML, and it is the only version a screen reader user
ever gets.

In Week 1 you learned that structure comes first and appearance later. Today is why. **The accessibility
tree is built from structure. CSS barely touches it.** A bold div looks like a heading and is not one in
the tree. A button with only an icon looks like a button and has no name in the tree.

---

## The concept in plain language

**Every element that matters needs a role and a name, and the right HTML element gives you both.**

| You write | Role in the tree | Where the name comes from |
|---|---|---|
| `<h2>Pantry hours</h2>` | heading, level 2 | its text |
| `<a href="#visit">Directions to the side door</a>` | link | its text |
| `<button type="submit">Sign up</button>` | button | its text |
| `<img src="map.svg" alt="Map: use the side door...">` | image | its `alt` |
| `<img src="logo.svg" alt="">` | **none**. Removed from the tree | decorative on purpose |
| `<label for="email">Email</label><input id="email">` | textbox | the label |
| `<fieldset><legend>Have you volunteered before?</legend>` | group | the legend |
| `<nav aria-label="Main">` | navigation landmark | the `aria-label` |
| `<div class="section-title">Shifts</div>` | **generic**. No role a screen reader moves to | none |

### Landmarks

`<header>`, `<nav>`, `<main>`, and `<footer>` become **landmarks** in the tree: banner, navigation,
main, and content info. Screen reader users jump between them the way you glance at the top of a page
and then down to the middle. A page built from divs has no landmarks at all.

### Headings are the table of contents

Screen reader users commonly move through a page by heading. The heading list is their table of
contents. Levels should form an outline: one h1, then h2s under it, h3s under those. **This course's
standard is that levels never skip.** WCAG 2.2 has no criterion that says exactly that; a skipped level
is widely treated as a structure problem, and you will be asked to say so precisely.

### Alternative text

`alt` answers one question: **if the image were gone, what would the reader need to know?**

- An informative image gets alt text that carries its information.
- A decorative image gets `alt=""`, empty, which removes it from the tree.
- An image of text should not exist. Use text. If you cannot, the alt text is that text.
- A missing `alt` attribute is different from an empty one. With no attribute, many screen readers read
  the file name.

### Labels

A form field's name comes from its `<label>`. The `for` on the label must match the `id` on the field,
character for character. A label that is visible and tied to its field helps everyone: screen reader
users hear it, voice control users can say it, and anyone can click the label text to focus the field.

---

## Worked example 1: the tool catches a missing name

The Week 3 swap board has four round buttons with an icon and no name.

```html
<button class="accept"><img src="check-icon.svg" alt=""></button>
```

```
node tools/web-check/check.js Courses/145010/units/unit-3-accessibility/05-labs/lab-w03-02-files/swap-board.html --widths 360
```

Part of the output:

```
    line 48:10  text-content  <button> must have accessible text
  axe at 360px: 2 violation(s)
    button-name (critical, 4 node(s))  Buttons must have discernible text  e.g. .urgent > .actions > .accept | .urgent > .actions > .decline | .normal > .actions > .accept
```

The image is empty-alt, so it adds nothing to the button's name, and the button has no text. The fix is
a name in the image's `alt`, and a good one says what the button does **and** to what:

```html
<button type="button" class="accept"><img src="check-icon.svg" alt="Accept Maya R.'s Friday swap"></button>
```

After the fix, Chrome's accessibility tree gives the button the role `button` and the name
`Accept Maya R.'s Friday swap`.

---

## Worked example 2: a name that exists but helps nobody

A team page with one photo:

```html
<img src="team.svg" width="200" height="200" alt="DSC_0419.jpg">
```

web-check, on that page, with the path shortened to the file name:

```
PASS  alt-filename.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
```

**It passes.** The attribute exists and is not empty. A screen reader user hears the file name,
spelled out or run together, depending on the screen reader. The same page with the attribute deleted entirely:

```
FAIL  alt-missing.html
  validation: 1 error(s), 0 warning(s)
    line 11:6  wcag/h37  <img> is missing required "alt" attribute
  axe at 360px: 1 violation(s)
    image-alt (critical, 1 node(s))  Images must have alternative text  e.g. img
```

A tool can tell whether a name exists. **It cannot tell whether the name means anything.** That half of
the job is yours.

---

## Worked example 3: the tool reads a placeholder as a name

On the Lantern Street page, the name field has no label, only a placeholder:

```html
<input type="text" name="name" class="req" placeholder="Your name">
```

Chrome's accessibility tree, read with a script on the build machine, gives it:

```
textbox "Your name"
```

The browser used the placeholder as the name, so axe's `label` rule passed it. A screen reader user
hears "Your name." So what is wrong?

Type one letter. The placeholder disappears. A sighted person who looks away and back no longer knows
what the box was for. Placeholder text is often pale. And voice control users have no visible label to
say. **3.3.2 Labels or Instructions** asks for labels or instructions when content requires input, and a
hint that vanishes the moment you start does not do the job.

The fix is a visible label that stays:

```html
<label for="volunteer-name">Your name</label>
<input type="text" id="volunteer-name" name="name" autocomplete="name" required>
```

---

## The wrong version: hiding the label to keep the design clean

A student wants the clean look of a placeholder and a label for the screen reader, so they write:

```html
<label for="n" style="display:none">Name</label>
<input type="text" id="n">
```

web-check on a test page containing only that label and field, part of the output:

```
  axe at 1280px: 1 violation(s)
    label (critical, 1 node(s))  Form elements must have labels  e.g. #n
```

`display: none` removes an element from the page **and** from the accessibility tree. The label exists in
the HTML and in nobody's experience. The tool is right to fail it.

If a label truly must be visually hidden, there is a CSS pattern for hiding something from the eye while
keeping it in the tree. That is an EXTENDED topic, and it is rarely the right call for a form field,
because sighted users need the label too.

---

## Why the wrong version is tempting

**Designs are often drawn without labels.** Mockups use placeholders because they look clean at small
sizes. The developer's job is to push back.

**The tool sometimes agrees with you.** The placeholder-only field passed. It is tempting to read a pass as
"correct" when it only means "not detectably wrong."

**Divs are flexible.** A div can be styled into anything, so it is tempting to build everything from
divs and style them into headings and buttons. The accessibility tree does not care how it looks.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Accessibility tree** | The browser's structure of roles, names, and states, built from your HTML, that assistive technology reads |
| **Role** | What kind of thing an element is: heading, link, button, textbox, image |
| **Accessible name** | What a particular element is called in the tree |
| **State** | A changing property: checked, expanded, required |
| **Landmark** | A region a screen reader can jump to: banner, navigation, main, content info |
| **Alternative text** | The `alt` attribute: the text that replaces an image in the tree |
| **Decorative image** | An image that adds no information. It gets `alt=""` |
| **Placeholder** | Hint text inside a field that disappears on input. Not a label |
| **`<fieldset>` and `<legend>`** | A group of related controls and the question that names the group |
| **ARIA** | Accessible Rich Internet Applications: attributes like `aria-label` that change the tree. Use HTML first |

---

## Self-check

**Question 1.** For each, say what a screen reader receives as the name: (a) `<img src="logo.svg"
alt="">` next to the organization's name in text, (b) `<img src="logo.svg">`, (c) `<img src="map.svg"
alt="map">` on a page whose only directions are in the map.

**Question 2.** web-check reports `label (critical, 1 node(s))  Form elements must have labels  e.g.
#volunteer-email` on a page where you can see the word "Email" right above the box. Give two likely
causes.

**Question 3.** Why does a page built entirely from styled divs look correct and pass many automated
checks, yet leave a screen reader user with almost nothing to navigate by?

---

### Answers

**1.** (a) Nothing. The image is removed from the tree, which is correct because the name is already
there as text. (b) No `alt` at all. The tool fails it, and many screen readers fall back to announcing
the file name. (c) "map." The attribute exists, so tools pass it, but it carries none of the directions.
It fails 1.1.1 Non-text Content in a way only a person catches.

**2.** The label's `for` does not match the input's `id` exactly, for example `for="email"` and
`id="volunteer-email"`. Or the word "Email" is not a `<label>` at all, such as a `<p>` or a `<span>`
placed above the box, which looks the same and is not tied to the field.

**3.** CSS controls how divs look, and the accessibility tree is built from what elements are. Styled
divs are generic in the tree: no headings to jump between, no landmarks, no button roles. Automated
rules check for things that are present and wrong, such as an image with no `alt`. A page with no
headings or landmarks often has nothing present for those rules to fail, and the rules that ask for
landmarks are best-practice rules that web-check does not run.
