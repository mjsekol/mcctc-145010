/*
 * signup.js · Open Mic Night · Labs W05-01 and W05-02 · STARTER
 *
 * Two jobs, both conveniences. The server checks everything again.
 *
 *   1. Tuesday: when the person opens the slot list, ask the web service at
 *      /api/slots how many places are left right now, and update the list.
 *   2. Thursday: when the person submits, check the answers here first, and
 *      show problems with the same accessible pattern the server uses.
 *
 * If this file never loads, the form still works: the browser's own checks
 * run, and the server refuses anything wrong and explains why.
 */

"use strict";

const form = document.querySelector("#signup-form");
const slotSelect = document.querySelector("#slot");

// ---------------------------------------------------------------------------
// Part 1 · Tuesday · Reading a web service
// ---------------------------------------------------------------------------

// Asks the server for the latest counts and rewrites each option's text.
// fetch() does not freeze the page: the rest of the page keeps responding
// while the request is out, and the code after await runs when it returns.
async function refreshSlots() {
  try {
    const response = await fetch("/api/slots");
    if (!response.ok) {
      return; // The server's own list is still on the page. Keep it.
    }
    const slots = await response.json();
    for (const slot of slots) {
      const option = slotSelect.querySelector(`option[value="${slot.id}"]`);
      if (!option) {
        continue;
      }
      const left = slot.places_left;
      const words = left > 0 ? `${left} ${left === 1 ? "place" : "places"} left` : "no places left";
      option.textContent = `${slot.label}, ${words}`;
      // A full slot cannot be chosen here. The server still checks, because
      // someone can fill it in the seconds between this request and Submit.
      option.disabled = left <= 0;
    }
  } catch (error) {
    // No network, or the server stopped. Leave the list as it was.
    console.warn("Could not refresh slots:", error.message);
  }
}

// The form is written in Lab W05-01. Until it exists, there is nothing to update.
if (slotSelect) {
  slotSelect.addEventListener("focus", refreshSlots);
}

// ---------------------------------------------------------------------------
// Part 2 · Thursday · Checking before sending, and saying what is wrong
// ---------------------------------------------------------------------------

// The same rules and the same sentences as validation.py. Keeping two copies
// in step is the price of checking in two places. The server's copy is the
// one that counts.
const MESSAGES = {
  performer_name: "Enter a stage name between 2 and 40 characters.",
  email_missing: "Enter an email address so we can confirm your slot.",
  email_format: "Enter an email address in the form name@example.com.",
  act_type: "Choose the kind of act: music, comedy, poetry, or other.",
  slot: "Choose a time slot from the list.",
  minutes: "Enter how long your act is, a whole number from 1 to 8 minutes.",
  agree: "Tick the box to agree to the house rules.",
};

// Where each message is linked from the summary, and which element carries
// aria-invalid. For a radio group, the fieldset carries it.
const FIELDS = {
  performer_name: { focus: "performer-name", marks: "performer-name" },
  email: { focus: "email", marks: "email" },
  act_type: { focus: "act-music", marks: "act-fieldset" },
  slot: { focus: "slot", marks: "slot" },
  minutes: { focus: "minutes", marks: "minutes" },
  agree: { focus: "agree", marks: "agree" },
};

function checkForm() {
  const errors = {};
  const data = new FormData(form);
  // TODO Lab W05-02, step 12: the same rules as validation.py, using MESSAGES.
  // Read values with data.get("name"). Put each problem in errors[fieldName].
  return errors;
}

// Removes every message this script or the server added, and the attributes
// that pointed at them, so a second submit starts clean. Provided.
function clearErrors() {
  document.querySelector("#error-summary")?.remove();
  for (const message of document.querySelectorAll(".field-error")) {
    message.remove();
  }
  for (const marked of document.querySelectorAll("[aria-invalid]")) {
    marked.removeAttribute("aria-invalid");
  }
  for (const described of document.querySelectorAll("[aria-describedby]")) {
    const kept = described.getAttribute("aria-describedby")
      .split(" ")
      .filter((id) => !id.endsWith("-error"));
    if (kept.length) {
      described.setAttribute("aria-describedby", kept.join(" "));
    } else {
      described.removeAttribute("aria-describedby");
    }
  }
  document.title = document.title.replace(/^Error: /, "");
}

// TODO Lab W05-02, step 13: write showErrors(errors). It must, using only
// createElement and textContent:
//   1. call clearErrors()
//   2. build a summary: a div with id "error-summary", tabIndex -1, and
//      aria-labelledby pointing at an h2, then a list of links, one per error,
//      each href="#" + FIELDS[name].focus
//   3. for each error, put a p.field-error with id FIELDS[name].focus + "-error"
//      next to its control, set aria-invalid="true" on FIELDS[name].marks, and
//      ADD the message id to that element's aria-describedby
//   4. put the summary at the top of <main>, prefix the title with "Error: ",
//      and move focus to the summary

// TODO Lab W05-02, step 14: set form.noValidate = true, then listen for
// "submit" on the form. If checkForm() finds errors, preventDefault() and
// showErrors(errors). If not, let the form go.

// TODO Lab W05-02, step 15: if the server sent back a page with a summary,
// move focus to it when the page loads.

// Provided: a link in the summary moves focus to the control itself, and
// scrolls its label into view, so the person lands on the thing to fix.
document.addEventListener("click", (event) => {
  const link = event.target.closest(".error-summary a");
  if (!link) {
    return;
  }
  const target = document.getElementById(link.getAttribute("href").slice(1));
  if (target) {
    event.preventDefault();
    target.focus();
    (target.closest(".field, fieldset") || target).scrollIntoView();
  }
});
