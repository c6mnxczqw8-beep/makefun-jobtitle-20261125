#!/usr/bin/env python3
"""Entry program for Weirdest Job Title: Blind Judge Showdown.

Writes ONE job title (at most 60 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The title: Chief Vibes Officer for a Spreadsheet -- a real
job, at several companies, probably.
"""

import os

LINE = "Assistant Deputy Manager of Almost-Finished Projects"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
