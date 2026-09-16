# Front Desk Checkout · User Guide
For: the Hillcrest Senior Center front desk   Version 1   Week 17

*Drafted with an AI assistant from the project README and the app, then lightly edited. Invented
composite for Gate 2 Week 17. Sections are numbered so you can cite them.*

---

## 1. What this is for

Front Desk Checkout keeps track of the center's shared items, such as the folding tables, the
portable projector, and the coffee urn. It shows what is on the shelf, which group has each item
that is out, and when it is due back. It replaces the clipboard at the front desk.

## 2. What it does, and what that means for you

| It can | Which means |
|---|---|
| Show every shared item and whether it is on the shelf | You can answer "is the projector free?" without walking to the storeroom |
| Record which group has an item, with a due date 7 days later | You know who to ask when something is missing |
| Keep a history of the 50 most recent check-outs and check-ins | You can see what happened last week |

## 3. Setting up

Before first use, set up the program on the front desk computer.

1. Open PowerShell in the **CheckoutDesk** folder.
2. Install the required package by typing `pip install flask` and pressing Enter.
3. Start the program by typing `python app.py`. You should see `Running on http://127.0.0.1:8165`.
4. To change how long items can be borrowed, open `app.py` in Notepad, change `LOAN_DAYS = 7` to
   the number of days you want, save the file, and start the program again.
5. To add a new item, open `checkout.db` with a database browser and add a row to the `items`
   table.

## 4. Opening Front Desk Checkout

1. Open the web browser on the front desk computer.
2. Go to `http://127.0.0.1:8165`. You should see **Shared items**, with a line such as
   **8 items. 2 checked out.**

## 5. Checking an item out

1. Find the item in the list. Items that are available have a green button.
2. Choose the group from the drop-down list next to the item.
3. Click the green button. You should see **Checked out:** followed by the item, the group, and the
   date it is due back.

The page is designed for people who use computers every day. If you are not comfortable with
computers, ask one of the younger volunteers to do check-outs for you.

## 6. Checking an item in

1. Find the item in the list. Items that are out have a dark blue button.
2. Click the dark blue button. You should see **Checked in:** followed by the item, and **It is back
   on the shelf.**

## 7. Seeing what is out and what happened

- The top of the Items page shows how many items there are and how many are checked out.
- Select **History** at the top of any page to see the 50 most recent check-outs and check-ins,
  newest first.
- To get a list you can print or send to the center director, press **Export to Excel** at the
  bottom of the History page. A spreadsheet named `checkout-history.xlsx` downloads to your
  Downloads folder.

## 8. What the messages mean

| On screen | What it means | What to do |
|---|---|---|
| **Checked out: ...** | The item is recorded as out, with its due date | Nothing |
| **Checked in: ... It is back on the shelf.** | The item is recorded as returned | Nothing |
| **... is already checked out to ...** | Someone recorded it as out before you | Check the shelf, then ask the group named |
| **... is already on the shelf.** | It was already checked in | Nothing |
| **Choose a group before checking an item out.** | No group was chosen | Choose a group, then check it out again |

## 9. When something goes wrong

| What you notice | Try this first | If that does not work |
|---|---|---|
| The page does not load | Wait one minute and reload the page | Restart the program yourself: open the **CheckoutDesk** folder and double-click **start-checkout.bat**. Leave the black window that opens running, then reload the page |
| The list shows the wrong items, or an item shows as out when it is on the shelf | Close the black program window. Delete the file **checkout.db** in the **CheckoutDesk** folder, then double-click **start-checkout.bat**. Your records rebuild automatically from the nightly snapshot, and the list is correct again | Contact the front office manager |

## 10. Keeping your data safe

Front Desk Checkout runs on infrastructure designed for 99.9 percent availability. Your data is
protected by automated nightly snapshots retained for 30 days, and by encryption at rest using
industry-standard AES-256. Point-in-time recovery lets you restore your instance to any moment within
the retention window, and our platform team monitors service health around the clock.

## 11. Privacy

The program stores item names, group names, and the time of each check-out and check-in. It does not
store the name of any person.

## 12. Support and warranty

The student developer will fix problems reported through the school until the end of Week 18. After
that, no support is promised unless it is agreed in writing through the school.

## 13. Words used in this guide

| Word | Meaning |
|---|---|
| CheckoutDesk folder | The folder on the front desk computer where the program lives |
| Check out | Record that a group has taken an item |
| Check in | Record that an item is back on the shelf |
| History | The list of recent check-outs and check-ins |
