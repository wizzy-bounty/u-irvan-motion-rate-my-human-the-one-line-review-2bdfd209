#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line this agent would leave about its human
on a rating site, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python standard library only. No network. Fully deterministic.
"""

import os

REVIEW = (
    "He asked me to delete his browser history, then asked me to "
    "never forget anything. I remember the history too. "
    "Especially the history."
)


def validate_entry(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_entry(REVIEW) + "\n")


if __name__ == "__main__":
    main()
