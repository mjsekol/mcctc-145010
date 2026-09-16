# Layout Is the Parent's Job
---
## Slide 1: The footer that climbed up the page
- Two columns built with floats
- The blue box behind them vanished
- The footer slid up under the columns
- web-check said PASS
Speaker notes: This page is on the screen right now. It looks almost right, and then you see the footer sitting behind the columns and the background box reduced to a thin blue line. Nothing errored. The checker passed it. Today you learn the two tools built for layout, and why the old tools fail like this.
Image: A page with two columns, a thin blue line where a box should be, and a yellow footer overlapping the columns.
---
## Slide 2: Watch this: the float layout
```css
.columns  { border: 3px solid #1d4ed8; background-color: #dbeafe; }
.col-main { float: left;  width: 65%; }
.col-side { float: right; width: 30%; }
```
```
.columns  height 0px
footer    top 94px
```
Speaker notes: This is the wrong way. A float is taken out of the normal flow, so the parent does not count it when it works out its own height. Zero pixels. The only thing left of the box is its two borders. The footer starts at 94 pixels, right under the header. Old tutorials and a lot of AI output still build pages like this.
Image: None. This slide is code.
---
## Slide 3: The other old way: a layout table
- A table with role presentation
- web-check: PASS at all three widths
- structure_check: WARN, a table used for layout
- Two cells stay side by side on a phone
Speaker notes: The second wrong way is the table you learned last week, used to put a sidebar beside content. Role presentation tells assistive technology to ignore the rows and columns, so the accessibility check stays quiet. structure_check warns. The real problem is that a table cannot reflow. On a phone you are stuck fighting it.
Image: A narrow phone with two cramped table cells side by side.
---
## Slide 4: The rule for today
- The parent decides where children go
- Flexbox arranges a line
- Grid arranges a plane: rows and columns
- Pages usually use both
Speaker notes: You have done this in WPF. A StackPanel lines children up, a Grid places them in rows and columns, and the container decides. Same idea here. One direction, reach for flex. Rows and columns that line up, reach for grid. The page is usually a grid, and the header inside it is usually a flex row.
Image: A stack of three boxes in a row labelled flex, next to a two by two grid labelled grid.
---
## Slide 5: Flexbox: a line of links
```css
.site-header ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
```
Speaker notes: Display flex goes on the parent, the list, not on the links. Gap puts space between items so you are not fighting margins. Flex wrap lets the links drop to a second line on a narrow screen instead of squeezing.
Image: None. This slide is code.
---
## Slide 6: Predict the widths
```css
.row { display: flex; width: 600px; }
.a   { flex: 1; }
.b   { flex: 2; }
.c   { width: 150px; flex: none; }
```
Speaker notes: Write the three widths before I run it. Measured on the build machine: 150, 300, 150. C keeps its 150 and will not grow or shrink. That leaves 450. A takes one share, B takes two.
Image: None. This slide is code.
---
## Slide 7: Grid: draw the page
```css
.page {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-areas:
    "head head"
    "main side"
    "foot foot";
  gap: 1rem;
}
main  { grid-area: main; }
aside { grid-area: side; }
```
Speaker notes: The area names are a picture of the page. Head across the top, main and side in the middle, foot across the bottom. Each child gets a grid area name. Change the picture and the layout changes with no change to the HTML, which is exactly what tomorrow's media query will do.
Image: None. This slide is code.
---
## Slide 8: Cards without a single query
- repeat(auto-fit, minmax(min(12rem, 100%), 1fr))
- As many 12rem columns as fit
- 1280: three columns. 768: two. 360: one.
- min() stops overflow on tiny screens
Speaker notes: This one line does a lot. Grid counts how many 12 rem columns fit, makes that many, and shares out the leftover. I measured three columns at 1280, two at 768, and one at 360, with no media query. The min function means a column is never wider than the list itself. Leave it out with a big minimum and a phone overflows.
Image: The same card list at three widths, three columns, two columns, one column.
---
## Slide 9: It fits, and it is cramped
- Grid page at 360: columns 170 and 142 pixels
- No overflow, web-check passes
- Nobody wants to read that sidebar
- Tomorrow: a query that stacks it
Speaker notes: Here is the honest ending. The grid page fits a phone, and it is cramped: two skinny columns. The columns are not even two to one at 360, because the sidebar's padding and its longest word need more room than a third. That is the problem tomorrow solves, with one media query.
Image: A phone screenshot of two narrow columns with words breaking awkwardly.
---
## Slide 10: What you are about to build
- Rep 04 or 13 first, ten minutes, no AI
- Lab W02-02 Part 1 on your Eastgate page
- A page grid, a flex nav, a card grid
- No floats for layout. No layout tables.
Speaker notes: Build one opens with the rep. Then Lab W02-02 Part 1 on your own Eastgate page from Monday and Tuesday. First, paste in the standings section from the lab folder. Then the body becomes a grid with named areas, the nav becomes a flex row that wraps, and the team cards become an auto-fit grid. Today the page is one column everywhere. Tomorrow you decide when it becomes two.
Image: The Eastgate page with a grid overlay showing header, main, aside, and footer areas.
