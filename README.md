# Skills Chile 🇨🇱

<p align="center">
  <img src="assets/skills-chile-hero.svg" alt="Skills Chile hero" width="100%" />
</p>

<p align="center">
  <strong>Repositorio de skills prácticas para Chile</strong><br>
  Skills listas para usar en GPT, Claude y otros asistentes con foco legal, operativo y documental.
</p>

<p align="center">
  <img alt="estado" src="https://img.shields.io/badge/estado-en%20construcci%C3%B3n-0a66c2">
  <img alt="skills" src="https://img.shields.io/badge/skills-1-0f766e">
  <img alt="pais" src="https://img.shields.io/badge/foco-Chile-dc2626">
  <img alt="licencia" src="https://img.shields.io/badge/licencia-MIT-111827">
</p>

---

## Qué es este repo

**Skills Chile** nace para reunir skills especializadas en problemáticas, normas, procesos y flujos reales de **Chile**.

La idea es simple:

- partir con una primera skill sólida;
- documentarla bien;
- hacerla fácil de reutilizar;
- e ir agregando más skills chilenas con el tiempo.

> **Primera skill del repositorio:** `proteccion-datos-chile`

---

## Primera skill: Protección de Datos Chile

La primera skill está enfocada en la **Ley 19.628** y en la reforma introducida por la **Ley 21.719**, que **entra en vigencia el 1 de diciembre de 2026** según la Biblioteca del Congreso Nacional / LeyChile.

Esta skill ayuda a:

- analizar cumplimiento legal y operativo;
- revisar políticas de privacidad;
- evaluar software, arquitectura, APIs y bases de datos;
- revisar encargados, transferencias internacionales e incidentes;
- distinguir entre **obligación legal**, **control recomendado** y **evidencia real**.

### Lo más importante

- **Hasta el 30 de noviembre de 2026**: la ley exigible sigue siendo la **Ley 19.628** vigente.
- **Desde el 1 de diciembre de 2026**: comienza a aplicar el nuevo régimen de la **Ley 21.719**.
- La skill evita errores comunes, como copiar reglas del GDPR automáticamente cuando no corresponden en Chile.

📌 Skill principal: [`skills/proteccion-datos-chile/SKILL.md`](skills/proteccion-datos-chile/SKILL.md)

---

## Roadmap

Este repo parte con una sola skill, pero está pensado para crecer.

Próximas líneas posibles:

- cumplimiento y gobierno digital en Chile;
- compras públicas / ChileCompra;
- documentación legal-operativa para pymes chilenas;
- tributación y procesos SII;
- ciberseguridad y cumplimiento local;
- protección al consumidor en Chile;
- skills sectoriales para salud, educación y ecommerce.

---

## Estructura del repo

```text
skills-chile/
├─ assets/
│  └─ skills-chile-hero.svg
├─ docs/
│  └─ guides/
│     ├─ agregar-skill-en-gpt.md
│     └─ agregar-skill-en-claude.md
├─ skills/
│  └─ proteccion-datos-chile/
│     ├─ SKILL.md
│     └─ references/
│        ├─ marco-y-vigencia.md
│        ├─ obligaciones-y-derechos.md
│        ├─ seguridad-incidentes-dpia-ia.md
│        └─ terceros-transferencias-sanciones.md
├─ LICENSE
└─ README.md
```

---

## Cómo usar una skill de este repo

La lógica es muy simple:

1. eliges la skill;
2. copias el contenido del `SKILL.md`;
3. lo agregas a tu GPT, Claude o proyecto;
4. si quieres más profundidad, sumas los archivos de `references/`.

Puedes usar la skill tal como está o adaptarla a tu empresa, cliente o proyecto.

---

## Cómo agregar una skill a GPT

Guía breve y simple: [`docs/guides/agregar-skill-en-gpt.md`](docs/guides/agregar-skill-en-gpt.md)

Resumen corto:

1. abre tu **GPT**, **Proyecto** o espacio de instrucciones;
2. crea una sección de instrucciones especializadas;
3. pega el contenido de `SKILL.md`;
4. si quieres más contexto, agrega también los archivos de referencia;
5. prueba con un caso real.

Ejemplo:

```text
Usa la skill proteccion-datos-chile para responder esta consulta.
Analiza el caso según su régimen temporal, obligaciones aplicables,
riesgos, evidencia faltante y acciones recomendadas.
```

---

## Cómo agregar una skill a Claude

Guía breve y simple: [`docs/guides/agregar-skill-en-claude.md`](docs/guides/agregar-skill-en-claude.md)

Resumen corto:

1. abre tu proyecto o espacio de trabajo en Claude;
2. crea una instrucción base o archivo de skill;
3. pega el `SKILL.md`;
4. agrega referencias si necesitas más profundidad;
5. prueba la skill con tareas concretas.

Ejemplo:

```text
Usa la skill proteccion-datos-chile.
Quiero una revisión rápida de esta política de privacidad chilena,
indicando brechas, artículos aplicables y prioridad de corrección.
```

---

## Filosofía del repo

Este repositorio busca que una skill sea:

- **clara**;
- **copiable**;
- **útil en la práctica**;
- **adaptable**;
- **entendible incluso para alguien con poco conocimiento técnico**.

No está pensado sólo para abogados o expertos. También apunta a:

- fundadores;
- pymes;
- equipos de producto;
- desarrolladores;
- consultores;
- personas que quieran empezar a usar IA con buenas instrucciones.

---

## Fuente legal principal de esta primera skill

La fecha de vigencia del nuevo régimen está verificada en la Biblioteca del Congreso Nacional / LeyChile:

- **Ley 21.719**: publicada el **13 de diciembre de 2024**;
- **entrada en vigencia**: **1 de diciembre de 2026**.

---

## Licencia

MIT.

---

## Nota final

Este repo parte con **una sola skill**, pero la idea es convertirlo en una colección real de **skills útiles para Chile**.

Si una skill ayuda a resolver un problema chileno real, entonces tiene espacio aquí.
