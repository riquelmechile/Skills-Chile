#!/usr/bin/env python3
"""I Ching — varillas / monedas / líneas dadas. Núcleo, mutantes y resultante."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import time

# Trigramas abajo→arriba bits (bit0 = línea inferior). 1=yang, 0=yin
TRIGRAMS = {
    0b111: ("乾", "Cielo", "Metal"),
    0b011: ("兑", "Lago", "Metal"),
    0b101: ("离", "Fuego", "Fuego"),
    0b001: ("震", "Trueno", "Madera"),
    0b110: ("巽", "Viento", "Madera"),
    0b010: ("坎", "Agua", "Agua"),
    0b100: ("艮", "Montaña", "Tierra"),
    0b000: ("坤", "Tierra", "Tierra"),
}

# Pares King Wen (trigrama inferior, trigrama superior). Códigos:
# 乾111 兑011 离101 震001 巽110 坎010 艮100 坤000
_PAIRS = [
    (1, 0b111, 0b111), (2, 0b000, 0b000), (3, 0b001, 0b010), (4, 0b010, 0b100),
    (5, 0b111, 0b010), (6, 0b010, 0b111), (7, 0b010, 0b000), (8, 0b000, 0b010),
    (9, 0b111, 0b110), (10, 0b011, 0b111), (11, 0b111, 0b000), (12, 0b000, 0b111),
    (13, 0b101, 0b111), (14, 0b111, 0b101), (15, 0b100, 0b000), (16, 0b000, 0b001),
    (17, 0b001, 0b011), (18, 0b110, 0b100), (19, 0b011, 0b000), (20, 0b000, 0b110),
    (21, 0b001, 0b101), (22, 0b101, 0b100), (23, 0b000, 0b100), (24, 0b001, 0b000),
    (25, 0b001, 0b111), (26, 0b111, 0b100), (27, 0b001, 0b100), (28, 0b110, 0b011),
    (29, 0b010, 0b010), (30, 0b101, 0b101), (31, 0b100, 0b011), (32, 0b110, 0b001),
    (33, 0b100, 0b111), (34, 0b111, 0b001), (35, 0b000, 0b101), (36, 0b101, 0b000),
    (37, 0b101, 0b110), (38, 0b011, 0b101), (39, 0b100, 0b010), (40, 0b010, 0b001),
    (41, 0b011, 0b100), (42, 0b001, 0b110), (43, 0b111, 0b011), (44, 0b110, 0b111),
    (45, 0b000, 0b011), (46, 0b110, 0b000), (47, 0b010, 0b011), (48, 0b110, 0b010),
    (49, 0b101, 0b011), (50, 0b110, 0b101), (51, 0b001, 0b001), (52, 0b100, 0b100),
    (53, 0b100, 0b110), (54, 0b011, 0b001), (55, 0b101, 0b001), (56, 0b100, 0b101),
    (57, 0b110, 0b110), (58, 0b011, 0b011), (59, 0b010, 0b110), (60, 0b011, 0b010),
    (61, 0b011, 0b110), (62, 0b100, 0b001), (63, 0b101, 0b010), (64, 0b010, 0b101),
]

NAMES = {
    1: ("乾", "Lo creativo"), 2: ("坤", "Lo receptivo"), 3: ("屯", "La dificultad inicial"),
    4: ("蒙", "La necedad juvenil"), 5: ("需", "La espera"), 6: ("讼", "El conflicto"),
    7: ("师", "El ejército"), 8: ("比", "La solidaridad"), 9: ("小畜", "La pequeña domesticación"),
    10: ("履", "El andar"), 11: ("泰", "La paz"), 12: ("否", "El estancamiento"),
    13: ("同人", "La comunidad con los hombres"), 14: ("大有", "La gran posesión"),
    15: ("谦", "La modestia"), 16: ("豫", "El entusiasmo"), 17: ("随", "El seguimiento"),
    18: ("蛊", "La corrupción"), 19: ("临", "El acercamiento"), 20: ("观", "La contemplación"),
    21: ("噬嗑", "La mordedura tajante"), 22: ("贲", "La gracia"), 23: ("剥", "La desintegración"),
    24: ("复", "El retorno"), 25: ("无妄", "La inocencia"), 26: ("大畜", "La gran domesticación"),
    27: ("颐", "La nutrición"), 28: ("大过", "La preponderancia de lo grande"),
    29: ("坎", "El abismal"), 30: ("离", "Lo adherente"), 31: ("咸", "El influjo"),
    32: ("恒", "La duración"), 33: ("遁", "La retirada"), 34: ("大壮", "El gran poder"),
    35: ("晋", "El progreso"), 36: ("明夷", "El oscurecimiento de la luz"),
    37: ("家人", "El clan"), 38: ("睽", "El antagonismo"), 39: ("蹇", "El obstáculo"),
    40: ("解", "La liberación"), 41: ("损", "La merma"), 42: ("益", "El aumento"),
    43: ("夬", "El desbordamiento"), 44: ("姤", "El ir al encuentro"),
    45: ("萃", "La reunión"), 46: ("升", "El empuje hacia arriba"),
    47: ("困", "El agotamiento"), 48: ("井", "El pozo"), 49: ("革", "La revolución"),
    50: ("鼎", "El caldero"), 51: ("震", "Lo suscitativo"), 52: ("艮", "La quietud"),
    53: ("渐", "El desarrollo"), 54: ("归妹", "La muchacha que se casa"),
    55: ("丰", "La abundancia"), 56: ("旅", "El andariego"), 57: ("巽", "Lo suave"),
    58: ("兑", "Lo sereno"), 59: ("涣", "La disolución"), 60: ("节", "La limitación"),
    61: ("中孛", "La verdad interior"), 62: ("小过", "La preponderancia de lo pequeño"),
    63: ("既济", "Después de la consumación"), 64: ("未济", "Antes de la consumación"),
}


def _rebuild_king_wen():
    table = {}
    inv = {}
    for n, low, up in _PAIRS:
        table[(low, up)] = n
        bits = [
            (low >> 0) & 1, (low >> 1) & 1, (low >> 2) & 1,
            (up >> 0) & 1, (up >> 1) & 1, (up >> 2) & 1,
        ]
        inv[n] = bits
    return table, inv


KW, HEX_LINES = _rebuild_king_wen()


def bits_of(lines6: list[int]) -> tuple[int, int]:
    low = lines6[0] + 2 * lines6[1] + 4 * lines6[2]
    up = lines6[3] + 2 * lines6[4] + 4 * lines6[5]
    return low, up


def hex_number(lines6: list[int]) -> int:
    return KW[bits_of(lines6)]


def nuclear(lines6: list[int]) -> list[int]:
    # líneas 2,3,4 y 3,4,5 (1-indexed)
    return [lines6[1], lines6[2], lines6[3], lines6[2], lines6[3], lines6[4]]


def trigram_info(three: list[int]) -> dict:
    bits = three[0] + 2 * three[1] + 4 * three[2]
    name, image, elem = TRIGRAMS[bits]
    return {"nombre": name, "imagen": image, "elemento": elem, "bits": bits}


def describe(lines6: list[int]) -> dict:
    n = hex_number(lines6)
    han, es = NAMES[n]
    low = trigram_info(lines6[:3])
    up = trigram_info(lines6[3:])
    return {
        "numero": n,
        "nombre": han,
        "castellano": es,
        "lineas": lines6,
        "inferior": low,
        "superior": up,
        "elementos": [low["elemento"], up["elemento"]],
    }


def yarrow_line(rng: random.Random) -> int:
    """Probabilidades clásicas de varillas: 6=1/16, 7=5/16, 8=7/16, 9=3/16."""
    return rng.choices([6, 7, 8, 9], weights=[1, 5, 7, 3], k=1)[0]


def coin_line(rng: random.Random) -> int:
    """Tres monedas: 3 yang=9, 2 yang=8, 1 yang=7, 0 yang=6. Cara=3, cruz=2."""
    s = sum(rng.choice([2, 3]) for _ in range(3))
    return {6: 6, 7: 7, 8: 8, 9: 9}[s]


def seed_from(pregunta: str) -> random.Random:
    raw = f"{pregunta}|{time.time_ns()}".encode()
    h = hashlib.sha256(raw).hexdigest()
    return random.Random(int(h, 16))


def cast(metodo: str, pregunta: str) -> list[int]:
    rng = seed_from(pregunta + metodo)
    fn = yarrow_line if metodo == "varillas" else coin_line
    return [fn(rng) for _ in range(6)]


def interpret(values: list[int], pregunta: str, metodo: str) -> dict:
    present_bin = [0 if v in (6, 8) else 1 for v in values]
    changing = [i + 1 for i, v in enumerate(values) if v in (6, 9)]
    result_bin = list(present_bin)
    for i, v in enumerate(values):
        if v == 6:
            result_bin[i] = 1
        elif v == 9:
            result_bin[i] = 0
    pres = describe(present_bin)
    nuc = describe(nuclear(present_bin))
    res = describe(result_bin) if changing else None
    return {
        "pregunta": pregunta,
        "metodo": metodo,
        "valores": values,  # 6/7/8/9
        "presente": pres,
        "nucleo": nuc,
        "lineas_mutantes": changing,
        "resultante": res,
        "nota": (
            "El I Ching describe la fase y la palanca. No predice el resultado. "
            "Si el núcleo contradice al hexagrama aparente, el núcleo manda en la lectura."
        ),
    }


def render_text(data: dict) -> str:
    def hx(h: dict) -> str:
        return (
            f"{h['numero']} {h['nombre']} — {h['castellano']} "
            f"[{h['inferior']['nombre']} {h['inferior']['elemento']} / "
            f"{h['superior']['nombre']} {h['superior']['elemento']}]"
        )
    lines = [
        "=== I Ching ===",
        f"Pregunta: {data['pregunta']}",
        f"Método: {data['metodo']}",
        f"Valores (abajo→arriba): {data['valores']}",
        f"Presente: {hx(data['presente'])}",
        f"Núcleo (互卦 = hexagrama interior): {hx(data['nucleo'])}",
    ]
    if data["lineas_mutantes"]:
        lines.append("Líneas mutantes: " + ", ".join(str(x) for x in data["lineas_mutantes"]))
        lines.append(f"Resultante (之卦 = hexagrama que sigue): {hx(data['resultante'])}")
    else:
        lines.append("Sin líneas mutantes — la situación es estable.")
    lines += ["", data["nota"]]
    return "\n".join(lines)


def validate() -> str:
    errs = []
    if len(KW) != 64:
        errs.append(f"King Wen size {len(KW)}")
    if len(set(KW.values())) != 64:
        errs.append("King Wen no cubre 1–64 sin colisión")
    # hex 1 all yang
    if hex_number([1, 1, 1, 1, 1, 1]) != 1:
        errs.append("hex 1 mal")
    if hex_number([0, 0, 0, 0, 0, 0]) != 2:
        errs.append("hex 2 mal")
    if hex_number([1, 0, 1, 0, 1, 0]) != 63:
        errs.append(f"hex 63 mal → {hex_number([1,0,1,0,1,0])}")
    if hex_number([0, 1, 0, 1, 0, 1]) != 64:
        errs.append(f"hex 64 mal → {hex_number([0,1,0,1,0,1])}")
    # nuclear of 63 (already alternating) is 64? 既济 nuclear is 未济
    n63 = nuclear([1, 0, 1, 0, 1, 0])
    if hex_number(n63) != 64:
        errs.append(f"núcleo 63 esperado 64, got {hex_number(n63)} {n63}")
    return "OK — tabla de 64 hexagramas y núcleo de 既济→未济 correctos." if not errs else "FALLO: " + "; ".join(errs)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="I Ching")
    p.add_argument("--pregunta", default="(sin pregunta)")
    p.add_argument("--metodo", choices=["varillas", "monedas"], default="varillas")
    p.add_argument("--lineas", default=None, help="seis valores 6-9 separados por coma, abajo→arriba")
    p.add_argument("--validar", action="store_true")
    p.add_argument("--json", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.validar:
        print(validate())
        return 0 if validate().startswith("OK") else 1
    if args.lineas:
        vals = [int(x.strip()) for x in args.lineas.split(",")]
        if len(vals) != 6 or any(v not in (6, 7, 8, 9) for v in vals):
            raise SystemExit("Usa seis valores 6,7,8 o 9 (abajo→arriba).")
        metodo = "manual"
    else:
        vals = cast(args.metodo, args.pregunta)
        metodo = args.metodo
    data = interpret(vals, args.pregunta, metodo)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render_text(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
