# Lecture Notes: How a Document Becomes a Page
## 145010 Web Design & Senior Capstone · Unit 1 · Week 1 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W01_HowADocumentBecomesAPage.md)
· no exported deck yet. Generate it from the repository root with
`node tools/gamma.js Courses/145010/units/unit-1-semantic-html/04-slides/MCCTC_145010_Slides_W01_HowADocumentBecomesAPage.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome and the
course checker, `tools/web-check/check.js`.

**Competencies:** 6.1.1 (the principles of HTML and its relationship with browsers) and 2.7.8
(static and dynamic sites).

---

## Why this exists

You have built pages before. In 145065 your CRUD app's Flask templates produced HTML, a browser
showed it, and that was the end of the conversation. This week starts one step earlier: what the
browser does with the text it receives.

It matters because **the browser never refuses a page.** It repairs what you wrote and shows the
repair. Everything that reads your page after that, your CSS, a screen reader, a search engine,
next week's script, works on the repaired version. If you never look at it, you never find out
that it differs from your file.

---

## The concept in plain language

An HTML file is text. The browser reads the text with a parser and builds a tree of objects
called the **DOM**, the Document Object Model. Each element in your file becomes a node in the
tree.

The parser follows rules written in the HTML standard, and those rules include what to do with
mistakes. A paragraph that contains a list gets closed when the list starts. Tags that cross each
other get untangled. A table row that is not inside a row group gets one. **Nothing tells you.**

Two views in Chrome show the two sides:

- **View Source**, Ctrl+U, shows the text that arrived.
- **DevTools, Elements** shows the tree the browser built.

The browser also does not know or care where the text came from. A **static** site sends a stored
file, the same bytes to everyone, until somebody edits the file. A **dynamic** site runs a
program for each request and builds the page then, so it can differ by person or by moment. Your
Flask projects were dynamic. Either way, the browser receives HTML and builds a tree.

---

## Worked example 1: the list inside a paragraph

```html
<h1>Saturday game day</h1>
<p>Bring:
  <ul>
    <li>Shin guards</li>
    <li>Water</li>
  </ul>
</p>
<table>
  <tr><th>Kickoff</th><th>Field</th></tr>
  <tr><td>9:00</td><td>A</td></tr>
</table>
```

The page looks fine. The Elements panel shows what Chrome built:

```html
<h1>Saturday game day</h1>
<p>Bring:
  </p><ul>
    <li>Shin guards</li>
    <li>Water</li>
  </ul>
<p></p>
<table>
  <tbody><tr><th>Kickoff</th><th>Field</th></tr>
  <tr><td>9:00</td><td>A</td></tr>
</tbody></table>
```

Three differences. The paragraph ends before the list. The `</p>` at the end had nothing to close,
so the parser made an empty paragraph. A `tbody` appeared that nobody typed.

---

## Worked example 2: crossed tags, and why the validator disagrees

```html
<p><b><i>Helmets are required in the shop area.</b></i> We have loaners.</p>
```

Chrome builds:

```html
<p><b><i>Helmets are required in the shop area.</i></b> We have loaners.</p>
```

It closed the tags in the right order for you. The validator does not repair the file. It reports
it. In Lab W01-01, this one line was responsible for 19 of `web-check`'s 21 validation errors,
because the validator treated the `i` as still open and reported every element after it as being
in the wrong place. Fixing that line alone took the count from 21 to 2.

**The lesson.** When a validator gives you a long list, do not fix it top to bottom. Look for the
line the errors cluster after.

---

## Worked example 3: static and dynamic, same browser

A static file served with Python's built-in server, on an explicit port:

```
python -m http.server 8140 --bind 127.0.0.1 --directory static
```

A dynamic page from a short standard-library program that builds the HTML on every request:

```
python serve_dynamic.py 8141
```

View Source on the dynamic page, captured on the build machine:

```html
<body>
  <h1>Saturday schedule</h1>
  <ul>
    <li>9:00 Hawks vs Comets, Field A</li>
    <li>10:30 Otters vs Lightning, Field B</li>
  </ul>
  <p>Built by the server at 11:13:23</p>
</body>
```

Refresh it and the time changes, because the program ran again. Refresh the static page and
nothing changes, because the same file was sent again. **The browser received ordinary HTML both
times.** Static or dynamic is a fact about the server.

**When each one fits.** Static: the content changes rarely and is the same for everyone, like a
league's code of conduct. It is cheap to host and hard to break. Dynamic: the content depends on
who is asking or on data that changes, like a referee's own assignments. It needs a running
program, and often a database and logins to protect.

---

## The wrong version, and what it produces

```html
<p>Every Tuesday from 5:30 to 8:30 p.m. Bring:
  <ul>
    <li>Your bike</li>
    <li>A lock</li>
  </ul>
</p>
```

It displays. In the Lab W01-01 starter, where these lines sit at 32 to 38, `web-check` reports:

```
line 32:6  no-implicit-close  Element <p> is implicitly closed by adjacent <ul>
line 38:6  close-order  Stray end tag '</p>'
```

The first line is the validator telling you what the browser did. The second is the leftover
`</p>` with nothing to close.

**The fix.** End the paragraph before the list starts:

```html
<p>Every Tuesday from 5:30 to 8:30 p.m. Bring:</p>
<ul>
  <li>Your bike</li>
  <li>A lock</li>
</ul>
```

### Write this down

> A page that displays proves the browser could repair it. It proves nothing about your file.

---

## Why the wrong version is tempting

In writing, "Bring:" and the list after it belong to one sentence, so putting them in one
paragraph feels right. And nothing on the screen argues with you. Every browser you have ever used
has shown you something no matter what you typed, so you learned that "it shows up" means "it
works." The habit that replaces it: after the page displays, open Elements, and run the checker.

---

## Vocabulary

| Term | What it means |
|---|---|
| **HTML** | The markup language that says what each piece of content is |
| **Parser** | The part of the browser that reads the text and builds the tree |
| **DOM** | The tree of element objects the browser builds from your file |
| **View Source** | The text as it arrived, Ctrl+U in Chrome |
| **Elements panel** | The DOM as the browser built it, in DevTools |
| **Validator** | A tool that reports where the file breaks the rules, without repairing it |
| **Static site** | Stored files, the same for everyone, changed only by editing |
| **Dynamic site** | A program builds each page when it is requested |

---

## Self-check

**Question 1.** Your page shows up correctly in Chrome. Name one thing that proves, and one thing
it does not prove.

**Question 2.** A validator reports 21 errors. Most of them name lines after line 48. What should
you do first, and why?

**Question 3.** A club wants a page that lists its meeting times, which change twice a year, and
a page where each member sees their own dues balance. Which should be static and which dynamic?

---

### Answers

**1.** It proves the browser could build a page from your text. It does not prove the text is
valid, or that the tree the browser built matches what you wrote. Check the Elements panel and
run the validator.

**2.** Look at line 48, or the first line the errors cluster after. One unclosed or misnested tag
makes everything after it look wrong to the validator. Fixing that line often removes most of
the list at once, as it did in the lab: 21 errors became 2.

**3.** The meeting times can be static: they are the same for everyone and change rarely, so
somebody edits the file twice a year. The dues page must be dynamic: it is different for each
member, so a program has to build it per request, and it needs logins to keep one member's
balance away from another.
