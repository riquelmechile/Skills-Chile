# Certificación y seguridad DTE

## Separación de entornos

Certificación y producción deben usar almacenes, claves, CAF, folios y endpoints separados. Un fixture o CAF de certificación no habilita producción.

## Seguridad mínima

1. clave privada fuera de la IA;
2. contraseña PKCS#12 sólo en memoria cuando deba utilizarse;
3. CAF y llave de timbraje cifrados;
4. reserva de folio transaccional;
5. XML validado contra XSD antes de firmar/enviar;
6. firma verificada después de generarla;
7. logs sin certificados, claves, CAF ni XML completo cuando contenga información sensible;
8. reintentos idempotentes y reconciliación de resultados ambiguos.

## Certificación

El contribuyente debe seguir el proceso oficial aplicable: postulación/registro, set de pruebas, folios de certificación, ejecución de pruebas, simulación/intercambio/muestras o pasos que el SII exija en el ambiente vigente, declaración correspondiente y autorización final.

No presentes el software como “certificado” sólo porque pasa pruebas locales. Conserva evidencia del ambiente y del estado oficial.
