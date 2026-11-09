# Online Retail Data Warehouse

A data pipeline that loads the Kaggle Online Retail dataset into PostgreSQL, cleans and validates it, builds a star schema, and checks data quality on every run.

## What it does

1. **Ingest** the raw CSV into PostgreSQL as text.
2. **Clean** the data: remove duplicates, move zero and negative prices to a rejected table, flag cancellations.
3. **Transform** the data: convert column types and standardize stock codes and country names.
4. **Build the warehouse**: a star schema with a sales fact table, and customer, product and date dimensions. The fact table is partitioned by month.
5. **Check quality**: seven checks run on every load, and failures are logged and fail the run.
6. **Archive** each run's transformed data and update a metadata catalog.
7. **Measure performance**: query plans are recorded, and a materialized view serves the monthly revenue report.

## Requirements

- Windows with PowerShell
- Python 3.11 or newer
- PostgreSQL 16 or newer, running locally
- The Kaggle dataset `online_retail.csv`

## Setup

1. Create a database called `retail_dw` in PostgreSQL.

2. Create and activate a virtual environment in the project folder:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:

   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=retail_dw
   DB_USER=postgres
   DB_PASSWORD=your_password
   ```

4. Place the dataset at `data/raw/online_retail.csv`.

## Run the pipeline

From the project root, with the virtual environment active:

```powershell
python scripts\run_pipeline.py
```

A full run runs these scripts in order, and stops if one fails:

| Script | Purpose |
|---|---|
| `ingest.py` | Load the CSV into `raw_online_retail` |
| `clean.py` | Clean the data into `clean_online_retail` and `rejected_rows` |
| `transform.py` | Convert types into `transformed_online_retail` |
| `quality_gate.py` | Check the cleaned and transformed data before loading. Stops the run on failure. |
| `warehouse.py` | Build the star schema |
| `data_quality.py` | Check the warehouse after loading and log the results |
| `archive.py` | Archive the run and update the metadata catalog |
| `performance.py` | Rebuild the materialized view and record query plans |

To run it daily, schedule `scripts\run_pipeline.py` with Windows Task Scheduler.

## Project layout

```
online-retail-de/
├── data/raw/            the source CSV 
├── docs/                design and pipeline documentation
├── logs/                data quality log 
├── scripts/             pipeline scripts
├── .env                 database settings 
└── requirements.txt
```

## Requirement coverage

| Requirement | Where |
|---|---|
| 1. Ingestion | `scripts/ingest.py`: CSV loaded as text with PostgreSQL `COPY` |
| 2. Missing values | `clean.py`: missing descriptions set to `UNKNOWN`; missing CustomerID kept as NULL |
| 2. Duplicates | `clean.py`: exact duplicates removed with `DISTINCT ON` |
| 2. Outliers | `clean.py`: `is_outlier` flag, log-scale IQR rule with multiplier 3 |
| 2. Integrity | `clean.py`, `transform.py`, `warehouse.py`: row count reconciliation at each step; `data_quality.py`: fact matches transformed |
| 3. Transformation | `transform.py`: typed columns, uppercased stock codes, renamed countries |
| 4. Warehouse design | `warehouse.py`: `fact_sales`, `dim_date`, `dim_customer`, `dim_product`; see `docs/schema.md` |
| 5. ETL pipeline | `scripts/run_pipeline.py` runs all steps in order |
| 5. Scheduling | Windows Task Scheduler, daily at 02:00; see `docs/pipeline.md` |
| 6. Partitioning | `warehouse.py`: monthly range partitions on `invoice_date`, plus a default partition |
| 6. Indexing | `warehouse.py`: indexes on `product_key`, `customer_key`, `date_key`; reasons in `docs/schema.md` |
| 7. Quality monitoring | `quality_gate.py` before the load, `data_quality.py` after; results in `dq_results` |
| 7. Alerts | A FAIL stops the run, writes a log line, and sets the scheduled task's status |
| 8. Versioning | `archive.py`: one copy of the transformed data per run, tagged with `run_id` |
| 8. Archiving | `archive_transformed`; old partitions can be detached (see `docs/schema.md`) |
| 9. Metadata | `archive.py`: `metadata_catalog` (tables, sources, transformations, locations); `lineage.py`: `lineage` table with one row per data movement per run, with row counts; see `docs/schema.md` and `docs/pipeline.md` |
| 10. Performance | `performance.py`: query plans in `docs/query_plans.md`; indexes; materialized view `mv_monthly_revenue` |
| 10. Caching | Database level only: the materialized view. No application-level cache. |
| 11. Deliverables | `scripts/`, `docs/`, `README.md` |

## Documentation

- [Warehouse schema](docs/schema.md)
- [ETL pipeline](docs/pipeline.md)
- [Data quality monitoring](docs/data_quality_monitoring.md)
- [Design decisions](docs/design_decisions.md)
- [Data profile](docs/data_profile.md)
- [Query plans](docs/query_plans.md)
- [Recommendations](docs/recommendations.md)
