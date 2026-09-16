# How a Document Becomes a Page
---
## Slide 1: This page is broken. You cannot tell.
- It opens in every browser
- It looks exactly the way you meant
- The document underneath is not your file
- Nothing on screen will ever tell you
Speaker notes: Every page you have ever built showed up in a browser. That felt like proof it was right. Today you find out it was never proof of anything. I am going to put a page on the screen that looks fine, and by the end of the next five minutes you are going to see three things in it that are not in the file.
Image: A clean, ordinary event page on a laptop screen, with a faint X-ray style overlay showing tangled markup underneath, navy and launch blue.
---
## Slide 2: The browser builds a tree from your text
- Your file is text
- The parser reads it and builds the DOM
- CSS, screen readers, and scripts use the DOM
- Nothing downstream ever reads your file
Speaker notes: Here is the whole model. An HTML file is text. The browser has a parser that reads that text and builds a tree of objects called the DOM. From then on, everything works on the tree. Your styles, the screen reader, next month's scripts. None of them look at your file again. So if the tree is different from the file, the tree wins.
Image: A simple left-to-right diagram: a text file icon, an arrow labelled parser, a tree of boxes labelled DOM, and three arrows out to CSS, screen reader, and script.
---
## Slide 3: The file
```html
<h1>Saturday game day</h1>
<p>Bring:
  <ul>
    <li>Shin guards</li>
    <li>Water</li>
  </ul>
</p>
<table>
  <tr><th>Kickoff</th><th>Field</th></tr>
</table>
```
Speaker notes: This is the file. Read it. Does anybody see anything wrong with it? Vote with your hands. Most rooms say it is fine. Hold on to your vote.
Image: None. This slide is code.
---
## Slide 4: What Chrome actually built
```html
<h1>Saturday game day</h1>
<p>Bring:
  </p><ul>
    <li>Shin guards</li>
    <li>Water</li>
  </ul>
<p></p>
<table>
  <tbody><tr><th>Kickoff</th><th>Field</th></tr>
</tbody></table>
```
Speaker notes: This is the Elements panel, copied exactly from Chrome. Three things are not in the file. The paragraph closed before the list, because a paragraph is not allowed to contain a list. The closing p tag at the end had nothing to close, so the browser made an empty paragraph. And a tbody appeared that nobody typed. No warning. No red text.
Image: None. This slide is code.
---
## Slide 5: Two views, two truths
- View Source, Ctrl+U: the text that arrived
- Elements panel: the tree the browser built
- They disagree whenever the browser repaired something
- Check both, every time
Speaker notes: Write this one down. View Source is what arrived. Elements is what the browser built. When they disagree, the browser fixed something for you, and you did not get a say in how. From today on, a page is not finished until you have looked at both.
Image: A split screen, View Source on the left and the Elements panel on the right, with the differing lines highlighted in launch blue.
---
## Slide 6: The wrong way to check your work
```
line 32:6  no-implicit-close  Element <p> is implicitly closed by adjacent <ul>
line 38:6  close-order  Stray end tag '</p>'
```
Speaker notes: This is what the validator in web-check said about that exact mistake in your lab file. The wrong way to check your work is to look at the page and decide it is fine. The page looked fine. The validator reports the file as you wrote it, and it does not repair anything. In the lab, one crossed pair of tags produced nineteen errors like this. Look for the line the errors cluster after, not the first one on the list.
Image: None. This slide is code.
---
## Slide 7: Where did the text come from?
- Static: a stored file, same for everyone
- Dynamic: a program builds each page on request
- The browser cannot tell the difference
- Both arrive as ordinary HTML
Speaker notes: Second half of the idea. That text had to come from somewhere. A static site hands over a stored file, the same bytes to everyone until someone edits it. A dynamic site runs a program for every request. Your Flask CRUD app was dynamic. And here is the point. The browser cannot tell which one it got. Watch.
Image: Two servers side by side, one handing out identical copies of a sheet of paper, the other printing a fresh sheet for each person in line.
---
## Slide 8: Same browser, two servers
```
python -m http.server 8140 --bind 127.0.0.1 --directory static
python serve_dynamic.py 8141

<p>Built by the server at 11:13:23</p>
```
Speaker notes: Two terminals, and I say each port out loud, because a server on the wrong port looks exactly like a working server. The first one hands out a file. The second one builds the page every time, and stamps the time on it. View Source on both. Refresh both. Only the dynamic one changes. Both arrived as plain HTML. Now I stop both servers, because a server left running is somebody else's problem tomorrow.
Image: None. This slide is code.
---
## Slide 9: When each one fits
- Static: code of conduct, directions, rules
- Dynamic: my games, my balance, my cart
- Ask: would two people need different bytes?
- Dynamic costs a server, and often logins
Speaker notes: Here is the question that settles it every time. Would two people asking for this page at the same moment ever need different bytes? A league's rules, no. That is static, cheap, and hard to break. A referee's own assignments, yes. That is dynamic, and it comes with a program to keep running and usually accounts to protect. Dynamic does not mean animated. It means built per request.
Image: A two-column comparison card, static on the left with a stack of identical pages, dynamic on the right with personalized pages.
---
## Slide 10: What you are about to build
- Lab W01-01 Part 1: the bike kitchen page
- Run web-check. Read where the errors cluster.
- Find what the browser built in Elements
- Fix it until web-check says PASS
Speaker notes: Build one is part one of the lab. The Harbor Lane Bike Kitchen page opens fine and has twenty-one validation errors. Your job is to find the one line causing most of them, see what Chrome built from it, and fill in the what-the-browser-built table before you fix anything. Then fix it and get a PASS. Build two, you meet your first client of the semester.
Image: The bike kitchen starter page in a browser beside a terminal showing the web-check FAIL line, navy and launch blue.
