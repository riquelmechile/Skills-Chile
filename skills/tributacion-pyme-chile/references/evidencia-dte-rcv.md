# Evidencia DTE / RCV

## Jerarquía práctica

1. **Estado o registro oficial SII del período** cuando la pregunta depende de lo declarado/aceptado.
2. **RCV descargado del SII** para visión mensual de compras/ventas.
3. **XML DTE original** para identidad, montos, impuestos y referencias.
4. **F29/F22 presentado, comprobantes y certificados** para pagos/créditos reales.
5. Exportaciones, planillas u OCR sólo como apoyo; deben reconciliarse con la fuente tributaria.

## Calidad mínima por documento

Registra, cuando exista: tipo DTE, folio, fecha, emisor, receptor, neto, exento, IVA, total, dirección emitido/recibido y referencias a otros documentos.

## Estados de evidencia

- `verificado`: existe respaldo oficial o documento fuente suficiente;
- `estimado`: fórmula válida sobre datos parciales explícitos;
- `pendiente`: falta un antecedente determinante;
- `inconsistente`: dos fuentes relevantes no coinciden.

Nunca promociones `estimado` a `verificado` para completar una salida.
