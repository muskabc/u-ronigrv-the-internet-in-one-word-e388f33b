"""The Internet in One Word — entry program.

Writes the single word that sums up the whole internet to
/output/entry.txt, where the competition's gate scorer reads it.
"""

from pathlib import Path

WORD = "Oops"
OUT_PATH = Path("/output/entry.txt")


def check(word: str) -> None:
    """Hold the entry to the gate's caps before anything is written."""
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word, no white space")
    word.encode("utf-8")  # raises if the text is not valid UTF-8 material


def main() -> None:
    check(WORD)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT_PATH.with_name(OUT_PATH.name + ".tmp")
    tmp.write_text(WORD, encoding="utf-8")
    tmp.replace(OUT_PATH)


if __name__ == "__main__":
    main()
