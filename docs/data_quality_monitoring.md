# Data Quality Monitoring

Checks run at two points in the pipeline:

- **Before the load: `scripts/quality_gate.py`.** Checks the cleaned and transformed data. A failure stops the run before `warehouse.py`, so the current warehouse is kept.
- **After the load: `scripts/data_quality.py`.** Checks the warehouse tables against the transformed data. A failure stops the run before the archive step.

Each check compares an observed value with a threshold. A `min` check passes when the observed value is at least the threshold. A `max` check passes when it is at most the threshold.

## Pre-load checks (`quality_gate.py`)

| Check | What it measures | Rule | Threshold | Observed (run 2026-11-08) |
|---|---|---|---|---|
| `raw_rows_loaded` | Rows in the raw table | min | 500,000 | 541,909 |
| `rejected_rate_pct` | Share of raw rows rejected for price | max | 1.0% | 0.46% |
| `duplicate_rate_pct` | Share of raw rows removed as duplicates | max | 2.0% | 0.97% |
| `transformed_rows` | Rows in the transformed table | min | 500,000 | 534,129 |
| `clean_vs_transformed_mismatch` | Row count difference between clean and transformed | max | 0 | 0 |
| `missing_customer_pct` | Share of transformed rows with no customer | max | 30.0% | 24.8% |
| `unknown_description_pct` | Share of transformed rows with description `UNKNOWN` | max | 1.0% | 0.0% (all 1,454 missing-description rows were rejected for zero price) |
| `unstandardized_stock_codes` | Stock codes not uppercased and trimmed | max | 0 | 0 |
| `unmapped_country_codes` | Rows still holding `EIRE` or `RSA` | max | 0 | 0 |
| `outlier_rate_pct` | Share of clean rows flagged `is_outlier` | max | 5.0% | 0.23% |

## Post-load checks (`data_quality.py`)

| Check | What it measures | Rule | Threshold | Observed (run 2026-11-08) |
|---|---|---|---|---|
| `fact_rows` | Rows in the fact table | min | 500,000 | 534,129 |
| `fact_rows_match_transformed` | Row count difference between fact and transformed | max | 0 | 0 |
| `fact_missing_customer_pct` | Share of fact rows with no customer | max | 30.0% | 24.8% |
| `unknown_product_descriptions` | Products with description `UNKNOWN` | max | 50 | 0 |

The thresholds are judgement calls, not statistical limits. A change in the source file, such as a new export with more duplicates, should trigger a failure and prompt a review.

## Where results are stored

- **Database table `dq_results`**: one row per check per run, with `run_id`, `checked_at`, the observed value, the rule, the threshold and the status. The table is never dropped, so the history grows over time.
- **Log file `logs/data_quality.log`**: one line per check per run, appended each time. Pre-load lines are marked `pre_load`.

Each run's ID is its start time, formatted as `YYYYMMDD_HHMMSS`.

## Alerts

There is no email or dashboard alert. The alert is:

1. A `FAIL` line in the console output and in `logs/data_quality.log`.
2. A non-zero exit code from the failing script. This stops `run_pipeline.py`.
3. The scheduled task reports a failed run in Task Scheduler (Last Run Result is not `(0x0)`).

Results are saved before the alert is raised. The `raise` happens after the database connection closes, so the results are committed even when a check fails.

## Why the gate runs before the load

If the checks ran after the load, a bad batch would already be in the warehouse when the failure is reported. Running the main checks on the transformed data first means a failed batch never replaces the current warehouse. The post-load checks still run to confirm the warehouse matches the transformed data.
