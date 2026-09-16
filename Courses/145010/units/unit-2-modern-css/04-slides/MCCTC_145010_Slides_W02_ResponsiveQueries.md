# Ask the Screen, or Ask the Box
---
## Slide 1: The mockup that only works at one width
- The design was drawn at 1280 pixels
- You built it exactly: 960 wide
- A coach opens it at the field
- The page is 600 pixels too wide
Speaker notes: Every designer draws at one width. Every page gets opened at hundreds of widths. Today you learn to write one page that asks a question about the space it has and changes its layout based on the answer. There are two questions you can ask, and they are different questions.
Image: A laptop mockup and a phone side by side, the phone showing only the left third of the same page.
---
## Slide 2: Watch this: desktop first, fixed widths
```css
.page { width: 960px; margin: 0 auto; display: grid;
        grid-template-columns: 640px 300px; gap: 20px; }
```
```
axe at 360px: 0 violation(s), OVERFLOWS by 600px
axe at 768px: 0 violation(s), OVERFLOWS by 192px
axe at 1280px: 0 violation(s)
```
Speaker notes: This is the wrong way. 960 minus 360 is 600. 960 minus 768 is 192. The laptop is perfect and everything else scrolls sideways. The tempting fix is a max width query that patches the phone, and then another, and then the rules fight. We are going to flip it instead.
Image: None. This slide is code.
---
## Slide 3: Mobile first
- Base styles are the phone layout
- One column, everything stacked
- min-width queries add columns when there is room
- A browser that ignores queries still works
Speaker notes: Write the simple layout first, the one that works on the smallest screen, with no fixed widths. Then add. Each query only adds something. Nothing has to undo anything. This is also why min width is the query you will write almost every time this week.
Image: A narrow single column that grows a second column as the frame widens.
---
## Slide 4: A media query asks about the screen
```css
.page {
  display: grid;
  grid-template-areas: "head" "main" "side" "foot";
}

@media (min-width: 48em) {
  .page {
    grid-template-columns: 2fr 1fr;
    grid-template-areas: "head head" "main side" "foot foot";
  }
}
```
Speaker notes: 48 em is 768 pixels at the default text size, and min width includes the number itself. I measured it: one column at 767, two at 768. Using em means the breakpoint moves if a reader sets bigger text, which is what you want. Pick breakpoints where your content starts to look wrong, not from a list of phone sizes.
Image: None. This slide is code.
---
## Slide 5: A container query asks about the box
```css
.booths > li { container-type: inline-size; }

@container (min-width: 20rem) {
  .booth {
    display: grid;
    grid-template-columns: 5rem 1fr;
  }
}
```
Speaker notes: Mark the box, then ask about it. This card puts its table number beside the text when its own slot is at least 20 rem wide. It does not care about the screen at all. Two ways this silently does nothing: no container type on any ancestor, and a container type on a flex item with no width, which I measured collapsing to zero pixels.
Image: None. This slide is code.
---
## Slide 6: The laptop shows the stacked card
- 1280: two card columns, each slot 307px
- 360: one card column, the slot is 328px
- The query is set at 320px
- Laptop stacked, phone side by side
Speaker notes: This surprises people, so read it slowly. On the laptop the booth list has two columns, so each card's box is narrower than on the phone. A media query cannot see that. The container query can, and it got both right. Measured on the build machine.
Image: The same booth card twice, narrow and stacked in a laptop grid, wide and side by side on a phone.
---
## Slide 7: Container queries are an enhancement
- Chrome 153 on the build machine: supported and tested
- Other browsers were not tested here
- Your base card must work with no query
- Delete the query: does the page still work
Speaker notes: Container queries are newer than media queries. I confirmed they work in the Chrome on the build machine. I did not test Firefox, Safari, or older Chrome, so check current support before you promise anything. The honest way to use them is as an extra. The base card is stacked and fine. The query makes it nicer where it runs.
Image: A stacked card labelled works everywhere, and a side by side card labelled extra where supported.
---
## Slide 8: The wide table scrolls in its own box
```html
<section class="table-scroll"
         aria-labelledby="times-caption" tabindex="0">
  <table>
    <caption id="times-caption">Club meeting times</caption>
  </table>
</section>
```
```css
.table-scroll { overflow-x: auto; }
```
Speaker notes: The table is allowed to be wider than a phone. The page is not. The section scrolls, it takes its name from the caption, and tabindex zero lets a keyboard user focus it and scroll with arrow keys. I first wrote a div with role region, and html-validate told me to use a section, because a named section already is a region.
Image: None. This slide is code.
---
## Slide 9: The tag the checker cannot see
- No viewport meta tag
- web-check: PASS, because it does not emulate a phone
- Emulated phone: laid out at 980 pixels
- Desktop layout shrunk to about a third
Speaker notes: One line in the head makes a phone lay the page out at its real width. Without it, a phone pretends to be about 980 pixels wide and shrinks the result. On the build machine an emulated phone reported an inner width of 980 and a scale of 0.37, with two columns showing. Web-check sets a narrow window on a desktop browser, so it passes this page anyway. Always keep the tag.
Image: A phone showing a tiny two-column desktop page with unreadable text.
---
## Slide 10: What you are about to build
- Rep 05 or 10 first, ten minutes, no AI
- Lab W02-02 Part 2 on your Eastgate page
- A media query, a container query, a scroll box
- web-check shots at 360, 768, 1280, plus notes
Speaker notes: Build one opens with the rep. Then Part 2. The aside moves beside main on wide screens. The photo float moves inside a query so a phone stacks it. The team cards get a container query with a stacked base. The standings table gets its scroll box. Then you take screenshots at three widths, look at every one of them, and write what changed at each width. Web-check passing is the floor, not the finish.
Image: Three screenshots of the Eastgate page at phone, tablet, and laptop widths, side by side.
