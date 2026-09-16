/**
 * Team Shout-Outs
 *
 * Lets teammates write a short shout-out, preview it, post it to the wall,
 * filter the wall, and remove a shout-out.
 *
 * Loaded with defer, so every element exists before this runs.
 */

// Maximum length of a shout-out, in characters.
const MAX_LENGTH = 120;

// Starting shout-outs so the wall is not empty on first load.
let shoutouts = [
  { id: 1, text: "Huge thanks to Priya for fixing the drivetrain at 9 pm." },
  { id: 2, text: "Marcus rewired the whole arm in one period. GG." },
  { id: 3, text: "Shout-out to Lena for the scouting spreadsheet." },
  { id: 4, text: "gg to the pit crew, zero penalties all weekend." },
];
let nextId = 5;

// Cache the elements we use so we only look them up once.
const textBox = document.getElementById("shoutout-text");
const charCount = document.getElementById("char-count");
const preview = document.getElementById("preview");
const addButton = document.getElementById("add-button");
const filterBox = document.getElementById("filter");
const listEl = document.getElementById("shoutout-list");

/**
 * Update the character counter, and enable the Add button only when the
 * shout-out is between 1 and MAX_LENGTH characters long.
 */
function updateCounter() {
  const length = textBox.value.length;
  const remaining = MAX_LENGTH - length;
  const over = -remaining;

  if (remaining >= 0) {
    charCount.textContent = `${remaining} ${remaining === 1 ? "character" : "characters"} left`;
  } else {
    charCount.textContent = `${over} ${over === 1 ? "character" : "characters"} over the limit`;
  }

  addButton.disabled = length === 0 || length >= MAX_LENGTH;
}

/**
 * Draw the preview and the wall from the current state.
 */
function render() {
  // The preview shows exactly what will be posted.
  preview.innerHTML = `<p>${textBox.value}</p>`;

  // The filter is case-insensitive, so "gg" also finds "GG".
  const query = filterBox.value.trim();
  const visible = shoutouts.filter((s) => s.text.includes(query));

  listEl.innerHTML = "";
  for (const s of visible) {
    const item = document.createElement("li");
    item.className = "shoutout";
    item.innerHTML = `<p>${s.text}</p><span class="remove" data-id="${s.id}">Remove</span>`;
    listEl.appendChild(item);
  }
}

// One listener on the list handles every Remove control, including the ones
// added later. This is event delegation.
listEl.addEventListener("click", (event) => {
  const target = event.target.closest(".remove");
  if (!target) {
    return;
  }
  const id = Number(target.dataset.id);
  shoutouts = shoutouts.filter((s) => s.id !== id);
  render();
});

// Keep the counter and the preview in sync with every keystroke.
textBox.addEventListener("input", () => {
  updateCounter();
  render();
});

// Re-draw the wall as the person types in the filter box.
filterBox.addEventListener("input", render);

// Post the shout-out, then clear the box for the next one.
addButton.addEventListener("click", () => {
  const text = textBox.value.trim();
  if (text.length === 0) {
    return;
  }
  shoutouts.push({ id: nextId, text: text });
  nextId += 1;
  textBox.value = "";
  updateCounter();
  render();
});

// First draw.
updateCounter();
render();
