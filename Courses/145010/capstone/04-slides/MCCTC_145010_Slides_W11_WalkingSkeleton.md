# Deploy First: the Walking Skeleton
---
## Slide 1: It works on your laptop. So what?
- Your host is a different machine
- Different folders, different settings, maybe no saved files
- None of that shows up at your desk
- You find out when you deploy
Speaker notes: Every one of you has an app that runs on your own machine. That proves less than it feels like it proves. The host that will run your capstone builds your code somewhere else, with a different folder layout and different settings, and some hosts throw away files every time they restart. None of that shows up while you sit at your desk. You find out the day you deploy. So today the question is when you want to find out: this week, with four sprints left, or in Week 15, with none.
Image: A laptop with a green check mark beside a server rack with a question mark, deep navy and accent blue.
---
## Slide 2: What a walking skeleton is
- The thinnest path through every layer
- Running where it will finally run
- One page, one row, one health route
- Features come after it is deployed
Speaker notes: A walking skeleton is the smallest version of your system that still goes through every layer. For Full-Stack, a browser asks your app for a page and the app reads one row from the real database. For Industrial, one sensor reading reaches the panel and the dashboard. For AI-Integrated, one request reaches your service and comes back labelled. It is almost empty on purpose. And it runs where it will finally run, not on your laptop for now. Sign-in, forms, and styling wait until it is deployed.
Image: A simple skeleton figure made of three stacked boxes labelled browser, app, database, connected by arrows.
---
## Slide 3: The whole skeleton, almost
```python
DB_PATH = pathlib.Path(os.environ.get("PARTS_DB", HERE / "parts-skeleton.db"))
PORT = int(os.environ.get("PORT", "5330"))

@app.get("/")
def home():
    with closing(connect()) as conn:
        row = conn.execute(
            "SELECT code, name FROM bins ORDER BY code LIMIT 1").fetchone()
    code, name = row
    return PAGE.format(code=code, name=name, version=VERSION)
```
Speaker notes: This is the composite Parts Bin Board, for a volunteer bike repair co-op, and it is not a real organization. The whole home page is one query for one row. Look at the top two lines. The database path and the port come from environment variables, with local defaults. Tomorrow's clinic is about why. The file is in the clinic folder next to the notes, and it runs.
Image: None. This slide is code.
---
## Slide 4: Run it, on an explicit port
```
> python setup_db.py
database ready: parts-skeleton.db, 3 bins
> python skeleton.py
 * Running on http://127.0.0.1:5330
> curl.exe -s http://127.0.0.1:5330/health
{"bins":3,"database":"ok","status":"ok","version":"0.1.0"}
```
Speaker notes: This is real output from the build machine. Setup makes three invented bins. The server says exactly where it is listening, port 5330, because we never rely on a default port. The health route answers with the version and a count from the same table the page reads. Then I press Control C and check the port is free with netstat. Every server you start, you stop.
Image: None. This slide is code.
---
## Slide 5: Watch this
```python
conn = sqlite3.connect("parts-skeleton.db")   # relative path

@app.get("/health")
def health():
    return "ok"                                 # checks nothing
```
Speaker notes: Here is the version most of us would write first. It opens the database by a bare file name, and its health route returns ok without looking at anything. It works perfectly on my machine, because I always start it from the same folder. Now I am going to start it from the folder one level up, the way a host might. Predict what happens before I load the page.
Image: None. This slide is code.
---
## Slide 6: The real failure
```
GET /        500
sqlite3.OperationalError: no such table: bins
GET /health  200   ok
new file in the starting folder: parts-skeleton.db, 0 bytes
```
Speaker notes: The home page failed with no such table. The health route said ok at the same moment. And a brand new database file appeared, zero bytes. Here is what happened. The connect call could not find the real file, so it quietly created an empty one, and the empty one has no tables. The real problem was the wrong folder, and the message we got was about a missing table. On a host, this is a board that never shows a bin while your health log says fine every thirty minutes.
Image: None. This slide is code.
---
## Slide 7: The fix is two small habits
- Read the database path from an environment variable
- Open it with mode=rw so nothing is created
- Health reads the same table the page reads
- Wrong path now fails loudly: 500 and 503
Speaker notes: Two habits fix it. The path comes from an environment variable, so each machine says where its own file lives. And the connection opens with mode equals r w, which refuses to create a new empty file. With a wrong path, the page answered 500 with unable to open database file, and health answered 503. That is a good failure. It is loud, it is immediate, and the health route agrees with the page.
Image: A warning light next to a database cylinder with a crossed-out empty file.
---
## Slide 8: Putting it where it will run
- Connect the approved host to your repository [VERIFY]
- Add requirements.txt and the host's start command [VERIFY]
- Set PARTS_DB in the host's settings [VERIFY]
- Open the link from a device that is not yours
Speaker notes: Every step on this slide is marked verify, because hosts change their steps and your instructor sets the approved list. Usually you connect the host to your repository, add a requirements file so it installs Flask, set the start command the host documents, and set your environment variables in its settings page. Then you open the link from a phone or a machine that is not yours. A static host cannot run this at all, because a board that changes on every report is a dynamic site.
Image: A repository icon with an arrow to a cloud outline and a phone showing a single row.
---
## Slide 9: Ask the host one question first
- Does it keep files between deploys and restarts?
- If not, a SQLite file disappears [VERIFY]
- Then decide with your instructor, before real data
- Not approved yet? Run it on the lab machine
Speaker notes: This is the question that sinks Full-Stack capstones. Some hosts replace the whole file system on every deploy. If yours does, your SQLite file and every report in it disappear, and so does your thirty-day record. Find out this week, and if the answer is no, decide with your instructor: storage that persists, a hosted database, or the lab machine. And if the host is not approved yet, run the skeleton on the approved lab machine so you keep building. Write in your review that it is not yet reachable by the stakeholder. Do not call it deployed.
Image: A folder icon fading out as a server restarts, with a question mark.
---
## Slide 10: What you are about to build
- Your skeleton in src: one page, one row, health
- Settings from environment variables, local defaults
- Run locally, stop it, confirm the port is free
- Deploy by your architecture steps, log every surprise
- Update task three in sprint one, then commit
Speaker notes: Here is the build period. Strip your app down to one page that reads one row, plus a health route. Read the database path and port from environment variables. Run it on an explicit port, stop it, and check the port is free. Then follow your own deployment steps from section ten of your architecture on the approved host, and write down every step that went differently. Anything that takes more than twenty minutes gets a troubleshooting entry. Update your sprint file and commit before you leave.
Image: A checklist beside a small deployed page showing one parts bin, navy and accent blue.
---
