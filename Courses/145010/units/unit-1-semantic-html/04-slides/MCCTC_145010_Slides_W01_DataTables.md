# Data Tables, and How Data Reaches People
---
## Slide 1: Which station is Theo working?
- You glance up and left, and you know
- A screen reader cannot glance
- It moves one cell at a time
- Only header cells tell it where it is
Speaker notes: Look at a shift schedule and find Theo. You glanced up at the column and left at the row, and you had the answer in a second. Now imagine you cannot glance. You hear one cell at a time. Theo. Theo. Priya. Which station, what time? The only way a screen reader can tell you is if the table says which cells are headers. Most tables on the web do not.
Image: A shift schedule grid with one cell highlighted and faint lines running up to its column header and left to its row header.
---
## Slide 2: A table that only looks right
```html
<table>
  <tr><td>Route</td><td>Leaves</td><td>Last stop</td></tr>
  <tr><td>12</td><td>3:05 p.m.</td><td>Oak Street</td></tr>
</table>
```
Speaker notes: This is a bus table where every cell is a td. It looks like a table. It has a row that reads like headers. The browser has no idea the first row is special, because nothing in the markup says so.
Image: None. This slide is code.
---
## Slide 3: The wrong way, and what Chrome decided
```
LayoutTable
  LayoutTableRow
    LayoutTableCell "Route"
    LayoutTableCell "Leaves"
    LayoutTableCell "Last stop"
```
Speaker notes: This is Chrome's accessibility tree for that table, captured through the same headless Chrome our checker uses. Chrome labelled it a layout table. It decided the table was there to position things, not to hold data. The automated audit in web-check reported nothing about it. Structure check reports that the table has no header cells. Open the Accessibility tab and select a table in your own lab. Read the role.
Image: None. This slide is code.
---
## Slide 4: A data table
```html
<table>
  <caption>Buses leaving the east loop after school</caption>
  <thead>
    <tr><th scope="col">Route</th><th scope="col">Leaves</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">12</th><td>3:05 p.m.</td></tr>
  </tbody>
</table>
```
Speaker notes: Same data, now a data table. The caption names it. The header row is in thead, and its cells are th with scope col. The first cell of each body row is a th with scope row. Chrome now calls it a table, with column headers and row headers, and a screen reader can say which headers go with each cell.
Image: None. This slide is code.
---
## Slide 5: The parts, and their jobs
- caption names the table, first inside it
- th with scope col or row
- thead, tbody, tfoot group the rows
- tfoot holds totals and summaries
- No tables for page layout, ever
Speaker notes: Five things to remember. The caption comes first. Every header is a th, and the course validator requires a scope on every one. Rows go in groups. A totals row goes in tfoot, because it summarizes the columns rather than naming them. And a table never lays out a page. Next week grid does that.
Image: A labelled diagram of a table with its caption, header row, body rows, and footer row called out.
---
## Slide 6: What no checker catches
- Validator: every th needs a scope
- Axe: headers must point at real cells
- Headers pointing at the wrong cells pass both
- Only a person catches that
Speaker notes: For complicated tables there is a second technique, ids and headers attributes. I built one on purpose with headers pointing at the wrong night. With a scope on every th, it passed web-check and passed structure check. The tools check that the parts exist. They cannot check that the parts are right. You check that with the Accessibility tab, or by listening.
Image: A table cell with an arrow pointing confidently to the wrong column header, and a green check mark beside it that should not be there.
---
## Slide 7: The same data, four ways
- Responsive page: anyone with a link can read
- Mobile app: reminders, but who installs it
- Desktop app: one person, one computer
- Web app: log in and change shared data
Speaker notes: Second half. Data has to reach people, and a web page is one way. A mobile app can send reminders, and costs two platforms and an install nobody wants for six Saturdays. A desktop application is great for one person at one computer. You built one, the WPF panel. A web application lets people log in and change shared data. You built one of those too, the Flask CRUD app.
Image: Four cards showing the same schedule on a phone browser, a phone app, a desktop window, and a login screen.
---
## Slide 8: Three questions decide it
- Who needs the data?
- Where are they when they need it?
- Do they read it, or change it?
- Changing it means accounts and data to protect
Speaker notes: Ask three questions. Who needs it. Where are they. Do they only read it, or do they change it. Referees who are fifteen, standing at a field, who want to trade games, need to change shared data. That points at a web application, and a web application means logins and information about minors that someone has to protect. That cost is part of the answer.
Image: A simple decision flow with three questions leading to the four presentation options.
---
## Slide 9: What you are about to build
- Lab W01-02: the bike kitchen shift table
- Delete the layout table, keep the data
- Caption, header cells, scope, tfoot
- presentation.md: four options, real costs
Speaker notes: Build one is lab two. The starter has two tables. One holds the page together, and it goes. One holds the shift data, and it becomes a real data table. Check the Accessibility tab before and after, and read the role out loud both times. Then write the short comparison of the four ways the shift lead could get this schedule to volunteers. Build two, the league schedule, on your project page.
Image: The Lab W01-02 starter page beside the rebuilt page, with the Accessibility tab open on each.
