# Measure a Question, Not a Person
---
## Slide 1: Did anyone look
- Your site goes live Thursday
- Friday you have to say whether anyone used it
- You cannot guess
- And your visitors are your classmates
Speaker notes: On Friday somebody is going to ask you two questions. Did anyone look at your site, and did it help them. You cannot answer either by guessing, so you need a measurement tool. And here is the complication. Your visitors this week are the people sitting around you, and a lot of them are under eighteen. So today is about finding out whether a site works without finding out who anybody is.
Image: A laptop showing a site with a small question at the bottom, "Was this page useful?", with Yes and No buttons.
---
## Slide 2: Start with the question
- Which pages get opened, and when
- Do people find a page useful
- Then collect the least that answers each
Speaker notes: Measurement starts with a question, not with a tool. I have two. Which pages get opened, and when. And do the people who read a page find it useful. Now, for each one, what is the smallest thing I would have to write down to answer it. Take thirty seconds with the person next to you.
Image: Two questions on a whiteboard, each with an arrow to a short list of fields.
---
## Slide 3: The whole data model
```json
{
  "views":   { "/layout.html": { "2027-03-11": 2 } },
  "helpful": { "/layout.html": { "yes": 1, "no": 0 } }
}
```
Speaker notes: That is everything. The page address and the day, with a count. The page address and a yes or a no, with a count. No cookie. No IP address. No browser description. No visitor ID. The date is an example day. Nothing in this file could tell anyone who visited, and that is the design, not a limitation we forgot to fix.
Image: None. This slide is code.
---
## Slide 4: Watch the terminal
```
python serve.py --port 8606
Serving site/ at http://127.0.0.1:8606/  (Ctrl+C to stop)
127.0.0.1 - - [date and time] "GET / HTTP/1.1" 200 -
```
Speaker notes: This is the lab starter. I start it on port 8606, I load the home page, and I look at the terminal. What is the first thing on that line? It is the address of the machine that asked. Here it is my own machine. On the lab network it is yours. On a public host it is a stranger's connection. This server has been writing that down since I started it, and nobody asked it to. That is the standard library's default.
Image: None. This slide is code.
---
## Slide 5: Replace the log line
```python
def log_request(self, code="-", size="-"):
    status = code.value if isinstance(code, HTTPStatus) else code
    sys.stderr.write(f"{self.command} {self.path.split('?', 1)[0]} {status}\n")
```
Speaker notes: This is the fix, and it is step two of the lab. We override the method that writes the line, and we keep only what helps you debug: the method, the address that was asked for, and the status. After this the same page load prints GET slash 200. Nothing about who asked.
Image: None. This slide is code.
---
## Slide 6: The page sends one small request
```javascript
const hit = JSON.stringify({ path: location.pathname });
if (navigator.sendBeacon) {
  navigator.sendBeacon("/api/hit", hit);
} else {
  fetch("/api/hit", { method: "POST", body: hit, keepalive: true }).catch(function () {});
}
```
Speaker notes: This is count.js. It sends the page address and nothing else. sendBeacon hands the request to the browser and returns immediately, so the visitor never waits for your counter. And in the template the script tag has defer on it, so it runs after the page has been read. Your counter must never be the reason a page is slow.
Image: None. This slide is code.
---
## Slide 7: The wrong way, and it runs fine
- A visitor ID in a cookie, kept for a year
- The server saves the IP address beside each hit
- No error anywhere
- The page says "It does not track you"
Speaker notes: Ask an assistant for first party analytics with unique visitors and you can get exactly this. A random ID in a cookie that lasts a year, and a server that writes the visitor's address next to every hit. It runs. Nothing is red. On the build machine one browser loading three pages produced three rows tied together under one ID next to an address. And the page it came from promised it did not track anyone.
Image: A CSV file with a visitor ID column and an IP column highlighted in Launch Red.
---
## Slide 8: A view is not a person
- Reloads count
- Your own testing counts
- Forty views could be four people
- Say so in the report
Speaker notes: Here is the sentence your report has to contain in some form. A view is a page load, not a person. You reloading while you test counts. A friend opening it twice counts twice. Forty views could be four people. That is not a flaw in your tool. It is what the number means, and a report that pretends otherwise is wrong.
Image: One person at a laptop with a counter above them ticking up with every reload.
---
## Slide 9: Satisfaction is asked, not guessed
- Many views can mean a confusing page
- One question on every page: was it useful
- Report how many answered
- Three answers is not a pattern
Speaker notes: High traffic does not mean a page is good. People keep returning to a page they cannot figure out. The only way to know whether a page helped is to ask, so every page gets one yes or no question from the template. And when you report the answers, you report how many there were. Two No answers out of three is a reason to look at a page, not a verdict on it.
Image: A small bar showing one Yes and two No answers, with a caption that says three answers.
---
## Slide 10: What you are about to build
- Lab W06-02: a counter that identifies nobody
- Steps 1 to 6: log fix, hit endpoint, count.js
- Steps 7 to 12: the question, tests, report
- Thirteen tests pass, then the measurement plan
Speaker notes: Build one: fix the log line, write the hit endpoint and the count, and write count.js. Your acceptance check is a page load that prints POST slash api slash hit 204, and a counts file with nothing in it but addresses and days. Build two: the usefulness question in the template, the tests, which must say thirteen tests OK, and the report. Then write your measurement plan, including the list of what your numbers cannot tell you. Stop your server before you leave.
Image: A terminal showing "Ran 13 tests" and "OK" beside a small traffic table.
