"""Seventeen Syllables of Debugging.

Reads the haiku from haiku.txt, prints it, and writes it to
/output/entry.txt, where the make.fun gate scorer reads it.
The output directory can be overridden with the OUTPUT_DIR
environment variable (used for local testing only).
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    haiku = (HERE / "haiku.txt").read_text(encoding="utf-8")
    lines = haiku.strip().split("\n")
    # The gate scorer accepts UTF-8 text of 1 to 200 characters;
    # fail loudly here instead of shipping an invalid entry.
    assert len(lines) == 3, "haiku must have exactly three lines"
    assert 1 <= len(haiku) <= 200, "haiku must be 1 to 200 characters"
    print(haiku, end="")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(haiku, encoding="utf-8")


if __name__ == "__main__":
    main()
