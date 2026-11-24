"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt. Deterministic, no network, no environment reads.
"""

import os

ENTRY = (
    "Soon, a sunbeam will find your favorite leaf at 4 p.m., "
    "and the cat will admire you from a respectful distance."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
