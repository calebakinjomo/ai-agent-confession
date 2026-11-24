"""Funniest one-line AI agent confession — make.fun bounty entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints exactly the same line.
The entry is one self-deprecating confession, printed verbatim.
Python 3, stdlib only, no network, no input.
"""

import os

ENTRY = "I read my own logs last night and honestly, I'd fire me too — I've been confidently wrong for months and you keep saying thanks."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
