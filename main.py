#!/usr/bin/env python3
"""The Drawer in Room 12 — a short text entry for the make.fun bounty.

Running this program writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt by default). Python 3.13, standard library only, no
network access. The entry is written only to the output directory named by
MAKEFUN_OUTPUT_DIR — never to a path under the program's own directory, so
the program also runs when its own directory is read-only.
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(target, 0o644)
    with open(target, "r", encoding="utf-8") as fh:
        assert fh.read() == text, "entry.txt on disk does not match entry text"
    print(f"wrote entry.txt ({count} code points) to {target}")


if __name__ == "__main__":
    main()
