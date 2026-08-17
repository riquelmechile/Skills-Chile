# Tipos DTE y estados

## Tipos frecuentes del alcance documentado

| Tipo | Documento |
|---:|---|
| 33 | Factura Electrónica afecta |
| 34 | Factura No Afecta o Exenta Electrónica |
| 39 | Boleta Electrónica afecta |
| 41 | Boleta No Afecta o Exenta Electrónica |
| 52 | Guía de Despacho Electrónica |
| 56 | Nota de Débito Electrónica |
| 61 | Nota de Crédito Electrónica |

No confundas tipo 41 con boleta de honorarios.

## Máquina de estados recomendada

```text
draft
  -> calculated
  -> folio_reserved
  -> ted_generated
  -> schema_validated
  -> signed
  -> queued
  -> sent
  -> accepted | accepted_with_repair | rejected
```

`cancelled` puede existir antes del envío. Después de `sent`, un resultado incierto requiere reconciliación; no hagas retry ciego de la emisión ni devuelvas el folio al inventario por intuición.

## Evidencia por transición

- `calculated`: reglas y totales determinísticos;
- `folio_reserved`: reserva atómica y rango CAF válido;
- `schema_validated`: resultado XSD contra versión registrada;
- `signed`: firma verificable localmente;
- `sent`: evidencia de envío/identificador oficial cuando corresponda;
- estado final: respuesta oficial persistida.
