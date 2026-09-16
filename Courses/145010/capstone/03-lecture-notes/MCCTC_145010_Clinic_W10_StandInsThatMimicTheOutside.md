# Clinic · Stand-Ins That Mimic the Outside
## 145010 Senior Capstone · Week 10, Wednesday · 15 minutes · Analyze

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 10, Wednesday, or any week the room shows this signal: test plans
that say "test on the real thing" with nothing that works when the real thing is down.
**If you missed it,** you can learn the skill from this file alone. The two programs,
[stand_in_server.py](clinic-w10-stand-in/stand_in_server.py) and
[check_health.py](clinic-w10-stand-in/check_health.py), run on any lab machine with Python.
**Competencies:** 2.12.2 (develop a test system that accurately mimics external interfaces),
2.12.3 (realistic test cases that compare with expected performance), 2.7.5 (data transmission,
bandwidth, and latency), 2.11.6 (test a solution)

---

## Why this exists

Every capstone depends on something you do not control. A host. A hosted database. A sensor on a
Raspberry Pi across the room. A model server on lab hardware. Some day in the next eight weeks that
piece will be asleep, slow, broken, or in use by someone else.

If your only test is "try it on the real thing," that day you cannot test at all. Worse, you can
never test what happens **when** the real thing fails, because you cannot make it fail on command.
Your requirements have a failure table. Somebody has to check it.

A **stand-in** is a small program that answers the same address, in the same shape, as the real
piece, and can pretend to be in trouble when you tell it to. The state names this skill in 2.12.2:
a test system that accurately mimics external interfaces.

## The skill in plain language

A good stand-in has four properties:

1. **Same interface.** Same address, same kind of reply, same field names. Your code cannot tell
   the difference.
2. **An explicit port.** Always passed on the command line, never a default. A client pointed at
   the wrong port may get an answer from some other program and never know it.
3. **Modes.** At least a normal mode and one failure mode. Slow, error, and silent are the usual
   three.
4. **Invented data only.** Nothing real, nothing personal.

Every stand-in goes in section 9 of your architecture and section 3 of your test plan, with the
exact start command and the modes it simulates.

**What each track usually stands in for:**

| Track | Real piece | Usual stand-in | Modes worth having |
|---|---|---|---|
| Full-Stack | The host and its database | A local server and a local database with invented rows | normal, slow wake-up, database unreachable |
| Industrial / HMI | The sensor on the Pi | A replay file of recorded or generated readings | normal, hot afternoon, sensor silent |
| AI-Integrated | The model server | A stub server with canned answers | normal, slow, down, malformed answer |

## Worked example 1 · the stand-in server

*Composite, not a real organization.* The Parts Bin Board runs on an approved host. Its health
checker calls `GET /health` every 30 minutes to write the thirty-day log. The student needs to
test the checker when the host is fine, when it is waking up slowly, and when its database is
gone.

The full file is
[stand_in_server.py](clinic-w10-stand-in/stand_in_server.py), standard library only. The heart of
it:

```python
SLOW_SECONDS = 3  # a free-tier host waking up after a quiet night

REPLIES = {
    "normal": (200, {"status": "ok", "database": "ok", "version": VERSION}),
    "slow": (200, {"status": "ok", "database": "ok", "version": VERSION}),
    "error": (503, {"status": "error", "database": "unreachable", "version": VERSION}),
}

def do_GET(self):
    if self.path != "/health":
        self.send_reply(404, {"status": "error", "detail": "not found"})
        return
    if mode == "slow":
        time.sleep(SLOW_SECONDS)
    code, body = REPLIES[mode]
    self.send_reply(code, body)
```

The reply has the same keys in every mode, because the checker reads those keys. The server's
own log line never records who asked.

## Worked example 2 · the checker, run against every mode

The checker is [check_health.py](clinic-w10-stand-in/check_health.py). It calls `/health` once
and prints one line. The composite requirement says health must answer within 2 seconds, so the
checker reports `slow` above that.

In one terminal, from the `clinic-w10-stand-in` folder, start the stand-in in one mode. In a second
terminal, run the checker. Stop the server with Ctrl+C before starting the next mode.

```
python stand_in_server.py --port 5320 --mode normal
python check_health.py --port 5320
```

These are the real outputs from a run on the build machine. The `ms` numbers change a little from
run to run.

**Normal mode.** Server terminal, then checker terminal:

```
stand-in listening on http://127.0.0.1:5320 mode=normal
stand-in [normal] GET /health -> 200
```

```
result=ok status=200 ms=4 database=ok
```

**Slow mode.** The host is waking up:

```
stand-in listening on http://127.0.0.1:5320 mode=slow
stand-in [slow] GET /health -> 200
```

```
result=slow status=200 ms=3005 database=ok
```

**Error mode.** The host is up, the database is not:

```
stand-in listening on http://127.0.0.1:5320 mode=error
stand-in [error] GET /health -> 503
```

```
result=error status=503 ms=4 database=unreachable
```

Three states, three different lines, on demand, with the real host never touched. Each line is a
test case with an expected result that could come out wrong.

## Worked example 3 · turning modes into test cases

*Composite.* Section 4 of the test plan gains rows like these:

| ID | Req | Starting state | Action | Expected result |
|---|---|---|---|---|
| T-21 | NF2 | Stand-in on port 5320, mode normal | Run the checker once | `result=ok`, status 200 |
| T-22 | NF2 | Stand-in on port 5320, mode slow | Run the checker once | `result=slow`, ms above 2000, and the line is still written |
| T-23 | E1 | Stand-in on port 5320, mode error | Run the checker once | `result=error status=503 database=unreachable` |
| T-24 | E1 | Nothing running on port 5320 | Run the checker once | `result=down`, and the checker does not crash |

And section 3 of the test plan records the setup:

| Stand-in | Start command | Modes it simulates |
|---|---|---|
| Host health | `python stand_in_server.py --port 5320 --mode <mode>` | normal, slow, error |

## The wrong version, and what it costs

A test plan with this setup section:

```
Test setup: test everything on the real deployed site.
```

Here is what the checker printed on the build machine with nothing running on port 5320, which is
what a "real thing only" plan faces the day the host is down:

```
result=down status=none ms=0
```

That line is honest, and it is all you get. You cannot run T-21, T-22, or T-23. You cannot show
that the error message in E1 appears, because you cannot make the database disappear on command.
And NOT RUN is never a pass.

A second wrong version is leaving the port out. The stand-in refuses to start without one. This is
the real message:

```
usage: stand_in_server.py [-h] --port PORT [--mode {error,normal,slow}]
stand_in_server.py: error: the following arguments are required: --port
```

That refusal is on purpose. A stand-in on a default port can collide with another student's server,
and your checker would test the wrong program.

## Why the wrong version is tempting

Building a stand-in feels like building a second project. It is not. The one in this clinic is 81
lines, comments included, and uses only the standard library. The real thing also usually works when you try it, so a failure mode
feels like a fantasy. It is not a fantasy. **The day the host is down is the day your stakeholder
is watching.** A stand-in is how you already know what they will see.

## Do this today

The Gate 2 critique takes the first 40 minutes of the build period. After it:

1. List every piece of your system you do not control.
2. For each, write one row in section 9 of the architecture: the stand-in, the start command with
   an explicit port, and the modes.
3. Copy those rows into section 3 of `docs/measure-analyze/test-plan.md`, using the
   [Test Plan template](../05-labs/MCCTC_145010_Template_TestPlan.md).
4. Write one test case per mode.
5. If you have time, build the smallest stand-in now and commit it under `src/`. Run it. Stop it.
6. Commit. Stop every server you started before you leave.

Pick a port with your instructor so no two students use the same one. Never use a model server's
default port for anything of yours, as the
[AI-Integrated guide](../09-project/MCCTC_145010_TrackGuide_AIIntegrated.md) warns.

## If you are ahead, if you are behind

**Ahead.** Add a fourth mode that returns a reply with a missing field, and make your checker
report it instead of crashing. Real services fail that way too.

**Behind.** Write the rows in section 9 and section 3 today, even with no code. A planned
stand-in with a start command and modes is evidence. Build it in Sprint 1.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Test system that mimics external interfaces** | Your stand-in. 2.12.2. |
| **External interface** | Any piece your code talks to that you do not control. |
| **Test case** | A starting state, an action, and an expected result that could fail. 2.12.3. |
| **Expected performance** | The number the result is compared with, like 2 seconds. |
| **Latency** | How long a reply takes. The `ms` in the checker's line. 2.7.5. |
| **Port** | The number that says which program on a machine gets the request. |

## Self-check

**1.** Why does the stand-in reply with the same keys in error mode as in normal mode?

**2.** A classmate's stand-in model server has one mode, which always returns a perfect answer.
What is missing, and what does it cost?

**3.** Your checker prints `result=down status=none ms=0`. Name two different things that could
cause it.

### Answers

**1.** Because the checker reads those keys. If the error reply had different keys, the checker
might crash on a missing field instead of reporting the error, and you would be testing the wrong
failure.

**2.** A failure mode: slow, down, or malformed. Without one, the fallback and the error messages
can never be tested, so the failure rows in the requirements stay NOT RUN.

**3.** Nothing is running on that port, or the stand-in is running on a different port than the
checker was given. A firewall rule blocking the connection is another good answer.
