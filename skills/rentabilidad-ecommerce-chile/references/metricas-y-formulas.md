# Métricas y fórmulas

Define los componentes antes de calcular para evitar dobles conteos.

## Costos

`landedCost = costoProducto + fleteEntrada + embalaje + otrosCostosAdquisicion`

`costosVenta = comisionMarketplace + feePago + despachoVendedor + costosVariablesNoRecuperables`

## Contribución

`contribucion = precioCobrado + ingresoEnvio - landedCost - costosVenta - gastoAdsAtribuible - costoDevolucionesAtribuible`

## Margen y markup

`margenPct = contribucion / precioCobrado × 100`

`markupBrutoPct = (precioCobrado / landedCost - 1) × 100`

Margen y markup responden preguntas distintas. Declara cuál usas.

## Publicidad

`ROAS = ventasAtribuidas / gastoAds`

`MER = ventasTotales / gastoAdsTotal`

ROAS/MER son ratios de ingreso publicitario, no utilidad. Cruza siempre con contribución.

## Escenarios

Cuando el usuario fija un margen objetivo, muestra el objetivo como **supuesto de negocio**, no como regla de Chile ni del marketplace. Si un costo cambia por tramo, modela escenarios en vez de usar un promedio oculto.
