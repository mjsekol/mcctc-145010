/*
 * shift-board.js · Lab W04-01 STARTER
 *
 * What this file will do when you finish:
 *   1. Hide the shift rules behind a button that says whether they are open.
 *   2. Let a person take or drop each shift with a button.
 *   3. Keep a running total of hours and warn past the 12-hour limit.
 *
 * Right now it runs and does nothing useful. That is the starting line.
 * Open the Console in dev tools (F12). If you see the line below, the
 * browser found and ran this file.
 */

console.log("shift-board.js loaded");

// The most hours one person can pick in a week. It lives in one place, so a
// manager who changes the rule changes one line.
const HOUR_LIMIT = 12;

// ---------------------------------------------------------------------------
// Part 1 · The rules toggle (steps 6 to 9)
// ---------------------------------------------------------------------------

// TODO step 6: find the toggle button and the panel with document.querySelector.
// const rulesToggle = ...
// const rulesPanel = ...

// TODO step 7: write setRulesOpen(isOpen). It sets the panel's hidden property
// and the button's aria-expanded attribute, and nothing else.

// TODO step 8: start closed, then listen for "click" on the toggle.

// ---------------------------------------------------------------------------
// Part 2 · Taking shifts (steps 10 to 12)
// ---------------------------------------------------------------------------

// TODO step 10: find every "Take shift" button with document.querySelectorAll,
// then write totalHours(). It adds up data-hours for every button
// whose aria-pressed is "true", and returns a number.

// TODO step 11: write renderSummary(). It writes one sentence into #summary
// with textContent, and adds the class "over-limit" past HOUR_LIMIT.

// TODO step 12: give each button a click listener that flips aria-pressed
// and calls renderSummary(). Leave the button's label alone. Step 12 says why.
