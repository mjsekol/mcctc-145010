# Clinic · Configuration and Secrets
## 145010 Senior Capstone · Week 11, Wednesday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 11, Wednesday, or any week the room shows this signal: a secret,
password, or connection string in any committed file.
**If you missed it,** you can learn the skill from this file alone. The code is in
[`clinic-w11-config/`](clinic-w11-config/).
**Competencies:** 6.5.12 (publish to a web server), 6.4.7 (scripting that interacts with data
sources), 1.4.4 (system hardware to support software applications), 2.11.8 (document the problem
and the verified solution)

---

## Why this exists

**Your code runs in two places now, and they are not the same.** On the lab machine the database is
in one folder. On the host it is somewhere else. The port is different. If those values are typed
into the code, you edit the code every time you deploy, and one day you deploy the wrong edit.

**Some values are secrets.** The key Flask uses to sign sign-in cookies. The password to a hosted
database. A secret typed into a file and committed is public to anyone who can read the repository,
**and it stays in the history even after you delete the line.** Your repository is going to be read
by your instructor, your peer reviewers, and a defense panel. The rubric caps Security at 9 of 20
for a credential in the repository or its history.

So settings live outside the code, in **environment variables**, and the code refuses to start
without the ones it needs.

---

## The skill in plain language

1. **List every value that changes between your machine and the host.** Database path, port, secret
   key. Your architecture document, section 7, already has this list.
2. **Read each one with `os.environ`.** A value that is not secret may have a local default. A secret
   never has a default.
3. **Fail loudly when a required value is missing**, with a message that says what to set.
4. **Never print a secret.** Print that it is set, and its length if you need proof.
5. **Keep local copies of settings out of git.** Anything holding real values is listed in
   `.gitignore` before the file exists.
6. **If a secret is ever committed, it is burned.** Replace it and tell your instructor the same day.

---

## Worked example 1 · reading settings, failing loudly

The file is [`settings.py`](clinic-w11-config/settings.py). The heart of it:

```python
REQUIRED = ("PARTS_DB", "SECRET_KEY")

def load_settings():
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        raise SystemExit(
            "Cannot start. Missing environment variable(s): " + ", ".join(missing) + ".\n"
            "Set them in the host's environment settings, or in this terminal for a local run."
        )
    secret = os.environ["SECRET_KEY"]
    if len(secret) < MIN_SECRET_LENGTH:
        raise SystemExit(...)
    return {
        "PARTS_DB": os.environ["PARTS_DB"],
        "SECRET_KEY": secret,
        "PORT": int(os.environ.get("PORT", "5330")),   # not secret, so a default is fine
    }
```

Run in PowerShell from `clinic-w11-config/`, with nothing set:

```
python settings.py
```

```
Cannot start. Missing environment variable(s): PARTS_DB, SECRET_KEY.
Set them in the host's environment settings, or in this terminal for a local run.
```

Exit code 1. **That is the program doing its job.** It names both missing values at once and says
where to set them.

---

## Worked example 2 · a typed secret, then a generated one

```
$env:PARTS_DB = "C:\capstone\parts.db"
$env:SECRET_KEY = "partsbin2027"
python settings.py
```

```
Cannot start. SECRET_KEY has 12 characters. Use at least 32, generated, not typed.
```

A word you can remember is a word someone can guess. Generate the key instead:

```
$env:SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
python settings.py
```

```
settings loaded
  PARTS_DB    C:\capstone\parts.db
  PORT        5330
  SECRET_KEY  set, 64 characters, value not shown
```

Then with `$env:PORT = "8160"` the same program printed `PORT        8160`. Same code, different
setting, no edit.

**These variables last only as long as that terminal window.** On a host, you enter the same names
in the host's environment settings page. [VERIFY where your host keeps them] Write the **names** in
your architecture document and your README. Never the values.

---

## Worked example 3 · keeping local values out of git

Some students keep local values in a file so they do not retype them. That is fine if git never sees
the file. Add these lines to `.gitignore` **and commit that first**:

```
# local settings and data, never committed
.env
*.db
instance/
```

Then commit a file that lists the names with no values, so the next person knows what to set:

```
# settings-needed.txt
PARTS_DB     path to the SQLite file
SECRET_KEY   64 hex characters, generate with the secrets module
PORT         optional, default 5330
```

Before every push, check what is staged. `git status` and `git diff --staged` show you. (Git
commands were not run on the build machine for this note. Run them on yours.)

---

## The wrong version, and what it costs

[`settings_wrong.py`](clinic-w11-config/settings_wrong.py):

```python
SECRET_KEY = os.environ.get("SECRET_KEY", "partsbin2027")   # a secret in the code
PARTS_DB = os.environ["PARTS_DB"]                           # a crash with no advice
print("secret key in use starts with", SECRET_KEY[:4])
```

With nothing set, it crashed with this, and nothing in it says what to do. (The folder path at the
start of the second line is shortened here.)

```
Traceback (most recent call last):
  File "...\clinic-w11-config\settings_wrong.py", line 16, in <module>
    PARTS_DB = os.environ["PARTS_DB"]                           # a crash with no advice
               ~~~~~~~~~~^^^^^^^^^^^^
  File "<frozen os>", line 717, in __getitem__
KeyError: 'PARTS_DB'
```

With only `PARTS_DB` set, it ran happily:

```
started with database C:\capstone\parts.db
secret key in use starts with part
```

**That quiet success is the worse failure.** The app is running on a key anyone can read in the
repository, and the output leaks part of it. (The value in the file is invented and protects
nothing.)

**If a real secret was committed:**

1. **Tell your instructor today.** This is one of the moments your instructor steps in immediately.
2. **Replace the secret.** Generate a new one and set it on the host. The old one is burned, even if
   you delete the line, because the history still has it.
3. **Fix the code** so it reads the value from the environment.
4. **Write a troubleshooting entry**: what was exposed, when, what you replaced, how you checked.
5. **Whether to rewrite the repository history is your instructor's decision.** Do not force-push on
   your own.

---

## Why the wrong version is tempting

**A default makes the error go away.** `os.environ.get("SECRET_KEY", "dev")` means the app always
starts. That feels like robustness. It is the opposite: the app starts on a known key, on the host,
and nothing tells you.

**Typing the value is faster than setting a variable.** Once. Then it is in a commit forever.

---

## Do this today

1. List every setting in `docs/measure-analyze/architecture.md`, section 7: names and where each
   lives. No values.
2. Change `src/` to read them from `os.environ`, and stop with a clear message when a required one
   is missing.
3. Add the `.gitignore` lines above and commit them before any local settings file exists.
4. Set the variables on your host. [VERIFY]
5. Search your repository for the words `password`, `secret`, and `key`. Anything real you find goes
   to your instructor today.
6. **Commit.**

---

## If you are ahead, if you are behind

**If you are ahead:** add a test case to your test plan: "Given `SECRET_KEY` is not set, when the
app starts, then it exits with the missing-variable message." Run it and record it.

**If you are behind:** your skeleton is not deployed yet. Do steps 2 and 3 now anyway. They are
what makes the deploy work.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Publish to a web server** | Deploying with settings supplied by the host, not typed into code (6.5.12) |
| **Data source** | The database your code connects to through `PARTS_DB` (6.4.7) |
| **Document the problem and the verified solution** | The troubleshooting entry for an exposed secret (2.11.8) |
| **System hardware to support software** | Knowing what the host provides: its storage path, its port (1.4.4) |

---

## Self-check

**1.** Why may `PORT` have a default when `SECRET_KEY` may not?

**2.** A student commits a database password, notices an hour later, and deletes the line in the
next commit. Is the password safe now? What should happen?

**3.** Your app prints `KeyError: 'PARTS_DB'` on the host. What does that tell you, and what would a
better program have printed?

### Answers

**1.** A wrong port fails in plain sight and exposes nothing. A default secret means the app runs on
a key that is written in the repository, so anyone who reads the code can forge what the key
protects. A missing secret must stop the app.

**2.** No. The first commit still holds it in the history. The password must be changed wherever it
is used, the student tells the instructor that day, the code reads it from the environment, and a
troubleshooting entry records what happened. The instructor decides about the history.

**3.** The host does not have the `PARTS_DB` environment variable set. A better program checks for
it at startup and prints the name of the missing variable and where to set it, as `settings.py`
does.
