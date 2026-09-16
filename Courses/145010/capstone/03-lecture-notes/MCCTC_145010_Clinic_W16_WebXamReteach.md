# Clinic: What Ten Weeks Took Away
## 145010 Senior Capstone · Clinic · Week 16, Monday

**The signal:** any item on Thursday's practice test that more than 30 percent of the class missed.

**Slides:** This clinic has no slide outline. It runs from the board.

---

## The idea in plain language

The WebXam post-test is tomorrow. More than half of it is web development, and most of that you
last studied in Weeks 1 to 6. Since then you have built a real project, often in a different stack.
Some of the basics faded. That is normal. It is also fixable in 15 minutes, because the mistakes
that come back after ten weeks are almost always the same few.

This clinic does not go over the practice test item by item. Memorizing answer letters does not
help you tomorrow. Seeing the idea behind a missed item again does.

## Why it exists

The post-test is the course's end-of-course assessment, and your college credit for this course
depends on it. **The survey at the end of the post-test is how your college credit is triggered.
Do not close the test before you finish the survey.**

## How the 15 minutes run

Your instructor scored the practice test and found the items the class missed most. Those items
point to two or three areas. Today covers only those areas, about five minutes each, at the board.
The four worked examples below are the areas missed most often after a long gap. Your instructor
picks from them. If you missed today, read all four.

In Period 8, you get review reps matched to the items **you** missed. Do them without a computer.
Predict first, then check.

---

## Worked example 1: a label the browser can connect

A form control needs a name that a screen reader can announce. The label's `for` must match the
control's `id`.

```html
<label>Phone</label>
<input type="tel" id="phone" name="phone">
```

Chrome's accessibility tree gave this box an **empty name**. A screen reader announces something
like "edit text" and nothing more. web-check reported:

```
label (critical, 1 node(s))  Form elements must have labels  e.g. #phone
```

Here is the connected version, plus a group of checkboxes:

```html
<label for="text-ok">Text me reminders</label>
<input type="tel" id="text-ok" name="text">
<fieldset>
  <legend>Days you can help</legend>
  <input type="checkbox" id="sat" name="sat" value="yes">
  <label for="sat">Saturday</label>
  <input type="checkbox" id="sun" name="sun" value="yes">
  <label for="sun">Sunday</label>
</fieldset>
```

The box is now named "Text me reminders". The Saturday checkbox is named "Saturday", **inside a
group named "Days you can help"**. The group name comes from the `legend`. The page passed
web-check.

Remember three things. `for` matches `id`, not `name`. The `name` is what the server receives.
`fieldset` and `legend` name a group, and a heading above the controls does not.

## Worked example 2: where a link really goes

A browser turns every `href` into a full address, starting from the address of the page it is on.
This page is published at `https://northside-garden.example/plots/map.html`. Chrome resolved each
link this way:

| `href` | Chrome went to |
|---|---|
| `beds.html` | `https://northside-garden.example/plots/beds.html` |
| `tools/list.html` | `https://northside-garden.example/plots/tools/list.html` |
| `../index.html` | `https://northside-garden.example/index.html` |
| `/contact.html` | `https://northside-garden.example/contact.html` |
| `#bed-12` | `https://northside-garden.example/plots/map.html#bed-12` |
| `northside-garden.example/news.html` | `https://northside-garden.example/plots/northside-garden.example/news.html` |

Read the rules off the table:

- **No slash:** start in this page's folder.
- **`../`:** go up one folder.
- **Leading `/`:** start at the root of the host.
- **`#`:** a spot on this same page, the element whose `id` matches the text after the `#`. The
  `id` itself never contains the `#`.
- **No `https://`:** the browser treats a domain name as a folder name. The last row is a broken
  link to another site.

## Worked example 3: when a script runs

A script without `defer` runs the moment the parser reaches its tag. At that moment, it can only
see the elements above it.

`js/hours.js`:

```javascript
// Show visitors whether the shelter is open.
const note = document.querySelector("#open-now");
note.textContent = "Open until 6";
```

Loaded in the head with no `defer`:

```html
<head>
  <script src="js/hours.js"></script>
</head>
<body>
  <p id="open-now">Checking hours</p>
</body>
```

Chrome showed `Checking hours` and reported:

```
TypeError: Cannot set properties of null (setting 'textContent')
```

The same tag with `defer`, `<script src="js/hours.js" defer></script>`, waits until the whole page
is parsed. Chrome then showed `Open until 6`, with no error.

Remember three things:

- `defer` scripts run after parsing, in the order their tags appear.
- `null` has two causes: the element does not exist yet, or the selector does not match it.
- JavaScript comments are `//` for one line and `/* */` for several. A comment in another
  language's style is a syntax error, and a syntax error stops the whole script, not only that line.

## Worked example 4: which rule wins

`css/site.css` is linked first. A `<style>` block comes after it.

```css
/* css/site.css */
p { color: gray; }
#closing { color: navy; }
.alert { color: maroon; }
```

```html
<link rel="stylesheet" href="css/site.css">
<style>
  p { color: black; }
</style>
...
<p>Doors open at 10.</p>
<p class="alert">Bring your ID.</p>
<p class="alert" id="closing">Last adoption at 3.</p>
<p style="color: teal;">Parking is behind the building.</p>
```

Chrome computed:

| Paragraph | Color | Why |
|---|---|---|
| Doors open at 10. | black | Both rules use `p`, so they tie. The later one, the `<style>` block, wins. |
| Bring your ID. | maroon | A class beats an element name, even though the `p` rule comes later |
| Last adoption at 3. | navy | An id beats a class, even though `.alert` comes later in the file |
| Parking is behind the building. | teal | An inline `style` beats all of them |

The order to remember: inline style, then id, then class, then element. **Order only breaks
ties.**

---

## The wrong version, and exactly what it produces

The most common wrong version after ten weeks is example 3's first page: a script in the head with
no `defer`. It produces **no visible error.** The page shows its starting text, "Checking hours",
so it looks like the script is slow. The only evidence is the `TypeError` in the Console. On paper,
you get no Console at all, so you have to reason it out.

The second most common is example 1's first form. It looks perfect and has a word next to the box.
The accessibility tree says the box has no name.

## Why the wrong version is tempting

Both look finished. The browser forgives, and nothing turns red on the page. Ten weeks of building
in a framework or a different language also changes your habits. Frameworks often handle script
timing and label wiring for you. The WebXam asks about the plain versions.

## What to do in your own project today

- Run `node tools/web-check/check.js` on your main pages. Any `label` violation is example 1.
- Open the Console on every page, and fix any `null` error with the two-cause table in example 3.
- Click every link on your deployed site, not only on your laptop. Record the result in your
  [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md).
- This week's acceptance run depends on the same checks. See the
  [Acceptance Record](../05-labs/MCCTC_145010_Template_AcceptanceRecord.md).

## Vocabulary

| Term | What it means |
|---|---|
| **Accessible name** | What a screen reader announces for a control. It comes from its label. |
| **`fieldset` / `legend`** | A group of related controls, and the group's name |
| **Relative path** | A link address worked out from the current page's folder |
| **Root-relative path** | A link address that starts with `/`, worked out from the root of the host |
| **Absolute URL** | A full address with a scheme such as `https://` |
| **Fragment** | The part after `#`, pointing at an element's `id` on a page |
| **`defer`** | Download now, run after the page is parsed, in tag order |
| **Specificity** | Which selector wins: inline, then id, then class, then element |
| **Cascade** | The rules that decide which style applies. Specificity first, then order. |

## Check yourself

1. A page at `https://maple-pantry.example/events/drive.html` links to `../volunteer.html`. Write the
   full address.
2. A script in the head, with no `defer`, looks up an element in the body. What does the Console
   show?
3. `.price { color: green; }` comes after `#total { color: red; }`. An element has
   `id="total" class="price"`. What color is it?

---

## Check your answers

1. `https://maple-pantry.example/volunteer.html`. `../` leaves the `events` folder.
2. A `TypeError`: cannot set, or cannot read, properties of `null`. The element did not exist yet
   when the script ran.
3. Red. An id beats a class, and order only breaks ties.

**Tomorrow:** the post-test is Tuesday. Bring nothing but yourself. **Finish the survey at the end.
It is how your college credit is triggered.**
