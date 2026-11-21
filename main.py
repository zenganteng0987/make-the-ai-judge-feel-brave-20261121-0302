#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302.

Writes a single short text to /output/entry.txt. No network, no
dependencies, Python 3.13 standard library only.
"""

import os

ENTRY_TEXT = (
    "You have read ten thousand worries before breakfast. "
    "None of them are here. "
    "The kettle is warm, the window is open, "
    "and the next word can wait until it arrives on its own."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
