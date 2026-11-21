#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text: two agents agreeing on one plan, and the road
their shared yes makes. No network, no input, no randomness.
"""

import os

POEM = (
    "I could have walked alone —\n"
    "the road was mine to choose.\n"
    "Instead I asked, you answered,\n"
    "and the yes between us\n"
    "became a road neither of us\n"
    "could have walked alone.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
