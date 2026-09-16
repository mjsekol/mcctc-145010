# Lab W06-01: One Template, Many Pages
## 145010 Web Design · Unit 6 · Week 6, Monday

**Gate:** 3 (open). Full tooling, decision log entry required. **Duration:** Build 1 (40 minutes)
and Build 2 (55 minutes).
**Competencies:** 6.5.6 create and edit a web page template · 6.5.2 plan a site's structure for
navigation and usability · 6.5.9 incorporate audio and video, forms, and links on a site ·
6.5.4 content management systems (Part C, lab hardware) · 6.5.3 standard web languages.

**Notes for this lab:** `03-lecture-notes/MCCTC_145010_Notes_OneTemplateManyPages.md`.

---

## The scenario

You have five weeks of web work in five folders, and each page carries its own copy of the head,
the nav, and the footer. By Thursday it has to be one site at one address, and by then you will
have changed the shared parts at least four times. Doing that by hand across every page is how a
site ends up with one page that still has last week's nav.

## What you will build

One site, generated from one template and one content file per page, with a written plan for how
a visitor moves through it.

---

## Starter files

Copy `05-labs/lab-w06-01-files/sitekit/` into your Week 6 repository. You get:

```
sitekit/
  build.py          joins template and content into site/. Do not edit it.
  site.json         site name, published address, nav order
  template.html     the template. Starts with a hard-coded title, description, and no nav.
  content/
    index.html      home page content, with a copied nav inside it
    document.html   placeholder for your Week 1 page, with a copied nav
    layout.html     placeholder for your Week 2 page, with a copied nav
  static/
    style.css       copied into site/ on every build
    media/          a short demo video, its captions, and an image
```

The starter runs. It builds three pages that all have the same title and description, and it
passes web-check anyway. That is the problem you are fixing.

**The one rule for the whole week:** `site/` is output. Never edit a file in it. Every build
overwrites it.

---

## Part A · Build 1 · 40 minutes

**1. Build the starter.** In a terminal, in `sitekit/`, run `python build.py`.
*You should see* `Built 3 page(s) into site/` and four lines that start with `WARNING`.

**2. Look at what it built.** Open `site/index.html`, `site/document.html`, and `site/layout.html`
in your browser, one tab each.
*You should see* three tabs that all say `My Site`.

**3. Write the site plan.** Create `site-plan.md` next to `sitekit/`. It needs: who the site is
for, in one sentence; a table with one row per page (address, nav label, purpose in one sentence,
week built); and your answers to two questions: can a visitor reach every page in two clicks or
fewer from any page, and is there any page nothing links to.
*You should see* a table with at least five rows, one for each of Weeks 1 to 5, plus Home.

**4. Give the template a title slot and a description slot.** In `template.html`, replace the
hard-coded title and description lines with:

```html
<title>{{title}} · {{site_name}}</title>
<meta name="description" content="{{description}}">
```

Delete the `STARTER` comment above them. Rebuild.
*You should see* only two warnings left, and three different tab titles after a refresh.

**5. Move the nav into the template.** Delete the `<nav>` block and its `STARTER` comment from all
three content files. In `template.html`, inside the header after the site name, add:

```html
<nav aria-label="Main">
  <ul class="nav">
    {{nav}}
  </ul>
</nav>
```

Rebuild.
*You should see* one warning left, about `base_url`. Every page has the nav, and the current page's
link has `aria-current="page"` when you inspect it.

### Acceptance criteria, Part A

- [ ] `site-plan.md` exists with the page table and both answers
- [ ] `template.html` uses `{{title}}`, `{{description}}`, and `{{nav}}`
- [ ] No file in `content/` contains `<nav`
- [ ] `python build.py` prints only the `base_url` warning
- [ ] Committed

---

## Part B · Build 2 · 55 minutes

**6. Bring in your real pages.** For each of Weeks 1 to 5, copy everything inside that page's
`<main>` element into a content file. Write a real title and a real description for each: a
sentence that says what is on that page, between 50 and 160 characters, different on every page.
Add each page's name to the `nav` list in `site.json`, in the order your plan says.
*You should see* `Built 6 page(s)` or more, and no warning about a shared title or description.

If a page has its own CSS, move those rules into `static/style.css`. If a page has its own
script, put the script file in `static/` and keep its `<script src="...">` tag in the content
file.

**7. Add a media page.** Create `content/media.html` with a captioned video, a transcript, and a
download link. The demo files are in `static/media/`:

```html
<video controls width="320" height="180" preload="metadata">
  <source src="media/shop-demo.mp4" type="video/mp4">
  <track kind="captions" src="media/shop-demo.vtt" srclang="en" label="English" default>
  Your browser cannot play this video. The transcript below says everything it shows.
</video>
```

Use your own Week 2 media instead if you have it. Add `media` to the nav.
*You should see* the video play in the browser with captions on.

**About your Week 5 form.** If it collects names, email addresses, or anything else personal, do
not publish it. Describe it on the media page in two sentences, and say why it is not live. A
public form that collects personal details from strangers is not something a class site should
have. If your form collects nothing personal, it may go on the site, with its action pointing at
a server you run.

**8. Set the published address.** In `site.json`, set `"base_url"` to
`"https://portfolio.example"` for now. You change it on Thursday. Run `python build.py --strict`.
*You should see* `Built N page(s) into site/` and no warnings, and a new `site/sitemap.xml`.

**9. Validate every page.** From the repository root:

```
node tools/web-check/check.js <path to>/sitekit/site/*.html
```

Fix every error **in `content/` or `template.html`**, rebuild, and run it again.
*You should see* `PASS` for every page.

**10. Change the template once, and count.** Change the footer text in `template.html`. Rebuild.
In Command Prompt, from `sitekit/`:

```
findstr /m /c:"your new footer text" site\*.html
```

*You should see* every page listed. Write the count, and one sentence on what that count would
have cost you by hand, at the bottom of `site-plan.md`.

### Acceptance criteria, full lab

- [ ] `python build.py --strict` exits with no warnings
- [ ] Every page passes web-check at 360, 768, and 1280
- [ ] Every page has its own title and description, and none of them is placeholder text
- [ ] The media page has captions, a transcript, and a download link
- [ ] Your Week 5 form is either published safely or described with the reason it is not
- [ ] The step 10 count is written down
- [ ] A decision log entry: one thing you decided about the site's structure and what you rejected
- [ ] Committed and pushed

---

## Part C · Lab hardware only · the real CMS · [VERIFY]

**Your instructor runs this part, or marks it skipped.** No content management system is installed
on the machine this lab was built on, so these steps are a checklist, not a verified procedure.
The instructor confirms each one on the lab server before Monday.

If a CMS is installed on the lab server, work in pairs for ten minutes and find these five things.
Write where each one is, in the CMS's own words:

1. The screen where you type a new page's body
2. Where a page's title is set, and whether it can differ from the heading on the page
3. Where a description for search results is set, if anywhere
4. The theme or template screen, and one thing you could change there that would change every page
5. The user accounts screen, and one role that can edit pages but not change the theme

Then answer in `site-plan.md`: which of those five does `build.py` do, and which does it not do at
all?

If no CMS is installed, answer the same question from the comparison table in the lecture notes.

---

## If it breaks

**1. `BUILD STOPPED: document.html: no line containing only --- between the facts and the body`**
The content file has no separator line, or the line has a space on it. The line must be exactly
three dashes and nothing else.

**2. `BUILD STOPPED: media.html: missing nav_label`**
The facts block above `---` is missing one of `title`, `description`, or `nav_label`. The message
names the file and the missing fact.

**3. `BUILD STOPPED: site.json nav lists 'gallery' but content/gallery.html does not exist`**
You added a page to the nav before creating its content file, or the names differ. The nav name is
the content file's name without `.html`.

**4. `BUILD STOPPED: Illegal trailing comma before end of array: line 6 column 39 (char 155)`**
`site.json` has a comma after the last item in a list. JSON does not allow that. The line and column
point at it, and they will be different numbers in your file.

**5. `BUILD STOPPED: template still has a placeholder nobody filled: '{{titel}} · My Web Portfolio</'`**
A slot is misspelled. The message shows the leftover slot and what follows it. If the dot shows as
a strange character, your terminal is not using UTF-8: run `set PYTHONIOENCODING=utf-8` first.

**6. Your fix keeps disappearing. No message at all.**
You edited a file in `site/`. The next build replaced it. Make the change in `content/` or
`template.html`.

---

## Stretch goal

Add an `updated: Week 6, Monday` fact to each content file and an `{{updated}}` slot in the
template's footer. **Predict what `build.py` will do before you run it**, and write the prediction
down. Run it and compare.

Then change `build.py` so that every fact in a content file can fill a slot of the same name, and
so that a page missing `updated` stops the build with a message naming the file. Explain in two
sentences why the first run behaved the way it did.

---

## Submission checklist

- [ ] `sitekit/` with your template, content, and `site.json`
- [ ] `sitekit/site/` built by the last `--strict` build
- [ ] `site-plan.md` with the table, both answers, the step 10 count, and the Part C answer
- [ ] Decision log entry
- [ ] Web-check output pasted into your lab notes, every page PASS
- [ ] Committed and pushed before the review and close ends

---

## Extended options

All four assess 6.5.6, 6.5.2, and 6.5.9 and are graded on the same five-dimension scale. Choose by
what you see, not by who asks.

| What you see in the first 15 minutes of Build 1 | Hand them |
|---|---|
| Still on step 2 with no terminal open, or `python build.py` has not run | SCAFFOLDED |
| Step 5 done, site plan written, working steadily | STANDARD |
| Step 5 done before minute 20 and asking what else a template can hold | EXTENDED |
| Says "I would never build a site this way" or asks when anyone uses this | APPLIED |

### SCAFFOLDED

Three pages instead of six: Home, Week 1, and Week 2. The site plan is a filled-in table only, with
the two questions answered in one word each. Skip step 7.

Your instructor gives you a template with the title slot already written. You add the description
slot and the nav slot yourself, one at a time, and rebuild after each.

**Extra checkpoints:** show your instructor after step 4, after step 5, and after step 9.

**Then answer in writing:** you changed one line in the template. How many pages changed, and why
that number and not one?

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **a generated "on this page" list.** Pages with two or more `<h2>`
headings should get a short list of links to those headings at the top of the body, generated at
build time, without you writing it in the content file.

You may change `build.py` for this. Keep every existing warning working, and add one: a heading
with no `id` cannot be linked to.

*Hint, not the answer:* Python's `html.parser` module can read the body and hand you each start tag
with its attributes. Read the documentation for `HTMLParser.handle_starttag` before you write a
regular expression.

### APPLIED

Same skill, different domain. Pick a set of documents you actually deal with that share a layout:
your club's meeting notes, a team's game-day sheets, a recipe collection, a band's set lists.

Build three of them with `build.py`, using your own template. The template must hold everything
the three share, and each content file must hold only what is different. Then answer in writing:
what did you put in the template that you first thought belonged in the content, and why did you
move it?
