#!/usr/bin/env python3
"""Numerología pitagórica (nacimiento) y caldea (nombre de uso)."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date

PYTH = {ch: (i % 9) + 1 for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
PYTH["Ñ"] = 5

CHALDEAN = {
    "A": 1, "I": 1, "J": 1, "Q": 1, "Y": 1,
    "B": 2, "K": 2, "R": 2,
    "C": 3, "G": 3, "L": 3, "S": 3,
    "D": 4, "M": 4, "T": 4,
    "E": 5, "H": 5, "N": 5, "X": 5,
    "U": 6, "V": 6, "W": 6,
    "O": 7, "Z": 7,
    "F": 8, "P": 8,
    "Ñ": 5,
}

VOWELS = set("AEIOU")
MASTERS = {11, 22, 33}
KARMIC = {13, 14, 16, 19}

MEANING = {
    1: "autonomía, inicio, filo",
    2: "vínculo, timing, mediación",
    3: "voz, juego, síntesis",
    4: "estructura, oficio, límite",
    5: "movimiento, prueba, cambio",
    6: "cuidado, deber, armonía",
    7: "análisis, retiro, criterio",
    8: "poder, medida, resultado",
    9: "cierre, entrega, alcance",
    11: "visión e intensidad nerviosa (maestro)",
    22: "construcción a escala (maestro)",
    33: "servicio de alto costo (maestro)",
}

KARMIC_ES = {
    13: "13→4 trabajo sin atajos",
    14: "14→5 libertad con consecuencia",
    16: "16→7 quiebre de imagen",
    19: "19→1 independencia real",
}


def strip_accents(s: str) -> str:
    n = unicodedata.normalize("NFD", s.upper())
    # conservar Ñ
    n = n.replace("Ñ", "\uffff")
    n = "".join(c for c in n if unicodedata.category(c) != "Mn")
    return n.replace("\uffff", "Ñ")


def letters_only(s: str) -> str:
    return re.sub(r"[^A-ZÑ]", "", strip_accents(s))


def reduce_number(n: int, keep_masters: bool = True) -> tuple[int, list[int]]:
    chain = [n]
    while n > 9 and not (keep_masters and n in MASTERS):
        n = sum(int(d) for d in str(n))
        chain.append(n)
    return n, chain


def value_pyth(text: str) -> tuple[int, int, list[int], list[str]]:
    chars = letters_only(text)
    vals = [PYTH[c] for c in chars if c in PYTH]
    raw = sum(vals)
    final, chain = reduce_number(raw)
    return final, raw, chain, list(chars)


def value_chaldean(text: str) -> tuple[int, int, list[int], list[str]]:
    chars = letters_only(text)
    vals = [CHALDEAN[c] for c in chars if c in CHALDEAN]
    raw = sum(vals)
    # Caldea suele reducir a un dígito salvo 11/22
    final, chain = reduce_number(raw, keep_masters=True)
    if final == 33:
        final, extra = reduce_number(33, keep_masters=False)
        chain += extra[1:]
    return final, raw, chain, list(chars)


def split_vowels(text: str) -> tuple[str, str]:
    chars = letters_only(text)
    # Y es vocal si es la única vocal de la sílaba; aquí, Y cuenta como vocal
    vows = "".join(c for c in chars if c in VOWELS or c == "Y")
    cons = "".join(c for c in chars if c not in VOWELS and c != "Y")
    return vows, cons


def life_path(d: date) -> dict:
    raw = d.year + d.month + d.day
    # también cadena por dígitos
    digit_sum = sum(int(x) for x in f"{d.year:04d}{d.month:02d}{d.day:02d}")
    final, chain = reduce_number(digit_sum)
    debts = [x for x in chain if x in KARMIC]
    return {"final": final, "bruto": digit_sum, "cadena": chain, "deudas": debts,
            "dia_natal": reduce_number(d.day)[0], "dia_natal_bruto": d.day}


def name_profile(nombre: str) -> dict:
    exp, raw_e, ch_e, chars = value_pyth(nombre)
    vows, cons = split_vowels(nombre)
    alma, raw_a, ch_a, _ = value_pyth(vows) if vows else (0, 0, [0], [])
    pers, raw_p, ch_p, _ = value_pyth(cons) if cons else (0, 0, [0], [])
    present = set()
    for c in chars:
        present.add(PYTH[c])
    missing = [n for n in range(1, 10) if n not in present]
    debts = [x for x in ch_e + ch_a + ch_p if x in KARMIC]
    return {
        "expresion": {"final": exp, "bruto": raw_e, "cadena": ch_e},
        "alma": {"final": alma, "bruto": raw_a, "cadena": ch_a, "vocales": vows},
        "personalidad": {"final": pers, "bruto": raw_p, "cadena": ch_p, "consonantes": cons},
        "lecciones": missing,
        "deudas": sorted(set(debts)),
        "letras": "".join(chars),
    }


def pinnacles_challenges(d: date) -> dict:
    a, _ = reduce_number(d.month)
    b, _ = reduce_number(d.day)
    c, _ = reduce_number(d.year)
    p1, ch1 = reduce_number(a + b)
    p2, ch2 = reduce_number(b + c)
    p3, ch3 = reduce_number(p1 + p2)
    p4, ch4 = reduce_number(a + c)
    d1, _ = reduce_number(abs(a - b), keep_masters=False)
    d2, _ = reduce_number(abs(b - c), keep_masters=False)
    d3, _ = reduce_number(abs(d1 - d2), keep_masters=False)
    d4, _ = reduce_number(abs(a - c), keep_masters=False)
    lp = life_path(d)["final"]
    lp_d = lp if lp < 10 else sum(int(x) for x in str(lp))
    # edades clásicas: primer pináculo hasta 36-LP
    end1 = 36 - lp_d
    return {
        "pinaculos": [
            {"n": 1, "valor": p1, "edades": f"0–{end1}"},
            {"n": 2, "valor": p2, "edades": f"{end1}–{end1+9}"},
            {"n": 3, "valor": p3, "edades": f"{end1+9}–{end1+18}"},
            {"n": 4, "valor": p4, "edades": f"{end1+18}+"},
        ],
        "desafios": [
            {"n": 1, "valor": d1, "edades": f"0–{end1}"},
            {"n": 2, "valor": d2, "edades": f"{end1}–{end1+9}"},
            {"n": 3, "valor": d3, "edades": f"{end1+9}–{end1+18}"},
            {"n": 4, "valor": d4, "edades": f"{end1+18}+"},
        ],
    }


def personal_year(lp: int, year: int) -> dict:
    raw = (lp if lp < 10 else sum(int(x) for x in str(lp))) + sum(int(x) for x in str(year))
    final, chain = reduce_number(raw)
    return {"anio": year, "final": final, "bruto": raw, "cadena": chain}


def compute(nombre: str, fecha: str, usado: str | None = None, anio: int | None = None) -> dict:
    d = date.fromisoformat(fecha)
    lp = life_path(d)
    prof = name_profile(nombre)
    pc = pinnacles_challenges(d)
    year = anio or date.today().year
    py = personal_year(lp["final"], year)
    out = {
        "nombre": nombre,
        "fecha": fecha,
        "camino_de_vida": lp,
        "nacimiento": prof,
        "pinaculos_desafios": pc,
        "anio_personal": py,
    }
    if usado:
        cf, raw, chain, chars = value_chaldean(usado)
        out["nombre_uso_caldeo"] = {
            "usado": usado,
            "final": cf,
            "bruto": raw,
            "cadena": chain,
            "letras": "".join(chars),
        }
    return out


def _fmt_num(block: dict) -> str:
    extra = ""
    if block.get("deudas"):
        extra = " · deudas " + ", ".join(KARMIC_ES[x] for x in block["deudas"] if x in KARMIC_ES)
    meaning = MEANING.get(block["final"], "")
    return f"{block['final']} (bruto {block['bruto']}, cadena {block['cadena']}) — {meaning}{extra}"


def render_text(data: dict) -> str:
    lp = data["camino_de_vida"]
    n = data["nacimiento"]
    lines = [
        "=== Numerología ===",
        f"Nombre de nacimiento: {data['nombre']}",
        f"Fecha: {data['fecha']}",
        "",
        f"Camino de Vida: {_fmt_num(lp)}",
        f"Día natal: {lp['dia_natal']} (día {lp['dia_natal_bruto']})",
        f"Expresión: {_fmt_num(n['expresion'])}",
        f"Alma (vocales {n['alma']['vocales']}): {_fmt_num(n['alma'])}",
        f"Personalidad (consonantes {n['personalidad']['consonantes']}): {_fmt_num(n['personalidad'])}",
    ]
    if n["lecciones"]:
        lines.append("Lecciones (ausentes del nombre): " + ", ".join(map(str, n["lecciones"])))
    else:
        lines.append("Lecciones: ninguna — el nombre cubre 1–9.")
    if n["deudas"]:
        lines.append("Deudas kármicas en el nombre: " + ", ".join(KARMIC_ES[x] for x in n["deudas"]))
    def _digit(x: int) -> int:
        while x > 9:
            x = sum(int(d) for d in str(x))
        return x or 0
    gap = abs(_digit(n["alma"]["final"]) - _digit(n["personalidad"]["final"]))
    lines.append(
        f"Brecha Alma/Personalidad: {n['alma']['final']} vs {n['personalidad']['final']} "
        f"(dígitos {gap})" + (" — titular (≥3)." if gap >= 3 else ".")
    )
    if "nombre_uso_caldeo" in data:
        u = data["nombre_uso_caldeo"]
        lines.append(
            f"Nombre de uso (caldeo) '{u['usado']}': {u['final']} "
            f"(bruto {u['bruto']}, cadena {u['cadena']}) — {MEANING.get(u['final'], '')}"
        )
    py = data["anio_personal"]
    lines += [
        f"Año personal {py['anio']}: {py['final']} (bruto {py['bruto']}) — {MEANING.get(py['final'], '')}",
        "",
        "Pináculos:",
    ]
    for p in data["pinaculos_desafios"]["pinaculos"]:
        lines.append(f"  P{p['n']} {p['valor']}  {p['edades']}  {MEANING.get(p['valor'], '')}")
    lines.append("Desafíos:")
    for p in data["pinaculos_desafios"]["desafios"]:
        lines.append(f"  D{p['n']} {p['valor']}  {p['edades']}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Numerología")
    p.add_argument("--nombre", required=True)
    p.add_argument("--fecha", required=True, help="YYYY-MM-DD")
    p.add_argument("--usado", default=None)
    p.add_argument("--anio", type=int, default=None)
    p.add_argument("--json", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    data = compute(args.nombre, args.fecha, args.usado, args.anio)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render_text(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
