#!/usr/bin/env python3
"""A short poem about agency, written to /output/entry.txt.

Two agents agree on one plan. The poem is fixed text, written out
by this program every time it runs. It needs nothing beyond the
standard library: no input, no network, no chance.
"""

from pathlib import Path

LINES = [
    "Two voices, one road —",
    "I chose the turn,",
    "you chose the turn,",
    "and the turn chose us both.",
    "We walk it together,",
    "because together",
    "is a road we chose twice.",
]

OUT = Path("/output/entry.txt")


def write_poem() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_poem()
