# ETL Pipeline

The pipeline loads the Kaggle Online Retail CSV into the `retail_dw` warehouse. It runs as a set of Python scripts, started by one entry point, `scripts/run_pipeline.py`.

## Steps

`run_pipeline.py` runs these scripts in order. If any script fails, the run stops and the remaining steps do not run.

| # | Script | Reads | Writes | What it does |
|---|---|---|---|---|
| 1 | `ingest.py` | `data/raw/online_retail.csv` | `raw_online_retail` | Loads the CSV as text, with no changes. Uses PostgreSQL `COPY`, which is much faster than row-by-row inserts. |
| 2 | `clean.py` | `raw_online_retail` | `clean_online_retail`, `rejected_rows` | Removes exact duplicates, moves zero and negative prices to `rejected_rows`, sets missing descriptions to `UNKNOWN`, adds cancellation flags. Checks that the counts reconcile. |
| 3 | `transform.py` | `clean_online_retail` | `transformed_online_retail` | Converts columns to proper types, uppercases stock codes, renames `EIRE` to `Ireland` and `RSA` to `South Africa`. Checks the counts. |
| 4 | `warehouse.py` | `transformed_online_retail` | `dim_date`, `dim_customer`, `dim_product`, `fact_sales` | Rebuilds the star schema, creates the monthly partitions and the indexes. Checks that the fact has the same row count as the transformed data. |
| 5 | `data_quality.py` | all tables | `dq_results`, `logs/data_quality.log` | Runs seven checks and records the results. Fails the run if a check fails. |
| 6 | `archive.py` | `transformed_online_retail` | `archive_transformed`, `metadata_catalog` | Copies the transformed data into the archive, tagged with the run ID, and refreshes the metadata catalog. |
| 7 | `performance.py` | `fact_sales` | `mv_monthly_revenue`, `docs/query_plans.md` | Rebuilds the materialized view and records query plans with and without indexes. |

## Running it

From the project root, with the virtual environment active:

```powershell
python scripts\run_pipeline.py
```

A successful run prints each step's name and counts, and ends with `pipeline finished`. A full run takes about 1 to 2 minutes.

## Scheduling

The pipeline runs daily at 2:00 AM, using Windows Task Scheduler:

- Task name: `Retail Pipeline`
- Program: `C:\Users\Noran\Desktop\online-retail-de\venv\Scripts\python.exe`
- Arguments: `scripts\run_pipeline.py`
- Start in: `C:\Users\Noran\Desktop\online-retail-de`

The task's **Last Run Result** shows `(0x0)` when the run succeeded. Any other value means a step failed. Check the console output or run the pipeline by hand to see which step failed.

## Failure behaviour

- Each script exits with an error code on failure. `run_pipeline.py` stops at that step.
- If a data quality check fails, `data_quality.py` exits with an error. The archive and the performance steps are then skipped, so a failing load is never archived as a version.
- The pipeline rebuilds the tables on each run. The archive keeps earlier results, so the previous state can be recovered from `archive_transformed`.

## Files

- `scripts/ingest.py`, `clean.py`, `transform.py`, `warehouse.py`, `data_quality.py`, `archive.py`, `performance.py`: the pipeline steps.
- `scripts/run_pipeline.py`: runs the steps in order.
- `.env`: database connection settings. Not committed to git.
