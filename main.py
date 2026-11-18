#!/usr/bin/env python3
"""make.fun news-image-20261117 entry, v2.

The repository holds the finished poster as entry.png: a hero panel
for the Crimean Bridge and Kyiv lead story, five more stories of
Tuesday 17 November 2026 below it, and a ticker. This program copies
those exact bytes to the output directory, so both grader runs
produce the same image. Outside the grader, MAKEFUN_OUTPUT_DIR
stands in for /output.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def checked_bytes() -> bytes:
    """Return the poster bytes, refusing anything that is not a
    complete PNG within the competition's 1 MiB size cap."""
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("entry.png does not start with a PNG signature")
    if len(data) > MAX_BYTES:
        raise ValueError("entry.png is larger than 1 MiB")
    if not data.endswith(b"IEND\xaeB`\x82"):
        raise ValueError("entry.png is truncated: no IEND chunk at its end")
    return data


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(checked_bytes())
    if target.read_bytes() != SOURCE.read_bytes():
        raise IOError("written entry.png does not match the shipped poster")


if __name__ == "__main__":
    main()
