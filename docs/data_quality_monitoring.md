# Data Quality Monitoring

`scripts/data_quality.py` runs after the warehouse is loaded. It checks the result of each run against fixed thresholds, stores every result, and fails the run when a check fails.

## Checks

Thresholds were set from the measured values of the first run, with room for normal variation. Each check is a rule of the form "observed must be at least" (`min`) or "at most" (`max`) the threshold.

| Check | What it measures | Rule | Threshold | Observed (run 2026-11-08) |
|---|---|---|---|---|
| `raw_rows_loaded` | Rows in the raw table | min | 500,000 | 541,909 |
| `rejected_rate_pct` | Share of raw rows rejected for price | max | 1.0% | 0.46% |
| `duplicate_rate_pct` | Share of raw rows removed as duplicates | max | 2.0% | 0.97% |
| `missing_customer_pct` | Share of fact rows with no customer | max | 30.0% | 24.8% |
| `unstandardized_stock_codes` | Stock codes not uppercased and trimmed | max | 0 | 0 |
| `unknown_product_descriptions` | Products with no usable description | max | 50 | 0 |
| `fact_rows` | Rows in the fact table | min | 500,000 | 534,129 |

The thresholds are judgement calls, not statistical limits. A change in the source file, such as a new export with more duplicates, should trigger a failure and prompt a review.

## Where results are stored

- **Database table `dq_results`**: one row per check per run, with `run_id`, `checked_at`, the observed value, the rule, the threshold and the status. The table is never dropped, so the history grows over time.
- **Log file `logs/data_quality.log`**: one line per check per run, appended each time.

Each run's ID is its start time, formatted as `YYYYMMDD_HHMMSS`.

## Alerts

There is no email or dashboard alert. The alert is:

1. A line with `FAIL` in the console output and in `logs/data_quality.log`.
2. A non-zero exit code from `data_quality.py`. This stops `run_pipeline.py`, so the archive step is skipped.
3. The scheduled task reports a failed run in Task Scheduler (Last Run Result is not `(0x0)`).

Results are saved before the alert is raised. The `raise` happens after the database connection closes, so the results are committed even when a check fails.

## Known limitation

The warehouse is loaded before the checks run. If a check fails, the warehouse already holds the new data, and the failure is only reported afterwards. The fix is to run the checks on the transformed data, before the warehouse is rebuilt. See [recommendations.md](recommendations.md).
