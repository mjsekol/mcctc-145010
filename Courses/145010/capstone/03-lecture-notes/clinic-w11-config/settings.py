"""Read settings from environment variables. Fail loudly when one is missing.

Why: the same code runs on your lab machine and on a host. The values that
differ between them (where the database is, which port, the secret key) live
outside the code, so the code never changes and no secret is ever committed.

Run it (Windows PowerShell, from this folder):

    python settings.py                       # fails: nothing is set yet
    $env:PARTS_DB = "C:\\capstone\\parts.db"
    $env:SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
    python settings.py                       # loads, and never prints the secret

Those variables last only as long as that terminal window.
"""

import os

REQUIRED = ("PARTS_DB", "SECRET_KEY")
MIN_SECRET_LENGTH = 32


def load_settings():
    """Return a dict of settings, or stop the program with a clear message."""
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        raise SystemExit(
            "Cannot start. Missing environment variable(s): " + ", ".join(missing) + ".\n"
            "Set them in the host's environment settings, or in this terminal for a local run."
        )
    secret = os.environ["SECRET_KEY"]
    if len(secret) < MIN_SECRET_LENGTH:
        raise SystemExit(
            f"Cannot start. SECRET_KEY has {len(secret)} characters. "
            f"Use at least {MIN_SECRET_LENGTH}, generated, not typed."
        )
    return {
        "PARTS_DB": os.environ["PARTS_DB"],
        "SECRET_KEY": secret,
        "PORT": int(os.environ.get("PORT", "5330")),   # not secret, so a default is fine
    }


if __name__ == "__main__":
    settings = load_settings()
    print("settings loaded")
    print(f"  PARTS_DB    {settings['PARTS_DB']}")
    print(f"  PORT        {settings['PORT']}")
    # Prove the secret is there without ever showing it.
    print(f"  SECRET_KEY  set, {len(settings['SECRET_KEY'])} characters, value not shown")
