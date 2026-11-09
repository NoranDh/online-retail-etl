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

## Documentation

- [Warehouse schema](docs/schema.md)
- [ETL pipeline](docs/pipeline.md)
- [Data quality monitoring](docs/data_quality_monitoring.md)
- [Design decisions](docs/design_decisions.md)
- [Data profile](docs/data_profile.md)
- [Query plans](docs/query_plans.md)
- [Recommendations](docs/recommendations.md)
