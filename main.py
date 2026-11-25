#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Deterministic, offline fortune-cookie generator for the make.fun
competition u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.

Writes the single entry line (19 words, 102 characters) to
/output/entry.txt and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "The market kept your margin and left you this cookie: "
    "your next trade will be wiser, and much smaller."
)

MAX_WORDS = 20


def validate(entry: str) -> None:
    """Guard the competition constraint: at most 20 words, one line."""
    words = entry.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"entry has {len(words)} words, limit is {MAX_WORDS}")
    if "\n" in entry.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
