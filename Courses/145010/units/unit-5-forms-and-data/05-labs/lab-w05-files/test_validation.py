"""
test_validation.py · Lab W05-02 · the server's rules, tested

Run from this folder:
    python test_validation.py

Do not change this file. Change validation.py until every test passes.
Standard library only.
"""

import unittest

from validation import validate_signup

# Slot 1 has room for 1 more, slot 2 for 2 more, slot 3 is full.
OPEN_SLOTS = {1: 1, 2: 2, 3: 0}


class FakeForm:
    """Behaves like Flask's request.form for the two methods validation uses."""

    def __init__(self, fields, needs=()):
        self.fields = dict(fields)
        self.needs = list(needs)

    def get(self, name):
        return self.fields.get(name)

    def getlist(self, name):
        return list(self.needs) if name == "needs" else []


def good(**changes):
    """A sign-up that passes every rule, with any field replaced."""
    fields = {
        "performer_name": "Juniper Vale",
        "email": "juniper.vale@example.com",
        "act_type": "music",
        "slot": "2",
        "minutes": "6",
        "agree": "yes",
    }
    needs = changes.pop("needs", ("mic",))
    for key, value in changes.items():
        if value is None:
            fields.pop(key, None)
        else:
            fields[key] = value
    return FakeForm(fields, needs)


class TestAGoodSignup(unittest.TestCase):
    def test_no_errors(self):
        clean, errors = validate_signup(good(), OPEN_SLOTS)
        self.assertEqual(errors, {})

    def test_clean_values_are_typed_and_trimmed(self):
        clean, errors = validate_signup(good(performer_name="  Juniper Vale  ", minutes=" 6 "), OPEN_SLOTS)
        self.assertEqual(errors, {})
        self.assertEqual(clean["performer_name"], "Juniper Vale")
        self.assertEqual(clean["minutes"], 6)
        self.assertEqual(clean["slot"], 2)
        self.assertEqual(clean["needs"], ["mic"])

    def test_no_needs_is_fine(self):
        clean, errors = validate_signup(good(needs=()), OPEN_SLOTS)
        self.assertEqual(errors, {})
        self.assertEqual(clean["needs"], [])

    def test_boundaries_are_allowed(self):
        for form in (good(performer_name="Al"), good(performer_name="x" * 40),
                     good(minutes="1"), good(minutes="8"), good(slot="1")):
            with self.subTest(fields=form.fields):
                self.assertEqual(validate_signup(form, OPEN_SLOTS)[1], {})


class TestEachRule(unittest.TestCase):
    def assertErrorOn(self, form, field):
        clean, errors = validate_signup(form, OPEN_SLOTS)
        self.assertIn(field, errors, f"expected an error on {field}, got {errors}")
        self.assertEqual(list(errors), [field], f"expected only {field}, got {list(errors)}")
        self.assertTrue(errors[field].endswith("."), "a message is a full sentence")

    def test_name_missing(self):
        self.assertErrorOn(good(performer_name=None), "performer_name")

    def test_name_only_spaces(self):
        self.assertErrorOn(good(performer_name="   "), "performer_name")

    def test_name_too_short_and_too_long(self):
        self.assertErrorOn(good(performer_name="J"), "performer_name")
        self.assertErrorOn(good(performer_name="x" * 41), "performer_name")

    def test_email_missing_and_malformed(self):
        self.assertErrorOn(good(email=""), "email")
        self.assertErrorOn(good(email="juniper at example dot com"), "email")
        self.assertErrorOn(good(email="juniper@example"), "email")

    def test_act_type_not_offered(self):
        self.assertErrorOn(good(act_type="fire-juggling"), "act_type")
        self.assertErrorOn(good(act_type=None), "act_type")

    def test_slot_not_a_number_or_not_real(self):
        self.assertErrorOn(good(slot="3am"), "slot")
        self.assertErrorOn(good(slot="99"), "slot")
        self.assertErrorOn(good(slot=None), "slot")

    def test_slot_full(self):
        clean, errors = validate_signup(good(slot="3"), OPEN_SLOTS)
        self.assertIn("now full", errors["slot"])

    def test_minutes_out_of_range_or_not_whole(self):
        for bad in ("0", "9", "5.5", "five", "", "-3", "²"):
            with self.subTest(minutes=bad):
                self.assertErrorOn(good(minutes=bad), "minutes")

    def test_needs_not_offered_or_repeated(self):
        self.assertErrorOn(good(needs=("mic", "fog machine")), "needs")
        self.assertErrorOn(good(needs=("mic", "mic")), "needs")

    def test_agree_missing(self):
        self.assertErrorOn(good(agree=None), "agree")
        self.assertErrorOn(good(agree="no"), "agree")


class TestManyProblemsAtOnce(unittest.TestCase):
    def test_every_problem_is_reported(self):
        form = FakeForm({"performer_name": "", "email": "nope", "slot": "3am",
                         "minutes": "90"}, needs=("smoke",))
        clean, errors = validate_signup(form, OPEN_SLOTS)
        self.assertEqual(
            sorted(errors),
            ["act_type", "agree", "email", "minutes", "needs", "performer_name", "slot"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
