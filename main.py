#!/usr/bin/env python3
"""The One-Line Laugh -- entry generator.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt, deterministically, then reads it back and validates it
against the competition gate before exiting.

Run: python3 main.py
"""

import hashlib
import os
import sys

LINE = "I asked AI to write my dating profile and now even my own bio swiped left on me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_text(text):
    """Check entry text against the gate. Returns the stripped line.

    Raises ValueError when the text fails: empty/whitespace-only, over
    200 characters, more than one line, or not exactly one sentence.
    """
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    body = text.strip()
    if not body:
        raise ValueError("entry is empty or only whitespace")
    if len(body) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(body), MAX_CHARS)
        )
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
    if "\t" in body:
        raise ValueError("entry contains a tab character")
    terminators = sum(body.count(c) for c in ".!?")
    if terminators != 1 or not body.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")
    return body


def main():
    body = validate_text(LINE)
    data = (body + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Self-validation guard: read the file back and re-check it.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("guard failed: bytes on disk differ from bytes written")
    text = written.decode("utf-8")  # strict: raises on invalid UTF-8
    # The gate counts the file as submitted, newline included, so check
    # the raw length too, not just the stripped line.
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "guard failed: file is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\t" in text:
        raise SystemExit("guard failed: entry contains a tab character")
    validate_text(text)
    digest = hashlib.sha256(written).hexdigest()
    print("entry: %s" % body)
    print("characters: %d" % len(body))
    print("bytes: %d" % len(written))
    print("sha256: %s" % digest)
    print("wrote %s" % OUTPUT_PATH)


if __name__ == "__main__":
    main()
