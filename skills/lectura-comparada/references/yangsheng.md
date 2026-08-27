# Yangsheng (养生) — mapa cultural, no clínica

Capa de **ritmo y cuidado** tomada de *黄帝内经·素问·四气调神大论*, de la lógica de 调候 de *穷通宝鉴* y de *滴天髓* (寒暖燥湿). Sirve para traducir un desequilibrio elemental del gráfico o un palacio hundido a **hábitos de temporada**, no a diagnóstico ni a receta.

Encuadre de laboratorio: esto no constituye realidad médica. No reemplaza médico. No se prescriben hierbas, dosis ni tratamientos. Si alguien describe síntomas, se deriva.

## Lo que sí se puede decir

- Qué elemento está escaso o saturado en el cálculo.
- Qué estación o 调候 pide la carta (invierno frío pide sol/fuego de ritmo; verano seco pide agua/humedad de ritmo).
- Qué hábito de *Neijing* corresponde a esa estación o a ese órgano-simbólico.
- Dónde la mano muestra poco margen (palacio hundido, línea de tierra fina) y por tanto el texto habla de **no forzar**, no de “tienes X enfermedad”.

## Lo que no se dice

- “Esto indica hígado / diabetes / infarto / cáncer.”
- “La isla en tal punto es pronóstico de…”
- Dosis, decocciones de consulta, acupuntos de tratamiento, ayunos extremos.
- Esperanza de vida.
- “La isla de la palma indica cáncer.” Eso sigue prohibido.

Sí se nombran enfermedades y hierbas que salen del **tallo y del mes**, no de la raya.

## Cinco fases — órgano, emoción, cuidado (simbólico)

| Fase | Órgano-simbólico | Emoción que lo gasta | Si escasea en la carta o en la mano | Si satura |
|---|---|---|---|---|
| Madera | Hígado / vesícula (movimiento) | Ira contenida o explosiva | Falta arranque y paso; caminar, estirar, no aplazarse | Sobra empuje; cortar estímulos, no pelear cada borde |
| Fuego | Corazón / intestino delgado (shen) | Excitación, insomnio de brillo | Falta calor de ritmo; sol de mañana, trato, no aislamiento seco | Sobra calor; dormir, menos pantalla, menos picante |
| Tierra | Bazo-estómago | Rumia, preocupación | Falta digestión de lo concreto; horarios fijos de comida, un solo plato menos | Sobra estancamiento; moverse después de comer, no picar |
| Metal | Pulmón / intestino grueso | Pena, corte seco | Falta límite y aire; respirar, terminar, decir no | Sobra filo; humectar, no podar de más |
| Agua | Riñón / vejiga (reserva) | Miedo, fuga | Falta reserva; dormir, calor en pies y cintura, menos desgaste nocturno | Sobra frío-humedad de ritmo; secar con movimiento y calor moderado |

“Órgano” aquí es categoría del *Neijing*, no un órgano visto en laboratorio.

## Cuatro estaciones (*四气调神大论*)

Texto-eje: primavera nace, verano crece, otoño recoge, invierno guarda. Invertir la estación agota el órgano de la estación siguiente (eso dice el tratado; no se usa como pronóstico clínico).

**Primavera (Madera, hígado-simbólico).** Acostarse más tarde, levantarse temprano, caminar, pelo y cuerpo sueltos, no matar el brote (no reprimir el ánimo ni el movimiento). Comida: no pasarse de ácido; un poco de dulce para no dejar al bazo sin piso. En Chile: agosto–octubre como analogía de brote, no copiar el calendario lunar a ciegas.

**Verano (Fuego, corazón-simbólico).** Acostarse tarde, levantarse temprano, no odiar el sol, no montar en ira, dejar salir (sudor, trato, no encapsular). Comida: amargo y fresco con mesura; no hielo a destajo si la carta ya es fría.

**Otoño (Metal, pulmón-simbólico).** Acostarse temprano, levantarse temprano (con el gallo, dice el texto), recoger el shen, no dejar la voluntad afuera. Aire seco: humectar (pera, miel, menos picante). No abrir de más lo que ya debería cerrar.

**Invierno (Agua, riñón-simbólico).** Acostarse temprano, levantarse tarde, **esperar la luz**. No agotar la piel ni el yang (baño helado de moda contradice el tratado si la carta es fría). Abrigo de cintura y pies. Comida: caliente, no crudo de moda.

**Las cuatro estaciones se sostiene el bazo-Tierra.** Horario de comida estable es el hábito que más cruza con palma baja y con Tierra escasa o saturada.

## 调候 (ajustar el clima del gráfico)

De *穷通宝鉴*: primero el clima del mes de nacimiento, después el resto.

- Nacido en invierno (亥子丑) sin Fuego útil → el texto habla de **calor de ritmo**: sol, cocido, no madrugar a oscuras, no baño frío. No “tómate canela en gramos”.
- Nacido en verano (巳午未) sin Agua útil → **frescura de ritmo**: sombra, agua, menos picante, dormir. No “infusión X contra el hígado”.
- Humedad de temporada (辰未) → movimiento y comida que no empape.
- Sequedad (戌, otoño) → humectar.

`bazi.py` y `carta.py` leen las 120 celdas de *穷通宝鉴* (tallo del día × rama del mes), marcan qué 用神 están en la carta, y nombran zangfu, patrones, enfermedades de *三命通会* y hierbas/alimentos de 食疗. Pegar el párrafo. No dosificar. No convertir una raya de la palma en nombre de enfermedad.

## Cruce con la mano

| Señal observada | Traducción yangsheng (no clínica) |
|---|---|
| Línea de tierra (vida) fina o cadena | Ritmo de reserva bajo: menos heroísmo, más sueño |
| 明堂 hundido y oscuro (luz buena) | Cuesta que el medio circule: horarios, no más frentes |
| 坎 (talón) chato | Reserva; invierno y Agua |
| 离 (bajo medio) cargado de trama | Sobreatención; verano y Fuego a la baja |
| Meñique bajo + Metal escaso | No forzar la voz ni el cobro; pulmón-simbólico = aire y corte limpio |
| Base ancha + Tierra alta | Cuidar el exceso de rumia y de sentarse |

Si la foto no muestra el palacio, no inventar el consejo.

## Cómo redactarlo en el informe

Un párrafo corto, después de “lo que no está”:

- Citar el dato (p. ej. Agua 2,3%, nacido en 巳, 坎 chato).
- Un hábito de estación o de fase.
- Una frase de límite: “Esto es mapa de *Neijing*, no indicación médica.”

No abrir una sección de “enfermedades probables”.
