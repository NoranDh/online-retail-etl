import os
from datetime import datetime
from pathlib import Path 

import psycopg
from psycopg import sql
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

# layer, table, source, transformation 

CATALOG = [
    ("raw", "raw_online_retail", "data/raw/online_retail.csv",
     "Loaded as-is, every column TEXT (ingest.py)"),
    ("clean", "clean_online_retail", "raw_online_retail",
     "Duplicates removed, zero and negative prices moved out, missing descriptions set to UNKNOWN, cancellation flags (clean.py)"),
    ("clean", "rejected_rows", "raw_online_retail",
     "Zero and negative price rows, with the reason (clean.py)"),
    ("transform", "transformed_online_retail", "clean_online_retail",
     "Typed columns, stock codes uppercased, EIRE and RSA renamed (transform.py)"),
    ("warehouse", "dim_date", "transformed_online_retail",
     "One row per invoice date (warehouse.py)"),
    ("warehouse", "dim_customer", "transformed_online_retail",
     "One row per customer ID (warehouse.py)"),
    ("warehouse", "dim_product", "transformed_online_retail",
     "One row per stock code with category (warehouse.py)"),
    ("warehouse", "fact_sales", "transformed_online_retail and dimensions",
     "One row per invoice line, monthly partitions on invoice_date (warehouse.py)"),
    ("monitoring", "dq_results", "all tables",
     "Check results for every run (data_quality.py)"),
    ("archive", "archive_transformed", "transformed_online_retail",
     "Copy of each run's transformed data, tagged with run_id (archive.py)"),
]

def main():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS archive_transformed (
                run_id           TEXT,
                archived_at      TIMESTAMP DEFAULT now(),
                LIKE transformed_online_retail
                
                )
        """)
            cur.execute("""
                INSERT INTO archive_transformed
                SELECT %s, now(), t.* FROM transformed_online_retail t
            """, (run_id,))
            cur.execute("SELECT COUNT(*) FROM archive_transformed WHERE run_id = %s", (run_id,))
            archived = cur.fetchone()[0]

            cur.execute("""
                CREATE TABLE IF NOT EXISTS metadata_catalog (
                    table_name        TEXT PRIMARY KEY,
                    layer             TEXT,
                    source            TEXT,
                    transformation    TEXT,
                    storage_location  TEXT,
                    row_count         BIGINT,
                    last_run_id       TEXT,
                    updated_at        TIMESTAMP DEFAULT now()
                )
            """)
            for layer, table, source, transformation in CATALOG:
                cur.execute(sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table)))
                row_count = cur.fetchone()[0]
                cur.execute("""
                    INSERT INTO metadata_catalog
                        (table_name, layer, source, transformation, storage_location,
                         row_count, last_run_id, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, now())
                    ON CONFLICT (table_name) DO UPDATE SET
                        layer           = EXCLUDED.layer,
                        source          = EXCLUDED.source,
                        transformation  = EXCLUDED.transformation,
                        storage_location = EXCLUDED.storage_location,
                        row_count       = EXCLUDED.row_count,
                        last_run_id     = EXCLUDED.last_run_id,
                        updated_at      = now()
                """, (table, layer, source, transformation,
                      f"retail_dw.public.{table}", row_count, run_id))

    print(f"Archived {archived} rows to archive_transformed for run {run_id}")
    print(f"Catalog updated for {len(CATALOG)} tables")


if __name__ == "__main__":
    main()



