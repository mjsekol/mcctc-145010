# Lecture Notes: Where Script Lives
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W04_WhereScriptLives.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-4-client-side-scripting/04-slides/MCCTC_145010_Slides_W04_WhereScriptLives.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome and the
Lab W04-01 files. **If you were at BPA,** read this file first, then follow Monday in
`10-resources/MCCTC_145010_CatchUp_W04.md`.

**Competencies:** 6.3.1 select and apply scripting languages used in web development · 6.3.2
insert client-side script into a web page · 2.7.6 describe the characteristics and use of browser
plug-ins.

---

## Why this exists

For three weeks your pages have been documents. They look the same no matter what the person does.
Today a page starts to respond. Before it can, you have to answer two questions that Python never
asked you: **which language does the browser run**, and **when does your code run** compared with
the page it is changing.

Get the second one wrong and your first script fails with an error that looks like your code is
broken. Your code is fine. It ran too early.

---

## The concept in plain language

**The browser builds a tree.** It reads your HTML from top to bottom and turns every element into
an object in a tree, the **DOM** (Document Object Model). The tree is what gets drawn and what a
screen reader reads. The HTML file is the recipe. The tree is the meal.

**The browser runs JavaScript against that tree.** JavaScript is the one general-purpose language
every browser runs inside a page. That makes the choice for this week simple to state:

| Language | Where it runs | Use it for |
|---|---|---|
| **JavaScript** | In the visitor's browser, and on servers too | Anything the page does without asking the server: toggles, filters, counters, checks |
| **Python, C#, PHP** | On a server | Anything that needs stored data or must be trusted: saving, logging in, final validation |
| **WebAssembly** | In the browser, compiled from languages like C++, Rust, or C# | Heavy computing in the page. It still reaches the page through JavaScript. |
| **HTML and CSS** | In the browser | Structure and appearance. They are not programming languages in this sense. |

Week 5 uses Python on the server. This week, everything that responds is JavaScript.

**A script runs when the parser reaches it.** A `<script>` tag with no attribute stops the parser,
downloads the file, runs it, and only then carries on reading HTML. If the tag is in the `<head>`,
the `<body>` does not exist yet when your code runs.

**`defer` fixes that.** It tells the browser: download this while you keep reading, and run it once
the whole document is parsed. This course puts every script in the `<head>` with `defer`.

```html
<script src="shift-board.js" defer></script>
```

**View Source is the recipe. The Elements panel is the tree.** After a script changes the page,
they disagree. When you debug, look at the tree.

---

## Worked example 1: an inline script, and why it is not the habit

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Game night sign-up</title>
    <script>
      console.log(document.title);
    </script>
  </head>
  <body>
    <h1>Game night sign-up</h1>
  </body>
</html>
```

Console output:

```
Game night sign-up
```

The title exists, because `<title>` comes before the script. An inline script is code written
directly between the tags. It works, and it is fine for one line. It is not the habit, for three
reasons: the browser cannot cache it separately, `defer` does nothing on an inline script, and a
page with its logic spread through the markup is hard to read. This course puts script in a
separate `.js` file.

---

## Worked example 2: an external script with defer

`monday.html`, in the `<head>`:

```html
<script src="monday.js" defer></script>
```

`monday.js`:

```js
// 1. A paragraph that exists only in the DOM.
const note = document.createElement("p");
note.textContent = "This paragraph was added by script after the page loaded.";
document.querySelector("main").append(note);

// 2. A counter.
let headcount = 0;
const countButton = document.querySelector("#count-me-in");
const headcountText = document.querySelector("#headcount");

countButton.addEventListener("click", () => {
  headcount += 1;
  headcountText.textContent = `${headcount} ${headcount === 1 ? "person is" : "people are"} coming.`;
});
```

After two clicks, the page shows:

```
2 people are coming.
```

Now press **Ctrl+U** for View Source and search for "added by script". It is not there. Open dev
tools, **Elements** panel. The paragraph is there, at the end of `<main>`. The file did not change.
The tree did.

---

## Worked example 3: asking the tree questions in the Console

With the page from example 2 open, type these into the Console, one at a time:

```js
document.querySelector("h1").textContent
document.querySelectorAll("main p").length
document.querySelector("#nothing-has-this-id")
```

Output:

```
'Game night sign-up'
3
null
```

`querySelector` takes a CSS selector, the same kind you wrote in Week 2, and returns the first
match. `querySelectorAll` returns every match. The HTML file has two paragraphs in `<main>`, and the
tree has three, because the script added one. A selector that matches nothing returns `null`.
**Remember `null`.** It is in the next section.

---

## The wrong version, and the exact error

Take the `defer` off:

```html
<script src="monday.js"></script>
```

Reload with the Console open:

```
Uncaught TypeError: Cannot read properties of null (reading 'append')
```

Read it from the end. `append` is the method that failed. It failed because the thing before the
dot was `null`. The thing before the dot is `document.querySelector("main")`. The script ran while
the parser was still in the `<head>`, so `<main>` did not exist, so the query returned `null`.

Nothing else on the page works either, because a script stops at its first uncaught error. The
counter never gets its listener.

### Two causes of null, and only two, this week

| Cause | How to tell | Fix |
|---|---|---|
| The element does not exist yet | The script tag has no `defer` and sits above the element | Add `defer` |
| The selector does not match | Type the same `querySelector` into the Console after the page loads. It still returns `null`. | Fix the selector: `#` for an id, `.` for a class |

---

## Why the wrong version is tempting

Every tutorial from a certain era puts scripts in the head. "Load the code first" sounds like it
would make the page ready sooner. And the error message never mentions timing. It says `null`, and
`null` sounds like a typo. Students spend twenty minutes re-reading a selector that was right all
along.

The habit that prevents it: **every script tag gets `defer`**, and every `null` error gets the two
questions in the table above, in order.

---

## Plug-ins: how browsers used to run other languages

For a long time JavaScript was too limited for rich applications, video, or games. Browsers let
other companies' software run inside the page through **plug-ins**. A plug-in was a native program,
installed separately, that the browser handed part of the page to.

| Plug-in | What it did |
|---|---|
| Adobe Flash Player | Animation, video, and games in the page, written in ActionScript |
| Java applets, through the Java plug-in | Full Java programs running inside a page |
| Microsoft Silverlight | Rich applications and streaming video, written in C# and other .NET languages |

**Why they are gone.** A plug-in ran native code with far more access to the computer than a web
page has, so a flaw in a plug-in was a flaw in the whole machine. They crashed browsers, drained
batteries, and did not work on phones. As HTML5 video, the `<canvas>` element, and faster
JavaScript arrived, browsers removed plug-in support. Adobe ended support for Flash Player at the
end of 2020. [VERIFY] the exact dates before you cite them: Chrome's removal of the older plug-in
system around 2015, the Java browser plug-in being deprecated in Java 9 and removed in Java 11, and
the end of Silverlight support in 2021.

**Extensions are not plug-ins.** An ad blocker or a password manager is an **extension**. It is
built with web technologies, installed from a store, and limited to the permissions it asks for,
which you can read at `chrome://extensions`. An extension changes how your browser behaves. A
plug-in ran another program inside the page. When the WebXam says plug-in, it usually means
something a page needs in order to show its content. Today a page that needs one is a page most
visitors cannot use.

---

## Vocabulary

| Term | What it means |
|---|---|
| **DOM** | The tree of objects the browser builds from HTML. What is drawn and read aloud. |
| **Client-side script** | A program the browser downloads with the page and runs on the visitor's machine |
| **`<script src>`** | Loads an external script file |
| **`defer`** | Download in parallel, run after the document is parsed, in the order the tags appear |
| **`async`** | Download in parallel, run as soon as it arrives, in any order. For scripts that do not touch the page. |
| **`querySelector`** | Returns the first element matching a CSS selector, or `null` |
| **View Source** | The HTML file as the server sent it |
| **Elements panel** | The live DOM tree, including every change a script made |
| **Plug-in** | Native software a browser used to hand page content to, such as Flash. Removed from modern browsers. |
| **Extension** | A browser add-on built with web technologies and limited permissions, such as an ad blocker |

---

## Self-check

**Question 1.** Your script is in the `<head>` with no attribute. Its first line is
`const toggle = document.querySelector("#rules-toggle");` and the page does have a
`#rules-toggle`. What is in `toggle` when the next line runs, and why?

**Question 2.** You add `defer` and still get `Cannot read properties of null`. What do you check
next, and how, without editing any file?

**Question 3.** A friend says their browser "needs a Flash plug-in" to play an old game site, and
asks you to install one. What do you tell them?

---

### Answers

**1.** `null`. The script runs when the parser reaches it, and the parser has not reached
`<body>` yet, so there is no `#rules-toggle` in the tree. The next line that calls a method on
`toggle` throws.

**2.** The selector. With the page loaded, type the same `document.querySelector(...)` into the
Console. If it returns `null`, the selector does not match: check `#` against `.` and check the
spelling against the HTML.

**3.** Modern browsers no longer run Flash at all, and Adobe stopped supporting it, so there is
nothing safe to install. Fake "Flash updates" have long been used as a disguise for malware, so a
download claiming to be one today deserves no trust. Some old Flash content has been preserved by emulator projects; look for one from a source
you trust rather than installing anything.
