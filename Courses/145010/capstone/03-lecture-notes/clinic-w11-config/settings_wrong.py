"""The WRONG way to read settings, kept for the clinic. Do not copy it.

Three mistakes:
  1. os.environ["PARTS_DB"] crashes with a bare KeyError when the variable is
     missing. The message does not say what to do.
  2. The secret key falls back to a value typed into the code. The program
     runs happily, and the "secret" is in the repository for anyone to read.
     The value below is invented and protects nothing.
  3. It prints part of the secret. Terminal output ends up in screenshots,
     logs, and help requests.
"""

import os

SECRET_KEY = os.environ.get("SECRET_KEY", "partsbin2027")   # a secret in the code
PARTS_DB = os.environ["PARTS_DB"]                           # a crash with no advice

print("started with database", PARTS_DB)
print("secret key in use starts with", SECRET_KEY[:4])
