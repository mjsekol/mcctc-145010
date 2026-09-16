# Lecture Notes: Links and Paths
## 145010 Web Design & Senior Capstone · Unit 1 · Week 1 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W01_LinksAndPaths.md)
· no exported deck yet. Generate it from the repository root with
`node tools/gamma.js Courses/145010/units/unit-1-semantic-html/04-slides/MCCTC_145010_Slides_W01_LinksAndPaths.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome and
`structure_check`.

**Competencies:** 6.2.1 (absolute and relative links), 6.2.2 (an anchor to another section of the
same page), 6.2.3 (links that send email and download files), and the hyperlink and email parts
of 6.1.3.

---

## Why this exists

A link is a promise: click here and you will get there. When the promise breaks, the person
clicking gets an error page, or worse, nothing at all and no idea why. Links break for one reason
far more than any other: **the path was written from where the author was thinking, not from
where the page lives.**

You met this bug in 145060. A Python program opened `roster.txt`, worked from one folder, and
failed from another, because a relative path is resolved from the working directory. A link in a
page is the same bug with a different starting point.

---

## The concept in plain language

The browser turns every `href` into a full address by starting from **the page's own address**.

| You write | It means |
|---|---|
| `https://www.weather.gov/` | **Absolute.** This exact address, from anywhere. |
| `fields.html` | **Relative.** A file in the same folder as this page. |
| `pages/rules.html` | Into the `pages` folder beside this page. |
| `../index.html` | Up one folder from this page, then `index.html`. |
| `/index.html` | From the root. On a web server, the site root. On a `file://` page, the root of the drive. |
| `#rain` | **Fragment.** Scroll to the element on this page whose `id` is exactly `rain`. |
| `../index.html#rain` | Open that page, then scroll to that `id`. |
| `mailto:league@cedarhollowrec.example` | Open the visitor's email program, addressed to that address. |
| `files/form.pdf` with `download` | Ask the browser to save the file instead of showing it. |

Three rules decide most outcomes:

1. **Relative paths start in the page's folder.** Not the site's top folder. Not your terminal's
   folder.
2. **Fragments must match an `id` exactly.** Case included. A mismatch does nothing and reports
   nothing.
3. **Link text must make sense alone.** Screen reader users often pull up a list of every link on
   a page. "Click here" nine times is useless.

---

## Worked example 1: one page, three paths

The page is `site/pages/roster.html`. The folder has `site/images/logo.png` and nothing else.

```html
<a href="../images/logo.png">A</a>
<a href="images/logo.png">B</a>
<a href="/images/logo.png">C</a>
```

Chrome resolved them, from a page at that location on the build machine, to:

- A: `site/images/logo.png`. Exists.
- B: `site/pages/images/logo.png`. Does not exist.
- C: `file:///C:/images/logo.png` when the page is opened from the `C:` drive, which is the root of
  the drive, not the root of the site. On a web server whose root is `site/`, C would work.

B is the bug you will write most often. C is the one that works on the server and breaks on your
machine, or the reverse.

---

## Worked example 2: fragments

```html
<nav aria-label="Jump to">
  <a href="#fields">Fields</a>
  <a href="#Rain">Rain</a>
  <a href="#top">Top</a>
</nav>
...
<h2 id="fields">Fields</h2>
...
<h2 id="rain">Rain</h2>
```

Clicked in order from the top of a long page, verified in Chrome:

| Click | Scroll position after | Why |
|---|---|---|
| Fields | 1326 | Matches `id="fields"` |
| Rain | 1326, unchanged | `#Rain` does not match `id="rain"` |
| Top | 0 | `top` is special: with no element by that id, the browser goes to the top of the page |

The Rain link fails silently. `structure_check` catches it:

```
FAIL ANCHORS   line 3: #Rain has no element with id="Rain" on this page
```

`href="#"` also jumps to the top. It is almost always a placeholder somebody forgot, and
`structure_check` reports it as one.

---

## Worked example 3: email and download links

```html
<p>Print the <a href="files/coupon.txt" download>coupon (text file, 1 KB)</a>.</p>
<p>Questions go to <a href="mailto:boosters@bandcarwash.example">boosters@bandcarwash.example</a>.</p>
```

`structure_check` reports what each link hands people:

```
LINKS     line 18: download link hands people a .txt file ('coupon (text file, 1 KB)')
LINKS     line 21: email link to boosters@bandcarwash.example (anyone who reads the page source can collect this address)
```

Two habits in that markup:

- **The download link says what arrives.** File type and size, before the click. A phone user on
  a data plan deserves to know.
- **The email link shows the address.** A visitor on a shared computer with no email program set
  up can still copy it. And it is a role address, not a person's own, because anything in page
  source can be collected by any program that downloads the page.

`structure_check` fails any download link to a file type that can run code on the visitor's
machine, such as `.exe` or `.bat`. A page should never hand those out without a very good reason.

---

## The wrong version, and what it produces

Take a page that works, with `files/coupon.txt` and `pages/directions.html` beside it, and move
the page into a new `site/` folder without moving anything else. Nothing in the links changed.
`structure_check` on the moved copy:

```
FAIL FILES     line 18: <a href="files/coupon.txt"> points at a file that is not there
FAIL FILES     line 20: <a href="pages/directions.html"> points at a file that is not there
```

What a visitor sees when they click one:

- Opened as a file, Chrome shows an error page with the code `ERR_FILE_NOT_FOUND`.
- Served by `python -m http.server 8150`, the page says `Error code: 404` and
  `Message: File not found.`

**The fix** is to move the site as a whole, or rewrite the paths from the page's new folder.

### Write this down

> A relative path starts in the folder the page lives in.

---

## Why the wrong version is tempting

You write a link while looking at the file tree from the top, so `pages/rules.html` looks right
even when you are typing inside `pages/`. The editor does not complain. The link may even work,
because you tested it from a different page. And fragment typos are worse: the page does not
move, nothing turns red, and you assume you mis-clicked.

The habit that prevents it: before writing a path, say out loud which folder the page is in. Then
run `structure_check` on every page, not only the one you were editing.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Absolute URL** | A full address with a scheme and host, the same from anywhere |
| **Relative URL** | An address resolved from the current page's location |
| **`..`** | The folder above |
| **Fragment** | The part after `#`, naming an `id` on the page |
| **`mailto:`** | A link that opens an email program |
| **`download`** | An attribute that asks the browser to save rather than show |
| **Role address** | An email address for a job or group, not a person |
| **404** | The HTTP status for "not found" |

---

## Self-check

**Question 1.** A page lives at `site/pages/teams/hawks.html`. Write the relative link to
`site/index.html`, and to the `id="schedule"` section inside it.

**Question 2.** A jump link does nothing when clicked, and nothing appears in the console. Name the
two likeliest causes.

**Question 3.** Rewrite this so both links make sense on their own:
`<a href="files/waiver.pdf">Click here</a> for the waiver or <a href="mailto:teens@hollisstreetcc.example">email us</a>.`

---

### Answers

**1.** `../../index.html`, and `../../index.html#schedule`. Two folders up from `teams/` reaches
`site/`.

**2.** The fragment does not exactly match any `id`, often a difference in case or a hyphen. Or the
`href` is a bare `#`, which is a placeholder that only jumps to the top. `structure_check` reports
both.

**3.** One good version:

```html
Print the <a href="files/waiver.pdf" download>game night waiver (PDF)</a>, or email
<a href="mailto:teens@hollisstreetcc.example">teens@hollisstreetcc.example</a>.
```

Any version works if each link's text names its destination and the download says its file type.
