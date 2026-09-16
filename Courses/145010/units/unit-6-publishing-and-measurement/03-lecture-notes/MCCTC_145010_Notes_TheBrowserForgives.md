# Lecture Notes: The Browser Forgives. The Standard Does Not.
## 145010 Web Design · Unit 6 · Week 6, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W06_TheBrowserForgives.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-6-publishing-and-measurement/04-slides/MCCTC_145010_Slides_W06_TheBrowserForgives.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need
`05-labs/lab-w06-03-files/looks-fine/` and the course checker, `tools/web-check/check.js`.

**Competencies:** 6.5.1 implement web programming standards and protocols (W3C, HTML5) · 6.5.11
code a site for cross-platform and cross-browser compatibility and validation · 6.5.5 select an
integrated development environment.

---

## Why this exists

A compiler stops at your first mistake. A browser does not. Browsers were built to show whatever
they are given, because a browser that refused a slightly broken page would lose its users to one
that showed it.

So a browser repairs your markup and shows you the repair. Most of the time the repair is close to
what you meant. Some of the time it moves a list out of a paragraph, splits a card in two, or turns
a link to `shop map.html` into a link to `shop`. It never tells you.

**Validation is how you find out what you actually wrote.** Cross-browser testing is how you find
out what each browser does with it.

---

## The concept in plain language

**A standard is a written agreement about what markup means.** HTML is defined by the HTML Living
Standard, maintained by WHATWG. The W3C, the web's standards body, publishes CSS and many other
web standards and runs a free markup validator. "HTML5" is the name most people and most exam
questions use for modern HTML.

**Validation compares your source file to the standard.** It does not care how the page looks. It
reports markup that breaks the rules: tags closed in the wrong order, an element where it is not
allowed, an ID used twice, a required attribute missing.

**The standard also says how a browser must repair broken markup.** That is why modern engines
usually repair a broken page the same way. It is also why "it looks the same in two browsers" does
not mean "it is correct".

**Cross-browser testing** checks what different browser engines do with valid markup and your CSS
and script. The engine is what matters, not the logo:

| Browser | Engine |
|---|---|
| Chrome, Edge, Opera, Brave | Blink |
| Firefox | Gecko |
| Safari, and in most regions every other iPhone browser too **[VERIFY]** | WebKit |

**Two browsers on one engine are one test, not two.** Testing in Chrome and Edge tells you about
Blink twice. A Windows lab has no WebKit, so you cannot test Safari here, and your report has to
say so.

---

## Worked example 1: a page that looks fine

`looks-fine/club.html` opens in Chrome with a header, a list, two cards, a picture, and a footer.
Most people call it finished. Run the checker:

```
node tools/web-check/check.js 05-labs/lab-w06-03-files/looks-fine/club.html
```

Real output, from the build machine:

```
FAIL  .../looks-fine/club.html
  validation: 9 error(s), 0 warning(s)
    line 12:6  deprecated  <center> is deprecated: use CSS instead
    line 12:6  element-permitted-content  <center> element is not permitted as content under <header>
    line 16:6  no-implicit-close  Element <p> is implicitly closed by adjacent <ul>
    line 22:6  close-order  Stray end tag '</p>'
    line 28:52  element-permitted-content  <a> element is not permitted as a descendant of <a>
    line 36:13  no-dup-id  Duplicate ID "roles"
    line 37:6  wcag/h37  <img> is missing required "alt" attribute
    line 38:43  attr-quotes  Attribute "href" using unquoted value
    line 39:6  close-order  Stray end tag '</div>'
  axe at 360px: 1 violation(s)
    image-alt (critical, 1 node(s))  Images must have alternative text  e.g. img
```

(The axe line repeats at 768 and 1280.) Nine problems in a page that "looks fine".

---

## Worked example 2: what the browser built instead

Open DevTools, Elements panel. Compare with the source. On the build machine, Chrome built:

| In the source | In the page Chrome built | What it costs |
|---|---|---|
| A `<ul>` inside a `<p>` | The `<p>` closed before the list, and an extra empty `<p></p>` after it | Spacing you did not ask for, and an empty paragraph a screen reader may land on |
| A link inside a card that is itself a link | The card split into three siblings: a link, a paragraph, a link | The middle card is visibly broken if you look |
| `<a href=shop map.html>` | `href="shop"`, plus an attribute named `map.html` | The link goes to a page called `shop`, which does not exist |
| Two headings with `id="roles"` | Both kept. `#roles` finds the first one | A "jump to where we meet" link would land on "Team roles" |

None of those produced a message in the browser.

---

## Worked example 3: two engines, one repair

The instructor tool loads a page in Chrome and in Firefox and fingerprints the tree each one built:

```
node 05-labs/instructor/two_engines.js 05-labs/lab-w06-03-files/looks-fine/club.html
```

Build machine output:

```
chrome   Chrome/153.0.8010.48    360px  overflow 0px  elements 35  dom 025f9ff189
...
firefox  firefox/156.0           360px  overflow 0px  elements 35  dom 025f9ff189
...
Same dom fingerprint in both engines means both rebuilt the page into the same tree.
It does not mean the tree is the one you meant. Validate the source.
```

Blink and Gecko agreed on every repair. **Agreement is not correctness.** Both built the broken
card, and both sent the shop map link to `shop`. After the fix, both engines again agree with each
other, on a different fingerprint and 34 elements, and this time the tree is the one you wrote.

---

## Worked example 4: what cross-browser testing actually checks

Engines agree on parsing far more than they agree on everything else. Your matrix is where you look
for the rest:

| Check | Why it can differ |
|---|---|
| Layout at 360, 768, 1280 | Newer CSS features arrive in engines at different times |
| Keyboard only: Tab through every page | Focus styles and focus order are drawn by the browser |
| Video plays, captions toggle | Engines support different media formats and draw different controls |
| Form controls | Date pickers, number spinners, and validation messages look and behave differently |
| The feedback form sends | Script features and privacy settings vary |

A row in your matrix says what you checked and what you saw, in words. "Looks good" is not a row.

---

## Worked example 5: your editor is a checker too

**6.5.5, choosing an IDE,** is a real decision, not a formality. You already use VS Code. For web
work it earns its place with four things you should turn on today:

- **The Problems panel** (Ctrl+Shift+M) lists errors from every checker the editor runs.
- **Format Document** (Shift+Alt+F on Windows) re-indents a file, which makes a misplaced closing
  tag visible.
- **Emmet abbreviations**, built in: type `ul>li*3` and accept the suggestion that appears.
  It is off for Gate 1 reps, because Gate 1 has no autocomplete.
- **An HTML validation extension**, if your lab allows one. **[VERIFY]** which extension the lab
  machines have. VS Code checks CSS and JavaScript as you type; its built-in HTML support
  completes and formats tags, and a validator extension or `web-check` is what catches invalid
  nesting.

The reason to pick an IDE for a job: it should catch this week's mistakes while you type, before a
checker or a visitor does.

---

## The wrong version: validating what DevTools shows you

It is tempting to copy the page out of the Elements panel ("Copy outerHTML") and validate that.
On the build machine, the copied version of `club.html` reported **6** errors instead of 9:

```
line 11:6  deprecated  <center> is deprecated: use CSS instead
line 11:6  element-permitted-content  <center> element is not permitted as content under <header>
line 28:1  no-trailing-whitespace  Trailing whitespace
line 35:13  no-dup-id  Duplicate ID "roles"
line 36:6  wcag/h37  <img> is missing required "alt" attribute
line 38:1  no-trailing-whitespace  Trailing whitespace
```

The list-inside-paragraph, both stray end tags, the link inside a link, and the unquoted address
**all disappeared**, because the browser had already repaired them. Two new complaints about
whitespace appeared that are not in your file at all.

### Write this down

> Validate the file you wrote, not the page the browser built.

---

## Why the wrong version is tempting

DevTools is where you debug everything else, and the Elements panel looks like your code. It is
not your code. It is the browser's repaired tree, and it has already hidden the mistakes you are
looking for.

The same trap appears on a site built from a template: validate the files in `site/`, then fix the
errors in `content/` and `template.html`.

---

## Vocabulary

| Term | What it means |
|---|---|
| **W3C** | The World Wide Web Consortium. Publishes web standards and runs a markup validator. |
| **WHATWG** | The group that maintains the HTML Living Standard. |
| **HTML5** | The common name for modern HTML. |
| **Validation** | Checking a source file against the standard's rules. |
| **Error recovery** | The browser's repair of broken markup, which the standard describes. |
| **Rendering engine** | The part of a browser that parses and draws pages: Blink, Gecko, WebKit. |
| **Cross-browser testing** | Checking behavior in more than one engine, by hand, with written results. |
| **Deprecated** | Still recognized, no longer allowed in new work. `<center>` is one. |
| **IDE** | Integrated development environment. An editor with checking, running, and debugging built in. |

---

## Self-check

**Question 1.** A page passes in Chrome and in Edge. Your teammate writes "tested in two browsers,
cross-browser complete." What is wrong with that sentence?

**Question 2.** `club.html` has `<a href=shop map.html>`. The link text says "shop map". Where does
the link go in Chrome and Firefox, and why does neither browser warn you?

**Question 3.** Why does validating the Elements panel copy report fewer errors than validating the
file?

---

### Answers

**1.** Chrome and Edge both use the Blink engine, so that is one engine tested twice. Cross-browser
testing needs different engines, at least Gecko as well, and an honest note that WebKit (Safari)
was not tested on a Windows lab machine.

**2.** It goes to `shop`. An unquoted attribute value ends at the first space, so the value is
`shop` and `map.html` becomes a separate, meaningless attribute. The standard says how to repair
that, both engines follow it, and neither reports repairs to the visitor.

**3.** The Elements panel shows the tree after the browser's error recovery. Misnested and stray
tags have already been moved or dropped, so the validator never sees them. Only the source file
still contains the mistakes.
