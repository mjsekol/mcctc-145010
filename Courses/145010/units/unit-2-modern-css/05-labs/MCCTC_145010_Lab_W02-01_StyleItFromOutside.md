# Lab W02-01 · Style It From Outside
## 145010 Web Design & Senior Capstone · Week 2, Monday (Part 1) and Tuesday (Part 2)

**Competencies:** 6.1.7 (integrate inline and external styles), 6.5.7 (create and attach CSS),
6.2.7 (hover effect on a link), 6.2.4 (wrap text around an image with CSS), 6.2.5 (resize an
image with CSS), 6.2.6 (insert audio and video with HTML tags), 6.5.8 (format layout, including
iframes)

**Grade category:** Lab & Practice. Part 1 is due at the end of Monday. Part 2 is due at the end of
Tuesday.

---

## The situation

The Eastgate Esports Club is an invented high school club, and its officers wrote a clean,
semantic page for the spring bracket and then ran out of time. It has every heading, list, and
table it needs, no styling at all, and a qualifier-night photo straight off a camera that is 2,400
pixels wide. The officers want it to look like the club on a laptop and still work on the phone
people will actually open it on.

**What you will build:** one external stylesheet that gives the bracket page its type, color, link
effects, and media sizing, plus the video, audio, and embedded bracket board the page is missing.

---

## Before you start

Copy `lab-w02-01-files/` into your own work repository as `eastgate/`, and commit it untouched.
Every checker command runs **from the root of the course repository**, the folder that contains
`tools/` and `Courses/`, exactly as in Week 1. Replace `<your path>` with the path to your work
folder.

Read the Monday notes, `03-lecture-notes/MCCTC_145010_Notes_AttachingCSSAndTheCascade.md`, if you
missed Monday's instruction, and the Tuesday notes,
`03-lecture-notes/MCCTC_145010_Notes_MediaInTheFlow.md`, before Part 2.

Open the page in Chrome with DevTools open (F12) and keep DevTools open all week.

---

## The starter

| File | What it is |
|---|---|
| `index.html` | The bracket page. Valid, semantic, and unstyled. Comments mark where Part 1 and Part 2 add things. |
| `styles/site.css` | A stub. It is not attached to anything yet, and its one rule changes nothing you can see. |
| `media/team-photo.jpg` | The qualifier-night photo, 2400 by 1600, about 312 KB |
| `media/bracket-recap.webm` and `.mp4` | An 11-second narrated welcome clip, the same video in two formats |
| `media/bracket-recap.vtt` | Captions for the clip, three timed lines |
| `media/bracket-recap-poster.jpg` | A still frame to show before the video plays |
| `media/match-call.mp3` | A 6-second announcer call |
| `embeds/bracket-board.html` | A local page that **stands in for a third-party bracket service**. A real club would paste an embed snippet from that service. This one needs no account and no network. |

The media was generated for this course. The narration is a computer voice.

**The starter loads and does nothing useful.** Run the checker on it before you change anything:

```
node tools/web-check/check.js <your path>/eastgate/index.html --widths 360,768,1280
```

It fails. Write the three overflow numbers in `eastgate/notes.md`. You fix them on Tuesday.

If the command itself errors instead of printing `PASS` or `FAIL`, your checker setup from Week 1 is
broken. Follow [the web-check README](../../../../../tools/web-check/README.md) before you go on.

---

## Part 1 · Monday · Type, color, links, and the cascade

**Step 1.** Run `structure_check` on the starter.

```
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your path>/eastgate/index.html
```

*Observable result:* `PASS`, `0 fail, 0 warn`. The structure is already right. Everything you do
this week is appearance, and none of it should change this result.

**Step 2.** Attach the stylesheet. Replace the comment on line 8 of `index.html` with a `<link>`
element that points at `styles/site.css`.

*Observable result:* nothing on the page changes. In DevTools, open Elements, click the `<html>`
line, and find the `html { color: inherit; }` rule in the Styles pane with `site.css` next to it.
**That is your proof the file loaded.** If it is not there, go to "If it breaks" before you write
another rule.

**Step 3.** Replace the stub rule in the Part 1 block with a `body` rule: a sans-serif font stack,
a line height of 1.5, a dark body text color, a white background, no margin, and 1rem of padding
on the left and right.

*Observable result:* the whole page switches from a serif font to a sans-serif one, and the text
no longer touches the edges of the window.

**Step 4.** Give `h1`, `h2`, and `h3` one club color in a single rule, and style `.club-name` and
`.seed`. Choose colors with at least 4.5:1 contrast against white. Write each ratio in a comment.

*Observable result:* every heading changes color at once, from one rule.

**Step 5.** Style the round 1 table: collapse the borders, add padding to `th` and `td`, add a
bottom border to each row, and left-align the text.

*Observable result:* the table has lines between rows and no double borders.

**Step 6.** Style links. Give `a` a color that passes contrast and keep the underline. Then write
one rule for `a:hover` **and** `a:focus-visible` that changes the text color and the background
color, and a second rule that gives `a:focus-visible` a visible outline.

*Observable result:* point at a nav link and it changes. Then take your hand off the mouse, click
the address bar, and press Tab until a nav link is focused. **It changes the same way, and it has
an outline.**

**Step 7.** Prove the cascade. In `site.css`, give `.season-note` one color. In `index.html`, add
an inline `style` attribute to the season note paragraph with a **different** color.

*Observable result:* the paragraph shows the inline color. Select it in DevTools. The Styles pane
shows your `.season-note` rule with its `color` line struck through.

In `notes.md`, write two or three sentences: which color won, which rule lost, and the cascade
rule that decided it. Then say whether you would keep an inline style like this in a real site,
and why.

**Step 8.** Run both checkers and commit.

*Observable result:* `structure_check` still reports `0 fail, 0 warn`. `web-check` still fails
with the same three overflow numbers, plus or minus a few pixels from your padding. That is
expected until Part 2. Commit with a message that says Part 1 is done.

---

## Part 2 · Tuesday · Media that fits, and media that is accessible

**Step 9.** Add `width="2400" height="1600"` to the photo's `<img>`. Then, in the Part 2 block,
write one rule for `img` and `video` that sets `max-width: 100%` and `height: auto`.

*Observable result:* run `web-check`. The overflow is gone at all three widths. Write the new
result in `notes.md` next to the old numbers.

**Step 10.** Float the photo. Give `.photo` `float: right`, a width of 45%, and a left and bottom
margin. Give the `#club-night` section `display: flow-root`.

*Observable result:* at a wide window the paragraphs wrap beside the photo and continue under it.
The "Round 1 schedule" heading starts **below** the photo, not beside it.

**Step 11.** Add the recap video where the step 11 comment is: a `<video>` with `controls`,
`width="640"`, `height="360"`, `preload="metadata"`, and the poster image, containing two
`<source>` elements (WebM first, then MP4), a `<track kind="captions">` with `srclang`, `label`,
and `default`, and a fallback paragraph with a download link. Give it an `h3` above it.

*Observable result:* the player appears with the poster frame. **Captions probably do not appear
yet.** Serve the folder:

```
cd <your path>/eastgate
python -m http.server 8000
```

Open `http://127.0.0.1:8000/` and play the clip. The three caption lines appear as the narrator
speaks. Stop the server with Ctrl+C when you are done testing.

**Step 12.** Add the match call where the step 12 comment is: an `h3`, an `<audio controls>`
with a fallback paragraph, and a paragraph that starts `Transcript:` with the exact words the
announcer says. Listen to the clip to get them.

*Observable result:* an audio player, and the transcript text directly under it.

**Step 13.** Embed the bracket board where the step 13 comment is: an `<iframe>` with
`src="embeds/bracket-board.html"`, a `title` that says what is in it, `width="640"`,
`height="360"`, `loading="lazy"`, and a class. In CSS, give that class `display: block`,
`box-sizing: border-box`, `width: 100%`, `height: auto`, `aspect-ratio: 16 / 9`, and a border.

*Observable result:* set DevTools to a 360-pixel-wide device. With 1rem of body padding, the
frame is 328 pixels wide and 184.5 pixels tall.

**Step 14.** Run both checkers at all three widths, look at the page at 360, 768, and 1280, and
commit.

*Observable result:* `web-check` reports `PASS` with `0 violation(s)` at every width.
`structure_check` reports `0 fail`.

---

## Acceptance criteria

1. `index.html` links `styles/site.css`, and nothing in `index.html` is styled inline except the
   one season note paragraph from step 7.
2. Every heading color, link color, and text color has a contrast ratio of at least 4.5:1 against
   its background, written in a comment.
3. A link looks the same when hovered and when focused with the keyboard, and the keyboard version
   has a visible outline.
4. `notes.md` names the winning color, the losing rule, and the cascade rule that decided it.
5. The photo is never wider than its column, keeps its 3:2 shape, and has text wrapping beside it
   at 1280.
6. The next section never starts beside the photo.
7. The video has two sources, a captions track that loads when the page is served, and fallback
   content. The audio has a transcript on the page.
8. The iframe has a `title` and is 16:9 at every width.
9. `web-check` passes at 360, 768, and 1280. `structure_check` reports zero FAIL lines.
10. `notes.md` holds the before and after overflow numbers.

---

## If it breaks

CSS almost never shows an error on the page. These are the likeliest problems and what you
actually see.

### Part 1

**The page looks exactly like the starter.** Your `<link>` path is wrong. The Console shows
`Failed to load resource: net::ERR_FILE_NOT_FOUND`. `structure_check` shows
`FAIL FILES     line 8: <link href="css/site.css"> points at a file that is not there` (with your
path in it). `web-check` does **not** catch this.

**One declaration does nothing, and the rest of the rule works.** A typo in a property name, such
as `colour`. The browser drops that one declaration and keeps the others. In DevTools the line
appears in the Styles pane struck through with a warning icon. On the build machine, a rule
written with `colour` kept only its `line-height`, and the headings stayed the body text color.

**Your `.season-note` color never shows.** That is step 7 working. An inline style beats any
stylesheet rule. If it happens on an element you did not give an inline style, look for a more
specific selector, which the Styles pane lists above yours.

**Hover works, and Tab shows nothing but a thin ring.** You wrote `a:hover` without
`a:focus-visible`. On the build machine, a link styled that way still had a transparent background
after Tab put focus on it.

### Part 2

**Captions never appear.** You opened the file by double-clicking it. The Console shows
`Unsafe attempt to load URL file:///.../media/bracket-recap.vtt from frame with URL file:///.../index.html. 'file:' URLs are treated as unique security origins.`
Serve the folder with `python -m http.server 8000` and use the `http://127.0.0.1:8000/` address.

**The video player stays empty.** A `<source>` path is wrong. The Console shows
`Failed to load resource: net::ERR_FILE_NOT_FOUND` once per bad source, and `structure_check`
reports each one as a `FILES` failure. The fallback paragraph does not appear, because the browser
does support video.

**The bracket board is a tall box on a phone.** You left out `height: auto`, so the `height="360"`
attribute still sets the height and the ratio is ignored. On the build machine it measured 328 by
360 instead of 328 by 184.5.

**The "Round 1 schedule" heading sits next to the photo.** The float escaped its section. Add
`display: flow-root` to `#club-night`. On the build machine at 1280, without it, the section ended
at 607 pixels and the photo at 762, and the next heading started at 627.

---

## Stretch goal

Give the photo `shape-outside` so the text follows a shape instead of a rectangle. You will need a
shape that makes sense for this photo, and you will need to explain in `notes.md` what changed at
360 pixels and why.

---

## Submission checklist

- [ ] `eastgate/index.html` with the link, the one inline style, the video, audio, transcript, and
      iframe
- [ ] `eastgate/styles/site.css` with Part 1 and Part 2 blocks and contrast ratios in comments
- [ ] `eastgate/notes.md` with the cascade explanation and the before and after overflow numbers
- [ ] `web-check` passes at 360, 768, and 1280
- [ ] `structure_check` reports zero FAIL lines
- [ ] You watched the clip with captions on a served page
- [ ] Committed and pushed at the end of Monday and again at the end of Tuesday

---

## Extended options

Choose one, or your instructor will hand you one. All four are graded on the same scale and
assess the same competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes of Monday | Give them |
|---|---|
| Still has no `site.css` rule showing in the Styles pane after step 2 | SCAFFOLDED |
| Through step 5 and reading the Styles pane without being asked | STANDARD or EXTENDED |
| Asks how to change the whole color scheme without editing every rule | EXTENDED |
| Asks why anyone styles a bracket page, or says this is not their kind of site | APPLIED |

### SCAFFOLDED

Same page and the same targets, smaller steps. Your instructor gives you a `site.css` with every
selector already written and the declarations missing:

```css
body { }
h1, h2, h3 { }
a { }
a:hover, a:focus-visible { }
a:focus-visible { }
.season-note { }
img, video { }
#club-night { }
.photo { }
.board-frame { }
```

Fill in the declarations. In Part 2, the video, audio, and iframe markup are the same as STANDARD.
**Extra checkpoints:** show your instructor after step 2, step 6, and step 11.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **one place to change the club colors.** Rewrite `site.css` so the
purple and the teal are each written once, and every rule that uses them refers to that one place.
Then change the purple to a different accessible color and show that every heading, the hover
background, and the iframe border all change together.

Write in `notes.md` what the browser does when a rule refers to a name that was never defined.

*Hint, not the answer:* MDN's page "Using CSS custom properties (variables)" covers declaring a
value once and reading it everywhere. Search MDN for that title.

### APPLIED

Same skills, a different domain. Take a page you care about that has no styling: a plain-text
recipe you cook, a set list for a band, a training plan for a sport you play. Build it as valid,
semantic HTML with at least one table, one photo you took yourself (no people's faces), one short
video or audio clip you recorded yourself with captions or a transcript, and one embedded local
page. Then do every step of this lab to it.

Answer in `notes.md`: which of your media elements was hardest to make fit a phone, and what did
`web-check` not tell you about it.

All four options are graded with the same rubric as STANDARD.
