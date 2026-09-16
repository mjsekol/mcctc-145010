# Where Styles Come From, and Who Wins
---
## Slide 1: You changed the CSS and nothing happened
- You saved the file
- You refreshed twice
- The page did not change
- No error anywhere on the screen
Speaker notes: Everybody in this room is going to have this moment this week, probably today. You edit a rule, you save, you refresh, and the page looks exactly the same. There is no red text and no message. Today you learn the two reasons this happens, and how to find out which one it is in under a minute instead of twenty.
Image: A browser window showing an unstyled page beside a code editor with a saved stylesheet, both calm, no error anywhere.
---
## Slide 2: A rule is a selector plus declarations
```css
.theme {                /* selector: which elements */
  color: #047857;       /* declaration              */
  font-weight: 700;     /* declaration              */
}
```
Speaker notes: Here is the whole grammar. The selector picks elements. Each declaration is one property and one value, ending in a semicolon. If you have written XAML styles, this is the same idea with less typing. A typo in a property name does not crash anything. The browser drops that one declaration and keeps going, which is the first way nothing happens.
Image: None. This slide is code.
---
## Slide 3: Styles come from three places
- External: a link element pointing at a .css file
- Internal: a style block inside the page head
- Inline: a style attribute on one element
- External is the default. Inline is the exception.
Speaker notes: External is where almost everything you write lives, because one file styles every page. Internal is for one page that genuinely differs. Inline is one element, one time, and it is the hardest to find later because it hides in the HTML. The state standard asks you to use inline and external, so you will do both today, on purpose.
Image: Three labelled arrows, from a CSS file, a style block, and an attribute, all pointing at one paragraph.
---
## Slide 4: Attaching the external sheet
```html
<head>
  <meta charset="utf-8">
  <title>Spirit Week</title>
  <link rel="stylesheet" href="styles/site.css">
</head>
```
Speaker notes: One line, in the head. The href is a relative path from the HTML file to the CSS file, exactly like the links you wrote last week. Watch the folder name. I am going to type this in front of you now, and I am going to type it wrong.
Image: None. This slide is code.
---
## Slide 5: Watch this: css/style.css
- The real file is styles/site.css
- The page loads in Times New Roman
- Console: Failed to load resource: net::ERR_FILE_NOT_FOUND
- web-check: PASS. structure_check: FAIL FILES
Speaker notes: This is the wrong way, and look at how quiet it is. The page renders, in the browser default font, with a black heading. Nothing on the page says anything failed. The Console does, and so does the Network tab. And here is the lesson inside the lesson: web-check passes this page, because an unstyled page is still valid and still accessible. structure_check looked for the file and failed it. A pass from one tool only means that tool found nothing.
Image: A DevTools Console panel with one red line reading Failed to load resource, next to a plain unstyled page.
---
## Slide 6: When rules disagree, the cascade picks
- One winner per property, not per rule
- Inline beats stylesheet rules
- Then specificity: id, then class, then element
- Then order: later wins a tie
Speaker notes: This is the second reason nothing happens. Your rule loaded, and it lost. The browser compares declarations for the same property on the same element. Inline wins. If both are in stylesheets, the more specific selector wins. If specificity ties, the later one wins. Per property: a rule can lose its color and still win its font weight.
Image: A bracket diagram: inline, then specificity, then source order, with a single winner at the end.
---
## Slide 7: Predict both spans
```html
<link rel="stylesheet" href="styles/site.css">  <!-- .theme: green, bold -->
<style> .theme { color: #6d28d9; } </style>
<span class="theme">Pajama Day</span>
<span class="theme" style="color: #b0001d;">Decades Day</span>
```
Speaker notes: Write down the color and the weight of both spans before I run it. Then I will open the Styles pane and we will read the answer off the screen. The measured result: Pajama Day is purple and bold. Decades Day is red and bold. The external rule lost the color both times and still won the weight both times.
Image: None. This slide is code.
---
## Slide 8: Hover is a selector state
```css
a:hover,
a:focus-visible {
  color: #ffffff;
  background-color: #1d4ed8;
}
a:focus-visible { outline: 3px solid #b45309; }
```
Speaker notes: A hover effect is a rule with a state on the end. Hover matches while the pointer is over the link. Focus-visible matches when the keyboard put focus there. Write them together, always. I tested hover alone on the build machine: after pressing Tab, the background did not change at all. A keyboard user gets nothing but the browser's thin default ring.
Image: None. This slide is code.
---
## Slide 9: Your debugging order, every time
- Console first: did the file load
- Elements panel: is the element the one you think
- Styles pane: is your rule listed, and struck through
- Computed tab: what value actually won
Speaker notes: Four stops, in this order, and it takes under a minute. If the file did not load, nothing else matters. If your rule is not listed, your selector does not match. If it is listed and struck through, it lost, and the pane tells you what beat it. Resist fixing a lost rule with an inline style. Find out why it lost first.
Image: The four DevTools panels arranged left to right with numbered badges.
---
## Slide 10: What you are about to build
- Rep 01 or 06 first, ten minutes, no AI
- Lab W02-01 Part 1: attach the Eastgate stylesheet
- Type, color, hover, and keyboard focus
- Prove the cascade with one inline style
Speaker notes: Build one opens with the Gate 1 rep. Then the Eastgate Esports Club page, which is invented. It has structure and no styling. You attach the stylesheet and prove it loaded, then give it type, color, and a link effect that works for a mouse and a keyboard. Step seven asks you to add one inline style on purpose and write down which rule lost and why. That sentence is graded. Web-check will fail this page today because of a giant photo. That is tomorrow's problem, and the lab tells you so.
Image: The unstyled Eastgate bracket page on the left, a styled version with purple headings on the right.
