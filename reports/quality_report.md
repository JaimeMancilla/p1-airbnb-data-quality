# Reporte de calidad de datos
##Dataset: Airbnb Buenos Aires - enero 2026

## Resumen antes/después

| Métrica | Antes | Después |
|---|---|---|
| Filas | 27,348 | 27,348 |
| Columnas | 85 | 72 |
| Duplicados | 0 | 0 |
| Nulos totales | 489,229 | 50,171 |
| Reducción de nulos | | 89.7% |

## Variables nuevas creadas
- 'tiene_resenas' - binaria (1/0)
- 'dias_activo' - días entre primera y última reseña
- 'dias_desde_ultima_resena' - días desde primera reseña al scrape

## Decisiones de limpieza
1. Eliminadas 17 columnas con más del 40% de nulos
2. Imputados 'beds', 'bedrooms', 'bathrooms' con mediana por 'room_type'
3. 'review_scores_*' conservados como NaN (propiedades sin reseñas)
4. Fechas convertidas a datetime

## Insight destacado
847 propiedades (3.52%) llevan más de 3 años sin reseña
