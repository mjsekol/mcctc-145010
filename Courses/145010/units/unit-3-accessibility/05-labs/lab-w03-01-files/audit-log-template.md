# Accessibility Audit Log · Lantern Street volunteer page

Copy this file into your repository as `audit/audit-log.md` and fill it in.

**Auditor:** your first name only
**Page audited:** `lab-w03-01-files/index.html`, the starter, before you changed anything
**Standard:** WCAG 2.2, Level A and AA

---

## Pass 1 · The tool pass

Run this from the repository root and paste the complete output below, unedited.

```
node tools/web-check/check.js <path to your copy of index.html>
```

```
paste the output here
```

**Count:** web-check reported ___ validation errors and ___ distinct axe rules.

---

## Pass 2, Pass 3, Pass 4 · The log

One row per problem. A problem that appears in three places is one row with three line numbers.

| # | Line(s) | What is wrong, in one sentence | Who it stops, and from doing what | WCAG 2.2 success criterion, number and name | Found by | Fix |
|---|---|---|---|---|---|---|
| 1 | | | | | web-check / me / both | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

Add rows as you need them.

**Rules for the "WCAG" column.**

- Write the number **and** the name exactly as W3C publishes it. `1.4.3 Contrast (Minimum)` is right. `contrast` is not.
- If you believe a problem is real and you cannot find a success criterion it fails, write `no WCAG criterion found` and say why it still matters. That is an allowed answer. A made-up criterion number is not.

**Rules for the "Found by" column.**

- `web-check` means the tool reported it in Pass 1.
- `me` means the tool said nothing about it and you found it.
- `both` means the tool reported it and you would have found it anyway. Be honest.

---

## Summary

1. How many problems did web-check report? How many did you log in total?
2. Which problem on your list would stop a real volunteer soonest, and who is that volunteer?
3. Name one problem the tool missed and explain why a tool could not have caught it.
4. Name one row where you were unsure which success criterion applied, and what you decided.
