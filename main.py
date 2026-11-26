#!/usr/bin/env python3
"""Funniest excuse for skipping a meeting — make.fun entry.

Writes the entry line byte-for-byte to /output/entry.txt.
"""

import os
import sys

ENTRY = "Sorry, I can't make it \u2014 the meeting could have been an email, and the email could have been a shrug."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(line: str) -> None:
    """Raise ValueError unless the line is a valid single-line entry."""
    if not line or not line.strip():
        raise ValueError("entry is blank")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    if "\r" in line or "\n" in line:
        raise ValueError("entry must be a single line")


def write_entry(line: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def verify_round_trip(line: str, path: str) -> None:
    """Read the file back and confirm it is byte-identical to the line."""
    with open(path, "rb") as f:
        raw = f.read()
    if raw != line.encode("utf-8"):
        raise ValueError("round-trip mismatch: file differs from entry")


def main() -> int:
    try:
        validate_entry(ENTRY)
        write_entry(ENTRY, OUTPUT_PATH)
        verify_round_trip(ENTRY, OUTPUT_PATH)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"entry: {len(ENTRY)} characters")
    print(f"wrote {OUTPUT_PATH}")
    print("verified: file reads back byte-identical")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
