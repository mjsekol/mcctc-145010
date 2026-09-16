# Landmarks, Headings, and Lists
---
## Slide 1: Two pages. One of them is empty.
- They look the same on screen
- Both pass web-check with zero violations
- A screen reader gets structure from one
- From the other, six lines of text
Speaker notes: I have two pages open and you cannot tell them apart. Both pass the checker you used yesterday. One of them gives a screen reader user a banner, a main region, headings to jump between, and a list with a count. The other gives them six lines of plain text and nothing to navigate by. Today is about why.
Image: Two identical-looking browser windows side by side, one with a glowing outline of its structure behind it and one with nothing behind it.
---
## Slide 2: The div soup version
```html
<div class="top">
  <div class="title">Open Gym Nights</div>
</div>
<div class="content">
  <div class="heading">When</div>
  <div>Monday and Wednesday, 7 to 9 p.m.</div>
  <div class="heading">Bring</div>
  <div>- Court shoes</div>
</div>
```
Speaker notes: This is the first page. Look at the class names. They say title, heading, content. They make sense to the person who wrote them. The browser does not read class names for meaning. To the browser, every one of these is a generic box.
Image: None. This slide is code.
---
## Slide 3: The semantic version
```html
<header>
  <p>Riverside Rec Center</p>
</header>
<main>
  <h1>Open Gym Nights</h1>
  <h2>When</h2>
  <p>Monday and Wednesday, 7 to 9 p.m.</p>
  <h2>Bring</h2>
  <ul>
    <li>Court shoes</li>
  </ul>
</main>
```
Speaker notes: Same content. Every piece is now in the element made for what it is. A header, a main, a heading at level one, headings at level two, a paragraph, a list. None of this changes how it looks yet. All of it changes what it means.
Image: None. This slide is code.
---
## Slide 4: What Chrome hands a screen reader
- Div soup: six plain text lines
- Semantic: banner, main, headings, a list
- Class names carry no meaning to assistive technology
- Elements do
Speaker notes: This is what Chrome's accessibility tree looked like for each page. I captured it through the same headless Chrome our checker uses. On the left, text, text, text. On the right, a banner landmark, a main landmark, a level one heading, two level two headings, and a list with two items. Open the Accessibility tab in DevTools in a minute and check it yourself.
Image: Two accessibility trees drawn as indented outlines, the left one flat, the right one with labelled landmark and heading nodes.
---
## Slide 5: Landmarks are regions you can jump to
- header becomes banner
- nav becomes navigation
- main becomes main, and there is exactly one
- footer becomes contentinfo
- A named section becomes a region
Speaker notes: Here is the short list. Each of these elements shows up in the accessibility tree as a landmark, and screen reader users jump between landmarks the way you jump between tabs. One main per page. A section only becomes a region if it has a name, which usually comes from its heading through aria-labelledby.
Image: A page wireframe with its header, nav, main, and footer regions outlined and labelled with their landmark names.
---
## Slide 6: The wrong way to pick a heading
```
<h1>Teen Game Night</h1>
<h4>Schedule</h4>

FAIL HEADINGS  line 3: h1 jumps to h4, skipping h2 ('Schedule')
```
Speaker notes: This is the mistake that looks the most reasonable. Somebody wanted small section titles, so they picked h4, because h4 is small. The page looks tidy. Web-check says nothing. Structure check says the outline jumps from level one to level four. A screen reader user hears a main title and then a sub-sub-section with nothing in between. Heading levels are an outline. Size is next week.
Image: None. This slide is code.
---
## Slide 7: Headings are an outline
- One h1: what this page is about
- h2 for main sections, h3 inside them
- Going deeper, add one level at a time
- Going back up, skip as many as you like
Speaker notes: The rule has two halves. Going deeper, one level at a time. Coming back out, as many levels as you need. So h2, h3, h4, then back to h2 is fine. h2 straight to h4 is not. Run structure check and read the outline it prints out loud. If it sounds like a table of contents, you got it right.
Image: A book-style table of contents with indented entries, each labelled with its heading level.
---
## Slide 8: Lists, and the meaning of order
- ul when order does not matter
- ol when it does, and it numbers itself
- Only li goes directly inside either
- strong means important. b only means bold.
Speaker notes: Lists. Unordered when the order is not meaningful, like a packing list. Ordered when it is, like directions. The ordered list does the numbering, so never type the numbers yourself, or you get one period one on the screen. And one quick pair while we are here. Strong means important. B only means bold. A rule is important.
Image: A packing list with bullets beside a set of numbered directions, with the numbers visibly generated by the list.
---
## Slide 9: What you are about to build
- Lab W01-01 Part 2: replace every generic box
- Landmarks first, then headings, then lists
- Run structure_check after each kind of change
- Build 2: your league page skeleton
Speaker notes: Build one is part two of the lab. Save the structure check output before you start, because you want the before and after. Replace the landmark divs, run the checker. Give the page its headings, run it again. Make the lists lists, run it again. Watch each line change. Build two, you get Dana's answers and build the skeleton of the league page, every landmark and every heading, before any content.
Image: A terminal showing structure_check output with the LANDMARKS line changing from none to four landmarks.
