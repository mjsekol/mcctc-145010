# Links and Paths
---
## Slide 1: It worked on my machine
- The link worked when you tested it
- Somebody moved the page into a folder
- Now two links lead to an error page
- Not one character in the links changed
Speaker notes: You have lived this bug already. In 145060, a Python program opened roster dot t x t, worked from one folder, and failed from another, because relative paths start from the working directory. Links in a web page have the same bug with a different starting point. Today you learn exactly where that starting point is.
Image: A folder tree with one page being dragged into a subfolder, and two dotted link lines snapping behind it.
---
## Slide 2: Every link is resolved from the page
- Absolute: the full address, same from anywhere
- Relative: starts in the page's own folder
- Two dots climb one folder
- A leading slash starts from the root
Speaker notes: Here is the rule. The browser takes whatever you wrote in href and turns it into a full address, starting from the address of the page it is on. Not from the top of your site. Not from your terminal. From the folder the page lives in. Two dots means go up one folder. A leading slash means start at the root, and on a file on your own machine the root is the whole drive, not your site.
Image: A folder tree with the current page highlighted and arrows showing where each kind of path starts counting from.
---
## Slide 3: One page, three paths
```html
<!-- this page is site/pages/roster.html -->
<a href="../images/logo.png">A</a>   <!-- site/images/logo.png -->
<a href="images/logo.png">B</a>      <!-- site/pages/images/logo.png -->
<a href="/images/logo.png">C</a>     <!-- file:///C:/images/logo.png -->
```
Speaker notes: These are the real addresses Chrome resolved from a page in that folder. A climbs out of pages and finds the image. B looks for an images folder inside pages, which does not exist. C starts at the root of the drive, because this page was opened as a file. On a web server whose root was the site folder, C would work. That is the one that works on the server and breaks on your machine.
Image: None. This slide is code.
---
## Slide 4: The wrong way: move the page
```
FAIL FILES     line 18: <a href="files/coupon.txt"> points at a file that is not there
FAIL FILES     line 20: <a href="pages/directions.html"> points at a file that is not there

ERR_FILE_NOT_FOUND
Error code: 404
Message: File not found.
```
Speaker notes: I moved a working page into a new folder and changed nothing else. Structure check found both broken links. The bottom lines are what a visitor sees. Opened as a file, Chrome shows an error page with that code. Served by Python's server, you get a 404 page that says file not found. The links did not change. Where the page lives changed.
Image: None. This slide is code.
---
## Slide 5: Fragments jump inside a page
- href="#rain" jumps to id="rain"
- The match is exact, case included
- A mismatch does nothing and reports nothing
- href="#" is a placeholder that jumps to the top
Speaker notes: A fragment is the part after the hash sign. It scrolls to the element whose id matches it exactly. Capital R Rain and lowercase rain are different. When they do not match, the page does not move, nothing turns red, and you assume you mis-clicked. I tested it. The scroll position did not change at all.
Image: A long page with a jump menu at the top and a dotted arrow landing exactly on a matching heading, and a second arrow stopping short.
---
## Slide 6: Email and download links
```html
<p>Print the <a href="files/coupon.txt" download>coupon (text file, 1 KB)</a>.</p>
<p>Questions go to
  <a href="mailto:boosters@bandcarwash.example">boosters@bandcarwash.example</a>.</p>
```
Speaker notes: Two more kinds. The download attribute asks the browser to save the file instead of opening it, and the link text says what is about to arrive and how big it is. The mailto link opens the visitor's email program. Notice the link text is the address itself, so someone on a shared computer can still copy it. And it is a role address, not a person's own, because anything in page source can be collected by anyone.
Image: None. This slide is code.
---
## Slide 7: Link text must stand alone
- Screen reader users can list every link
- Nine links that say click here are useless
- Name the destination in the link
- Downloads: say the file type and size
Speaker notes: One habit that costs nothing. Read each link's text with nothing around it. A screen reader user can pull up a list of every link on the page, and on a lot of pages that list says click here, click here, click here. Name where the link goes. For a download, say what kind of file it is and roughly how big.
Image: A screen reader style list of links, half reading click here and half reading descriptive names, the descriptive half highlighted.
---
## Slide 8: Before you write a path
- Say which folder this page is in
- Trace the path from there, out loud
- Run structure_check on every page
- Click every link, every time
Speaker notes: Here is the habit that prevents all of it. Before you type a path, say out loud which folder this page is in. Then trace the path from there. Then run structure check on every page, not only the one you were editing, because the broken link is usually on the page you forgot about. Then click everything.
Image: A checklist card with four boxes, the first one ticked, navy and launch blue.
---
## Slide 9: What you are about to build
- Lab W01-01 Part 3: every link lands
- Ids for sections, then the jump menu
- The page in pages/ finds its way home
- A download and an email link that stand alone
Speaker notes: Build one is part three of the lab. Give the sections ids and point the menu at them. Fix the volunteer link, then fix the volunteer page's way back, which is the one everybody gets wrong. Then the download and the email link. Both checkers, both pages, three widths. Build two, you draw a link map for the league site on paper before you write a single link.
Image: A small site map with three pages and arrows between them, each arrow labelled with its relative path.
