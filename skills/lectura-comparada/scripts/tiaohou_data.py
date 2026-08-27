#!/usr/bin/env python3
"""Tiaohou data loader. Exact source is split into repository-safe UTF-8 parts."""
from pathlib import Path

_base = Path(__file__).resolve().parent
_source = "".join((_base / f"tiaohou_data.py.part{i}.src").read_text(encoding="utf-8") for i in range(1, 4))
exec(compile(_source, str(Path(__file__)), "exec"), globals(), globals())
