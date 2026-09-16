# Where Script Lives
---
## Slide 1: Your code is right and it still fails
- You wrote three correct lines of JavaScript
- The Console says null
- Nothing on the page works
- The code is fine. It ran too early.
Speaker notes: Here is the first script most people ever write for a page, and it fails. The selector is right. The element exists. The browser still says null. By the end of these fifteen minutes you will know exactly why, and the fix is one word. First, a bigger question: why is this JavaScript at all, when you already know two languages?
Image: A browser Console with one red error line, and a calm HTML file beside it that clearly contains the element.
---
## Slide 2: The browser runs one language in the page
- JavaScript runs in every browser, inside the page
- Python, C#, PHP run on the server
- WebAssembly runs compiled code, reached through JavaScript
- This week, everything that responds is JavaScript
Speaker notes: You write Python and C# already, and both of them will matter again next week, on the server. But inside the page, the browser runs one general-purpose language, and that is JavaScript. WebAssembly exists and it is impressive, but it still talks to the page through JavaScript. So the choice for a hand-written page is not really a choice. That is competency 6.3.1.
Image: A simple two-column diagram: browser side with JavaScript, server side with Python, C#, and PHP, and an arrow between them.
---
## Slide 3: The file is the recipe. The tree is the page.
- The browser reads HTML top to bottom
- It builds a tree of objects: the DOM
- The tree is drawn and read aloud
- Scripts read and change the tree
Speaker notes: When the browser reads your HTML, it builds a tree of objects called the DOM. The tree is what gets drawn and what a screen reader reads. Your HTML file is the recipe for that tree. JavaScript works on the tree, not on the file. Keep that picture, because in a minute we will watch the file and the tree disagree.
Image: An HTML snippet on the left, and the matching node tree on the right, navy boxes joined by blue lines.
---
## Slide 4: Asking the tree a question
```js
document.querySelector("h1").textContent
document.querySelectorAll("main p").length
document.querySelector("#nothing-has-this-id")
```
Speaker notes: These are Console queries. The first returns the heading text. The second counts paragraphs in main. The third returns null, because nothing matches. querySelector takes the same selectors you wrote in Week 2. Remember what null looks like, because it is on the next slide.
Image: None. This slide is code.
---
## Slide 5: Watch this
```html
<head>
  <script src="monday.js"></script>
</head>
```
Speaker notes: The script tag is in the head, with no attribute. The script's first real line looks for the main element and appends a paragraph to it. Predict what happens before I reload.
Image: None. This slide is code.
---
## Slide 6: The real error
```
Uncaught TypeError: Cannot read properties of null (reading 'append')
```
Speaker notes: Read it from the end. append is what failed. It failed because the thing before the dot was null. The thing before the dot was the query for main. Main did not exist yet, because a script with no attribute runs the moment the parser reaches it, and the parser was still in the head. Nothing after this line runs either. The counter never gets its listener.
Image: None. This slide is code.
---
## Slide 7: One word fixes it
```html
<script src="monday.js" defer></script>
```
Speaker notes: defer tells the browser to download the file while it keeps reading, and to run it once the whole document is parsed. Every script this course writes goes in the head with defer. The end of the body also works, and the notes compare the two. async is different: it runs whenever the download finishes, which suits scripts that never touch the page.
Image: None. This slide is code.
---
## Slide 8: Two causes of null, in this order
- Did the element exist yet? Check for defer.
- Does the selector match? Test it in the Console.
- Hash for an id, dot for a class
- The error text is identical for both
Speaker notes: Every null error this week has one of two causes. First, timing, and defer rules it out. Second, the selector, and you can test that without editing anything by typing the same query into the Console after the page loads. The error message is word for word the same either way, so the message alone cannot tell you which.
Image: A two-step checklist card with a clock icon on step one and a magnifier on step two.
---
## Slide 9: View Source and the Elements panel disagree
- View Source shows the file the server sent
- Elements shows the live tree
- The script added a paragraph
- Only one of them shows it
Speaker notes: Press Control U for View Source and search for the added paragraph. It is not there. Open the Elements panel. It is there. The file did not change. The tree did. When you debug a page that has a script, look at the tree.
Image: Two panes side by side, View Source without the paragraph and Elements with it highlighted.
---
## Slide 10: Plug-ins, and why they are gone
- Flash, Java applets, Silverlight ran inside pages
- Native code with far too much access
- Crashes, security holes, no phone support
- Browsers removed plug-in support entirely
- Your ad blocker is an extension, not a plug-in
Speaker notes: Before JavaScript could do much, browsers handed parts of pages to plug-ins, which were whole native programs. Flash was the famous one. They were a security problem, they crashed, and they never worked on phones, so browsers removed the system. Adobe ended Flash support at the end of 2020. Extensions are different: web technology, a store, and a list of permissions you can read. Today's Build 2 asks you to write that difference down with sources.
Image: A museum-style shelf with three retired plug-in boxes, and a modern extensions page on a screen beside it.
---
## Slide 11: What you are about to build
- Lab W04-01, steps 1 to 5
- Load shift-board.js with defer
- Break it on purpose and paste the error
- Then the plug-in note, half a page, with sources
Speaker notes: Build one is the first five steps of the shift board lab. You will load the script the right way, then take defer off on purpose and paste the exact error into your notes, because recognising it later is worth more than avoiding it once. Build two is the plug-in note. Name your sources, and mark anything you could not confirm.
Image: The shift board page with dev tools open and the Console showing the loaded message.
---
