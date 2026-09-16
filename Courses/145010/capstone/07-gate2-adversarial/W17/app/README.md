# Front Desk Checkout · README
## Gate 2 Week 17 source files · developer notes · invented composite

**Invented for a Gate 2 exercise.** The Hillcrest Senior Center, its front desk, its groups, and
its items do not exist. Every record the app creates is invented.

This README is for developers. The user guide you are evaluating is `../user-guide.md`.

---

## What it is

A small Flask app that tracks the center's shared items: which are on the shelf, which group has
each item that is out, and when it is due back. It keeps a history of the 50 most recent check-outs
and check-ins.

On the front desk computer, this folder is installed as **CheckoutDesk**. The front office manager
is the stakeholder.

| File | What it does |
|---|---|
| `app.py` | The whole program: routes, database setup, seed data |
| `templates/base.html` | The page frame, styles, and navigation |
| `templates/index.html` | The Items page |
| `templates/history.html` | The History page |
| `start-checkout.bat` | Starts the program from this folder on Windows |

## How to run it

Python 3.13 and Flask 3.1 are already installed on the lab machines. The app uses port **8165**.

**Keep your test database out of the repository.** Point the app at a file in your temp folder
first, so nothing you try can damage anything you care about.

PowerShell:

```
cd <this folder>
$env:CHECKOUT_DB = "$env:TEMP\checkout-gate2.db"
python app.py
```

Git Bash:

```
cd <this folder>
CHECKOUT_DB="$TEMP/checkout-gate2.db" python app.py
```

Open `http://127.0.0.1:8165` in a browser. Stop the app with Ctrl+C in the window where it runs.

If you do not set `CHECKOUT_DB`, the app creates `checkout.db` in this folder. **Delete it before
you commit.** It does not belong in a repository.

## What happens at start

`init_db()` runs once, before the server starts. If the database file is missing, it creates the
two tables and fills them with invented seed data: eight items, two of them already checked out.
If the file exists, it is used as it is.

## Addresses

| Method and address | What it does |
|---|---|
| `GET /` | The Items page |
| `POST /checkout/<id>` | Checks an item out to the chosen group, due back in 7 days |
| `POST /checkin/<id>` | Checks an item back in |
| `GET /history` | The History page |
| `GET /health` | A small JSON status: item count, checked-out count, event count |

## Checking the app yourself

You may test anything the user guide says, on your own copy, with your temp database. Some useful
commands, from a second terminal while the app runs:

```
curl -s http://127.0.0.1:8165/health
curl -s http://127.0.0.1:8165/history
curl -s -o NUL -w "%{http_code}\n" http://127.0.0.1:8165/some-address
```

In Windows PowerShell 5.1, type `curl.exe`, because `curl` there means a different command. In Git
Bash, use `-o /dev/null` instead of `-o NUL`.

**Stop the app when you finish**, and make sure nothing is left on port 8165.
