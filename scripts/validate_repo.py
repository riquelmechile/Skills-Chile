#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        fail(f"{skill_dir.relative_to(ROOT)}: falta SKILL.md", errors)
        return

    text = skill_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    name = fm.get("name", "")
    description = fm.get("description", "")

    if not NAME_RE.fullmatch(name):
        fail(f"{skill_file.relative_to(ROOT)}: name inválido '{name}'", errors)
    if name != skill_dir.name:
        fail(f"{skill_file.relative_to(ROOT)}: name debe coincidir con el directorio", errors)
    if not description or len(description) > 1024:
        fail(f"{skill_file.relative_to(ROOT)}: description ausente o >1024 caracteres", errors)
    if len(text.splitlines()) > 500:
        fail(f"{skill_file.relative_to(ROOT)}: SKILL.md supera 500 líneas; usa referencias", errors)

    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (skill_dir / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            fail(f"{skill_file.relative_to(ROOT)}: enlace roto -> {target}", errors)


def validate_svg(svg: Path, errors: list[str]) -> None:
    text = svg.read_text(encoding="utf-8")
    lowered = text.lower()
    for token in ["<script", "<foreignobject", "javascript:", "data:image", "onclick=", "onload="]:
        if token in lowered:
            fail(f"{svg.relative_to(ROOT)}: contenido SVG no permitido '{token}'", errors)
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        fail(f"{svg.relative_to(ROOT)}: XML inválido: {exc}", errors)
        return
    if not root.attrib.get("viewBox"):
        fail(f"{svg.relative_to(ROOT)}: falta viewBox", errors)
    tags = {el.tag.split("}")[-1] for el in root.iter()}
    if "title" not in tags or "desc" not in tags:
        fail(f"{svg.relative_to(ROOT)}: requiere title y desc accesibles", errors)


def main() -> int:
    errors: list[str] = []
    if not SKILLS.exists():
        fail("falta directorio skills/", errors)
    else:
        for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            validate_skill(skill_dir, errors)

    for svg in sorted((ROOT / "assets").glob("*.svg")):
        validate_svg(svg, errors)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "01-DIC-2026" not in readme and "1 de diciembre de 2026" not in readme:
        fail("README.md: falta fecha de vigencia 01-DIC-2026", errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = sum(1 for p in SKILLS.iterdir() if p.is_dir())
    print(f"OK: {skill_count} skill(s) y SVGs validados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
