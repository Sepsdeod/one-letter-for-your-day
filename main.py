#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one character, the letter G, to /output/entry.txt.

G stands for "googled my symptoms at 2 a.m." — the day in one letter:
a small, vivid, funny, true moment everyone recognises.

Why G: the letter fits its word exactly (G is the initial of "googled"),
and the moment is specific rather than a vague mood — a 2 a.m. search
bar, a symptom, a spiral. The output is a fixed constant, so every run
is deterministic and byte-identical.
"""

import os
import re

LETTER = "G"
OUTPUT_PATH = "/output/entry.txt"

# Guard: the entry must be exactly one character, a letter A-Z,
# with no newline, whitespace or control characters.
LETTER_RE = re.compile(r"^[A-Z]$")


def validate(letter):
    if not isinstance(letter, str) or not LETTER_RE.match(letter):
        raise ValueError("entry must be exactly one character A-Z")
    return letter


def main():
    letter = validate(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
