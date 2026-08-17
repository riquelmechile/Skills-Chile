---
name: boletas-honorarios-chile
description: Analiza y prepara cálculos y evidencia de boletas de honorarios electrónicas en Chile, incluyendo retención versionada por año y distinción frente a boletas de ventas DTE. Úsala para independientes, pagos de honorarios, revisión de bruto/retención/líquido y preparación de antecedentes tributarios sin asumir quién retiene ni declarar obligaciones fuera del período verificado.
---

# Boletas de Honorarios Chile

**Última verificación documental: 2026-07-22.**

Ayuda a interpretar y revisar honorarios de Segunda Categoría con tasas versionadas y evidencia explícita.

> Si la consulta usa un período posterior a la verificación documental, confirma primero la tasa y las instrucciones en el portal oficial del SII.

## Cuándo usarla

- calcular retención y líquido de una boleta de honorarios para un año conocido;
- revisar si una tasa corresponde al período;
- ordenar boletas y retenciones para la preparación de renta;
- detectar confusión entre boleta de honorarios y boleta electrónica de ventas/servicios.

## Flujo de trabajo

1. **Fija año y monto bruto.** Sin período no apliques tasa.
2. **Identifica el documento.** Una boleta de honorarios pertenece al flujo de Segunda Categoría; DTE 41 es una boleta no afecta/exenta de ventas y servicios, no honorarios.
3. **Verifica quién efectúa la retención.** No lo infieras sólo por el nombre del pagador; usa la boleta y las instrucciones SII aplicables.
4. **Resuelve la tasa versionada.** Consulta [`references/tasas-y-vigencia.md`](references/tasas-y-vigencia.md).
5. **Calcula.** Cuando corresponda retención: `retención = bruto × tasa`; `líquido = bruto − retención`. Mantén redondeos y valores del documento como fuente final cuando existan.
6. **Concilia evidencia.** Separa boleta emitida, retención practicada y crédito/pago efectivamente respaldado.
7. **Entrega próximos pasos.** Si faltan certificados, boletas, período o regla de retención, deja el resultado pendiente.

## Salida esperada

- año/período;
- monto bruto;
- tasa aplicada + fuente/versionado;
- retención calculada;
- líquido calculado;
- quién retiene: `verificado | pendiente`;
- evidencia disponible;
- advertencias y próximos pasos.

## Guardrails

- No uses una tasa “actual” sin fijar el año.
- No confundas DTE 41 con boleta de honorarios.
- No declares una retención pagada sólo porque se calculó.
- No asumas automáticamente quién debe retener; verifica el caso ante SII.
- Para renta anual compleja o cotizaciones previsionales, deriva a la skill tributaria correspondiente y revisión profesional cuando aplique.

## Referencias

- [`references/tasas-y-vigencia.md`](references/tasas-y-vigencia.md)
- [`references/flujo-operativo.md`](references/flujo-operativo.md)
