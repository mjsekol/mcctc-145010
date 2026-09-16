// Ridgeview Robotics Club: parts checkout list.
// No framework, no network. Data comes from parts-data.js.

// The working list starts as a copy of the seed data. Adding a checkout pushes
// onto this array and re-renders.
const items = CHECKOUTS.slice();

// A counter the instructor probe reads, to measure how much sorting the page
// does while you type. It is not used by the app itself.
window.__sortCompares = 0;

function daysBetween(fromDate, toDate) {
  // Returns the number of whole days from fromDate to toDate.
  // A negative result means toDate is in the future.
  const ms = new Date(toDate) - new Date(fromDate);
  return Math.round(ms / 86400000);
}

function compareByDue(a, b) {
  window.__sortCompares += 1;
  return daysBetween(TODAY, a.dueBack) - daysBetween(TODAY, b.dueBack);
}

function dueSoonCount() {
  // Count parts due back within the next 7 days.
  let count = 0;
  for (const item of items) {
    const diff = daysBetween(TODAY, item.dueBack);
    if (diff >= 0 && diff < 7) {
      count += 1;
    }
  }
  return count;
}

function matchesQuery(item, query) {
  const q = query.trim().toLowerCase();
  if (q === "") {
    return true;
  }
  return item.part.toLowerCase().includes(q);
}

function render(query) {
  // Sort every part by due date, soonest first, then show the ones that match.
  const sorted = items.slice().sort(compareByDue);
  const visible = sorted.filter((item) => matchesQuery(item, query));

  const body = document.getElementById("checkout-body");
  body.innerHTML = "";
  for (const item of visible) {
    const row = document.createElement("tr");

    const part = document.createElement("td");
    part.textContent = item.part;
    row.appendChild(part);

    const member = document.createElement("td");
    member.textContent = item.member;
    row.appendChild(member);

    const note = document.createElement("td");
    note.innerHTML = item.note;
    row.appendChild(note);

    const due = document.createElement("td");
    due.textContent = item.dueBack;
    row.appendChild(due);

    body.appendChild(row);
  }

  document.getElementById("due-soon").textContent = dueSoonCount();
}

function addCheckout(event) {
  event.preventDefault();
  const partInput = document.getElementById("part");
  const noteInput = document.getElementById("note");
  const part = partInput.value.trim();
  const note = noteInput.value.trim();
  if (part === "") {
    return;
  }
  items.push({
    part: part,
    member: "You",
    note: note,
    checkedOut: TODAY,
    dueBack: addDays(TODAY, 14),
  });
  partInput.value = "";
  noteInput.value = "";
  render(document.getElementById("filter").value);
}

function addDays(dateString, days) {
  const date = new Date(dateString);
  date.setDate(date.getDate() + days);
  return date.toISOString().slice(0, 10);
}

document.getElementById("add-form").addEventListener("submit", addCheckout);
document.getElementById("filter").addEventListener("input", function () {
  render(this.value);
});

render("");
