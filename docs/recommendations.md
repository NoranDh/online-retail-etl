# Recommendations

These are improvements for a production version of this pipeline. The current version is built for a one-off dataset and a daily rebuild.

## Load and rebuild

1. **Incremental loads.** The pipeline drops and rebuilds every table on each run. That works for 534,000 rows but takes longer as data grows. Load only new invoices, identified by invoice date or a source watermark, and merge them into the warehouse.
2. **Keep rejected batches for review.** When the quality gate fails, the run stops and the batch is only described in the log. Save the failing batch to a quarantine table so someone can inspect it before the next run.
3. **Stable surrogate keys.** Customer and product keys are generated in a fixed order on each rebuild, so they can change between runs. Incremental loads need keys that never change for the same customer or product. Keep the keys in a persistent table and only add new ones.
4. **Refresh the materialized view without locking.** The view is dropped and recreated on each run. Once loads are incremental, refresh it with `REFRESH MATERIALIZED VIEW CONCURRENTLY`, which needs the unique index that already exists.

## Partitions and retention

5. **Create partitions in advance.** Partitions are created for the months present in the data. A production load should create next month's partition on a schedule, before its data arrives.
6. **Archive retention.** `archive_transformed` grows by about 534,000 rows per run. Keep the last N runs, and detach older partitions into cold storage rather than keeping every copy in one table.
7. **Monitor partition sizes.** Check that no month is growing much faster than the others, and that the default partition stays empty. Rows there mean the partitions are missing a month.

## Data quality

8. **Outlier review.** Outliers are flagged with `is_outlier` (0.23% of rows in the current run) and kept. Add a review step that lists the flagged rows by stock code and country, so someone can confirm whether they are bulk orders or errors.
9. **Negative-price adjustments.** The two rows with stock code `B` ("Adjust bad debt") are quarantined. Confirm based on business logic whether adjustments should be reported separately rather than dropped.
10. **Thresholds from history.** The current thresholds are fixed numbers. Once `dq_results` holds several runs, set them from the recent history instead, for example the mean plus or minus three standard deviations.
11. **Alert delivery.** Alerts are a log line and a failed task. Send them to email or a chat channel so someone sees a failure without opening the log.

## Performance

12. **Add indexes for the queries that matter.** Each index makes its matching lookup about 8 to 15 times faster: customer 1.1 ms against 107 ms, product 10.5 ms against 83 ms, and date 7.2 ms against 110 ms. Aggregations over most of the table are not helped, and the materialized view handles those. Check the plans in `query_plans.md` again after the first incremental run.
13. **Use the materialized view for reports.** Point the frequent monthly reports at `mv_monthly_revenue` rather than the fact table.

## Operations

14. **Secrets.** Database credentials are in `.env`, which is not committed. In production, use a secrets manager or the scheduler's credential store.
15. **Version control.** The project is not yet in git. Commit the scripts and docs, and tag each release that changes the schema.
16. **Tests.** The checks in `clean.py`, `transform.py`, `warehouse.py` and `data_quality.py` run against live data. Add unit tests for the mapping rules, such as the country renames and the category assignment, on small fixed inputs.
