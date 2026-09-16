# Lecture Notes: Media in the Flow
## 145010 Web Design & Senior Capstone · Week 2 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W02_MediaInTheFlow.md) · no exported deck yet. Generate it from the repository root with `node tools/gamma.js Courses/145010/units/unit-2-modern-css/04-slides/MCCTC_145010_Slides_W02_MediaInTheFlow.md --export pptx`

If you missed class, you can learn this concept from this file alone. The pages used below are
in [examples/tue-media/](examples/tue-media/), with shared files in
[examples/media/](examples/media/) and [examples/embeds/](examples/embeds/).

**Competencies:** 6.2.4 (insert an image and wrap text around it with CSS), 6.2.5 (resize an
image with CSS), 6.2.6 (insert audio and video with HTML tags), 6.5.8 (format layout, including
iframes).

---

## Why this exists

Text is polite. It wraps to fit whatever box it lands in. **Images, video, audio players, and
iframes are not.** Each one arrives with a size of its own: a photo from a phone is thousands of
pixels wide, a video file knows its resolution, and an iframe defaults to 300 by 150 unless you
say otherwise. Drop one into a 360-pixel phone screen and it pushes the whole page sideways.

Today's idea in one line: **an outside thing drops into your flow, and CSS decides its size.**

---

## The concept in plain language

**Four elements, one job each.**

| Element | What it drops in | What you must add |
|---|---|---|
| `<img>` | a picture | `alt` text, and `width` and `height` attributes so the browser reserves space |
| `<video controls>` | a video with play controls | one or more `<source>` files, a `<track kind="captions">`, fallback content |
| `<audio controls>` | a sound with play controls | fallback content, and a transcript on the page |
| `<iframe>` | a whole other page | a `title` that says what is inside |

**Two CSS declarations make any image or video fit its box.**

```css
img,
video {
  max-width: 100%;   /* never wider than the box it sits in */
  height: auto;      /* keep the shape when the width shrinks */
}
```

`max-width` wins over `width`. An image told `width: 800px; max-width: 100%` in a 328-pixel box
comes out 328 pixels wide.

**Wrapping text around an image is what `float` is for.** Float the `figure`, give it a width,
and put `display: flow-root` on the section that holds it, so the float stays inside that
section. This is the one legitimate float this week. Tomorrow you lay out pages, and floats are
the wrong tool for that.

**An iframe has no natural shape, so you give it one.**

```css
.map-frame {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 3;
}
```

---

## Worked example 1: the image that fits

From [examples/tue-media/css/media.css](examples/tue-media/css/media.css), with a 1200 by 800
photo floated in a figure at `width: 40%`. Measured on the build machine:

```
width 360:   figure 131px wide, image 131 x 87
width 768:   figure 294px wide, image 294 x 196
width 1280:  figure 307px wide, image 307 x 205
```

The image is never wider than its figure, and 131 by 87 is the same 3:2 shape as 1200 by 800.
That is `height: auto` doing its job.

At 1280 the page body is capped at 48rem, which is why the figure stops growing.

---

## Worked example 2: video with captions, and audio with a transcript

```html
<video controls width="640" height="360" preload="metadata">
  <source src="media/bracket-recap.webm" type="video/webm">
  <source src="media/bracket-recap.mp4" type="video/mp4">
  <track kind="captions" src="media/bracket-recap.vtt" srclang="en" label="English" default>
  <p>Your browser cannot play this video.
     <a href="media/bracket-recap.mp4">Download the video (MP4)</a>.</p>
</video>

<audio controls preload="metadata" src="media/match-call.mp3">
  <p>Your browser cannot play this audio.
     <a href="media/match-call.mp3">Download the match call (MP3)</a>.</p>
</audio>
<p>Transcript: Match two is starting. Byte Night and Lag Wizards, report to station four.</p>
```

The browser tries each `<source>` in order and plays the first one it can. The paragraph inside
`<video>` only shows in a browser that has no video support at all. It is **not** what shows when
a file path is wrong.

A captions file is plain text in WebVTT format:

```
WEBVTT

1
00:00:00.300 --> 00:00:03.421
Welcome to the Eastgate Esports Club spring bracket.
```

With the Eastgate lab page served over `http`, Chrome on the build machine reported the track
loaded with 3 cues, and the first cue's text was the line above. `default` turns the captions on without the viewer
hunting for a button.

---

## Worked example 3: an iframe with a shape

[examples/tue-media/index.html](examples/tue-media/index.html) embeds a local page that stands in
for a third-party map:

```html
<iframe class="map-frame" src="../embeds/cafeteria-map.html"
        title="Cafeteria seating map for lunch B" width="400" height="300"></iframe>
```

Measured on the build machine with the CSS above:

```
width 360:   328 x 246
width 768:   736 x 552
width 1280:  768 x 576
```

Every size is 4:3, and none is wider than its column.

**The trap:** delete `height: auto` and the `height="300"` attribute wins. The ratio is ignored.
On the Eastgate lab page, with a `height="360"` attribute and no `height: auto`, the frame
measured 328 by 360 at a 360-pixel width instead of 328 by 184.5.

---

## The wrong version, and exactly what goes wrong

[examples/tue-media/too-wide.html](examples/tue-media/too-wide.html):

```css
.mural-wide { width: 800px; height: auto; }
```

Looks fine on a laptop. `web-check` on the build machine:

```
FAIL  .../tue-media/too-wide.html
  axe at 360px: 0 violation(s), OVERFLOWS by 456px
  axe at 768px: 0 violation(s), OVERFLOWS by 48px
  axe at 1280px: 0 violation(s)
```

456 is 800 pixels of image plus 16 pixels of body padding, minus the 360-pixel screen. On a phone
the whole page now scrolls sideways, and every line of text is harder to read. The fix is
`max-width: 100%`, and you can keep the `width: 800px` if 800 is the most you ever want.

### The one that passes and is still wrong

[examples/tue-media/no-captions.html](examples/tue-media/no-captions.html) has a narrated video
and no `<track>`.

```
PASS  .../tue-media/no-captions.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  ...
```

`web-check` cannot listen to your video. It does not know there is speech in it, so it cannot
know captions are missing. **A deaf viewer gets none of the narration, and the checker says
PASS.** Captions are a human check. Week 3 covers the compliance side.

### The captions that vanish on your machine

Open a page by double-clicking the file, and Chrome loads it from a `file:` address. Chrome then
refuses to load the `.vtt` file. On the build machine, with a plain Chrome, the Console said:

```
Unsafe attempt to load URL file:///.../media/bracket-recap.vtt from frame with URL
file:///.../index.html. 'file:' URLs are treated as unique security origins.
```

and the track reported 0 cues. Your markup is fine. Serve the folder instead:

```
python -m http.server 8000
```

Open `http://127.0.0.1:8000/`. When the Eastgate lab page was served this way on the build
machine, its track loaded with 3 cues. Stop the server with Ctrl+C.

---

## Why the wrong version is tempting

You build on a laptop. At 1280 pixels an 800-pixel image looks like a sensible choice, and
nothing on your screen tells you a phone is suffering. Fixed pixel sizes feel precise, and
precision feels like control.

The float version of the mistake is tempting for a different reason. You float a figure, the
text wraps, it looks right, and you move on. Remove `display: flow-root` from the demo and the
next heading climbs up beside the photo. Measured at 1280 on the build machine: the section ended
at 339 pixels, the figure at 392, and the next heading started at 359, beside the figure.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Replaced element** | An element whose content comes from outside the page: `img`, `video`, `iframe` |
| **`max-width: 100%`** | Never wider than the containing box, even if `width` says otherwise |
| **`height: auto`** | Work out the height from the width and the element's shape |
| **`aspect-ratio`** | A shape for a box that has none, written as width / height |
| **`float`** | Move a box to one side and let text wrap around it |
| **`display: flow-root`** | Make a box contain the floats inside it |
| **`<source>`** | One file a `video` or `audio` element may play, tried in order |
| **`<track kind="captions">`** | A timed text file for speech and important sound |
| **WebVTT** | The `.vtt` text format captions are written in |
| **Transcript** | The words of an audio clip written on the page |
| **Fallback content** | What a browser with no media support shows instead |

---

## Self-check

**Question 1.** An image has `width="1200" height="800"` attributes and the CSS
`img { max-width: 100%; }` with nothing else. What size is it on a 360-pixel screen with 16
pixels of padding each side, and what is wrong with it?

**Question 2.** A classmate's video has two `<source>` elements with the wrong folder name. They
expect the fallback paragraph to show. What do they actually see, and where is the evidence?

**Question 3.** `web-check` reports PASS on a page with a narrated video. Name one thing that
PASS does not tell you, and how you would check it.

---

### Answers

**1.** 328 pixels wide and 800 pixels tall. `max-width` shrank the width, but the `height`
attribute still sets the height, so the photo is stretched tall. Add `height: auto`. Verified on
the build machine: 328 x 800 without it.

**2.** An empty video player that never plays. The fallback paragraph is only for browsers with
no video support. The evidence is the Console, which on the build machine showed
`Failed to load resource: net::ERR_FILE_NOT_FOUND` once per source, and `structure_check`,
which reports each missing `src` as a `FILES` failure. `web-check` passed that page.

**3.** It does not tell you whether the video has captions, or whether the captions match the
speech. Check that a `<track kind="captions">` exists, serve the page, turn captions on, and
watch the clip with the sound off.
