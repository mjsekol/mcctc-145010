# Parts checkout list

An invented composite page for Gate 2, Week 14. **Ridgeview Robotics Club is not a real
organization.** Every name and note in the data is invented.

## What it is

A single page with client-side JavaScript, no framework and no network. Members type a part and a
short note, the checkout appears in the list, a filter box narrows the list as you type, and a count
shows how many parts are due back within 7 days. The data lives in `parts-data.js`, so the page runs
straight from a file.

## Run it

```
Open index.html in Chrome.
```

No server and no port. The page reads `parts-data.js` and `app.js` from this folder.

## Check it

From the repository root:

```
node tools/web-check/check.js Courses/145010/capstone/07-gate2-adversarial/W14/index.html
```

## Files

| File | What it is |
|---|---|
| `index.html` | The page |
| `app.js` | The client-side script |
| `parts-data.js` | The seed data and the reference date |
| `REQUIREMENTS.md` | What the page was built from. Read it first |
