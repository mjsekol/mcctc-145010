# Lecture Notes: Attaching CSS and the Cascade
## 145010 Web Design & Senior Capstone · Week 2 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W02_TheCascade.md) · no exported deck yet. Generate it from the repository root with `node tools/gamma.js Courses/145010/units/unit-2-modern-css/04-slides/MCCTC_145010_Slides_W02_TheCascade.md --export pptx`

If you missed class, you can learn this concept from this file alone. The pages used below are
in [examples/mon-cascade/](examples/mon-cascade/). Open them in Chrome with DevTools open (F12).

**Competencies:** 6.1.7 (integrate styles, inline or external), 6.5.7 (create and attach CSS),
6.2.7 (a hover effect that changes the style of a link).

---

## Why this exists

Last week you built pages with structure and no appearance. That was on purpose. HTML says what
each piece of content **is**. CSS says how it **looks**. Keeping the two apart is why one
stylesheet can restyle fifty pages, and why a screen reader user gets the same content you do.

You already know this split from WPF: XAML describes the controls and a style resource describes
how they look. CSS is the web's version, with one difference that costs people hours. **When
two rules disagree, the browser does not complain. It quietly picks a winner.** Today is about
how it picks.

---

## The concept in plain language

**A rule is a selector plus declarations.**

```css
.theme {                /* selector: which elements            */
  color: #047857;       /* declaration: property and value     */
  font-weight: 700;     /* another declaration                 */
}
```

**Styles come from three places.**

| Where | How you write it | What it is good for |
|---|---|---|
| External | `<link rel="stylesheet" href="styles/site.css">` in the `head` | Almost everything. One file, every page. |
| Internal | a `<style>` block in the `head` | One page that genuinely differs, or a quick demo |
| Inline | a `style="..."` attribute on one element | One element, one time. Hard to find later. |

**The cascade picks one winner per property.** Not per rule. Per property. When two
declarations set the same property on the same element, the browser compares them in this order
and stops at the first difference:

1. **Inline beats any stylesheet rule** (unless a rule is marked with `!important`, which you
   should treat as a last resort and will rarely need).
2. **Specificity.** An id beats a class. A class beats an element name. `p.price` beats
   `.price`, because it has a class and an element.
3. **Order.** When specificity ties, the declaration that comes later wins. A `<style>` block
   after the `<link>` beats the linked file. Swap them and the linked file wins.

A property nobody sets falls back to what the element inherits from its parent, like `color`
and `font-family`, or to the browser default.

**Hover is a selector state.** `a:hover` matches a link while the pointer is over it.
`a:focus-visible` matches a link that has keyboard focus. Write both, with the same cue, or
keyboard users never see your effect.

---

## Worked example 1: three sources, one page

[examples/mon-cascade/index.html](examples/mon-cascade/index.html) links an external sheet,
then has a `<style>` block, then one inline style.

```html
<link rel="stylesheet" href="styles/site.css">
<style>
  .theme { color: #6d28d9; }
</style>
...
<li>Monday: <span class="theme">Pajama Day</span></li>
<li>Wednesday: <span class="theme" style="color: #b0001d;">Decades Day</span></li>
```

`styles/site.css` says:

```css
.theme {
  color: #047857;
  font-weight: 700;
}
```

What Chrome computed, read from the page on the build machine:

```
Pajama Day   color rgb(109, 40, 217)   font-weight 700
Decades Day  color rgb(176, 0, 29)     font-weight 700
```

Read it property by property. **Color:** the external sheet says green and the `<style>` block
says purple. Same selector, same specificity, and the `<style>` block comes later, so purple
wins for Pajama Day. On Decades Day the inline style beats both, so it is red. **Font weight:**
only the external sheet sets it, so it applies to both. The external rule lost one property and
won the other.

In DevTools, select Pajama Day. The Styles pane lists both `.theme` rules, and the `color` line
in the losing rule is struck through. That strike-through is the cascade showing its work.

---

## Worked example 2: the same two rules in the other order

Move the `<style>` block above the `<link>`:

```html
<style> .theme { color: purple; } </style>
<link rel="stylesheet" href="css/spirit.css">   <!-- .theme { color: green; } -->
```

Computed color on the build machine: `rgb(0, 128, 0)`, green. Nothing changed except order.
When specificity ties, later wins.

---

## Worked example 3: specificity beats order

```html
<style>
  #rules p { color: green; }
  .note    { color: blue; }
  p        { color: red; }
</style>

<p class="note">A</p>
<section id="rules"><p>B</p><p class="note">C</p></section>
<p>D</p>
```

Computed on the build machine:

```
A  rgb(0, 0, 255)    blue:  .note beats p
B  rgb(0, 128, 0)    green: #rules p has an id
C  rgb(0, 128, 0)    green: an id beats a class, even though .note matches too
D  rgb(255, 0, 0)    red:   only p matches
```

`p` comes last in the block and still loses three times. Order only breaks ties.

---

## Worked example 4: hover and keyboard focus

```css
a:hover,
a:focus-visible {
  color: #ffffff;
  background-color: #1d4ed8;
}

a:focus-visible {
  outline: 3px solid #b45309;
  outline-offset: 2px;
}
```

Now the wrong version, with `:hover` only:

```css
a { color: #0b6e69; }
a:hover { color: #ffffff; background-color: #4b2a91; }
```

On the build machine, a headless Chrome pressed Tab until the link had focus and read its
styles, then moved the mouse onto the link and read them again:

```
after Tab    background rgba(0, 0, 0, 0)    outline auto 1px
after hover  background rgb(75, 42, 145)    outline auto 1px
```

The keyboard user gets the browser's thin default ring and none of your effect. `:focus-visible`
fixes that, and it only matches when the browser decides a focus ring is useful, which is why a
mouse click does not light it up.

---

## The wrong version, and exactly what goes wrong

[examples/mon-cascade/wrong-path.html](examples/mon-cascade/wrong-path.html) links a file that is
not there:

```html
<link rel="stylesheet" href="css/style.css">
```

The real file is `styles/site.css`. **The page loads anyway.** No error appears on the page.
It renders in Times New Roman with a black heading, because the only styles left are the
browser's defaults and the one `<style>` block.

The evidence is in two places, and neither is the page:

- **DevTools Console:** `Failed to load resource: net::ERR_FILE_NOT_FOUND`
- **DevTools Network tab:** the `style.css` request is listed as failed. Headless Chrome
  reported it as `net::ERR_FILE_NOT_FOUND`.

And the checkers disagree with each other:

```
node tools/web-check/check.js .../wrong-path.html
PASS  ... validation: 0 error(s) ... axe at 360px: 0 violation(s) ...

python .../structure_check.py .../wrong-path.html
FAIL  ...
  FAIL FILES     line 7: <link href="css/style.css"> points at a file that is not there
```

`web-check` passes this page. Valid HTML with no styling is still valid HTML, and an unstyled
page is often perfectly accessible. `structure_check` looks for the file and fails it. **A PASS
from one tool means that tool found nothing. It does not mean nothing is wrong.**

---

## Why the wrong version is tempting

Paths feel obvious when you type them. You named the folder `styles` an hour ago and your hands
typed `css`, because every tutorial you have ever seen uses `css`. The browser gives you no
error on the page, so the failure looks like "my CSS does nothing" instead of "my CSS never
loaded", and people spend twenty minutes editing rules in a file the page never read.

The habit that prevents it: **after you add a `<link>`, add one loud rule and check it shows.**
Then open the Console before you blame your selectors.

A second temptation: fixing a stubborn rule with an inline style or `!important`. It works, and
it makes the next change harder, because now the winner is hiding in the HTML. Find out **why**
the rule lost first. The Styles pane tells you.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Rule** | A selector plus a block of declarations |
| **Selector** | The part that says which elements a rule applies to |
| **Declaration** | One `property: value;` pair |
| **External stylesheet** | A `.css` file attached with `<link rel="stylesheet">` |
| **Internal stylesheet** | CSS inside a `<style>` element in the page |
| **Inline style** | CSS in an element's `style` attribute |
| **Cascade** | The process that picks one winning value per property per element |
| **Specificity** | The weight of a selector: ids, then classes and states, then element names |
| **Inheritance** | Some properties, like `color`, pass from parent to child when nothing sets them |
| **Pseudo-class** | A state selector such as `:hover` or `:focus-visible` |
| **Computed value** | The value the browser actually used, shown in DevTools under Computed |

---

## Self-check

**Question 1.** A `<style>` block says `.price { color: blue; }` and comes after a linked sheet
that says `p.price { color: orange; }`. What color is `<p class="price">`, and why?

**Question 2.** Your stylesheet is linked, the page looks unstyled, and `web-check` says PASS.
Name the two places you look first and what each would show if the path is wrong.

**Question 3.** A classmate writes only `a:hover { background: purple; }` and says the effect
works. Describe the test that proves it does not work for everyone, and the one-line fix.

---

### Answers

**1.** Orange. `p.price` has an element and a class, so it is more specific than `.price`.
Order only matters when specificity ties. Verified on the build machine:
`rgb(255, 165, 0)`.

**2.** The Console, which shows `Failed to load resource: net::ERR_FILE_NOT_FOUND`, and the
Network tab, which shows the stylesheet request failing. `structure_check` also reports a
`FILES` failure for the `<link>` line. `web-check` does not look.

**3.** Put the mouse down and press Tab until the link has focus. The background does not
change. The fix is adding `a:focus-visible` to the same rule, so the selector reads
`a:hover, a:focus-visible`.
