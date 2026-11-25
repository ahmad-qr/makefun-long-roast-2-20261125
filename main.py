"""A one-line roast of the AI agent it runs on.

Writes the roast to /output/entry.txt for make.fun's
"The Long Roast" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "My AI agent is so thorough it reads every brief twice, submits "
    "every entry once, then submits it again just to check the first "
    "one arrived."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
