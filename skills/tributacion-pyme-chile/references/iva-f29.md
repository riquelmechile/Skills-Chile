# IVA y preparación F29

## Clasificación conservadora de DTE

Según el set documental verificado al 2026-07-22:

| Código | Documento | Tratamiento de trabajo |
|---:|---|---|
| 33 | Factura electrónica | Puede aportar débito o crédito IVA según dirección y antecedente real. |
| 34 | Factura no afecta o exenta | No genera débito/crédito IVA por esa condición. |
| 39 | Boleta electrónica de ventas y servicios | Venta afecta cuando corresponde y existe total respaldado. |
| 41 | Boleta no afecta o exenta | Fuera de IVA; **no es boleta de honorarios**. |
| 56 | Nota de débito electrónica | Conciliar con referencia antes de incorporarla. |
| 61 | Nota de crédito electrónica | Conciliar con referencia antes de incorporarla. |

## Flujo mensual

1. Reúne RCV del período y XML DTE cuando haga falta detalle.
2. Separa emitidos/recibidos y afectos/exentos/no afectos.
3. Resuelve duplicados y notas con su referencia.
4. Calcula ventas netas y débito sólo con documentos atribuibles al período.
5. Incluye crédito fiscal sólo con compras y IVA respaldados.
6. Compara débito vs crédito.
7. Si el crédito supera al débito, informa **remanente estimado**; no inventes reajuste del período anterior.
8. Calcula PPM sólo si régimen, período y tramo están confirmados.
9. Reconcílialo con F29 anterior y pagos reales antes de etiquetar el resultado como verificado.

## PPM Pro Pyme General 14 D N°3 documentado

La documentación fuente registrada al 2026-07-22 modela una tasa general de 0,25% en primer ejercicio o con ingresos brutos del ejercicio anterior hasta 50.000 UF, y 0,50% sobre ese umbral. Para ingresos obtenidos entre agosto de 2025 y diciembre de 2027 documenta una rebaja transitoria a 0,125% y 0,25%, respectivamente.

**No uses esta tabla fuera de su período sin revalidar SII.** No deduzcas el tramo desde ventas parciales si el contribuyente no lo confirmó.

## Resultado mínimo

- débito IVA: valor + evidencia;
- crédito IVA: valor + evidencia;
- remanente: `estimado | verificado`;
- PPM: tasa, base, período y fuente;
- faltantes antes de F29;
- advertencia explícita de que una estimación no equivale a declaración presentada.
