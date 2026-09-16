# Lecture Notes: One Template, Many Pages
## 145010 Web Design · Unit 6 · Week 6, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W06_OneTemplateManyPages.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-6-publishing-and-measurement/04-slides/MCCTC_145010_Slides_W06_OneTemplateManyPages.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need the Lab W06-01
starter, `05-labs/lab-w06-01-files/sitekit/`, and Python 3 to try the examples.

**Competencies:** 6.5.6 create and edit a web page template · 6.5.4 content management systems ·
6.5.2 plan a site's structure for navigation and usability · 6.5.9 media, forms, and links on a
site · 6.5.3 standard web languages in site development.

---

## Why this exists

You have five weeks of pages. Each one has its own copy of the `<head>`, its own nav, its own
footer. Now change the site name.

You open five files. You change five lines. You miss one. Nothing tells you, because a page with
the old name is still a valid page. A visitor finds it three weeks later.

Every site bigger than one page has this problem. The fix is older than any of the tools that use
it: **keep what every page shares in one place, and keep what each page says in another.**

---

## The concept in plain language

A **template** is a page with holes in it. The holes are called slots, and this course writes them
as `{{name}}`. The template holds everything that is the same on every page: the doctype, the
stylesheet link, the nav, the footer.

A **content file** holds only what is different about one page. In this course, that is four
things: the title, the description, the nav label, and the body.

A **build step** joins them. `build.py` reads the template, reads each content file, fills the
slots, and writes one finished page per content file into `site/`.

**`site/` is output.** You never edit it. Every build overwrites it.

A **content management system (CMS)** is this same idea with more around it: a database instead of
a folder of content files, an admin screen instead of a text editor, user accounts so several
people can edit, and a theme system instead of one template file. Organizations use one so that
the people who write the words never touch the layout, and the people who own the layout change it
once for every page.

---

## Worked example 1: one slot, three different pages

The starter template has a hard-coded title:

```html
<title>My Site</title>
```

`python build.py` in the starter prints:

```
Built 3 page(s) into site/
WARNING: template.html never uses {{title}}, so every page gets the same title
WARNING: template.html never uses {{description}}, so every page gets the same description
WARNING: template.html never uses {{nav}}, so every page gets the same nav
WARNING: site.json has no base_url, so no sitemap.xml was written
```

Open the three pages in three tabs. Every tab says "My Site". Change the line to a slot:

```html
<title>{{title}} · {{site_name}}</title>
```

Each content file already has its own title in its facts block:

```
title: Week 1 Document
description: Replace this with one sentence describing your Week 1 semantic document...
nav_label: Document
---
<h1>Week 1 document</h1>
```

Rebuild. The first warning is gone, and the tab now says `Week 1 Document · My Web Portfolio`.

**Notice what did not warn.** The starter passes web-check with zero errors. A validator checks
that each page is valid on its own. It cannot tell that three valid pages share one title. That is
what the build warning is for.

---

## Worked example 2: the nav belongs in the template

In the starter, every content file carries its own copy of the nav. Delete those copies and put
one slot in the template:

```html
<nav aria-label="Main">
  <ul class="nav">
    {{nav}}
  </ul>
</nav>
```

`build.py` fills it from the order in `site.json`, and marks the page you are on:

```html
<li><a href="index.html">Home</a></li>
<li><a href="document.html">Document</a></li>
<li><a href="layout.html" aria-current="page">Layout</a></li>
```

`aria-current="page"` tells a screen reader "you are here", and gives your stylesheet something to
underline. You wrote it once. Every page gets the right one.

---

## Worked example 3: change once, count the pages

Change the footer in `template.html` from "Built for 145010 Web Design." to "Made in Room 114."
Rebuild. Then, in Command Prompt, ask which output files contain the new text:

```
findstr /m /c:"Made in Room 114" site\*.html
```

In the starter, after the change:

```
site\document.html
site\index.html
site\layout.html
```

Every page is listed. In the reference site that is six pages from one edit. VS Code's search
across files (Ctrl+Shift+F) gives the same answer. This is the entire
argument for templates, and it is also 6.5.6 on the WebXam: create **and edit** a page template.

---

## Worked example 4: plan the structure before you fill the template

A template's nav is only as good as the plan behind it. Before you add pages, write a table:

| Address | Nav label | Purpose, in one sentence |
|---|---|---|
| `/` | Home | Say what is here and link to every piece |
| `/document.html` | Document | Show semantic markup |
| `/layout.html` | Layout | Show a layout that adapts |
| `/media.html` | Media | Show captioned video and a download |

Then ask two questions. Can a visitor reach every page in two clicks from any page? Is there a
page nobody can reach? `build.py` answers the second one for you:

```
WARNING: content/extra.html is not in the navigation, so a visitor cannot reach it by clicking
```

---

## The wrong version, and what it costs

Editing the output.

A validation error is on `site/layout.html`, line 40. You open `site/layout.html`, fix line 40,
and web-check passes. Then you change one word in a content file and rebuild. The error is back,
because `build.py` rewrote `site/layout.html` from the content file you never fixed.

There is no error message for this. The only symptom is a fix that keeps undoing itself.

The same failure in a CMS looks like this: someone edits the theme's files directly on the server,
the theme updates, and the edit is gone.

### Write this down

> Fix the source, then rebuild. `site/` is output.

---

## Why the wrong version is tempting

The error message names `site/layout.html`, because that is the file web-check read. The fastest
route to a green result is the file it named. It even works, once.

The habit that prevents it: when a checker names a generated file, ask which source made it. The
body came from `content/layout.html`. The head, nav, and footer came from `template.html`.

---

## When a template is the wrong tool

Be honest about the trade. A template adds a build step, a folder you must not edit, and a new way
to fail: a slot nobody filled. `build.py` stops rather than shipping one:

```
BUILD STOPPED: template still has a placeholder nobody filled: '{{author}}</footer>\n</body>\n</'
```

For one page that will never change, a template is more work than it saves. For two pages that
share a nav, it already pays.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Template** | A page with slots. Holds everything every page shares. |
| **Slot** | A marked hole in a template, written `{{name}}` here, filled at build time. |
| **Content file** | One page's own facts and body, with no layout in it. |
| **Build** | The step that joins template and content into finished pages. |
| **Static site generator** | A program that builds finished pages ahead of time. `build.py` is a tiny one. |
| **CMS** | A content management system: templates plus a database, an admin screen, and user accounts. |
| **Theme** | A CMS's word for its set of templates and styles. |
| **Site map (plan)** | A table or diagram of every page and how visitors move between them. |
| **`aria-current`** | An attribute that marks the current item in a set, such as the page you are on. |

---

## Self-check

**Question 1.** Web-check reports an error on `site/document.html`. Where do you fix it, and how do
you decide?

**Question 2.** The starter template passes web-check, yet `build.py` warns about it. What can
`build.py` see that a validator cannot?

**Question 3.** Your school's front office wants to post a new announcement every week without
learning HTML, and the principal wants the logo changed on every page next month. Name what a CMS
gives each of them.

---

### Answers

**1.** Find which part of the page the error is in. Body content came from
`content/document.html`. The head, nav, and footer came from `template.html`. Fix it there, rebuild,
and run web-check again. Never fix it in `site/`, because the next build overwrites it.

**2.** It sees all the pages at once. A validator checks one page against the rules for one page,
and a shared title is valid on every page. `build.py` compares pages to each other, so it can tell
that three pages have the same title, or that a page is missing from the nav.

**3.** The front office gets an admin screen where they type the announcement into a form, and the
CMS puts it into the template, so they never touch HTML. The principal's change is made once, in
the theme, and every page shows the new logo on its next build or request.
