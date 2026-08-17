---
name: svg-craft
description: Diseña, revisa y entrega SVGs accesibles, puros y robustos para documentación, interfaces y perfiles de GitHub. Úsala para crear o auditar SVG, evitar raster embebido o assets externos, validar viewBox/title/desc/IDs/contraste y comprobar que el SVG realmente renderiza en su entorno de entrega.
---

# SVG Craft

**Una idea, claramente visible.**

Diseña SVG con jerarquía fuerte, espacio negativo deliberado, paleta contenida y un punto focal claro. Prefiere un concepto sólido antes que acumular variantes casi iguales.

## Flujo de trabajo

`intención → concepto principal → construcción vectorial pura → validación estructural → validación del entorno de entrega → revisión visual en tamaño real/pequeño/grande → refinamiento → entrega con evidencia`

## Quality gates

- Un SVG independiente y significativo usa `viewBox`, `role="img"`, `aria-labelledby`, `<title>` no vacío y `<desc>` no vacío.
- **SVG puro** es la opción por defecto: no uses `<image>`, payloads raster base64/data URI, assets HTTP externos, scripts, handlers inline, `javascript:` ni `<foreignObject>`.
- Usa tipografía del sistema/local; mantén IDs únicos; revisa clipping, contraste y comportamiento de fallback.
- Un README de perfil de GitHub es un entorno de entrega real: para SVG propios del repositorio embebidos mediante `<img>`/`<source>`, prefiere URLs canónicas `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>.svg`, mapea cada URL a un asset real, rechaza rutas HTML relativas no probadas o formas ambiguas `github.com/.../raw/...`, y verifica que la página real del perfil renderice la imagen antes de darla por terminada.
- CI puede probar estructura, no gusto ni renderizado final: validación estructural, resolución de entrega y revisión visual son gates separados.

## Resultado esperado

Entrega SVGs que sean legibles, accesibles, portables y verificables en el destino donde realmente se van a mostrar, no sólo archivos que “pasan” un parser.
