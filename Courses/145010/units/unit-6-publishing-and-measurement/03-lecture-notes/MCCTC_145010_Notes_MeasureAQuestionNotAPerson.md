# Lecture Notes: Measure a Question, Not a Person
## 145010 Web Design · Unit 6 · Week 6, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W06_MeasureAQuestion.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-6-publishing-and-measurement/04-slides/MCCTC_145010_Slides_W06_MeasureAQuestion.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need your sitekit from
Monday and the files in `05-labs/lab-w06-02-files/`.

**Competencies:** 1.10.5 monitor customer expectations and determine satisfaction using measurement
tools · 6.5.3 standard web languages (markup and script) in site development.

---

## Why this exists

The project brief asks a plain question: did anyone look at your site, and did it help them? You
cannot answer that by guessing. You need a measurement tool.

The tools most sites use answer far more than that question. Many of them identify each browser so
they can count "unique visitors", record where visitors seem to be, and follow them across pages
and visits. Your visitors this week are classmates, and many of them are under 18. **You do not
need to know who anyone is to find out whether a page is useful.** So you will build a tool that
never finds out.

---

## The concept in plain language

**Start with the question, then collect the least that answers it.**

| Question | The smallest record that answers it |
|---|---|
| Which pages get opened, and when? | The page address and the day |
| Do people find a page useful? | The page address and a yes or a no, from people who chose to answer |

That is the whole data model. No cookie. No IP address. No browser description. No ID.

Two facts to hold onto:

- **A page view is a page load, not a person.** Reloads count. Your own testing counts. Two people
  sharing a laptop count as one browser. Nothing in a view count tells you how many humans there
  were, and your report has to say so.
- **Satisfaction is asked, not inferred.** A page with many views might be confusing, so people
  keep coming back to it. The only way to know whether a page helped is to ask, and to report how
  few people answered.

---

## Worked example 1: what a server writes down without being asked

Start the Lab W06-02 starter and load the home page:

```
python serve.py --port 8606
```

The terminal shows:

```
Serving site/ at http://127.0.0.1:8606/  (Ctrl+C to stop)
127.0.0.1 - - [date and time] "GET / HTTP/1.1" 200 -
```

The first thing on that line is the address of the machine that asked for the page. On your own
machine it is `127.0.0.1`. On a lab network it is a classmate's machine. On a public host it is a
stranger's connection. The standard library writes it by default.

The fix replaces the log line with one that keeps only what you need to debug:

```python
def log_request(self, code="-", size="-"):
    status = code.value if isinstance(code, HTTPStatus) else code
    sys.stderr.write(f"{self.command} {self.path.split('?', 1)[0]} {status}\n")
```

Now the same page load prints:

```
GET / 200
```

**There is a second place.** When a request crashes your handler, the server itself prints a report,
and on the build machine its first line was:

```
Exception occurred during processing of request from ('127.0.0.1', 54584)
```

That is the visitor's address and connection port again, from a different part of the standard
library. The lab's `QuietServer` replaces that report with the traceback alone. Two fixes, because
there were two leaks, and you only find the second one by making something crash.

---

## Worked example 2: the hit, from the page to the file

The page sends one small request when it loads. `count.js` does it:

```javascript
if (!location.protocol.startsWith("http")) {
  return;                       // opened from disk: no server to count with
}
const hit = JSON.stringify({ path: location.pathname });
if (navigator.sendBeacon) {
  navigator.sendBeacon("/api/hit", hit);
} else {
  fetch("/api/hit", { method: "POST", body: hit, keepalive: true }).catch(function () {});
}
```

`sendBeacon` hands the request to the browser and returns at once. The visitor never waits for
your counter. The template loads the script with `defer`, so it runs after the page is read:

```html
<script src="count.js" defer></script>
```

The server checks the address against the list of real pages, then adds one to today's count.
On the build machine, a headless Chrome loaded six pages of the reference site, the layout page
twice, and answered Yes on the widget page. `data/counts.json` then held this, and nothing else:

```json
{
  "helpful": {
    "/widget.html": {"no": 0, "yes": 1}
  },
  "views": {
    "/": {"2027-03-11": 1},
    "/document.html": {"2027-03-11": 1},
    "/layout.html": {"2027-03-11": 2},
    "/media.html": {"2027-03-11": 1},
    "/widget.html": {"2027-03-11": 1}
  }
}
```

(The real file spreads each entry over several lines, and holds the day the counter actually ran.
The day shown here is an example. Everything else is identical.)

The server refuses anything that is not a page on the site, so nobody can fill your file with
made-up keys:

```
POST /api/hit  {"path": "/admin.php"}   ->  400 {"error": "not a page on this site"}
```

---

## Worked example 3: asking the question

Every page gets the same short form from the template:

```html
<form id="helpful-form" method="post" action="/api/helpful">
  <input type="hidden" name="page" value="{{page_path}}">
  <button type="submit" name="answer" value="yes">Yes</button>
  <button type="submit" name="answer" value="no">No</button>
</form>
<p id="helpful-status" role="status"></p>
```

It works two ways. With the script, `count.js` sends the answer in the background and writes
"Thanks. Your answer was counted." into the status paragraph, which a screen reader announces.
Without the script, the browser posts the form, the server counts it, and replies `303 See Other`
with the page's own address, so the visitor lands back where they were.

**The redirect address comes from your list of pages, never from the request.** A server that
redirects wherever the form says can be used to bounce people to another site. The test for it:

```
POST /api/helpful  page=https://evil.example/&answer=yes   ->  400, no Location header
```

---

## Worked example 4: reading the numbers honestly

`report.py` turns the counts into a table. With the invented sample data in the reference
implementation:

```
Page              Views  Useful   Not  Useful %
/                    36       3     0      100%
/layout.html         16       1     2       33%
/widget.html         27       7     1       88%
```

(Three of its six rows shown.) The honest reading of the layout row: it was loaded 16 times, three
answers came in, two said No. **Three answers is not a pattern.** It is a reason to look at the
page, not a verdict on it.

The report always ends with this line, because it is always true of this tool:

```
A view is a page load, not a person. Your own visits and reloads are in these numbers.
```

---

## The wrong version, and why it is worse than it looks

An AI assistant asked for "first-party analytics with unique visitors" produced this:

```javascript
function getVisitorId() {
  const match = document.cookie.match(/(?:^|; )visitor_id=([^;]+)/);
  if (match) return match[1];
  const id = crypto.randomUUID();
  document.cookie = "visitor_id=" + id + "; max-age=31536000; path=/";
  return id;
}
```

and a server that saves `self.client_address[0]` next to each hit. It runs. There is no error. On
the build machine, one browser loading three pages produced a cookie that lasts 365 days and a file
that looks like this:

```
timestamp,page,visitor,ip
...,/,403d88fb-10d5-454c-acd8-9a5e4af8a6fd,127.0.0.1
...,/schedule.html,403d88fb-10d5-454c-acd8-9a5e4af8a6fd,127.0.0.1
```

Every page one person visits is now tied together under one ID, for a year, next to their address.
The page the file came from said "It does not track you."

### Write this down

> Collect what answers the question. Nothing you collect can leak if you never collected it.

---

## Why the wrong version is tempting

"Unique visitors" sounds like the number that matters, and every analytics dashboard you have seen
shows it. "First-party" sounds like "private". The cookie is small and the code is short.

The question to ask before adding any field: **what would I do differently if I had it?** If the
answer is nothing, you do not need it. If the answer is "know who visited," that is the thing a
class site must not know.

**About third-party analytics services.** Many sites use a service run by another company. Such
services typically set cookies or similar identifiers, and typically record details such as the
visitor's IP address, browser, device, and approximate location, so they can report unique visitors
and where they came from. What any one service collects, keeps, and shares is in its own current
documentation, and it changes. **[VERIFY]** before you ever add one. In this course, any
third-party option is the instructor's decision, not yours.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Page view** | One load of one page. Not a person. |
| **First-party** | Collected by the site you are on, not by another company. It does not mean private. |
| **Identifier** | Any value that tells one visitor from another: a cookie ID, an IP address, a login. |
| **Beacon** | A small request the browser sends in the background without making the page wait. |
| **`defer`** | A script attribute: download now, run after the page is parsed. |
| **Response rate** | How many people answered, out of how many could have. Always report it. |
| **303 See Other** | A response that sends the browser to another address after a form post. |
| **Open redirect** | A server that sends visitors to any address a request names. A security hole. |

---

## Self-check

**Question 1.** Your report shows 40 views of the home page. A classmate says "40 people saw your
site." Give two reasons that may be wrong.

**Question 2.** Why does the server check each page address against `pages.json` instead of
counting whatever address arrives?

**Question 3.** A teammate wants to add a cookie "only so we can count unique visitors, we will
never look at who they are." Give the strongest argument for it and the strongest argument
against it, then say which wins for a class site and why.

---

### Answers

**1.** Any two of: reloads count as views; your own testing counts; one person visiting twice
counts twice; a view is a load, not a read or a person. Forty views could be four people.

**2.** So the counts file can only ever hold real pages. Without the check, anyone could send
thousands of made-up addresses and fill the file, or put text in it you never intended to store.
Refusing unknown addresses keeps the data small and predictable.

**3.** For: unique visitors is a more meaningful number than page loads, and a random ID is not a
name. Against: a long-lived ID ties every page one browser visits into one history, the site now
stores something that identifies a browser over time, and visitors include minors who were told
the site does not track them. For a class site the argument against wins, because the question
"was the site useful" does not need the ID, and data you do not collect cannot be misused or
leaked. A full-marks answer states both sides before choosing.
