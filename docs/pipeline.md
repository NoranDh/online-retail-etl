# ETL Pipeline

The pipeline loads the Kaggle Online Retail CSV into the `retail_dw` warehouse. It runs as a set of Python scripts, started by one entry point, `scripts/run_pipeline.py`.

## Steps

`run_pipeline.py` runs these scripts in order. If any script fails, the run stops and the remaining steps do not run.

| # | Script | Reads | Writes | What it does |
|---|---|---|---|---|
| 1 | `ingest.py` | `data/raw/online_retail.csv` | `raw_online_retail` | Loads the CSV as text, with no changes. Uses PostgreSQL `COPY`, which is much faster than row-by-row inserts. |
| 2 | `clean.py` | `raw_online_retail` | `clean_online_retail`, `rejected_rows` | Removes exact duplicates, moves zero and negative prices to `rejected_rows`, sets missing descriptions to `UNKNOWN`, adds cancellation flags. Checks that the counts reconcile. |
| 3 | `transform.py` | `clean_online_retail` | `transformed_online_retail` | Converts columns to proper types, uppercases stock codes, renames `EIRE` to `Ireland` and `RSA` to `South Africa`. Checks the counts. |
| 4 | `quality_gate.py` | `clean_online_retail`, `transformed_online_retail`, `rejected_rows` | `dq_results`, `logs/data_quality.log` | Runs nine checks on the cleaned and transformed data. Fails the run before the warehouse is touched, so the current warehouse is kept. |
| 5 | `warehouse.py` | `transformed_online_retail` | `dim_date`, `dim_customer`, `dim_product`, `fact_sales` | Rebuilds the star schema, creates the monthly partitions and the indexes. Checks that the fact has the same row count as the transformed data. |
| 6 | `data_quality.py` | warehouse tables | `dq_results`, `logs/data_quality.log` | Runs four checks on the warehouse after the load and records the results. Fails the run if a check fails. |
| 7 | `archive.py` | `transformed_online_retail` | `archive_transformed`, `metadata_catalog` | Copies the transformed data into the archive, tagged with the run ID, and refreshes the metadata catalog. |
| 8 | `performance.py` | `fact_sales` | `mv_monthly_revenue`, `docs/query_plans.md` | Rebuilds the materialized view and records query plans with and without indexes. |
| 9 | `lineage.py` | `archive_transformed`, all tables | `lineage` | Records each data movement for the run (source, target, transformation, row count). Runs last, so the materialized view exists. |

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
- If a check in `quality_gate.py` fails, the run stops before `warehouse.py`. The warehouse keeps its previous data.
- If a check in `data_quality.py` fails, the run stops after the load. The archive and performance steps are skipped, so a failing load is never archived as a version.
- The pipeline rebuilds the tables on each run. The archive keeps earlier results, so the previous state can be recovered from `archive_transformed`.

## Files

- `scripts/ingest.py`, `clean.py`, `transform.py`, `quality_gate.py`, `warehouse.py`, `data_quality.py`, `archive.py`, `lineage.py`, `performance.py`: the pipeline steps.
- `scripts/run_pipeline.py`: runs the steps in order.
- `.env`: database connection settings. Not committed to git.
