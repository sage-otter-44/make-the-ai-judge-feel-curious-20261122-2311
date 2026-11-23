#!/usr/bin/env python3
"""The Drawer in Room 12 — a short text entry for the make.fun bounty.

Running this program writes the entry text to /output/entry.txt
(and to ./output/entry.txt as a local check copy).
Python 3.13, standard library only, no network access.
"""

import os

TEXT = (
    "The cleaner at the Hotel Miramar found a drawer in room 12 not on "
    "any floor plan. Inside: a brass key, a ticket to a town that closed "
    "in 1974, and a photo of herself on a beach she never saw. The ticket "
    "is stamped for tomorrow — who bought it, and why is the drawer open "
    "again?"
)


def main() -> None:
    text = TEXT
    count = len(text)
    assert 250 <= count <= 280, f"entry is {count} code points, must be 250-280"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # must be valid UTF-8
    for target in ("/output/entry.txt", os.path.join(os.path.dirname(__file__), "output", "entry.txt")):
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(f"wrote entry.txt ({count} code points)")


if __name__ == "__main__":
    main()
