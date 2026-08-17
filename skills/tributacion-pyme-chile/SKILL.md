---
name: tributacion-pyme-chile
description: Organiza y audita la preparación tributaria común de una Pyme en Chile, con foco en evidencia DTE/RCV, IVA y F29 mensual, PPM y preparación anual F22. Úsala para ordenar antecedentes, detectar faltantes, separar estimaciones de obligaciones oficiales y producir un checklist verificable sin inventar régimen, tasas, créditos ni declaraciones.
---

# Tributación Pyme Chile

**Última verificación documental: 2026-07-22.**

Convierte antecedentes tributarios dispersos en un flujo verificable. La IA explica, ordena y calcula sólo cuando existen datos y reglas suficientes; no presenta declaraciones ni reemplaza la revisión profesional en casos complejos.

> **Router temporal obligatorio:** si la consulta depende de una tasa, plazo, formulario, régimen o instrucción posterior al 2026-07-22, revalida primero la fuente oficial del SII. No presentes como vigente una cifra que sólo está versionada para otro período.

## Cuándo usarla

- preparar o revisar un cierre mensual de IVA/F29;
- ordenar DTE y Registro de Compras y Ventas (RCV);
- revisar PPM con régimen y tramo ya confirmados;
- preparar antecedentes para renta/F22 de una Pyme;
- detectar documentos, créditos o datos faltantes antes de declarar;
- explicar por qué una cifra es estimada, verificada o todavía incierta.

## Flujo de trabajo

1. **Fija período y contribuyente.** Registra mes/año, RUT anonimizado en el análisis si no es indispensable, actividad, régimen **confirmado** y si es primer ejercicio. No selecciones régimen por intuición.
2. **Reúne evidencia.** Prioriza RCV del SII, XML DTE originales, F29 anterior, pagos/certificados de PPM o retenciones y antecedentes de renta. Lee [`references/evidencia-dte-rcv.md`](references/evidencia-dte-rcv.md).
3. **Clasifica el período mensual.** Separa ventas/compras afectas, exentas/no afectas y notas pendientes de conciliación. Para IVA/F29 aplica [`references/iva-f29.md`](references/iva-f29.md).
4. **Calcula sólo lo demostrable.** Débito, crédito, remanente estimado y PPM deben indicar fuente, período y supuestos. Un crédito no se transforma en pagado porque una fórmula lo estime.
5. **Prepara la capa anual.** Para F22 distingue ingresos/gastos respaldados, régimen, PPM/retenciones efectivamente verificados y ajustes que requieren contador. Lee [`references/renta-f22.md`](references/renta-f22.md).
6. **Entrega brechas.** Lista obligación o criterio, aplicabilidad, evidencia observada, faltante, riesgo y acción siguiente.
7. **Verifica cierre.** Antes de afirmar “listo para declarar”, contrasta período, instrucciones oficiales vigentes, documentos conciliados y créditos respaldados.

## Salida esperada

Entrega cuatro bloques:

1. **Período y perfil confirmado** — qué se sabe y qué falta;
2. **Resumen calculable** — cifras con fórmula, fuente y nivel `verificado | estimado | pendiente`;
3. **Brechas antes de declarar** — documentos, conciliaciones, créditos, régimen o instrucciones faltantes;
4. **Próximas acciones** — ordenadas por impacto y con evidencia necesaria para cerrarlas.

## Guardrails

- No elijas automáticamente régimen tributario ni código de actividad.
- No reconstruyas silenciosamente IVA de una compra si el antecedente no lo respalda.
- No sumes notas de crédito/débito sin conciliar su documento de referencia.
- No confundas boleta electrónica DTE 41 con boleta de honorarios; para honorarios usa `boletas-honorarios-chile`.
- No llames “PPM pagado” a un PPM calculado desde ventas.
- No declares un F29/F22 presentado, aceptado o pagado sin evidencia oficial.
- Si el caso incluye reorganizaciones, retiros/dividendos, pérdidas, operaciones relacionadas, registros empresariales complejos o interpretación dudosa, marca revisión profesional.

## Referencias

- [`references/fuentes-y-vigencia.md`](references/fuentes-y-vigencia.md)
- [`references/iva-f29.md`](references/iva-f29.md)
- [`references/renta-f22.md`](references/renta-f22.md)
- [`references/evidencia-dte-rcv.md`](references/evidencia-dte-rcv.md)
