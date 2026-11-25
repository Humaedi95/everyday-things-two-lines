"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Line 1 explains the everyday thing to a 10-year-old in one vivid sentence
built on an analogy. Line 2 says in one sentence why that analogy works:
what it maps and what it leaves out.
"""

import os

LINE1 = (
    "A traffic jam is a school hallway at lunchtime, with hundreds of kids all "
    "trying to squeeze through one narrow door at once, so everyone moves slower "
    "than if they had walked in a single line.\n"
)
LINE2 = (
    "It maps how too many bodies in too little space slow everyone down, but it "
    "leaves out that cars cannot shrink, turn sideways, or slip through a side "
    "door the way kids can.\n"
)
ENTRY = LINE1 + LINE2


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
