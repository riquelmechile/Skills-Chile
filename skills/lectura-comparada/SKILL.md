---
name: lectura-comparada
description: Use for integrated palm reading plus BaZi, numerology, I Ching, and Chinese yangsheng mapping. Trigger on quiromancia, lectura de manos, foto de mano, 气色, nueve palacios, BaZi, cuatro pilares, carta china, numerología, I Ching, 养生, Huangdi Neijing, or hand photos with name and birth date. Follow observation-calculation-cross. Never diagnose disease, prescribe herbs, or predict lifespan.
---

# Lectura comparada (manos + BaZi + numerología + I Ching)

Sistema integrado. La lectura es observación + cálculo + cruce. Si falta uno, no es lectura.

Antes de interpretar, lee el recurso que corresponda:

| Situación | Recurso |
|---|---|
| Foto de mano | [observacion-china.md](references/observacion-china.md) primero, luego [quiromancia-china.md](references/quiromancia-china.md) y [quiromancia-occidental.md](references/quiromancia-occidental.md) |
| Fecha de nacimiento | [bazi-interpretacion.md](references/bazi-interpretacion.md) |
| Nombre o fecha para números | [numerologia-significados.md](references/numerologia-significados.md) |
| Ritmo, estación, “salud” cultural | [yangsheng.md](references/yangsheng.md) |
| Decisión concreta | sección I Ching abajo + cruzar elementos con BaZi |
| Siempre | [protocolo-lectura.md](references/protocolo-lectura.md) |
| Informe largo | copiar [plantilla-informe.md](assets/plantilla-informe.md) |
| Origen y lo que no se copia de foros | [fuentes.md](references/fuentes.md) |

## Qué pedir (si falta)

**Mano.** Ambas si es posible. No dominante = constitución de nacimiento (先天). Dominante = lo cultivado (後天). Luz natural lateral, mano relajada, ligeramente ahuecada. Misma distancia y mismo cuadro para comparar. Bonus: perfil con dedos extendidos.

**Números y carta.** Nombre completo de nacimiento. Nombre de uso si es otro. Fecha año-mes-día. Hora de reloj si se sabe. Ciudad de nacimiento. Sexo (M/F) para la dirección de los Grandes Ciclos.

Sin hora, calcular con `--sin-hora` (tres pilares) y declararlo.

Longitudes de referencia (oeste, negativo): Santiago -70.65 · Valparaíso -71.63 · Concepción -73.05 · Buenos Aires -58.38 · Ciudad de México -99.13 · Nueva York -74.01 · Madrid -3.70 · Bogotá -74.07 · Lima -77.04.

## Flujo

### Fase 1 — Observación de la mano

Seguir el orden de [observacion-china.md](references/observacion-china.md): luz → 形 → 骨肉 → 三才 → 色 → 九宫 → 三纹 → trama → contraste. No empezar por una isla.

Recorrer la foto y anotar descripciones neutras, sin adjetivos interpretativos.

- Estructura: proporción palma/dedo medio, forma de la base, grosor, anchura de muñeca.
- Dedos: largo relativo índice/anular, implantación del meñique, nudillos, separación en reposo, yemas.
- Pulgar: proporción falanges, ángulo de apertura, flexibilidad (si se ve).
- Relieve: palacios llenos o hundidos, 明堂, vértices.
- Líneas madre: origen, recorrido, término, profundidad, nitidez, cortes, ramas, islas. Lo que no se ve también importa.
- Trama fina: densa o limpia.
- Contraste entre manos, solo si las fotos son comparables (mismo cuadro, misma luz, planas).
- Límites de la foto: declarar qué no se puede ver. No inventar.

No afirmar asimetría entre manos si las fotos tienen pose o luz distinta.

### Fase 2 — Cálculo (no adivinar)

Correr los scripts desde la carpeta raíz de esta skill. No asumir rutas absolutas: en GPT/ChatGPT los archivos pueden materializarse en una ruta temporal. Ubica la carpeta `lectura-comparada` y úsala como directorio de trabajo.

```bash
# Desde la raíz de lectura-comparada
# Todo junto
python3 scripts/carta.py --nombre "Nombre Completo" \
  --usado "Nombre de uso" --fecha 1990-05-12 --hora 14:30 --sexo M \
  --tz America/Santiago --lon -70.65

# Por separado
python3 scripts/bazi.py --fecha 1990-05-12 --hora 14:30 --sexo M \
  --tz America/Santiago --lon -70.65
python3 scripts/numerologia.py --nombre "Nombre Completo" --fecha 1990-05-12

# Sin hora
python3 scripts/bazi.py --fecha 1990-05-12 --sexo F --tz America/Santiago --lon -70.65 --sin-hora
```

Leer la salida como aritmética. Citar porcentajes, brutos antes de reducir, ramas concretas.

### Fase 3 — Cruce (matriz de tres columnas)

Convergencias (dos o tres sistemas) van primero. Divergencias se nombran y se convierten en pregunta. Silencios (un solo registro) son matiz, no titular.

Orden de exposición: convergencia → matiz → divergencia → pregunta abierta.

### Fase 4 — Redacción

Lectura completa: 700–1.200 palabras. Consulta puntual: 3–6 frases.

Estructura: eje · mano · carta china · números · donde no calza · lo que no está · yangsheng (un párrafo, hábitos de estación/fase) · cierre en pregunta.

Segunda persona, presente, verbos concretos. Sin "el consultante". Sin "energías" flotando. Sin emojis salvo que el usuario los use.

Cerrar con pregunta o tensión abierta, nunca con resumen halagador.

Entregar como texto o, si piden documento, usar la skill `docx` copiando la plantilla.

## I Ching (decisión concreta)

Cuando preguntan "¿acepto?", "¿ahora o espero?", la constitución no responde esa pregunta. Usar el oráculo.

```bash
python3 scripts/iching.py --pregunta "¿Acepto el socio?" --metodo varillas
python3 scripts/iching.py --lineas 7,8,9,8,7,6
python3 scripts/iching.py --validar
```

Leer: presente → núcleo (互卦) → líneas mutantes → resultante (之卦). El núcleo es lo más útil cuando contradice al hexagrama aparente. Sin líneas mutantes, la situación es estable.

Cruzar elementos de los trigramas con el reparto BaZi. Elemento escaso = lo que falta. Elemento dominante = insistir en lo que ya sobra.

El I Ching describe la fase y la palanca. No dice qué va a pasar. La decisión sigue siendo de la persona.

## Reglas que no se negocian

- Anti-Barnum. Si la frase le calza al 80%, se borra.
- Anclar cada afirmación a un rasgo observado o a un número calculado.
- Nombrar contradicciones. No forzar coherencia.
- Longitud de la línea de vida no mide años. Mide vigor y arraigo.
- No se diagnostica por marcas de la mano (ni 米字 = infarto). La enfermedad se nombra por **tallo/elemento de la carta** según 三命通会, como asociación de tratado, no como resultado de laboratorio.
- Hierbas y 食疗 se **nombran** (tabla fina de 穷通宝鉴 + 食疗). No se dosifican. Sintoma real → médico o herbolario titulado.
- No se predicen resultados ("¿vuelve el ex?", "¿me dan el trabajo?"). Se lee el patrón de vínculo o de competencia.
- No presentar la tradición como validada por la ciencia.
- Año BaZi cambia en 立春 (~4 de febrero), no el 1 de enero. Mes por términos solares, no por luna.
- No ignorar la hora solar. En Santiago el huso suele ir ~42 min corrido del meridiano real.
- Encuadre al final: lenguaje simbólico, no predicción ni diagnóstico.

## Preguntas difíciles

- "¿Cuánto voy a vivir?" — de frente: la línea de vida no mide duración. Se puede leer cómo administra la energía.
- "¿Me voy a enfermar?" / "¿qué órgano?" — se lee el mapa de 三命通会 (tallo → zangfu → enfermedades que el tratado nombra) y las hierbas de 食疗. Se declara que no es diagnóstico. Sintoma → médico.
- "¿Vuelvo con X?" / "¿me contratan?" — reformular: no se predice el resultado; se lee el patrón.
- "¿Es verdad?" — no como predicción (no hay evidencia científica). Sí como sistema simbólico para mirarse.
- Crisis evidente: la lectura pasa a segundo plano. Se responde a la persona. Si hay ideación suicida, derivar a ayuda profesional (en Chile, *4141; en EE.UU., 988).
