/*
 * count.js - lightweight first-party page-view counter for the Quarry Hill Skate Crew.
 *
 * Records one view per page load. Uses a first-party visitor ID so we can report
 * unique visitors as well as total views. Runs before the page renders so no view
 * is ever missed.
 */
(function () {
  "use strict";

  // Nothing to count when the page is opened from disk.
  if (location.protocol === "file:") {
    return;
  }

  // First-party visitor ID (never shared with third parties).
  function getVisitorId() {
    const match = document.cookie.match(/(?:^|; )visitor_id=([^;]+)/);
    if (match) {
      return match[1];
    }
    const id = crypto.randomUUID();
    document.cookie = "visitor_id=" + id + "; max-age=31536000; path=/; SameSite=Lax";
    return id;
  }

  // Send the hit and wait for confirmation, so the count is always accurate.
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/hit", false);
  xhr.setRequestHeader("Content-Type", "application/json");
  try {
    xhr.send(JSON.stringify({ path: location.pathname, visitor: getVisitorId() }));
  } catch (err) {
    // Counting must never break the page.
  }
})();
