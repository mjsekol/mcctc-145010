# One Apostrophe Away
---
## Slide 1: A real name crashes your sign-up page
- A volunteer's crop is called Grandma's peppers
- She searches for it on your page
- The page crashes. Nobody attacked anything
- Wednesday, your reviewer tries the same thing
Speaker notes: Here is a normal Tuesday at a community garden. The garden is invented, but the bug is real, and I ran it. A volunteer types the name of her bed, Grandma's peppers, into the search box. The page falls over. Nobody was trying to break in. She has an apostrophe. On Wednesday a classmate reviews your code, and the first thing on the security checklist is whether anything a person types reaches your database unsafely. So today, in fifteen minutes, we make sure it does not.
Image: A phone showing a search box with the words Grandma's peppers and a broken-page icon, deep navy and accent blue.
---
## Slide 2: The version most of us write first
```python
def find_crop(crop):
    sql = f"SELECT bed, volunteer FROM plots WHERE crop = '{crop}'"
    return db.execute(sql).fetchall()

print(find_crop("tomatoes"))
print(find_crop("x' OR '1'='1"))
print(find_crop("Grandma's peppers"))
```
Speaker notes: This is the version I see most, and it is the version AI assistants hand you when you ask for a quick search. It builds the query with an f-string. It reads nicely. Before I run it, predict three things. What does the tomatoes search print. What does the strange second one print. And what happens to Grandma's peppers.
Image: None. This slide is code.
---
## Slide 3: What it actually printed
```
[(1, 'Priya')]
[(1, 'Priya'), (2, 'Marcus'), (3, 'Hana')]
Traceback (most recent call last):
  ...
sqlite3.OperationalError: near "s": syntax error
```
Speaker notes: This is the real output from the build machine. Line one is fine. Line two asked for a crop that does not exist and got every volunteer in the table. That is SQL injection. The typed text became part of the query and made the condition true for every row. Line three is the one that should scare you more, because it happens on an ordinary day. The apostrophe ended the quoted string early, and the database could not read what was left.
Image: None. This slide is code.
---
## Slide 4: What went wrong
- The typed text was pasted into the SQL
- So the typer wrote part of your query
- An apostrophe ends the string early
- A crafted value changes what the query means
- The rubric caps Security at 9 for this
Speaker notes: One idea explains both failures. When you paste a value into the SQL text, the person who typed the value is now writing part of your query. Sometimes that is an accident, like the apostrophe. Sometimes it is on purpose. Either way, in the capstone rubric, input that reaches a query unparameterized is a must-fix security finding, and a must-fix security finding caps Security at 9 out of 20.
Image: A sheet of SQL with a sticky note pasted into the middle of it, the note's text leaking outside the lines.
---
## Slide 5: Values travel separately
```python
def find_crop(crop):
    rows = db.execute("SELECT bed, volunteer FROM plots WHERE crop = ?", (crop,))
    return rows.fetchall()

print(find_crop("tomatoes"))
print(find_crop("Grandma's peppers"))
print(find_crop("x' OR '1'='1"))
```
Speaker notes: Here is the fix. The question mark is a placeholder. The SQL text never changes. The value goes in the second argument, in a tuple, and notice the comma after crop, because that is what makes it a tuple of one. The database receives the query and the value separately, so the value is always treated as a value.
Image: None. This slide is code.
---
## Slide 6: Same three searches, fixed
```
[(1, 'Priya')]
[(2, 'Marcus')]
[]
```
Speaker notes: Real output again. Tomatoes finds Priya. Grandma's peppers finds Marcus, apostrophe and all. And the attack string is now a very strange crop name that nobody has, so it returns an empty list. Same database, same data, one change.
Image: None. This slide is code.
---
## Slide 7: In a Flask route, named placeholders
```python
bed = request.form.get("bed", type=int)
volunteer = request.form.get("volunteer", "").strip()
if bed is None or not volunteer:
    return "Choose a bed and enter your first name.", 400
db.execute(
    "INSERT INTO signups (bed, volunteer, day) VALUES (:bed, :volunteer, :day)",
    {"bed": bed, "volunteer": volunteer, "day": day},
)
```
Speaker notes: Your capstone reads values from a form, so here is the same idea in a route. Named placeholders with a colon, and a dictionary of values. There is a second defense here too. type equals int refused a bed number that was not a number, so a crafted bed value got a 400 and a message a person can act on. I tested this with Flask's test client. A name full of SQL was stored as plain text, and the table was still there afterward.
Image: None. This slide is code.
---
## Slide 8: What a placeholder cannot hold
- A placeholder holds a value, never a column name
- ORDER BY ? sorts by a constant, silently
- Check chosen columns against a fixed allow-list
- Partial search: the percent signs go in the value
- A list needs one question mark per value
Speaker notes: Three edge cases catch people. First, you cannot use a placeholder for a column or table name. ORDER BY question mark does not raise an error. It sorts by a constant, which changes nothing, and that wrong answer looks fine. So if a user picks the sort column, check it against a list you wrote. Second, for a LIKE search, put the percent signs inside the value, not the SQL. Third, for several values, build one question mark per value from the count.
Image: A padlocked box labelled value next to an open tray labelled column name with a checklist beside it.
---
## Slide 9: Two quieter mistakes
```
db.execute("... WHERE crop = ?", ("kale"))
sqlite3.ProgrammingError: Incorrect number of bindings supplied.
The current statement uses 1, and there are 4 supplied.

db.execute("... ORDER BY ?", ("volunteer",))
[(1, 'Tessa'), (2, 'Marcus')]        no error, not sorted by name
```
Speaker notes: Two I see every year. The first forgot the comma, so Python handed over the four letters of kale as four values, and the error message tells you exactly that if you read it. The second runs perfectly and returns rows in the wrong order. No error at all. That is the harder one to catch, and it is why your reviewer runs your code instead of reading it.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Search your code for execute and query
- Fix every f-string, plus, or format near SQL
- Add an allow-list wherever users choose a column
- Add an apostrophe test case to your test plan
- Commit before Wednesday's review
Speaker notes: Here is your build period. Search your project for every place you call execute or query. Any f-string, plus sign, percent sign, or format call near SQL gets fixed today. Anywhere a user picks a column or a sort order gets an allow-list. Then add a security case to section 4 of your test plan: a name with an apostrophe and the injection string, with the result you expect. The full note, with every output, is the Week 13 Monday clinic note. Commit before you leave, because your reviewer reads that commit on Wednesday.
Image: A checklist on a clipboard next to a laptop showing a search for the word execute, accent blue highlights.
---
