# Clinic · Reading a Web-Check Report
## 145010 Senior Capstone · Week 12, Monday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 12, Monday, or any week the room shows this signal: test plan runs
that say "web-check: failed" and no follow-up.
**If you missed it,** you can learn the skill from this file alone. The two pages are in
[`clinic-w12-webcheck/`](clinic-w12-webcheck/).
**Competencies:** 6.5.11 (cross-platform and cross-browser compatibility and validation), 6.5.1
(web standards, W3C and HTML5), 2.7.4 (how browsers and devices affect a page, including screen
readers), 6.1.2 (plan a page for devices, audience, and ADA requirements), 2.12.5 (make corrections
indicated by test results), 2.11.4 (gather and analyze data about a problem)

---

## Why this exists

**"web-check: failed" is not a test result.** It is the start of one. Your test plan needs to say
what failed, which requirement it breaks, and what you did about it. A result nobody reads is a
result nobody fixes.

Your signed agreement almost certainly has an accessibility criterion (NF3 in the composite project).
Every page that fails web-check is a signed criterion failing today. **The report tells you exactly
where**, if you know how to read it.

And the report has limits. A page can pass and still be hard to use with a keyboard or a screen
reader. This clinic shows you one of those, found on the build machine.

---

## The skill in plain language

From the repository root:

```
node tools/web-check/check.js <page.html> [--widths 360,768,1280]
```

The report has **three kinds of finding**. Read them in this order.

| Kind | Looks like | Comes from | What it means |
|---|---|---|---|
| **Validation error** | `line 2:2  element-required-attributes  ...` | html-validate | The markup breaks an HTML rule. The line and column point at it. |
| **Axe violation** | `color-contrast (serious, 1 node(s))  ...  e.g. p` | axe-core, WCAG A and AA rules, in headless Chrome | Something a disabled user will hit. `e.g.` names the element. |
| **Overflow** | `OVERFLOWS by 288px` | the page's width against the window's | The page is wider than the screen at that width. It is not responsive there. |

**Exit code 0 means all three are zero at every width.** Anything else is exit code 1.

**How to work a failing report:**

1. Fix validation errors first. Broken markup can cause axe findings that disappear once it is fixed.
2. **Fix one thing. Re-run.** Do not fix six things and hope.
3. The same axe rule at every width is **one problem**, not three.
4. Record what the report said, what you changed, and the re-run, in your test plan's results.

---

## Worked example 1 · the broken page

**A composite page for the composite Parts Bin Board.**
[`broken.html`](clinic-w12-webcheck/broken.html):

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Parts Bin Board: report a low bin</title>
<style>
  .hint { color: #b5b5b5; }
  .shelf { width: 640px; }
</style>
</head>
<body>
<main>
<h1>Report a low bin</h1>
<p class="hint">No name needed. The coordinator sees this list on open-shop night.</p>
<form action="/report" method="post">
  <select name="bin">
    <option value="B-01">B-01 Tubes, 26 inch</option>
    <option value="B-02">B-02 Brake pads, rim</option>
  </select>
  <input type="text" name="note" id="note" maxlength="120" placeholder="Optional note">
  <button type="submit">Mark low</button>
</form>
<div class="shelf" id="note">Shelf map: B-01 to B-12, left to right</div>
</main>
</body>
</html>
```

The real report from the build machine:

```
node tools/web-check/check.js Courses/145010/capstone/03-lecture-notes/clinic-w12-webcheck/broken.html
```

```
FAIL  Courses/145010/capstone/03-lecture-notes/clinic-w12-webcheck/broken.html
  validation: 2 error(s), 0 warning(s)
    line 2:2  element-required-attributes  <html> is missing required "lang" attribute
    line 24:24  no-dup-id  Duplicate ID "note"
  axe at 360px: 3 violation(s), OVERFLOWS by 288px
    color-contrast (serious, 1 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. p
    html-has-lang (serious, 1 node(s))  <html> element must have a lang attribute  e.g. html
    select-name (critical, 1 node(s))  Select element must have an accessible name  e.g. select
  axe at 768px: 3 violation(s)
    color-contrast (serious, 1 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. p
    html-has-lang (serious, 1 node(s))  <html> element must have a lang attribute  e.g. html
    select-name (critical, 1 node(s))  Select element must have an accessible name  e.g. select
  axe at 1280px: 3 violation(s)
    color-contrast (serious, 1 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. p
    html-has-lang (serious, 1 node(s))  <html> element must have a lang attribute  e.g. html
    select-name (critical, 1 node(s))  Select element must have an accessible name  e.g. select
```

Exit code 1.

---

## Worked example 2 · reading it line by line

**Count the problems, not the lines.** There are nine axe lines and only three axe problems, plus two
validation errors and one overflow. That is six findings, and two of them are the same problem
under different names, so there are five fixes.

| Report says | Rule means | The fix |
|---|---|---|
| `element-required-attributes`, line 2, and `html-has-lang` | The page does not say what language it is in, so a screen reader may read it with the wrong voice | `<html lang="en">` |
| `no-dup-id`, line 24 | Two elements share `id="note"`. A label pointing at `note` cannot know which one | Remove the `id` from the shelf map |
| `color-contrast`, `e.g. p` | The hint text is too pale. Grey `#b5b5b5` on white is about 2 to 1. WCAG AA asks 4.5 to 1 for normal text | `#555555`, about 7.5 to 1 |
| `select-name`, `e.g. select` | The drop-down has no label, so a screen reader announces an unnamed list | A `<label for="bin">` and `id="bin"` |
| `OVERFLOWS by 288px` at 360 only | `.shelf` is 640 pixels wide. 640 plus the 8-pixel page margin, minus 360, is 288 | `max-width: 640px` |

**Fix the first one and re-run.** With only `lang="en"` added, at one width. (The first line of
the output, which names the file, is left out here.)

```
node tools/web-check/check.js <your copy> --widths 360
```

```
  validation: 1 error(s), 0 warning(s)
    line 24:24  no-dup-id  Duplicate ID "note"
  axe at 360px: 2 violation(s), OVERFLOWS by 288px
    color-contrast (serious, 1 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. p
    select-name (critical, 1 node(s))  Select element must have an accessible name  e.g. select
```

One change removed two findings, `element-required-attributes` and `html-has-lang`. That is why
you re-run after each fix: the list gets shorter, and you learn which findings were the same problem.

---

## Worked example 3 · the fixed page, and what the tool did not see

[`fixed.html`](clinic-w12-webcheck/fixed.html), the part that changed:

```html
<html lang="en">
...
  .hint { color: #555555; }
  .shelf { max-width: 640px; }
...
  <label for="bin">Which bin is low?</label>
  <select name="bin" id="bin">
  ...
  <label for="note">Note, optional, up to 120 characters</label>
  <input type="text" name="note" id="note" maxlength="120">
...
<p class="shelf">Shelf map: B-01 to B-12, left to right</p>
```

```
PASS  Courses/145010/capstone/03-lecture-notes/clinic-w12-webcheck/fixed.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

Exit code 0.

**Look back at the broken page's text box.** It had no label, only `placeholder="Optional note"`, and
axe never reported it. On the build machine, the same page with the placeholder removed did report
it: `label (critical, 1 node(s))  Form elements must have labels`. **Axe accepted the placeholder as
the box's name.** A human would not: the placeholder vanishes as soon as a volunteer starts typing,
and it never said the note is limited to 120 characters. The fixed page has a real label anyway.

**What web-check cannot tell you.** Whether a label makes sense. Whether the tab order follows the
page. Whether a screen reader user can finish the task. Whether alternative text describes the
image. Whether the page works on the co-op's actual desktop. Those are your keyboard and Narrator
walkthroughs, and they stay in your test plan.

---

## The wrong version, and what it costs

The wrong version is a test plan result like this:

```
| T-11 | NF3 | FAIL | web-check: failed |
```

It records nothing anyone can act on. Next week nobody knows whether it is the same failure or a new
one. **What it costs:** a signed criterion stays broken for weeks, and in Week 16 the stakeholder's
acceptance run finds it for you.

A useful result line:

```
| T-11 | NF3 | FAIL | report page: 2 validation errors, 3 axe rules (color-contrast, html-has-lang, select-name), overflow 288px at 360. Fixed in a1b2c3d, re-run PASS |
```

---

## Why the wrong version is tempting

**The report is long, and it looks worse than it is.** Nine axe lines feel like nine problems, so
students close the terminal. Counting by rule, it was three.

**"Failed" feels like the whole answer.** It is the first word of the answer.

---

## Do this today

1. Run web-check on every page your skeleton serves. Save each page's HTML from the browser, or
   render it the way your test plan says.
2. For each failure, write the rule id and the element in `docs/measure-analyze/test-plan.md`,
   section 6, as a new run block.
3. Fix one finding, re-run, repeat, until PASS.
4. Add one human check the tool cannot do: tab through the page with the keyboard only.
5. **Commit** the fixes and the results together.

---

## If you are ahead, if you are behind

**If you are ahead:** run with `--shots` into a folder outside your repository and look at the page
at 360 wide. Then do the Narrator walkthrough your test plan names, and record it.

**If you are behind:** run web-check on your home page only, today. One page, read properly, beats
five pages marked "failed."

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Validation** | Checking markup against HTML rules, the html-validate section (6.5.11) |
| **W3C, HTML5 standards** | The rules that validator enforces, such as a `lang` on `<html>` and unique ids (6.5.1) |
| **Cross-platform compatibility** | The page working at 360, 768, and 1280 wide, and on the named devices (6.5.11) |
| **Screen reader** | Software that reads the page aloud, which needs labels and a language (2.7.4) |
| **ADA requirements** | Accessibility the page is planned for from the start (6.1.2) |
| **Corrections indicated by test results** | Fixing what the report found and re-running (2.12.5) |

---

## Self-check

**1.** A report shows `color-contrast` at 360, 768, and 1280. How many problems is that, and why?

**2.** Your page passes web-check. Your stakeholder says a volunteer using a screen reader could not
submit the form. How can both be true?

**3.** A report shows `OVERFLOWS by 40px` at 360 and nothing at 768. What kind of problem is it, and
where do you look?

### Answers

**1.** One. The same element fails the same rule at each width, so one color change fixes all three
lines.

**2.** Automated checks catch only part of accessibility. The form might have a confusing label, a
button that is not reachable by keyboard, or a focus order that jumps. Only a human walkthrough with
a screen reader finds those. The example in this note showed axe accepting a placeholder as a label.

**3.** A responsive layout problem: something on the page is wider than a 360-pixel screen. Look for
a fixed width, a wide table, a long unbroken word, or an image with no `max-width`, and re-run at 360
after each change.
