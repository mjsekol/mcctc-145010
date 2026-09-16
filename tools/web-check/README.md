# web-check

The page checker for 145010. It is the same tool your course materials were verified with.

## Why you run it

A page can look right in your browser and still be broken. The markup can be invalid, a form
field can have no label, text can be too faint to read, or the layout can spill off a phone
screen. You will not see most of that by looking. This tool finds the part a machine can find,
every time, in a few seconds.

**It does not find everything.** Automated checks catch only part of what makes a page
accessible. Keyboard order, whether alt text actually describes the image, and what a screen
reader says still need you. A passing result means "no machine-detectable problems", not
"accessible".

## What it checks

For every page you give it:

1. **HTML validation**, with html-validate. This runs offline.
2. **An accessibility audit**, with axe-core, inside headless Chrome, using the WCAG 2.0 and 2.1
   Level A and AA rules.
3. **Horizontal overflow** at each width. A page wider than the screen is the usual sign that a
   layout is not responsive.

It runs the audit and the overflow check at 360, 768, and 1280 pixels wide unless you pick other
widths.

## Set it up once

You need Node.js and Chrome or Edge. Your instructor confirms both are on the lab machines.

From the root of this course repository:

```
cd tools/web-check
npm install
cd ../..
```

`npm install` downloads the three libraries listed in `package.json` into a `node_modules`
folder here. That folder is large and is never committed.

If the tool cannot find your browser, set `CHROME_PATH` to the full path of `chrome.exe` or
`msedge.exe`.

## Run it

From the root of this course repository, give it the path to your page:

```
node tools/web-check/check.js path/to/your/index.html
```

Check several pages at once, pick widths, or save a screenshot at each width:

```
node tools/web-check/check.js index.html about.html
node tools/web-check/check.js index.html --widths 360,1280
node tools/web-check/check.js index.html --shots screenshots
```

Other options: `--no-validate` skips validation, `--no-axe` skips the browser audit, and
`--json` prints one result object per page.

## Read the result

```
PASS  index.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

A `FAIL` lists every problem with its line number or the element it found. The exit code is 0
only when every page passes, so you can use it in a script.

**Two rules are switched off on purpose.** A lowercase `<!doctype html>` is valid, and Week 2
teaches inline styles, so neither is reported.
