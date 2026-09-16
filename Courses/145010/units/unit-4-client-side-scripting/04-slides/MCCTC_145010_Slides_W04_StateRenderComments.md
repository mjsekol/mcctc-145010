# State, Render, and Comments That Tell the Truth
---
## Slide 1: The page that contradicts itself
- The button says you dropped the shift
- The total still counts it
- Nobody wrote a bug on purpose
- Two handlers each updated their own piece
Speaker notes: Here is a bug you will write this week if nobody warns you. One handler updates the button and the total. Another handler updates only the button. Now the page says two different things. Nothing crashed. Today is about the pattern that makes this bug impossible, the one line that turns typed text into running code, and the fact that your comments are public.
Image: A shift board where one button reads dropped and the total beneath it still includes that shift, both circled.
---
## Slide 2: Three parts, one direction
- State: what is true right now, in one place
- Render: the one function that writes the page
- Events: change the state, then call render
- Handlers never touch the page directly
Speaker notes: State, render, events. The state is the truth. Render reads the truth and makes the page match. Events change the truth and call render. Every framework you will ever meet is a fancier version of this, and you are writing it by hand so you know what the framework is doing for you.
Image: A loop diagram: person acts, handler changes state, render, page, back to person.
---
## Slide 3: The pattern in code
```js
const votes = new Set();

function render() {
  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(votes.has(button.textContent)));
  }
  tally.textContent = `You voted ${votes.size} of ${MAX_VOTES} times.`;
}
```
Speaker notes: The state is one Set. Render loops over every button and sets aria-pressed from the Set, then writes the tally from the Set. Nothing in here knows which button was clicked. It does not need to. It makes the whole page match the state, every time.
Image: None. This slide is code.
---
## Slide 4: The handler only changes state
```js
button.addEventListener("click", () => {
  const name = button.textContent;
  if (votes.has(name)) {
    votes.delete(name);
  } else if (votes.size < MAX_VOTES) {
    votes.add(name);
  }
  render();
});
```
Speaker notes: The handler decides what the truth is now, and then calls render. The cap of two is why this matters. A third click changes nothing, and the page still has to say two of two. One render keeps every part of the page in agreement.
Image: None. This slide is code.
---
## Slide 5: Two ways to put words on a page
- textContent puts characters on the page
- innerHTML sends a string to the HTML parser
- The parser builds elements, and some run code
- If a person typed it, it is text
Speaker notes: This is the security rule of the week. textContent never creates an element. innerHTML hands your string to the same parser that read your HTML file, and it builds whatever the string describes, including elements with event attributes that run JavaScript. The rule is short: if a person typed it, it is text, so it goes in with textContent.
Image: Two pipes: one labelled textContent delivering plain letters, one labelled innerHTML delivering assembled parts.
---
## Slide 6: The wrong way, and what it does
```js
preview.innerHTML = `<p>${textBox.value}</p>`;
```
```
typed:  <img src="x" onerror="document.body.dataset.owned='yes'">
result: 1 image element in the preview, and the onerror code ran
```
Speaker notes: This is a live preview of what the person is typing. Type an image tag with a broken source and an error handler. The parser builds a real image, the image fails to load, and the browser runs the handler as JavaScript. No error, no warning. That is cross-site scripting. Now watch me change one word, innerHTML to textContent, and type the same thing. The characters appear, and nothing runs.
Image: None. This slide is code.
---
## Slide 7: Comments say why
- Not what the line does. Why.
- Why this number lives in a constant
- Why the test is greater than, not greater or equal
- Why the panel starts visible
Speaker notes: A comment that repeats the code is noise, and a comment that disagrees with the code is a trap for the next reader. The comments worth writing answer a question the code cannot answer. Why is it greater than and not greater or equal? Because exactly twelve hours is allowed. Change a line, reread the comment above it.
Image: A code block with one useless comment struck through and one why-comment highlighted.
---
## Slide 8: Every comment is public
- A .js file is downloaded by every visitor
- View Source shows every comment
- No passwords, keys, or notes about people
- No "this check is fake, fix later"
Speaker notes: Open View Source on any page and click the script file. Every comment is there. That is fine for comments that explain the code. It is a problem for anything you would not say to the visitor's face. And a comment admitting a check is fake is an invitation.
Image: A browser View Source window with a comment line highlighted and an eye icon beside it.
---
## Slide 9: Three kinds of comment
```js
/*
 * shift-board.js
 * Loaded with defer, so every element exists when this runs.
 */

// Exactly 12 is allowed. Only more than 12 is over.
summary.classList.toggle("over-limit", hours > HOUR_LIMIT);
```
```html
<!-- The rules panel starts visible, so the page works if the script fails. -->
```
Speaker notes: A header block at the top of the file says what the file does and what a reader must know before line one. Line comments sit above the line whose reason is not obvious. HTML comments use the angle bracket form, and that form does not work inside a JavaScript file.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Lab W04-01, steps 13 to 15, and submit
- A comments pass: every comment true, header block present
- Project Define: your component's state, events, and keys
- web-check must pass before you submit
Speaker notes: Build one finishes the lab. Read every comment against the line under it, add the header block, search your file for innerHTML, and run web-check. Build two starts the project. Before any code, write your component's state as a code block in the decision log, list its events, and list the keys it must support.
Image: A decision log page with a small state object in a code block and a list of keys beside it.
---
