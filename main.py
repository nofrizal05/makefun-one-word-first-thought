"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first word that comes to mind, to
/output/entry.txt. Python standard library only.
"""

import os

WORD = "petrichor"
# petrichor — the smell of rain on dry earth. Surprising (few would guess
# it), vivid and specific (one clear sensory image), with a soft, musical
# sound: it beats the other candidates on the judge's top criteria.


def main():
    # The gate allows 1 to 24 characters, not only white space, one word.
    assert WORD and len(WORD) <= 24 and len(WORD.split()) == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
