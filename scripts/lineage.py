import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

conn_params = dict(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# source, target, transformation, query that returns the row count written to the target
LINEAGE = [
    ("data/raw/online_retail.csv", "raw_online_retail",
     "Loaded as text, no changes (ingest.py)",
     "SELECT COUNT(*) FROM raw_online_retail"),
    ("raw_online_retail", "clean_online_retail",
     "Duplicates removed, zero and negative prices moved out, missing descriptions set to UNKNOWN, flags added (clean.py)",
     "SELECT COUNT(*) FROM clean_online_retail"),
    ("raw_online_retail", "rejected_rows",
     "Zero and negative price rows, with the reason (clean.py)",
     "SELECT COUNT(*) FROM rejected_rows"),
    ("clean_online_retail", "transformed_online_retail",
     "Typed columns, stock codes uppercased, EIRE and RSA renamed (transform.py)",
     "SELECT COUNT(*) FROM transformed_online_retail"),
    ("transformed_online_retail", "dim_date",
     "One row per invoice date (warehouse.py)",
     "SELECT COUNT(*) FROM dim_date"),
    ("transformed_online_retail", "dim_customer",
     "One row per customer ID (warehouse.py)",
     "SELECT COUNT(*) FROM dim_customer"),
    ("transformed_online_retail", "dim_product",
     "One row per stock code with category (warehouse.py)",
     "SELECT COUNT(*) FROM dim_product"),
    ("transformed_online_retail and dimensions", "fact_sales",
     "One row per invoice line, linked to dimension keys (warehouse.py)",
     "SELECT COUNT(*) FROM fact_sales"),
    ("fact_sales", "mv_monthly_revenue",
     "Revenue by month and country, cancellations excluded (performance.py)",
     "SELECT COUNT(*) FROM mv_monthly_revenue"),
    ("transformed_online_retail", "archive_transformed",
     "Copy tagged with run_id (archive.py)",
     "SELECT COUNT(*) FROM archive_transformed WHERE run_id = (SELECT MAX(run_id) FROM archive_transformed)"),
]


def main():
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS lineage (
                    lineage_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    run_id          TEXT,
                    recorded_at     TIMESTAMP DEFAULT now(),
                    source          TEXT,
                    target          TEXT,
                    transformation  TEXT,
                    row_count       BIGINT
                )
            """)

            cur.execute("SELECT MAX(run_id) FROM archive_transformed")
            run_id = cur.fetchone()[0]

            # Rerunning lineage for the same run replaces its rows instead of adding duplicates.
            cur.execute("DELETE FROM lineage WHERE run_id = %s", (run_id,))

            for source, target, transformation, count_sql in LINEAGE:
                cur.execute(count_sql)
                row_count = cur.fetchone()[0]
                cur.execute("""
                    INSERT INTO lineage (run_id, source, target, transformation, row_count)
                    VALUES (%s, %s, %s, %s, %s)
                """, (run_id, source, target, transformation, row_count))

    print(f"Recorded {len(LINEAGE)} lineage steps for run {run_id}")


if __name__ == "__main__":
    main()
