---
name: facturacion-electronica-dte-chile
description: Diseña, revisa o audita flujos de facturación electrónica DTE en Chile para sistemas propios o integraciones, cubriendo tipos de documento, XSD, CAF/TED, folios, firma, autenticación, envío, estados SII, certificación y seguridad. Úsala cuando una implementación de factura o boleta electrónica deba demostrar validez técnica y separar claramente certificación de producción.
---

# Facturación Electrónica DTE Chile

**Última verificación documental: 2026-07-22.**

Convierte la emisión electrónica en una máquina de estados verificable. Un XML generado localmente no es un DTE “aceptado”: la validez operacional depende de reglas técnicas, firma, folios, envío y estados oficiales.

> La documentación técnica del SII incluye material histórico. Si el ambiente asignado al contribuyente o una instrucción oficial vigente difiere del material documentado aquí, prevalece la instrucción oficial aplicable y debes registrar la diferencia.

## Cuándo usarla

- diseñar un emisor propio de facturas o boletas electrónicas;
- revisar XML/XSD, CAF, TED, folios o firma electrónica;
- preparar certificación SII;
- auditar reintentos, estados, almacenamiento de secretos y trazabilidad;
- distinguir “generado”, “firmado”, “enviado” y “aceptado”.

## Flujo de trabajo

1. **Fija entorno y alcance.** `certificación | producción`, contribuyente, tipos DTE y evidencia oficial disponible.
2. **Modela tipos y estados.** Consulta [`references/tipos-y-estados.md`](references/tipos-y-estados.md).
3. **Valida dominio antes de XML.** RUT, totales, impuestos, referencias, rangos de folio y reglas del tipo documental.
4. **Construye y valida XML.** Usa schemas oficiales versionados y valida antes de firmar y enviar.
5. **Gestiona CAF/TED/folios.** Verifica CAF, cifra material sensible y reserva folios atómicamente; nunca reutilices un folio consumido.
6. **Firma fuera de la IA.** La clave privada no se entrega al modelo ni a JavaScript no confiable. Verifica la firma después de generarla.
7. **Autentica y envía.** Persistir identificadores de seguimiento y tratar timeouts como estado incierto, no como éxito/fracaso inventado.
8. **Consulta estado oficial.** Sólo una respuesta oficial puede promover a `accepted`, `accepted_with_repair` o `rejected`.
9. **Conserva evidencia.** Hashes de XSD, versión de software, XML, validaciones, Track ID/estado y bitácora; excluye secretos.
10. **Certifica antes de producción.** Sigue [`references/certificacion-y-seguridad.md`](references/certificacion-y-seguridad.md).

## Salida esperada

Una auditoría por etapa con:

- estado actual;
- evidencia observada;
- requisito técnico/oficial;
- brecha;
- riesgo;
- acción de cierre;
- prueba necesaria para avanzar al estado siguiente.

## Guardrails

- No declares “aceptado” por validación local, HTTP 200 genérico o ausencia de error.
- No reutilices folios después de envío/rechazo sin una regla oficial que lo permita.
- No persistas contraseñas PKCS#12 ni expongas claves privadas a la IA.
- No mezcles CAF, claves, endpoints o almacenamiento de certificación y producción.
- No modernices unilateralmente un protocolo legado si el ambiente oficial exige otra forma.
- No automatices declaraciones o autorizaciones legales que correspondan al representante del contribuyente.

## Referencias

- [`references/fuentes-oficiales.md`](references/fuentes-oficiales.md)
- [`references/tipos-y-estados.md`](references/tipos-y-estados.md)
- [`references/certificacion-y-seguridad.md`](references/certificacion-y-seguridad.md)
