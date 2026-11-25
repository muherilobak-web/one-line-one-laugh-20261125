#!/usr/bin/env python3
"""One Line, One Laugh -- entry program.

Concept: compare two things that should never share a sentence -- a trivial
household object and a grand life ambition -- and force them together with a
single shared routine, so the jump in scale itself becomes the joke.

Validation matters here because the bounty is judged on exactly one line:
a stray newline, invisible control character, or padding space would break
the "one line" contract and cost the entry before the joke is even read.
"""

import os

ENTRY = "My houseplants and my dreams have the same care routine: water once, forget, apologize to the corpse."


def main():
    line = ENTRY

    # Validate: exactly one line, 1-200 characters, no control characters.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip check failed: entry.txt differs from validated line")

    print("wrote {} ({} characters)".format(out_path, len(line)))


if __name__ == "__main__":
    main()
