# Raw Data Profile



## Scope

- **Source:** `data/raw/online_retail.csv` (Kaggle "Online Retail Dataset")
- **Loaded by:** `scripts/ingest.py` into `raw_online_retail` in database `retail_dw`
- **Rows after load:** 541,909
- **Database:** PostgreSQL 18.1 (Windows)

All columns in the raw table are `TEXT`, so every check below compares text unless it casts to a number. Each query was run in pgAdmin's Query Tool, connected to `retail_dw`.

## Summary

Percentages use the 541,909 total rows.

| # | Check | Rows | % of total |
|---|---|---|---|
| 1 | `customer_id` is NULL | 135,080 | 24.9% |
| 2 | `customer_id` is an empty string | 0 | 0.0% |
| 3 | Cancellation invoices (`invoice_no` starts with `C`) | 9,288 | 1.7% |
| 4 | Quantity zero or negative | 10,624 | 2.0% |
| 5 | Unit price exactly zero (`0.0`) | 2,515 | 0.5% |
| 6 | Unit price negative | 2 | 0.0% |
| 7 | Description is NULL or empty | 1,454 | 0.3% |
| 8 | Exact duplicate rows | 5,268 | 1.0% |

## Check details

Each check lists the query used and the result.

### 1 and 2. Missing CustomerID

```sql
SELECT COUNT(*) FROM raw_online_retail WHERE customer_id IS NULL;
SELECT COUNT(*) FROM raw_online_retail WHERE customer_id = '';
```

Results: 135,080 NULL, 0 empty strings. The CSV leaves the field blank, and COPY loads a blank unquoted field as NULL. Missing customers are therefore true NULLs, not empty text.

### 3. Cancellations

```sql
SELECT COUNT(*) FROM raw_online_retail WHERE invoice_no LIKE 'C%';
```

Result: 9,288.

### 4. Zero or negative quantity

```sql
SELECT COUNT(*) FROM raw_online_retail
WHERE quantity LIKE '-%' OR quantity = '0';
```

Result: 10,624. This is a text match. It catches values starting with `-` and the exact text `0`. A value written differently, such as `0.0`, would not match. This query does not check for those.

### 5 and 6. Unit price zero or negative

The first attempt used text matching and returned 2. That was an undercount, because the zero prices are stored as `0.0`, which does not equal `'0'`. The check was rerun as a numeric comparison:

```sql
SELECT unit_price, COUNT(*)
FROM raw_online_retail
WHERE unit_price::numeric <= 0
GROUP BY unit_price
ORDER BY COUNT(*) DESC;
```

| unit_price (text) | Rows |
|---|---|
| `0.0` | 2,515 |
| `-11062.06` | 2 |

The cast ran over every row without an error, so every `unit_price` value is a valid number.

The two negative-price rows are:

| invoice_no | stock_code | description | quantity | unit_price | customer_id |
|---|---|---|---|---|---|
| A563186 | B | Adjust bad debt | 1 | -11062.06 | NULL |
| A563187 | B | Adjust bad debt | 1 | -11062.06 | NULL |

Both have stock code `B`, which is not a product code, and no customer. The description points to an accounting adjustment, not a sale.

### 7. Missing description

```sql
SELECT COUNT(*) FROM raw_online_retail
WHERE description IS NULL OR description = '';
```

Result: 1,454.

### 8. Exact duplicates

A duplicate is a row whose eight source columns match another row exactly. `loaded_at` is excluded, because it's set by the load, not by the source.

```sql
SELECT COUNT(*) - (
    SELECT COUNT(*) FROM (
        SELECT DISTINCT invoice_no, stock_code, description, quantity,
               invoice_date, unit_price, customer_id, country
        FROM raw_online_retail
    ) d
) AS duplicate_rows
FROM raw_online_retail;
```

Result: 5,268 rows beyond the first copy of each distinct row.

## Open items

These were not measured yet. They should be checked before the cleaning script is final.

- Whether the 2,515 zero-price rows are also cancellations, and how many have a missing CustomerID.
- Extreme quantities (for example 80,995 units). No count has been taken for this.
- The format of `customer_id` values (stored as text such as `17850.0`). The float suffix is handled in Step 3.
