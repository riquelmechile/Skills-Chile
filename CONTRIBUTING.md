# Contribuir a Skills Chile

Gracias por ayudar a construir una colección de skills útiles para Chile.

## Qué buscamos

Una nueva skill debe resolver un problema chileno concreto y ser reutilizable. Puede cubrir legislación, cumplimiento, trámites, procesos públicos, tributación, seguridad, ecommerce, salud, educación u otros dominios relevantes para Chile.

## Requisitos mínimos

1. Crear una carpeta en `skills/<nombre>/`.
2. Incluir `SKILL.md` con frontmatter YAML válido.
3. Usar un nombre en minúsculas, números y guiones.
4. Explicar claramente **qué hace** y **cuándo usarla**.
5. Mantener `SKILL.md` conciso; mover detalle a `references/` cuando corresponda.
6. Si contiene información jurídica o regulatoria, indicar fecha de última verificación y priorizar fuentes oficiales.
7. Separar hechos normativos de recomendaciones, heurísticas o buenas prácticas.
8. No incluir secretos, credenciales ni datos personales reales innecesarios.
9. Ejecutar `python scripts/validate_repo.py` antes de abrir un PR.

## Estructura recomendada

```text
skills/nombre-skill/
├─ SKILL.md
├─ references/
│  ├─ marco.md
│  └─ controles.md
├─ examples/          # opcional
└─ scripts/           # opcional
```

## Regla de calidad

Una skill no debe ser un PDF convertido a prompt. Debe transformar conocimiento en un flujo que el modelo pueda ejecutar:

`ALCANCE → REGLA → APLICABILIDAD → EVIDENCIA → RIESGO → ACCIÓN → VERIFICACIÓN`

## Pull request

Explica:

- problema chileno que resuelve;
- fuentes usadas;
- fecha de verificación;
- ejemplos probados;
- limitaciones conocidas.
