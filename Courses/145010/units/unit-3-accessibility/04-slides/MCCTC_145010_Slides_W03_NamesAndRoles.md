# Names, Roles, and the Accessibility Tree
---
## Slide 1: The page nobody sees
- A screen reader never looks at a pixel
- It asks the browser questions
- The answers come from your HTML
- CSS barely changes them
Speaker notes: Everything you styled last week is invisible to a screen reader. It does not see the green header or the bold section titles. It asks the browser, for every element, what are you and what are you called. The browser answers from your HTML. Today you learn to read those answers, because they are the only version of your page some people will ever get.
Image: A web page on the left and a plain indented tree of labels on the right, joined by an arrow.
---
## Slide 2: Role, name, state
- Role: heading, link, button, textbox, image
- Name: what this particular one is called
- State: checked, expanded, required
- Together they form the accessibility tree
Speaker notes: Three answers. The role says what kind of thing it is. The name says which one. The state says what is happening to it right now. A button with a role and no name is announced as button, and nothing else. Try using a form where every button is called button.
Image: A single button drawn with three labelled tags hanging from it: role, name, state.
---
## Slide 3: The right element gives you both
```html
<h2>Pantry hours</h2>                     <!-- heading, level 2 -->
<button type="submit">Sign up</button>    <!-- button "Sign up" -->
<label for="email">Email</label>
<input type="email" id="email">           <!-- textbox "Email" -->
<img src="logo.svg" alt="">               <!-- removed: decorative -->
<div class="section-title">Shifts</div>   <!-- generic: nothing -->
```
Speaker notes: Read the comments. Every real element hands the tree a role and a name for free. The empty alt removes a decorative image on purpose. And the last line looks exactly like a heading on screen and is nothing at all in the tree. That is Week 1's rule, structure first, turning into a person's experience.
Image: None. This slide is code.
---
## Slide 4: Finding the tree in Chrome
- F12, Elements panel
- Select an element
- Open the Accessibility pane
- Read the role and the name out loud
Speaker notes: I am going to show you this live. Select the element in the Elements panel and look for the Accessibility pane. Your version of Chrome may put it in a slightly different place, so watch where I click. From today, when you are not sure what a screen reader gets, you do not guess. You read it here.
Image: A browser developer tools panel with an Accessibility section highlighted in light blue.
---
## Slide 5: The tool catches a missing name
```
<button class="accept"><img src="check-icon.svg" alt=""></button>

    button-name (critical, 4 node(s))  Buttons must have
    discernible text  e.g. .urgent > .actions > .accept
```
Speaker notes: The swap board has four icon buttons. The image inside each one is empty alt, so the button has no name at all, and web-check catches it. Good. The fix is a name in the alt, and a good name says what and to which: Accept Maya R.'s Friday swap. Four buttons all called Accept pass the tool and fail the person.
Image: None. This slide is code.
---
## Slide 6: Watch the tool pass this
- alt="DSC_0419.jpg"
- web-check: PASS, zero violations
- A screen reader reads the file name
- The name exists. It means nothing
Speaker notes: This is the deliberate failure. I give an image the camera's file name as its alt text and run the checker. It passes. The attribute is there and it is not empty, and that is all a tool can know. The person listening hears a file name. From here on, every alt text you write answers one question: if the image were gone, what would I need to know.
Image: A photo placeholder with a caption reading DSC_0419.jpg and a green PASS badge next to a sad face.
---
## Slide 7: Placeholders pass too
- The name field has only a placeholder
- Chrome uses it as the name
- axe passes it
- Type one letter and the instruction vanishes
Speaker notes: This one surprised me when I checked it. Chrome takes the placeholder as the field's name, so the screen reader says Your name, and the tool is satisfied. Now type one letter. The hint is gone. A sighted person who looks away no longer knows what the box is for. 3.3.2 Labels or Instructions. The fix is a visible label that stays.
Image: A text field shown twice: once with grey hint text, once with one typed letter and no hint.
---
## Slide 8: Landmarks and headings are the map
- header, nav, main, footer become landmarks
- Headings form the table of contents
- Levels do not skip in this course
- WCAG has no criterion saying exactly that
Speaker notes: Screen reader users jump by landmark and by heading. A page of divs gives them nothing to jump to. On skipped heading levels, be precise. This course's standard is that they do not skip. WCAG 2.2 does not have a criterion that says exactly that, and when you write the audit row, you say so rather than inventing a number.
Image: A page outline with h1, h2, h3 indented like a table of contents beside four labelled page regions.
---
## Slide 9: Hiding a label hides it from everyone
```html
<label for="n" style="display:none">Name</label>
<input type="text" id="n">

<!--  label (critical, 1 node(s))  Form elements must have labels  -->
```
Speaker notes: A student wants the clean look and a label for the screen reader. Display none removes the label from the page and from the tree. The checker is right to fail it. Sighted users need the label too, so the answer is almost always a visible one.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: swap board, Part 2, names and roles
- Every button named with its action and its swap
- Build 2: the Lantern Street audit, passes 1 and 2
- Log what the tool missed, not only what it found
Speaker notes: Build 1 is Part 2 of the swap board. Name every button properly, give the search box a real label, and make Settings a heading. Build 2 starts the audit on the page you will rebuild. Pass 1 is the tool. Pass 2 is you in the Accessibility pane, image by image and field by field. Do not fix anything yet. Tomorrow's keyboard pass needs the page broken.
Image: A two-column audit log template with the column headers Found by and WCAG criterion highlighted.
---
