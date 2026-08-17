---
name: rentabilidad-ecommerce-chile
description: Calcula y audita rentabilidad de productos y campañas de ecommerce en Chile usando costos reales, comisiones, despacho, devoluciones, publicidad y métricas como margen, markup y ROAS. Úsala para fijar o revisar precios y campañas sin inventar comisiones, impuestos, costos logísticos ni umbrales privados de negocio.
---

# Rentabilidad Ecommerce Chile

**Última verificación metodológica: 2026-08-17.**

Convierte ventas brutas en contribución económica explicable. El objetivo no es “hacer que el margen dé”, sino mostrar qué dato falta y cuánto cambia la decisión cuando ese dato varía.

## Cuándo usarla

- evaluar si un SKU realmente gana dinero;
- comparar precio, costo, comisión y despacho entre marketplaces;
- revisar campañas por ROAS sin ignorar margen;
- calcular precio de equilibrio o escenarios;
- detectar productos sin costo confiable antes de escalar publicidad.

## Flujo de trabajo

1. **Fija unidad de análisis.** SKU/variante, canal, período y moneda CLP.
2. **Reúne ingresos.** Precio efectivamente cobrado, descuentos, ingreso de envío y devoluciones/bonificaciones atribuibles.
3. **Reúne costos reales.** Producto, flete de entrada, embalaje, despacho pagado por vendedor, comisión marketplace, fee de pago, costos no recuperables y otros variables. Nunca inventes porcentajes.
4. **Separa impuestos correctamente.** No trates IVA recuperable/no recuperable como si fueran lo mismo; si el tratamiento tributario no está claro, marca pendiente y deriva a `tributacion-pyme-chile`.
5. **Calcula métricas canónicas.** Usa [`references/metricas-y-formulas.md`](references/metricas-y-formulas.md).
6. **Cruza publicidad.** ROAS alto no garantiza utilidad. Imputa gasto publicitario de forma consistente con el período/atribución.
7. **Hace escenarios.** Precio actual, precio mínimo con margen objetivo declarado por el operador y sensibilidad ante comisión/despacho/devoluciones.
8. **Entrega decisión con confianza.** Sigue [`references/evidencia-y-decisiones.md`](references/evidencia-y-decisiones.md).

## Salida esperada

Por SKU/canal:

- ingreso efectivo;
- costo landed;
- costos variables de venta;
- gasto publicitario atribuible;
- contribución CLP;
- margen %;
- markup %;
- ROAS/MER cuando corresponda;
- datos faltantes;
- decisión `escalar | mantener | corregir | no concluyente` con razones.

## Guardrails

- No hardcodees comisión de marketplace: usa tarifa/estado real o pide el dato.
- No copies umbrales comerciales privados de otra empresa como estándar universal.
- No llames “margen” al markup ni los intercambies.
- No uses ROAS solo para decidir si una campaña es rentable.
- No mezcles costos de dos cuentas, canales o variantes.
- Si faltan costo del producto, comisión o despacho material, la conclusión debe ser `no concluyente`.

## Referencias

- [`references/metricas-y-formulas.md`](references/metricas-y-formulas.md)
- [`references/evidencia-y-decisiones.md`](references/evidencia-y-decisiones.md)
