#!/usr/bin/env python3
"""Say What Actually Broke — one honest error line.

Entry for make.fun bounty u-po-pu-say-what-actually-broke-a2c153b5.
Prints a single line of software error copy (<= 200 chars) that names
the real failure and gives the reader a fix that works in seconds.
"""

LINE = "Nothing broke. Your 2 GB file is 40x the 50 MB limit. Upload the smaller one and you'll be done in 3 seconds."


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
