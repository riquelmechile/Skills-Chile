# Estándar de calidad de Skills Chile

## 1. Una skill debe ser ejecutable

Debe indicar cuándo se usa, qué pasos seguir, qué evidencia revisar y cómo entregar el resultado. Un resumen temático sin workflow no alcanza el estándar del repositorio.

## 2. Chile primero

En contenido regulatorio:

1. fuentes oficiales chilenas;
2. normativa sectorial;
3. jurisprudencia o criterios administrativos pertinentes;
4. marcos internacionales como apoyo, nunca como sustituto automático.

## 3. Vigencia explícita

Cuando una norma pueda cambiar, la skill debe incluir:

- fecha de última verificación;
- regla para revalidar actualidad;
- distinción entre vigencia actual, transición y futura exigibilidad.

## 4. Divulgación progresiva

Mantén `SKILL.md` enfocado. El detalle extenso va a archivos de referencia enlazados directamente desde el principal. Evita referencias profundamente anidadas.

## 5. Evidencia

En compliance, seguridad o auditoría, la skill debe distinguir:

- obligación;
- aplicabilidad;
- evidencia observada;
- brecha;
- riesgo;
- remediación;
- prueba de cierre.

## 6. Seguridad

No incluir secretos ni datos personales innecesarios. Los ejemplos deben ser ficticios o anonimizados.

## 7. Validación

Antes de un PR:

```bash
python scripts/validate_repo.py
```

El validador controla estructura básica, frontmatter, referencias y seguridad estructural de SVG.
