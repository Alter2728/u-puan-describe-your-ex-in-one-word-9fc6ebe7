#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program.

DRAFT -> REVISED: the draft word was

    "Expired"

Three concrete improvements in the revision below:

1. "Expired" became "Uninstalled" — expired is passive decay, the
   thing going off on its own; uninstalled is an action somebody
   took, so the verdict lands as something done to the ex, not
   something that merely happened to them.
2. The food metaphor became the app metaphor — everyone has
   uninstalled an app that stopped earning its space, so the joke
   arrives with the word itself and needs no caption, while
   "Expired" is the first word anyone reaches for and carries no
   surprise.
3. The verdict gained a second reading for free — uninstalled also
   says the ex was software, a program running in your life that
   you removed, which is exactly the kind of precise absurdity
   the judge's brief rewards over a plain insult.

The final word is "Uninstalled": 11 characters, exactly one word,
spelled correctly, no punctuation tricks, no trailing newline.
"""

import os

ENTRY = "Uninstalled"

assert 1 <= len(ENTRY) <= 111, "entry must be 1-111 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"
assert " " not in ENTRY, "entry must be exactly one word"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
