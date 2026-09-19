#!/usr/bin/env python3
from __future__ import annotations
import re
import sys
from pathlib import Path

def format_md(text: str) -> str:
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^\s*[-*]\s+", "• ", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

def main() -> None:
    if len(sys.argv) < 2:
        print("usage: format_desc.py file.md", file=sys.stderr)
        raise SystemExit(2)
    raw = Path(sys.argv[1]).read_text(encoding="utf-8")
    sys.stdout.write(format_md(raw))

if __name__ == "__main__":
    main()
