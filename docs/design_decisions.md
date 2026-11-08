# Cleaning Decisions



Measured counts come from [data_profile.md](data_profile.md).

## Decisions

| Issue | Rows | Decision | Reason |
|---|---|---|---|
| Missing CustomerID | 135,080 | Keep in the sales table with no customer link | About 25% of rows. Dropping them would remove real revenue and distort totals. Analysis by customer excludes them. |
| Zero unit price | 2,515 | Quarantine | A zero price is either a free item or a data error. It should not count toward revenue. |
| Negative unit price | 2 | Quarantine | Both rows are adjustments (stock code `B`, "Adjust bad debt", no customer), not sales. Their price is not a valid sale price, and guessing a corrected value would make up data. |
| Exact duplicates | 5,268 | Remove, keep one copy | The same invoice, product, quantity, time and customer, loaded twice. Keeping both would double count sales. |
| Cancellations (`C` invoices) | 9,288 | Keep, add flag `is_cancelled` | They are real events. Keeping them lets totals reconcile. Revenue analysis filters them out. |
| Zero or negative quantity | 10,624 | Keep, add flag | Some may overlap with cancellations; that overlap has not been measured yet. The flag covers these rows without guessing. |
| Missing description | 1,454 | Keep, set description to `UNKNOWN` | The stock code still identifies the product, so the sale is still valid. |
| Extreme quantity (e.g. 80,995) | Not yet counted | Flag only, do not remove | A large quantity can be a real bulk order. The threshold for flagging is not decided yet. |

## Quarantine

Quarantined rows are not deleted. They move to a `rejected_rows` table with a `reason` column (for example `zero_unit_price` or `negative_unit_price`). This keeps every excluded row traceable.

Order of processing, so each row is counted once:

1. Remove exact duplicates, keeping one copy.
2. Quarantine rows with a zero or negative unit price.
3. Load everything else into the clean table.

Reconciliation check after each run:

```
rows in raw table = rows in clean table + rows quarantined + duplicates removed
```

## Cleaning run

Run with `scripts/clean.py` on the raw table loaded from the Kaggle file. The script checks the reconciliation and rolls back if it fails.

| Step | Rows |
|---|---|
| Raw rows | 541,909 |
| Exact duplicates removed | 5,268 |
| Rows after deduplication | 536,641 |
| Rejected (zero or negative unit price) | 2,512 |
| Clean rows | 534,129 |

Reconciliation: 536,641 = 534,129 + 2,512, and 541,909 = 536,641 + 5,268.

The profile counted 2,517 zero or negative prices in the raw table (2,515 zero, 2 negative). The run rejects 2,512. The 5 difference are zero-price rows that had exact duplicates. Deduplication runs first, so each of those is counted once, as one rejected row.

Duplicates are removed, not moved to `rejected_rows`, so the removed copies are not stored anywhere. Their count appears only in this run's output.

Customer reconciliation for rows without a CustomerID:

| Step | Rows |
|---|---|
| Raw rows with NULL customer_id | 135,080 |
| Removed as duplicates (inferred from the difference) | 43 |
| Rejected as zero or negative price | 2,472 |
| Transformed rows with NULL customer_id | 132,565 |

The 43 duplicates are inferred, not queried directly: 135,080 − 2,472 − 132,565 = 43. The 40 other rejected rows (2,512 − 2,472) have a CustomerID, so they don't appear in this table.

The raw table has 4,372 distinct customers, and the clean data has 4,371. The one missing customer (13256) has only one row, a zero-price line of 12,540 units, which was rejected. That customer has no valid sales, so they are not in `dim_customer`. The rejected row still holds the customer ID, so the customer can be traced.

Flags and values set on clean rows:
- `is_cancelled`: true for invoices starting with `C`.
- `has_nonpositive_quantity`: true for quantity zero or negative.
- `description`: `UNKNOWN` where the source was missing or empty.
- `customer_id`: left as NULL for rows without a CustomerID. No separate flag. A NULL is the marker.

Product codes whose only rows were rejected are absent from `dim_product`. For example, `DCGS0055` has no description and a zero price, so its one row was rejected. That is why the `unknown_product_descriptions` check reports 0.

## Transformation

Run with `scripts/transform.py` on the clean table. It rebuilds `transformed_online_retail` on every run, so the result is the same each time.

Type conversions. All source values were text, so the table is rebuilt with typed columns. A check on every value found no failed conversions.

| Column | Source type | Target type | Reason |
|---|---|---|---|
| `quantity` | TEXT | INTEGER | Whole units, needed for sums. |
| `unit_price` | TEXT | NUMERIC(10,2) | Money is stored as an exact decimal. Floats round, which causes cent errors in totals. |
| `invoice_date` | TEXT | TIMESTAMP | Needed for filtering and for the monthly partitions in Step 4. |
| `customer_id` | TEXT such as `17850.0` | INTEGER | An ID, not a quantity. The source's `.0` is removed by casting through NUMERIC first. NULL stays NULL. |

Standardization:
- `stock_code`: trimmed and uppercased with `UPPER(TRIM(...))`, so `m` becomes `M` and `gift_0001_20` becomes `GIFT_0001_20`.
- `country`: `EIRE` becomes `Ireland` (the old name for Ireland) and `RSA` becomes `South Africa` (the country code). Other values are unchanged. `Unspecified` and `European Community` are kept as they are, because they are values in the source, not country names to correct.

The `UPDATE` is safe to run twice. Standardized values do not match the old values, so a rerun changes nothing.

Verification, comparing the output with the clean table:

| Check | Expected | Result |
|---|---|---|
| Row count | Same as clean table | 534,129 |
| Stock codes not standardized | 0 | 0 |
| Ireland rows | Same as `EIRE` rows in clean table | 8,180 |
| South Africa rows | Same as `RSA` rows in clean table | 57 |

The script raises an error if any check fails, which rolls back the run.

## Open questions

- Which threshold, if any, triggers the flag for extreme quantities.
