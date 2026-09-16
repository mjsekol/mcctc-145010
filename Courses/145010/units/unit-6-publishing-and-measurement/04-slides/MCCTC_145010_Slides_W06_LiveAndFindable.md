# Live and Findable
---
## Slide 1: A folder is not a website
- Your site works on your laptop
- Nobody else can reach it
- Today it gets addresses anyone can type
- And every one of them has to answer
Speaker notes: Right now your site is a folder. It works, it validates, it counts. And nobody but you can see it. Today it becomes a set of addresses that anyone can type into a browser. That changes who reads it. People will, and so will programs called crawlers that read pages for search engines. Both need the same things from you, and we are going to check for all of them.
Image: A folder icon on the left and a browser address bar on the right, joined by an arrow.
---
## Slide 2: A server maps addresses to files
- /layout.html sends site/layout.html
- / usually sends index.html
- Anything missing sends a 404
- Publishing puts site/ where a server can reach it
Speaker notes: A web server is a program that turns an address into a file. Ask for slash layout dot html and you get the layout page. Ask for slash and most servers send index dot html. Ask for something that is not there and you get a 404. Publishing is putting your built files somewhere a server hands them to anyone who asks. That is the whole idea.
Image: A table of three addresses with arrows to three files and one arrow to a 404 sign.
---
## Slide 3: The smallest web server there is
```
python -m http.server 8606 --bind 127.0.0.1 --directory site

GET /             -> 200
GET /about.html   -> 404
POST /api/hit     -> 501, "Unsupported method ('POST')."
```
Speaker notes: Python ships a server. One line, explicit port, and it serves your site folder. The first two results are what you expect. Look at the third. This server serves files and runs no code, so your counter has nowhere to send its hit. That is a static host in miniature. Pages work, counts do not. If you publish to a static host, your report has to say where your counter actually ran.
Image: None. This slide is code.
---
## Slide 4: The capital letter that breaks on the host
```
GET /Layout.html  -> 200     (on this Windows machine)
```
Speaker notes: Same server, one capital L. It works, because Windows ignores case in file names. Many hosts run on systems where file names are case sensitive, and there this is a 404. Check your own host. Your links work on your machine and break after you publish. The habit that prevents it is boring and completely effective: lowercase file names, and links typed exactly as the file is named.
Image: None. This slide is code.
---
## Slide 5: Every page says what it is
- A title that names this page first
- A description that differs on every page
- One h1, headings in order
- Link text that says where it goes
Speaker notes: Search engine optimization, taught honestly, starts here. A title that leads with what this page is. A description that is a real sentence and different on every page. One main heading and headings in order. Link text that says where it goes, never click here. Search engines commonly show the title and may show the description in results, and a person reads those before deciding to click. That part you control. Anyone who promises you a ranking cannot back that promise up.
Image: A mock search result with the title and description lines labelled.
---
## Slide 6: Two files at the root
```
# Every crawler may read every page.
User-agent: *
Disallow:

Sitemap: https://portfolio.example/sitemap.xml
```
Speaker notes: robots dot txt asks crawlers what they may read. An empty Disallow means nothing is off limits. The last line says where the sitemap is. The sitemap lists every page by its full address, which is why you cannot finish it until you know where your site will live. The address here ends in dot example, which is reserved for documentation, so it can never be somebody's real site. You replace it with yours.
Image: None. This slide is code.
---
## Slide 7: The comment lies, the rule wins
```
# Allow all crawlers to index the whole site so volunteers can find us.
User-agent: *
Disallow: /

PROBLEM  robots.txt tells every crawler to stay out of the whole site (Disallow: /)
```
Speaker notes: Here is the wrong way. The comment says allow everything. The rule says stay out of everything. A person reads the comment and moves on. A crawler never reads comments. Every page works, no browser shows an error, and the file asks search engines to skip the whole site. The checker catches it. And remember this: robots dot txt is a request, not a lock. It never makes a page private.
Image: None. This slide is code.
---
## Slide 8: Check it like a visitor and a crawler
- check_site.py crawls from your home page
- Every link, every sitemap address, robots.txt
- Shared titles and descriptions
- --as is your published address
Speaker notes: check_site dot py walks your running site from the home page. It follows every link, requests every address in the sitemap, reads robots dot txt, and compares every title and description. The dash dash as option is the address your site will have once it is published. Give it the wrong one and it tells you the sitemap is pointing somewhere else. No problems found is the line you want.
Image: A terminal showing "No problems found." under a short summary line.
---
## Slide 9: Telling people it is live
- Say what the link is before asking for a click
- Say what the site records
- Ask for one specific thing
- Make no an acceptable answer
Speaker notes: Networking etiquette is on the exam, and this is where it gets real. Your launch message goes to three classmates through the class channel. It says what the link is, what the site records about them, and one specific thing to try. And it makes saying no free. A bare link, check out my site, or the same message five times is the version nobody wants to receive.
Image: A short message bubble with the four parts labelled.
---
## Slide 10: What you are about to build
- Quiz first, fifteen minutes, Monday to Wednesday
- Part C: publish locally, pass check_site
- Part D: real address, rebuild, publish
- Three launch messages, then real traffic
Speaker notes: After your Gate 1 rep there is a fifteen minute quiz on Monday through Wednesday. Then part C: serve your site on 8606 and make check_site say no problems found. Build two is part D. Put your real address in site dot json and robots dot txt, rebuild, and publish on the route you and I agreed. Then send three launch messages. In Period 8 you visit each other's sites, and that is the real traffic your report is about tomorrow.
Image: A checklist of quiz, Part C, Part D, and launch messages, with a small live site beside it.
