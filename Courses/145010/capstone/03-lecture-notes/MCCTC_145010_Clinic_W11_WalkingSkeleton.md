# Clinic · Deploy First: the Walking Skeleton
## 145010 Senior Capstone · Week 11, Tuesday · 15 minutes · Improve

**Slides for this clinic:** [outline](../04-slides/MCCTC_145010_Slides_W11_WalkingSkeleton.md).
There is no exported deck yet. To generate one when Gamma credits are available, from the
repository root:
`node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W11_WalkingSkeleton.md --export pptx`

**When this clinic runs.** Week 11, Tuesday, or any week the room shows this signal: anyone still
building features with nothing deployed.
**If you missed it,** you can learn the skill from this file alone. The code is in
[`clinic-w11-skeleton/`](clinic-w11-skeleton/).
**Competencies:** 6.5.12 (publish to a web server), 6.4.7 (scripting that interacts with data
sources), 1.4.4 (system hardware to support software applications), 2.7.8 (static versus dynamic
sites)

---

## Why this exists

**The problems that sink a capstone cannot be found on your laptop.** A host builds your code on a
different machine, with a different folder layout, different settings, and sometimes a file system
that forgets things. None of that shows up while you run `python app.py` at your desk.

So you deploy first. Before sign-in, before the form, before styling. **A walking skeleton is the
thinnest path through every layer, running where it will finally run.** For a Full-Stack project,
that is one page on your host that reads one row from the real database.

Finding a hosting problem in Week 11 costs you a day. Finding it in Week 15 costs you the capstone,
because your thirty-day clock and your usability sessions both depend on a deployed system.

**This is the hardest day of Sprint 1.** Expect the first deploy to fail. That is the skeleton
doing its job.

---

## The skill in plain language

A walking skeleton has three properties.

1. **It touches every layer.** Browser, application, database. For Industrial/HMI: sensor, service,
   panel, dashboard. For AI-Integrated: front end, your service, the model or its stand-in.
2. **It runs where the real thing will run.** The approved host, the approved lab machine, the
   device in its approved place. Not "on my laptop for now."
3. **It is almost empty.** One row. One reading. One labelled answer. Anything more is a feature,
   and features come after.

Add a **health route** from day one. Thursday's clinic covers what it must check.

---

## Worked example 1 · the skeleton, run locally

**Composite project, not a real organization:** the Parts Bin Board for a volunteer bike repair
co-op. Every bin in the database is invented.

The files are [`setup_db.py`](clinic-w11-skeleton/setup_db.py) and
[`skeleton.py`](clinic-w11-skeleton/skeleton.py). The part that matters:

```python
DB_PATH = pathlib.Path(os.environ.get("PARTS_DB", HERE / "parts-skeleton.db"))
PORT = int(os.environ.get("PORT", "5330"))

def connect():
    # mode=rw refuses to create a new empty file when the path is wrong
    return sqlite3.connect(f"file:{DB_PATH.as_posix()}?mode=rw", uri=True)

@app.get("/")
def home():
    with closing(connect()) as conn:
        row = conn.execute("SELECT code, name FROM bins ORDER BY code LIMIT 1").fetchone()
    code, name = row
    return PAGE.format(code=code, name=name, version=VERSION)
```

Two settings come from environment variables, with local defaults: where the database is, and which
port to use. Wednesday's clinic explains why.

Run it in PowerShell from `clinic-w11-skeleton/`:

```
python setup_db.py
python skeleton.py
```

Output on the build machine:

```
database ready: parts-skeleton.db, 3 bins
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5330
Press CTRL+C to quit
```

In a second terminal:

```
curl.exe -s http://127.0.0.1:5330/health
```

```
{"bins":3,"database":"ok","status":"ok","version":"0.1.0"}
```

And `http://127.0.0.1:5330/` showed the page with **B-01, Tubes, 26 inch**. The page HTML went
through `node tools/web-check/check.js` and printed `PASS`, 0 validation errors, 0 axe violations at
360, 768, and 1280.

**Stop the server** with Ctrl+C in its terminal. Then confirm the port is free:

```
netstat -ano | findstr LISTENING | findstr :5330
```

No output means nothing is listening. On the build machine it printed nothing.

---

## Worked example 2 · the same skeleton, wrong database path

A host keeps files in a different place from your laptop. This is the most common first failure.
To see it locally, point `PARTS_DB` at a folder that does not exist and start the server again:

```
$env:PARTS_DB = "C:\no-such-folder\parts.db"
python skeleton.py
```

The home page answered **500**, and the server terminal printed:

```
sqlite3.OperationalError: unable to open database file
```

The health route answered **503**:

```
{"database":"OperationalError","status":"fail","version":"0.1.0"}
```

**That is a good failure.** It is loud, it happens at the first request, and the health route agrees
with the page. Remove the variable afterward with `Remove-Item Env:PARTS_DB`.

---

## Worked example 3 · putting it where it will run

**Every step in this section is [VERIFY].** Hosts change their steps and their free tiers. The
program's host list is set by your instructor, and nothing here was run on a host from the build
machine.

For a Flask and SQLite project on an approved full-stack host, the steps usually look like this:

1. Connect the host to your repository. [VERIFY on the host's own documentation]
2. Add a `requirements.txt` so the host installs Flask. [VERIFY]
3. Set the start command. Hosts usually run a production server such as Gunicorn rather than the
   development server in the warning above. [VERIFY which one your host documents]
4. Set `PARTS_DB` in the host's environment settings. Many hosts also set `PORT` themselves.
   [VERIFY]
5. **Find out whether the host keeps files between deploys and restarts.** On some free tiers the
   file system is replaced every deploy, which would erase a SQLite file. [VERIFY for your host,
   before you trust it with real reports] If it does, stop and decide with your instructor: storage
   that persists, a hosted database, or the lab machine.
6. Open the host's link from a device that is not yours. Record what you saw in the sprint file.

**Static hosts cannot run this.** A static host, such as Cloudflare Pages, serves files. It does not
run Python on each request. A board that changes when a volunteer reports a bin is a dynamic site,
and that is the 2.7.8 answer your defense panel wants.

**The local alternative.** If the host is not approved yet, or is down, run the skeleton on the
approved lab machine with a local database, as in example 1. That keeps you building. **It does not
meet "reachable by the stakeholder."** Write that plainly in your Sprint 1 review, and ask your
instructor at standup where the system will run.

---

## The wrong version, and what it costs

[`skeleton_wrong.py`](clinic-w11-skeleton/skeleton_wrong.py) opens the database by a relative
name and has a health route that checks nothing:

```python
conn = sqlite3.connect("parts-skeleton.db")   # relative to wherever you started

@app.get("/health")
def health():
    return "ok"                                    # checks nothing
```

Started from the folder above, on port 5331, it answered the home page with **500** and printed:

```
sqlite3.OperationalError: no such table: bins
```

Meanwhile `/health` answered **200** with `ok`. And a new file appeared in the folder the server was
started from: `parts-skeleton.db`, **0 bytes**. `sqlite3.connect()` quietly created an empty
database, so the real error ("wrong folder") turned into a confusing one ("no such table").

**What it costs:** on a host, this is a board that never shows a bin while your health log records
"ok" every thirty minutes. You find out when the coordinator emails you. The file was deleted after
the run.

---

## Why the wrong version is tempting

**It works on your machine, every time**, because you always start it from the same folder. Nothing
tells you the path is fragile until the one day it is not your machine.

**Deploying feels like a finishing step.** It is not. It is the step with the most unknowns, which
is exactly why it goes first.

---

## Do this today

1. Put your skeleton in `src/` in your repository. One page, one row, one health route.
2. Read the database path and the port from environment variables, with local defaults.
3. Run it locally on an explicit port. Stop it. Confirm the port is free.
4. Follow your architecture's deployment steps (`docs/measure-analyze/architecture.md`, section 10)
   on the approved host. Write down every step that was different from what you planned.
5. Every deploy failure over twenty minutes gets an entry in `troubleshooting-log.md`.
6. Update task 3 in `docs/improve/sprint-1.md` and **commit**.

---

## If you are ahead, if you are behind

**If you are ahead:** your skeleton is deployed. Open it on a phone at 360 wide and on the co-op-style
desktop your requirements name. Then run your test plan's integration case against the deployed
link and record it.

**If you are behind:** you have features and no deploy. Stop feature work today. Strip your app to
one page and one row in a branch, deploy that, and bring the features back afterward.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Publish to a web server** | Putting the skeleton on the approved host, reachable by someone else (6.5.12) |
| **Dynamic site** | Pages built on each request from data, like the bin board (2.7.8) |
| **Static site** | Files served as they are, with no code running per request (2.7.8) |
| **Interact with data sources** | The page reading a row from the database (6.4.7) |
| **System hardware to support software** | Where it runs, and what that machine or host provides (1.4.4) |

---

## Self-check

**1.** A classmate's skeleton has sign-in, a form, and three pages, all running on their laptop.
Is it a walking skeleton? Why or why not?

**2.** In the wrong version, why did the error say "no such table" instead of "file not found"?

**3.** Your host is not approved until Thursday. What do you run until then, and what do you write
in your Sprint 1 review?

### Answers

**1.** No. It is not running where it will finally run, so none of the hosting problems have been
found yet. It also carries features a skeleton does not need. A skeleton is thin and deployed.

**2.** Because `sqlite3.connect()` creates a new, empty database file when the file is missing. The
connection succeeded, the empty database had no tables, and the query failed on the missing table.
Opening with `mode=rw` stops that and fails at the real problem.

**3.** Run the skeleton on the approved lab machine with a local database, on an explicit port. In
the review, write that the system is not yet reachable by the stakeholder, why, and the day the host
decision is due. Do not call it deployed.
