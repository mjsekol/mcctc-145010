# Parts Counter Lookup
## Draft portfolio entry, résumé line, and interview story · `presentation/portfolio-entry.md`

*Drafted with an AI assistant from the student's notes and lightly edited. Not yet committed.
Invented composite for Gate 2 Week 18. Sections are numbered so you can cite them.*

---

A fast, modern parts lookup tool I built for Birchwood Auto Parts that changed how their counter
works.

## 1. The problem

Customers at Birchwood Auto Parts often bring in old or superseded part numbers. The counter staff,
most of whom had never used anything more advanced than a paper binder, needed a tool simple
enough that anyone could use it without getting confused. Until then they flipped through a
600-page cross-reference book while the customer waited.

## 2. What I did

- I designed and coded every line of this project from scratch, on my own, with no outside
  libraries and no AI assistance.
- I built a search that finds the current part from an old part number, including a partial
  number.
- I ran usability sessions with five people, and changed the results so parts that are in stock
  are listed first.
- When peer review found that my search built its database query from strings, I rewrote it with
  parameters.

## 3. My approach

Leveraging a modern, scalable, cloud-native architecture and agile best practices, I delivered a
robust, user-centric solution that drives digital transformation and unlocks synergies across the
organization. My passion for innovation and my commitment to excellence ensured that every
stakeholder need was not only met but exceeded.

## 4. The result

- Lookup time dropped from about a minute and a half to about thirty seconds.
- The tool handled more than 2,100 lookups in its first thirty days.
- The store manager accepted the project.
- It ran for 38 days without anyone touching it.
- The project was recognized with the Birchwood Auto Parts Student Partner of the Year award.

## 5. What I would do differently

I would test on the counter's older tablet in Week 10, not Week 16. That one criterion is still an
open follow-up.

## 6. Built with

Python, Flask, SQLite, HTML, and CSS, on the store's internal network.

## 7. Screens

Two screenshots of the search page, with invented part numbers.

## 8. Links

- **Repository:** public, after my instructor removed the store's parts data file
- **Live tool:** internal to the store, not shared

## 9. Permission

The store was happy for me to share this project.

---

## 10. Résumé line

```
Built a parts lookup web app for Birchwood Auto Parts that handled 2,100+ lookups in its first
month; named Student Partner of the Year.
```

I left AI tools off the résumé line on purpose. The line is for results, and the tools belong in the
portfolio.

## 11. Interview story

```
The situation:    Counter staff at an auto parts store were losing minutes on every old part
                  number, looking it up in a paper binder while customers waited.
What I had to do: Deliver a lookup tool they would use, that passed the seven criteria the
                  store manager signed, and that kept running for thirty days without me.
What I did:       I built the search, then rewrote it when peer review found an injection risk.
                  Usability testing showed people picking parts that were out of stock, so I
                  put in-stock parts first. The first thirty-day clock reset when the host
                  restarted, so I made the app start by itself.
The result:       More than 2,100 lookups in the first month, and a Student Partner of the Year
                  award from the store.
```

## 12. Where this points

Web development and internal business tools. I plan to stay in touch with the store manager through
the school.
