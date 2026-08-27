#!/usr/bin/env python3
"""BaZi loader. Exact source is split into repository-safe UTF-8 parts."""
from pathlib import Path

_base = Path(__file__).resolve().parent
_source = "".join((_base / f"bazi.py.part{i}.src").read_text(encoding="utf-8") for i in range(1, 6))
exec(compile(_source, str(Path(__file__)), "exec"), globals(), globals())
