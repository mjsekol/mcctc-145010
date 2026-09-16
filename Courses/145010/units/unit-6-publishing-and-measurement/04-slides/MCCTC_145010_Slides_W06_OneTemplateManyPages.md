# One Template, Many Pages
---
## Slide 1: Change the site name
- Five weeks, five pages, five copies of the nav
- Now rename the site
- Five files, five edits, one you will miss
- Nothing warns you
Speaker notes: Here is the job. You have five pages from five weeks, and every one of them has its own copy of the header, the nav, and the footer. Somebody asks you to rename the site. You open five files and you change five lines, and on a real site with forty pages you miss one. Nothing tells you, because a page with the old name is still a perfectly valid page. Today is about never having that problem again.
Image: Five browser tabs in a row, four showing a new site name and one showing the old one, circled in Launch Red.
---
## Slide 2: A site is a template plus content
- Template: everything every page shares
- Content file: only what makes this page different
- Build step: joins them into finished pages
- site/ is output. You never edit it.
Speaker notes: Three parts. The template is a page with holes in it. The content file holds the four things that are different about one page: its title, its description, its nav label, and its body. The build step fills the holes. And the folder it writes into is output, which means every build overwrites it. Write that last line down, because it is the mistake of the day.
Image: A diagram with a template shape on the left, three content cards in the middle, and three finished pages on the right, navy and Launch Blue.
---
## Slide 3: A content file
```
    title: Week 1 Document
    description: My Week 1 semantic document: headings, lists, and a data table.
    nav_label: Document
    ---
    <h1>Week 1 document</h1>
    <p>Everything that was inside my Week 1 main element goes here.</p>
```
Speaker notes: This is a whole content file, shown indented so the slide tool keeps it on one card. In the real file every line starts at the left edge. Above the line of three dashes are the page's own facts. Below them is the body. There is no doctype, no head, no nav, no footer. None of that belongs to this page. It belongs to every page, so it lives in the template.
Image: None. This slide is code.
---
## Slide 4: The template's slots
```html
<title>{{title}} · {{site_name}}</title>
<meta name="description" content="{{description}}">
...
<nav aria-label="Main">
  <ul class="nav">
    {{nav}}
  </ul>
</nav>
<main id="main">
{{content}}
</main>
```
Speaker notes: Every pair of curly braces is a slot. build.py fills title and description from the content file, builds the nav from the order in site.json, and drops the body into content. It also marks the current page in the nav with aria-current, so a screen reader says you are here. You write that once and every page gets the right one.
Image: None. This slide is code.
---
## Slide 5: What the starter says
```
Built 3 page(s) into site/
WARNING: template.html never uses {{title}}, so every page gets the same title
WARNING: template.html never uses {{description}}, so every page gets the same description
WARNING: template.html never uses {{nav}}, so every page gets the same nav
WARNING: site.json has no base_url, so no sitemap.xml was written
```
Speaker notes: This is the real output of the starter. Three pages built, four warnings. Open the three pages and look at the tabs. Every one says My Site. Now here is the part that should bother you. The starter passes web-check with zero errors. A validator checks one page at a time, and a shared title is valid on every page. Only something that looks at all the pages together can see it.
Image: None. This slide is code.
---
## Slide 6: Watch me fix the footer
- Open site/index.html and change the footer
- Open site/document.html and change it too
- Rebuild
- Both changes are gone
Speaker notes: I am going to do this the wrong way on purpose. I will open the generated pages and fix the footer in two of them. It works. I can see it in the browser. Now I rebuild, and both edits vanish, because build.py rewrote site from the template I never touched. There is no error message for this. The only symptom is a fix that keeps undoing itself.
Image: A before and after pair of footers, the edited one crossed out in Launch Red after the rebuild.
---
## Slide 7: Fix the source, then rebuild
- The body came from content/
- The head, nav, and footer came from template.html
- A checker names site/ because that is what it read
- Ask which source made the line, and fix that
Speaker notes: When web-check names a file in site, it is telling you where it looked, not where to fix. The body came from a content file. Everything around the body came from the template. So the question every time is which source made this line. Fix it there and rebuild. This is also exactly how a real content management system works: edit the theme files on the server and the next theme update wipes your change.
Image: An arrow from a highlighted line in site/layout.html back to the line in content/layout.html that produced it.
---
## Slide 8: That is what a CMS is
- The same idea: content apart from layout
- Plus a database instead of a folder
- Plus an admin screen instead of an editor
- Plus accounts so many people can edit
Speaker notes: A content management system is this idea with more around it. The words live in a database, people type them into an admin screen, several people have accounts, and the templates are called a theme. Organizations use one so the people who write never touch the layout, and the people who own the layout change it once. Our build.py is a tiny static site generator. It has the separation and none of the rest, and that is enough to see how it works.
Image: A comparison of build.py and a CMS admin screen, with matching parts connected by lines.
---
## Slide 9: Plan the structure first
- Every page, its address, its purpose in one sentence
- Every page reachable in two clicks
- No page that nothing links to
- build.py warns about the last one
Speaker notes: A template's nav is only as good as the plan behind it. Before you add pages, write the table. Address, nav label, and one sentence on what the page is for. Then ask two questions. Can somebody get anywhere in two clicks? Is there a page nobody can reach? If a content file is missing from the nav, build.py tells you.
Image: A simple site map with Home at the top and five pages beneath it, each one click away.
---
## Slide 10: What you are about to build
- Lab W06-01: your five weeks, one template
- Steps 1 to 5: plan, slots, nav into the template
- Steps 6 to 10: your pages, media, strict build
- Change the footer once and count the pages
Speaker notes: Build one is the plan and the template. Write the site plan first, then add the three slots, then move the nav out of the content files and into the template. Build two brings in your real pages from weeks one to five, adds the media page, and has to pass build dot py dash dash strict and web-check on every page. The last step is the payoff. Change the footer once, rebuild, and count how many pages changed. Write the number down.
Image: A file tree showing template.html, site.json, and a content folder with five files, beside a site folder of generated pages.
