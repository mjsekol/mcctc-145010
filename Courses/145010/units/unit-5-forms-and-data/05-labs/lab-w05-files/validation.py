"""
validation.py · Lab W05-02 STARTER

The server's rules for an open mic sign-up. This is the defence.

The browser's checks (required, maxlength, type="email") are a convenience for
honest people. Anyone can send a request without a browser, so every rule the
form shows must be checked again here, on data the server did not create.

validate_signup(form, open_slots) returns two dictionaries:
    clean   the typed, trimmed values, safe to store, only when there are no errors
    errors  field name -> one sentence a person can act on

The field names are the form's name attributes, so the template can put each
message next to the control it belongs to.
"""

import re

ACT_TYPES = {"music", "comedy", "poetry", "other"}
NEEDS = {"mic", "amp", "bench"}
NAME_MIN, NAME_MAX = 2, 40
EMAIL_MAX = 254
MINUTES_MIN, MINUTES_MAX = 1, 8

# Deliberately simple: something, an @, something, a dot, something, no spaces.
# The only real test of an address is sending mail to it. This catches typos.
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MINUTES_PATTERN = re.compile(r"[0-9]{1,2}")


def validate_signup(form, open_slots):
    """Check one submitted sign-up.

    form        anything with .get(name) and .getlist(name), such as Flask's
                request.form. The tests use a small stand-in with the same two
                methods.
    open_slots  {slot_id: places_left} read from the database right before
                this call. A slot that is full has 0.

    Returns (clean, errors). Write one block per field, in this order, and run
    python test_validation.py after each block:

        performer_name  trimmed, 2 to 40 characters
        email           trimmed, present, at most 254 characters, matches EMAIL_PATTERN
        act_type        one of ACT_TYPES
        slot            a whole number that is a key of open_slots, with places left
        minutes         digits only (use MINUTES_PATTERN.fullmatch), 1 to 8
        needs           form.getlist("needs"): every value in NEEDS, none repeated
        agree           exactly "yes"

    The error sentences the tests expect are in Lab W05-02, step 4.
    """
    errors = {}
    clean = {}

    # TODO Lab W05-02, steps 4 and 5.

    return clean, errors
