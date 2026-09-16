# Clinic · Parameterized Queries
## 145010 Senior Capstone · Clinic · Week 13, Monday

**The signal:** any project that builds SQL with string formatting (an f-string, `+`, `%`, or
`.format` inside a query). Peer Code Review 1 is Wednesday, and this is the first thing a reviewer
checks under Security.

**Slides:** [outline](../04-slides/MCCTC_145010_Slides_W13_ParameterizedQueries.md). No exported
deck yet. To generate it when Gamma credits are available, from the repository root:
`node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W13_ParameterizedQueries.md --export pptx`

**If you missed it,** you can learn the skill from this file alone. Every example below was run on
the build machine with Python 3.13 and Flask 3.1, and the output is pasted exactly.

**Competencies:** 6.4.7 (code scripting to interact with data sources), 6.4.4 (the concept of a
form action), 1.1.9 (give and receive constructive feedback, because Wednesday's review checks this)

**The examples use the Northside Community Garden, an invented organization.** It is a composite,
not a real client.

---

## The idea in plain language

**The SQL text and the values travel separately.** You write the query with a placeholder, `?` or
`:name`, where a value goes. You hand the values to the database in a second argument. The database
never reads a value as SQL, so no value can change what the query does.

## Why it exists

Anything a person types can end up in your query: a first name, a search box, a hidden form field
somebody edited. If you paste that text into the SQL string, the person is writing part of your
query. Two things go wrong. A name with an apostrophe crashes the page. A crafted value changes the
query, and that is called **SQL injection**.

**The rubric treats this as serious.** In the capstone rubric, input that reaches a database query
unparameterized is a must-fix Security finding, and a must-fix Security finding caps Security at 9
of 20. See [the Capstone Rubric, part 2A](../09-project/MCCTC_145010_Capstone_Rubric.md#2a-the-five-dimension-code-review--24-points).

---

## Worked example 1 · a `?` placeholder

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE plots (bed INTEGER, crop TEXT, volunteer TEXT)")
db.executemany(
    "INSERT INTO plots VALUES (?, ?, ?)",
    [(1, "tomatoes", "Priya"), (2, "Grandma's peppers", "Marcus"), (3, "sunflowers", "Hana")],
)

def find_crop(crop):
    rows = db.execute("SELECT bed, volunteer FROM plots WHERE crop = ?", (crop,))
    return rows.fetchall()

print(find_crop("tomatoes"))
print(find_crop("Grandma's peppers"))
print(find_crop("x' OR '1'='1"))
```

Output:

```
[(1, 'Priya')]
[(2, 'Marcus')]
[]
```

**Read the third line.** The attack string was treated as a crop name. No crop is called that, so
the answer is an empty list. The apostrophe in the second search is ordinary text too.

**Note the comma in `(crop,)`.** That makes a tuple of one value. Without it you get the error in
the "two quieter mistakes" section below.

## Worked example 2 · named placeholders in a Flask route

Your capstone probably reads values from a form. Here is a route that does it safely, tested with
Flask's test client so no server is needed.

```python
import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE signups (bed INTEGER, volunteer TEXT, day TEXT)")

@app.post("/signup")
def signup():
    bed = request.form.get("bed", type=int)
    volunteer = request.form.get("volunteer", "").strip()
    day = request.form.get("day", "")
    if bed is None or not volunteer:
        return "Choose a bed and enter your first name.", 400
    db.execute(
        "INSERT INTO signups (bed, volunteer, day) VALUES (:bed, :volunteer, :day)",
        {"bed": bed, "volunteer": volunteer, "day": day},
    )
    db.commit()
    return f"Saved bed {bed}.", 201

client = app.test_client()
r = client.post("/signup", data={"bed": "2", "volunteer": "Deshawn", "day": "Saturday"})
print(r.status_code, r.get_data(as_text=True))
r = client.post("/signup", data={"bed": "2); DROP TABLE signups; --", "volunteer": "Deshawn"})
print(r.status_code, r.get_data(as_text=True))
r = client.post("/signup", data={"bed": "3", "volunteer": "Robert'); DROP TABLE signups; --", "day": "Sunday"})
print(r.status_code, r.get_data(as_text=True))
print(db.execute("SELECT bed, volunteer, day FROM signups").fetchall())
```

Output:

```
201 Saved bed 2.
400 Choose a bed and enter your first name.
201 Saved bed 3.
[(2, 'Deshawn', 'Saturday'), (3, "Robert'); DROP TABLE signups; --", 'Sunday')]
```

**Two defenses are working here.** `type=int` refused a bed number that was not a number, so the
second request got a 400 with a message a person can act on. The named placeholders stored the
strange name as plain text, and the table still exists.

**One more thing to notice.** The response echoes `bed`, which is an integer, and never echoes the
name or day. Text a person typed that goes back into a page must be escaped. Jinja templates do that
for you. A hand-built f-string response does not. A page that runs text a person typed as markup has a
cross-site scripting problem, and Review 2 looks at security again from scratch.

## Worked example 3 · partial search, several values, and a column name

```python
term = "tomato"
print(db.execute("SELECT bed, crop FROM plots WHERE crop LIKE ?", (f"%{term}%",)).fetchall())

beds = [2, 4]
marks = ", ".join("?" for _ in beds)
print(db.execute(f"SELECT bed, volunteer FROM plots WHERE bed IN ({marks})", beds).fetchall())

def sorted_plots(column):
    allowed = {"bed", "crop", "volunteer"}
    if column not in allowed:
        raise ValueError(f"cannot sort by {column!r}")
    return db.execute(f"SELECT bed, volunteer FROM plots ORDER BY {column}").fetchall()

print(sorted_plots("volunteer"))
print(sorted_plots("bed; DROP TABLE plots"))
```

With four beds (cherry tomatoes, peppers, roma tomatoes, sunflowers), the output is:

```
[(1, 'cherry tomatoes'), (3, 'roma tomatoes')]
[(2, 'Marcus'), (4, 'Luis')]
[(3, 'Hana'), (4, 'Luis'), (2, 'Marcus'), (1, 'Priya')]
ValueError: cannot sort by 'bed; DROP TABLE plots'
```

(The last line is the final line of the traceback.)

**Three rules come out of this.** The `%` signs go in the value, never in the SQL. For a list, you
build one `?` per value from the count, never from the values. **A placeholder can only hold a
value, never a table or column name**, so a column name a user chooses is checked against a fixed
list you wrote.

**Another language.** Node 22 on the build machine has a built-in `node:sqlite` module. The same
idea ran there: `db.prepare("SELECT bed, volunteer FROM plots WHERE crop = ?")` and then
`.all("x' OR '1'='1")` printed `[]`. Node printed an `ExperimentalWarning` because that module is
still experimental. A C# version was not run here, because the SQLite library for .NET is not
installed on the build machine. The idea in C# is the same: parameters are added to the command,
never pasted into its text.

---

## The wrong version, and exactly what it produces

```python
def find_crop(crop):
    sql = f"SELECT bed, volunteer FROM plots WHERE crop = '{crop}'"
    return db.execute(sql).fetchall()

print(find_crop("tomatoes"))
print(find_crop("x' OR '1'='1"))
print(find_crop("Grandma's peppers"))
```

Output, with the traceback shortened and its last line exact:

```
[(1, 'Priya')]
[(1, 'Priya'), (2, 'Marcus'), (3, 'Hana')]
Traceback (most recent call last):
  ...
sqlite3.OperationalError: near "s": syntax error
```

**The second line is the attack.** The query became `WHERE crop = 'x' OR '1'='1'`, which is true
for every row, so every volunteer came back. **The third line is a real person** whose crop has an
apostrophe. The page crashes for them, on a normal day, with no attacker anywhere.

### Two quieter mistakes

```python
db.execute("SELECT bed FROM plots WHERE crop = ?", ("kale"))
```

```
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.
```

`("kale")` is a string, not a tuple, so Python handed over four letters. Add the comma.

```python
print(db.execute("SELECT bed, volunteer FROM plots ORDER BY ?", ("volunteer",)).fetchall())
```

```
[(1, 'Tessa'), (2, 'Marcus')]
```

No error, and the list is not sorted by name. The placeholder became the constant text
`'volunteer'`, and sorting by a constant changes nothing. **This one produces a wrong answer that
looks fine**, which is the hardest kind of bug to catch.

## Why the wrong version is tempting

An f-string is how you have built every other string for two years. It reads naturally, and on your
own test data it works, because you never typed an apostrophe. AI assistants also produce it often,
especially when asked for "a quick search." Nothing fails until a real person with a real name uses
it, and by then it is live.

---

## What to do in your project today

1. Search your code for `execute(` and `query(` and read every line. Any `f"`, `+`, `%`, or
   `.format` near SQL gets fixed today.
2. Find every place a user chooses a column or sort order. Add an allow-list.
3. Add one security case to your [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md), section
   4: a name with an apostrophe and the string `x' OR '1'='1`, with the expected result written down.
4. Before Wednesday, read the Security checklist in the
   [Peer Code Review template](../05-labs/MCCTC_145010_Template_PeerCodeReview.md). Your reviewer
   will ask whether any input reaches a query unsafely.
5. If you fixed something, write a [Troubleshooting Log](../05-labs/MCCTC_145010_Template_TroubleshootingLog.md)
   entry or a decision log entry, and commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Parameterized query** | A query whose values are passed separately from its SQL text |
| **Placeholder** | The `?` or `:name` in the SQL that marks where a value goes |
| **SQL injection** | Input that changes what a query does because it was pasted into the SQL |
| **Binding** | Handing a value to the database for one placeholder |
| **Allow-list** | A fixed list of accepted values; anything else is refused |
| **Form action** | The address a form sends its data to, here `/signup` |

---

## Check yourself

1. A classmate says, "My search box only takes crop names, so injection cannot happen." What would
   you type into their search box to test that claim, and what result proves them wrong?
2. Why does `ORDER BY ?` not work, and what do you do instead?
3. Your query runs fine with `("kale",)` and fails with `("kale")`. Explain the difference in one
   sentence.

---

## Check your answers

**1.** Type `x' OR '1'='1`. If the results show every row instead of none, the input is being pasted
into the SQL. Also try a real value with an apostrophe, such as `Grandma's peppers`. A crash proves
the same problem without any attack.

**2.** A placeholder can only stand for a value, so `ORDER BY ?` sorts by a constant and the order
does not change. Check the requested column against a fixed set of allowed names, then put the
checked name into the SQL.

**3.** `("kale",)` is a tuple holding one string, while `("kale")` is only a string, which Python
splits into four separate values.
