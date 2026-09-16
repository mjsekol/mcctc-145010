# Media in the Flow
---
## Slide 1: The photo that broke the phone
- You add one photo from your phone
- It looks great on your laptop
- On a phone, the page slides sideways
- Every line of text is now harder to read
Speaker notes: A phone photo is thousands of pixels wide. Text wraps to fit its box. Photos, videos, and embedded pages do not, unless you tell them to. By the end of today every outside thing you drop into a page will fit the box it lands in, on any screen.
Image: A phone showing a page cut off on the right edge, with a horizontal scroll bar.
---
## Slide 2: Four elements that bring in outside things
- img: a picture, with alt, width, and height
- video controls: sources, captions track, fallback
- audio controls: fallback, plus a transcript
- iframe: a whole page, with a title
Speaker notes: Each one arrives with a size of its own. An iframe defaults to 300 by 150. A video knows its resolution. An image knows its pixel size. The width and height attributes on an image are still worth writing, because they let the browser reserve the right shape before the file arrives.
Image: Four boxes of different sizes spilling past the edge of a narrow column.
---
## Slide 3: Watch this: width 800px
```css
.mural-wide { width: 800px; height: auto; }
```
```
axe at 360px: 0 violation(s), OVERFLOWS by 456px
axe at 768px: 0 violation(s), OVERFLOWS by 48px
axe at 1280px: 0 violation(s)
```
Speaker notes: This is the wrong way. Eight hundred pixels looks sensible on a laptop, and web-check says the laptop is fine. At 360 the page is 456 pixels too wide: 800 of image, plus 16 of padding, minus 360 of screen. That number in the web-check output is the one to look for all week.
Image: None. This slide is code.
---
## Slide 4: Two lines that fix it
```css
img,
video {
  max-width: 100%;
  height: auto;
}
```
Speaker notes: Max-width says never wider than the box you are in, and it wins over width. Height auto says keep your shape when the width shrinks. Leave out height auto on an image that has a height attribute, and the attribute keeps the height. I measured that: 328 wide and 800 tall on a phone. A stretched photo.
Image: None. This slide is code.
---
## Slide 5: Wrapping text is what float is for
```css
.mural-story { display: flow-root; }
.mural {
  float: left;
  width: 40%;
  margin: 0 1rem 0.5rem 0;
}
```
Speaker notes: Float the figure, give it a width, and the text flows around it and then continues underneath at full width. Flow-root on the section keeps the float inside that section. Without it, the next heading climbs up beside the photo. I measured that at 1280: the section ended at 339 pixels and the figure at 392. This is the one legitimate float this week.
Image: None. This slide is code.
---
## Slide 6: Video with captions
```html
<video controls width="640" height="360" preload="metadata">
  <source src="media/bracket-recap.webm" type="video/webm">
  <source src="media/bracket-recap.mp4" type="video/mp4">
  <track kind="captions" src="media/bracket-recap.vtt"
         srclang="en" label="English" default>
  <p>Your browser cannot play this video.</p>
</video>
```
Speaker notes: The browser tries each source in order. The track points at a WebVTT text file with timed lines. Default turns captions on. The paragraph inside is only for a browser with no video support. It is not what you see when your path is wrong. A wrong path gives you an empty player and an error in the Console.
Image: None. This slide is code.
---
## Slide 7: The page that passes and is still wrong
- A narrated clip with no captions track
- web-check: PASS at all three widths
- The checker cannot hear your video
- A deaf viewer gets none of the narration
Speaker notes: This is the other kind of wrong. Nothing is broken according to the tool. The tool has no idea there is speech in the file, so it has no idea captions are missing. Captions are a human check, and the audio clip needs a transcript on the page for the same reason. Week three picks up the compliance side.
Image: A green PASS badge next to a video player showing a speaking character and no caption text.
---
## Slide 8: Captions that vanish on your machine
- Double-click the file: Chrome loads it from file:
- Chrome refuses the .vtt file. Zero cues.
- Console: Unsafe attempt to load URL
- Fix: python -m http.server 8000
Speaker notes: Your markup can be perfect and captions still will not show, if you opened the page by double-clicking it. Chrome treats every file address as its own origin and will not load the captions file. Serve the folder with Python on an explicit port, open 127.0.0.1 colon 8000, and the same track loads with three cues. Stop the server with Control C when you are done.
Image: A terminal running a Python server on port 8000 beside a video with captions showing.
---
## Slide 9: An iframe needs a shape
```css
.map-frame {
  display: block;
  box-sizing: border-box;
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 3;
}
```
Speaker notes: An iframe has no natural shape, so give it one. Full width, height auto, and a ratio. I measured 328 by 246 on a phone and 736 by 552 at 768. Forget height auto and the height attribute wins and the ratio is ignored. And every iframe needs a title that says what is inside it.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Rep 03 or 08 first, ten minutes, no AI
- Lab W02-01 Part 2 on the Eastgate page
- Fit the photo, then wrap text around it
- Add the captioned video, the audio, the board
Speaker notes: Build one opens with the rep. Then Part 2 of the Eastgate lab. The photo that made web-check fail yesterday gets fixed first, and you write down the overflow number before and after. Then the float with flow-root, the video with its captions track, the match call audio with a transcript, and the bracket board in an iframe sized with a ratio. The lab is done when web-check passes at all three widths and you have seen the captions on a served page.
Image: The Eastgate page at phone width with the photo, video, and bracket board all fitting the column.
