# P1 · Limpieza y calidad de datos
## Airbnb Buenos Aires — enero 2026

![Python](https://img.shields.io/badge/Python-3.11-blue)
![pandas](https://img.shields.io/badge/pandas-2.0-green)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-orange)
![GCP](https://img.shields.io/badge/GCP-Cloud_Storage-blue)

## Objetivo

Recibir un dataset sucio del mundo real (27.348 filas × 85 columnas) 
y dejarlo limpio, documentado y listo para análisis. Base de todo 
proyecto de datos.

## Resultado principal

| Métrica | Antes | Después |
|---|---|---|
| Columnas | 85 | 72 |
| Nulos totales | 489.229 | 50.171 |
| Reducción de nulos | | **89.7%** |
| Duplicados | 0 | 0 |

## Estructura

p1-airbnb-data-quality/
├── data/
│   └── processed/       ← dataset limpio
├── notebooks/
│   └── 01_eda_quality.ipynb
├── src/
│   └── clean.py         ← funciones reutilizables
├── tests/
│   └── test_clean.py    ← 5 tests con pytest
├── reports/
│   └── quality_report.md
└── Dockerfile

## Decisiones técnicas

- **Imputación por grupos:** `beds`, `bedrooms` y `bathrooms` 
  imputados con mediana por `room_type` en vez de mediana global
- **Columnas eliminadas:** 17 columnas con más del 40% de nulos
- **`price` vacío:** columna de precio 100% nula en este scrape, 
  limitación documentada

## Variables derivadas creadas

| Variable | Descripción |
|---|---|
| `tiene_resenas` | Binaria (1/0) — tiene al menos una reseña |
| `dias_activo` | Días entre primera y última reseña |
| `dias_desde_ultima_resena` | Días entre última reseña y scrape |
| `antiguedad_total` | Días desde primera reseña al scrape |

## Consultas SQL (DuckDB)

- Distribución por tipo de propiedad
- Mediana de días activo por tipo
- Propiedades inactivas hace más de 365 días

## Cómo reproducir

```bash
# Instalar dependencias
pip install -r requirements.txt

# Correr tests
pytest tests/ -v

# Ejecutar notebook
jupyter notebook notebooks/01_eda_quality.ipynb
```

## Dataset en cloud

gs://portfolio-ds-jaime/p1-airbnb/listings_clean.csv

## Stack

Python · pandas · DuckDB · pytest · Docker · GCP Cloud Storage