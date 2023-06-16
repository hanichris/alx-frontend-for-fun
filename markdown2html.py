#!/usr/bin/python3
"""Markdown to HTML converter."""
from pathlib import Path
import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) != 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    files = sys.argv[1], sys.argv[2]
    path = Path(files[0])
    if not path.is_file():
        sys.stderr.write(f"Missing {files[0]}\n")
        sys.exit(1)
