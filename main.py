#!/usr/bin/env python3
"""Write one funny honest appliance error line to entry.txt.

The line is a washing machine's flat, put-upon report of an unbalanced
load: one sock has unionised with the drum, and the machine refuses to
spin until it resigns. The humour comes from the truth of the fault,
not from a pun bolted on. It stays in the machine's own voice throughout
-- a coded error, a named fault, then a deadpan refusal -- with no word
explaining the joke, so the surprise (a sock forming a union) lands
inside a fault the machine could plausibly report.
"""

import os

LINE = (
    "ERROR E07: Unbalanced load. One sock has unionised with "
    "the drum. I will not spin until it resigns."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
