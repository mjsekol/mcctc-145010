// count.js (STARTER): counts one page load and handles the "Was this page useful?" form.
// Copy this file into your sitekit's static/ folder.
//
// The rule: send the page's address and, when asked, a yes or a no. Nothing else.
// No cookies. No localStorage. No identifier of any kind.
(function () {
  "use strict";

  // Opened straight from disk (file://) there is no server to count with.
  if (!location.protocol.startsWith("http")) {
    return;
  }

  // TODO step 6: send one page view to /api/hit.
  //   The body is JSON text: {"path": location.pathname}
  //   Use navigator.sendBeacon(url, text) so the visitor never waits for it.
  //   If sendBeacon does not exist, use fetch with method POST and keepalive: true,
  //   and catch any failure so the page carries on.

  // TODO step 9: find the form with id helpful-form and the paragraph with id helpful-status.
  //   On submit: stop the normal submission, read which button was pressed
  //   (event.submitter.value), and POST page and answer to the form's action as
  //   new URLSearchParams, with the header Accept: application/json.
  //   On success, disable both buttons and put a thank-you sentence in the status paragraph.
  //   On failure, say the answer could not be sent. Never throw.
})();
