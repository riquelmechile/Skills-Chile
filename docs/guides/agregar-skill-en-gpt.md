# Cómo usar una skill de Skills Chile en ChatGPT

No necesitas programar.

> En ChatGPT, la forma más simple de reutilizar una skill hoy es mediante **instrucciones de un Proyecto** o las **Instructions de un GPT personalizado**. Los archivos de referencia pueden subirse como archivos del proyecto o como Knowledge del GPT.

## Opción A — Proyecto de ChatGPT (la más fácil)

Los Proyectos permiten agrupar chats, archivos e instrucciones personalizadas.

1. Crea un **Nuevo proyecto** en ChatGPT.
2. Abre el menú `⋯` del proyecto → **Configuración del proyecto**.
3. Copia el contenido de `SKILL.md` y pégalo en las instrucciones del proyecto.
4. Sube los archivos de `references/` como fuentes del proyecto.
5. Abre un chat dentro del proyecto y prueba una tarea real.

### Prompt de prueba

```text
Usa las instrucciones de protección de datos de este proyecto.
Revisa esta política de privacidad para Chile y entrega:
1. régimen temporal aplicable;
2. brechas;
3. evidencia faltante;
4. acciones priorizadas.
```

## Opción B — GPT personalizado

La creación y edición de GPTs se realiza en la experiencia web y requiere un plan que permita crear GPTs.

1. Abre el editor de GPTs en ChatGPT web.
2. En **Instructions**, pega el contenido de `SKILL.md`.
3. En **Knowledge**, sube los archivos de `references/`.
4. Agrega 2 o 3 iniciadores de conversación.
5. Prueba antes de compartir o publicar.

### Qué va dónde

| Contenido | Lugar recomendado |
|---|---|
| reglas, workflow y guardrails | Instructions |
| leyes, referencias y documentación extensa | Knowledge / archivos |
| ejemplos de consultas | Conversation starters |

## Importante

No copies secretos, credenciales ni datos personales reales como “ejemplos”. Para temas legales actuales, permite búsqueda web o verifica fuentes oficiales antes de cerrar una respuesta.

## Documentación oficial

- OpenAI Help — Crear y editar GPTs: https://help.openai.com/es-419/articles/8554397-creating-and-editing-gpts
- OpenAI Help — Proyectos en ChatGPT: https://help.openai.com/es-419/articles/10169521-using-projects-in-chatgpt
