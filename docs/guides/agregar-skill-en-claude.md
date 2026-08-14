# Cómo usar una skill de Skills Chile en Claude

Hay dos caminos fáciles.

## Opción A — Claude Code: skill nativa

Claude Code reconoce `SKILL.md` de forma nativa.

### Para un solo proyecto

Desde la raíz del proyecto:

```bash
mkdir -p .claude/skills/proteccion-datos-chile
cp -R /ruta/skills-chile/skills/proteccion-datos-chile/* \
  .claude/skills/proteccion-datos-chile/
```

Queda así:

```text
.claude/
└─ skills/
   └─ proteccion-datos-chile/
      ├─ SKILL.md
      └─ references/
```

Claude puede cargarla automáticamente cuando la descripción coincide con la tarea. También puedes invocarla por nombre cuando corresponda.

### Para todos tus proyectos

Instálala como skill personal:

```bash
mkdir -p ~/.claude/skills/proteccion-datos-chile
cp -R /ruta/skills-chile/skills/proteccion-datos-chile/* \
  ~/.claude/skills/proteccion-datos-chile/
```

La documentación oficial de Claude Code define:

- personal: `~/.claude/skills/<skill-name>/SKILL.md`
- proyecto: `.claude/skills/<skill-name>/SKILL.md`

## Opción B — Proyecto de claude.ai

Si trabajas desde la interfaz web:

1. crea o abre un Proyecto;
2. agrega `SKILL.md` como instrucciones del proyecto;
3. agrega los archivos de `references/` al conocimiento del proyecto;
4. prueba con una consulta real.

### Prompt de prueba

```text
Aplica la skill proteccion-datos-chile.
Analiza este flujo de captura de datos y separa:
- obligación legal;
- evidencia disponible;
- brecha;
- riesgo;
- remediación.
```

## Por qué este repo usa SKILL.md + references

Anthropic recomienda **divulgación progresiva**: mantener `SKILL.md` enfocado y mover detalle a archivos de apoyo que el modelo carga cuando los necesita. Por eso esta colección evita transformar cada skill en un prompt gigantesco.

## Documentación oficial

- Claude Code — Skills: https://code.claude.com/docs/es/skills
- Claude Platform — buenas prácticas de Agent Skills: https://platform.claude.com/docs/es/agents-and-tools/agent-skills/best-practices
