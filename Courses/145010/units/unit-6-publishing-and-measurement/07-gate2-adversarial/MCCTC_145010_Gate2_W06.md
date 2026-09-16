# Gate 2: Adversarial Review · Week 6
## 145010 Web Design · Unit 6 · Week 6, Friday

**40 minutes.** Individual, silent. You may and should run it. You may not ask an AI tool whether
it is correct, because AI output is what is being reviewed.

The site is in `gate2-w06-files/`. Copy the whole folder somewhere of your own before you run it:
the server writes a file next to itself.

**The Quarry Hill Skate Crew is invented.** So is its park. Nothing here is a real group's site.

---

## What you are looking at

Somebody gave an AI assistant the requirements in Part A and published what it produced. It looks
finished. Every page loads. Your job is to find what is wrong with it.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**One of them is genuinely arguable.** Reasonable people could disagree about whether it is a
defect at all, or which category it belongs in. You are scored on your reasoning, so if you think
something is arguable, say what the other side would say.

---

## PART A: The requirements

> Build a small website for the Quarry Hill Skate Crew, a volunteer group of high school students
> who keep a community skate park open on weekends.
>
> 1. Three pages: Home, Schedule, and Volunteer. **Each page has its own title and its own meta
>    description.**
> 2. Valid HTML that passes the course checker at 360, 768, and 1280 pixels.
> 3. A page-view counter that records **the page and the day**. **No cookies, no IP addresses, no
>    identifiers of any kind.** The volunteers and most visitors are minors.
> 4. **The counter must never slow a page down.**
> 5. **Every page may be read by search engines**, so people looking for volunteer shifts can find
>    the crew. Provide `robots.txt` and `sitemap.xml`.
> 6. The Volunteer page has a "before your shift" checklist that visitors can tick off. Nothing is
>    sent anywhere.
> 7. The server runs on an explicit port.

---

## PART B: What the AI produced

```
gate2-w06-files/
  serve.py            the server and the counter's storage
  site/
    index.html        Home
    schedule.html     Schedule
    volunteer.html    Volunteer, with the checklist
    style.css
    count.js          the page-view counter
    robots.txt
    sitemap.xml
```

Run it from your copy:

```
python serve.py --port 8616
```

Open `http://127.0.0.1:8616/` and click through all three pages. Then use what you have from this
week:

```
node tools/web-check/check.js <your copy>/site/*.html
python <your sitekit>/check_site.py http://127.0.0.1:8616 --as https://skatecrew.example
```

Look at the server terminal. Look at what appears next to `serve.py` after you have clicked around.
Open DevTools: the Application tab shows cookies, and the Network tab shows every request and how
long it took.

**Stop the server before you hand in.**

---

## What to submit

For each defect: **file and line**, **category**, **what goes wrong for a real person**, and **the
fix**. Then one final entry: **what I was unsure about**, naming something specific. That entry is
scored, and a blank costs more than a wrong guess.

| # | File and line | Category | What goes wrong, and for whom | Fix |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**What I was unsure about:**

### How to spend 40 minutes

- **First 5:** run it and click every page. Tick every checklist box by clicking its words.
- **Next 10:** run both checkers. Read every line of their output.
- **Next 10:** read Part A one requirement at a time and point at the line that meets it.
- **Rest:** read every comment against the code under it. Ask whether it is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start.

**Four of five is a strong score.**
