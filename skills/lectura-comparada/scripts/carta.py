#!/usr/bin/env python3
"""Puente BaZi + numerología en una sola salida."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bazi  # noqa: E402
import numerologia  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Carta integrada BaZi + numerología")
    p.add_argument("--nombre", required=True)
    p.add_argument("--usado", default=None)
    p.add_argument("--fecha", required=True)
    p.add_argument("--hora", default=None)
    p.add_argument("--sexo", required=True, choices=["M", "F", "m", "f"])
    p.add_argument("--tz", default="America/Santiago")
    p.add_argument("--lon", type=float, default=-70.65)
    p.add_argument("--sin-hora", action="store_true")
    p.add_argument("--anio", type=int, default=None)
    p.add_argument("--json", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    chart = bazi.compute(args.fecha, args.hora, args.sexo, args.tz, args.lon, args.sin_hora)
    nums = numerologia.compute(args.nombre, args.fecha, args.usado, args.anio)
    if args.json:
        print(json.dumps({"bazi": chart.as_dict(), "numerologia": nums},
                         ensure_ascii=False, indent=2))
        return 0
    print(bazi.render_text(chart))
    print()
    print(numerologia.render_text(nums))
    print()
    print("=== Puente (cruce mínimo) ===")
    dm = chart.day_master
    lp = nums["camino_de_vida"]["final"]
    exp = nums["nacimiento"]["expresion"]["final"]
    scarce = min(chart.elements, key=chart.elements.get)
    top = max(chart.elements, key=chart.elements.get)
    from glosario import t as zh
    print(f"Amo del Día {zh(dm['tallo'])} {dm['elemento']} {dm['polaridad']} · "
          f"elemento alto {top} {chart.elements[top]}% · escaso {scarce} {chart.elements[scarce]}%")
    print(f"Camino {lp} · Expresión {exp} · "
          f"Alma {nums['nacimiento']['alma']['final']} · "
          f"Personalidad {nums['nacimiento']['personalidad']['final']}")
    print("Usar como aritmética. El eje de la lectura sale del cruce con la mano, no de este bloque.")
    print()
    print("=== Párrafo yangsheng (pegar en el informe, sin adornar) ===")
    print(chart.tiaohou["parrafo"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
