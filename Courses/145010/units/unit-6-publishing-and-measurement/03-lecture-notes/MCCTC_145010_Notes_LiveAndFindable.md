# Lecture Notes: Live and Findable
## 145010 Web Design · Unit 6 · Week 6, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W06_LiveAndFindable.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-6-publishing-and-measurement/04-slides/MCCTC_145010_Slides_W06_LiveAndFindable.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need your sitekit and
`check_site.py` from `05-labs/lab-w06-03-files/`.

**Competencies:** 6.5.12 publish the completed website to a web server · 6.5.14 incorporate search
engine optimization into web pages · 1.4.8 use electronic media to communicate and follow network
etiquette.

---

## Why this exists

A site on your laptop is a folder. A site on a server is a set of addresses that anyone can type.
The difference is not the files. It is who can reach them.

Once the addresses are public, two kinds of visitor arrive. People, who need every link to work and
every page to say what it is. And crawlers, programs that read pages so search engines can list
them. Both read the same markup. **This lesson is about making the addresses answer, and making
each page describe itself honestly to both.**

What this lesson will not do is promise you a search ranking. Nobody outside a search company can,
and anyone who does is selling something.

---

## The concept in plain language

**A web server maps addresses to files.** Ask for `/layout.html` and it sends `site/layout.html`.
Ask for `/` and most servers send `index.html`. Ask for something that is not there and it sends a
404.

**Publishing is putting your built files where a server can hand them out.** Two kinds of host:

| Kind | What it runs | What that means for this course |
|---|---|---|
| Static host | Nothing. It serves files. | Your pages work. Your counter's `/api/hit` has nowhere to go. |
| Host that runs a program | Your `serve.py`, or something like it | Pages and counter both work. |

**Search engine optimization (SEO), taught honestly, is five habits and two files:**

1. A `<title>` that names this page, not only the site.
2. A `<meta name="description">` that says what this page contains, different on every page.
3. One `<h1>`, and headings in order, so the page's structure is readable by a program.
4. Link text that says where the link goes. "Download the caption file", not "click here".
5. Valid markup, which you did yesterday.
6. `robots.txt` at the root, saying which addresses crawlers may read.
7. `sitemap.xml` at the root, listing every page by its **full** address.

Search engines commonly show a page's title as the clickable line in a results list, and may show
its description under it, though they can choose other text from the page **[VERIFY]** in each
search engine's current documentation. Either way, the title and description are what a person
reads before deciding to click. That part you control.

---

## Worked example 1: the smallest possible web server

Python ships one. From your sitekit folder:

```
python -m http.server 8606 --bind 127.0.0.1 --directory site
```

Checked on the build machine:

```
GET /             -> 200
GET /about.html   -> 404
POST /api/hit     -> 501, "Unsupported method ('POST')."
```

That last line is a static host in miniature. It serves your pages and cannot run your counter. If
you publish to a static host, your pages go live and your counts do not, and your report has to say
which route you used.

---

## Worked example 2: an address that works here and fails there

Same server, one capital letter:

```
GET /Layout.html  -> 200
```

On Windows, file names ignore case, so `Layout.html` finds `layout.html`. Many web hosts run on
systems where file names are case sensitive, and there the same request is a 404 **[VERIFY]** for
your host. Your links work on your machine and break after publishing.

The habit: lowercase file names, always, and links typed exactly as the file is named.

---

## Worked example 3: each page describes itself

From the reference site, the head of the widget page, generated from its content file:

```html
<title>Pizza Order Splitter · Jordan&#x27;s Web Portfolio</title>
<meta name="description" content="The Week 4 build: a calculator that works out how many pizzas a group needs, written in plain JavaScript with no framework.">
<link rel="canonical" href="https://portfolio.example/widget.html">
```

`&#x27;` is the apostrophe in "Jordan's". `build.py` escapes every title and description, so a
quotation mark typed in a content file can never end the attribute early. The browser shows it as
an ordinary apostrophe.

The title leads with what is on this page. The description is a sentence a person would read. The
canonical link says "this is the official address for this page", which matters when the same page
can be reached two ways, like `/` and `/index.html`.

`https://portfolio.example` is a placeholder. The `.example` name is reserved for documentation
and never belongs to a real site. You replace it with your published address.

---

## Worked example 4: the two files at the root

`robots.txt`, from the reference site:

```
# Every crawler may read every page.
User-agent: *
Disallow:

Sitemap: https://portfolio.example/sitemap.xml
```

An empty `Disallow:` means nothing is off limits. `sitemap.xml`, written by `build.py` from
`site.json`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://portfolio.example/</loc></url>
  <url><loc>https://portfolio.example/document.html</loc></url>
  ...
</urlset>
```

Every `<loc>` is a full address. That is why a sitemap cannot be finished until you know where the
site will live.

Now check the running site the way a crawler would meet it:

```
python check_site.py http://127.0.0.1:8606 --as https://portfolio.example
```

```
Checked 5 address(es) and 4 sitemap entries.
No problems found.
```

`--as` is the published address. The checker swaps it for the local one so it can test the sitemap
before the site is live. Give it the wrong one and it says so:

```
PROBLEM  sitemap.xml: 'https://portfolio.example/' is not a full address under https://jordan.example
```

---

## Worked example 5: telling people it is live

**1.4.8** is on the exam: use electronic media to communicate and follow network etiquette. A
launch message is where that stops being abstract. A good one, sent through the class channel:

> Hi Sam. My Week 6 site is live at (address). It is my five instruction-phase projects in one
> place. It counts page loads and asks one yes or no question, and it does not use cookies or keep
> addresses. If you have two minutes, try the pizza splitter on the Widget page and tell me whether
> it made sense. No need to reply if you are busy.

What makes it good: it says what the link is before asking anyone to click it, it says what the site
records, it asks for one specific thing, and it makes saying no free. What makes a bad one: a bare
link, "check out my site", a message to people you do not know, or the same message sent five
times.

---

## The wrong version: the comment says one thing, the rule says another

```
# Allow all crawlers to index the whole site so volunteers can find us.
User-agent: *
Disallow: /
```

A person reads the comment and moves on. A crawler ignores comments and reads `Disallow: /`, which
asks every crawler to stay out of every page. The site is live, every page works, and the file
asks search engines not to read any of it. No browser will ever show you an error.

`check_site.py` catches it:

```
PROBLEM  robots.txt tells every crawler to stay out of the whole site (Disallow: /)
```

### Write this down

> `robots.txt` is a request to crawlers, not a lock. It does not make anything private.

Anything published is public. A page listed as off limits can still be opened by anyone who has the
address, and crawlers that ignore the file can still read it. If a page should not be public, do not
publish it.

---

## Why the wrong version is tempting

`Disallow` sounds like "disable". Some tools and templates ship with `Disallow: /` so that
unfinished sites are not read while they are being built, and nobody changes it at launch. And the
comment is right there, telling you everything is fine.

The habit: read the rule, not the comment, and run the checker after every publish.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Web server** | A program that answers requests for addresses by sending files or program output. |
| **Static host** | A host that serves files and runs none of your code. |
| **Publish** | Put built files where a server hands them to anyone who asks. |
| **Crawler** | A program that reads pages so a search engine can list them. |
| **SEO** | Search engine optimization: making pages describe themselves clearly to people and crawlers. |
| **`robots.txt`** | A root file asking crawlers to stay out of certain addresses. A request, not a lock. |
| **`sitemap.xml`** | A root file listing every page by its full address. |
| **Canonical link** | A tag naming the official address of a page that can be reached more than one way. |
| **Netiquette** | The expected manners of online communication. |

---

## Self-check

**Question 1.** Your site is on a static host. Every page loads, and your traffic report is empty.
What happened, and what are your two options?

**Question 2.** Two pages share the description "Welcome to my website." Name the problem for a
person looking at search results, and the tool in this course that reports it.

**Question 3.** A student wants to keep one page private, so they add `Disallow: /private.html` to
`robots.txt`. What is wrong with that plan, and what should they do instead?

---

### Answers

**1.** A static host serves files and runs no program, so `/api/hit` has nothing behind it and no
count is ever recorded. Either run `serve.py` somewhere that runs Python, such as the lab route or a
host that runs programs, or keep the static host for pages and say in the report that the counter
ran only on the lab route.

**2.** Both results say the same thing, so a person cannot tell the pages apart and cannot tell what
either one contains. `build.py` warns about shared descriptions, and `check_site.py` reports them as a
problem.

**3.** `robots.txt` is a public file and a request to crawlers, so the student has published the
address of the page they wanted hidden, and the page is still public to anyone who types it. If a
page should not be public, do not publish it.
