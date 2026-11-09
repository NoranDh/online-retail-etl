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

with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE IF EXISTS transformed_online_retail;

        CREATE TABLE transformed_online_retail AS
        SELECT 
                invoice_no,             
                stock_code,
                description, 
                quantity::integer               AS quantity,
                invoice_date::timestamp         AS invoice_date,
                unit_price::numeric(10,2)       AS unit_price,
                customer_id::numeric::integer   AS customer_id,
                country,
                is_cancelled,
                has_nonpositive_quantity,
                is_outlier,
                loaded_at
        
        FROM clean_online_retail;
 """)

        cur.execute("""
        UPDATE transformed_online_retail
           SET stock_code = UPPER(TRIM(stock_code)),
           country = CASE
           WHEN country = 'EIRE' THEN 'Ireland'
           WHEN country = 'RSA' THEN 'South Africa'
           ELSE country
    END;
    """)

        # validate the results by comparing clean with transform
        cur.execute("SELECT COUNT(*) FROM clean_online_retail")
        expected_total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM transformed_online_retail")
        total = cur.fetchone()[0]
        if total != expected_total:
            raise ValueError(f"expected {expected_total} rows, got {total}")

        cur.execute("""
            SELECT COUNT(*) FROM transformed_online_retail
            WHERE stock_code <> UPPER(TRIM(stock_code))
        """)
        bad_codes = cur.fetchone()[0]
        if bad_codes != 0:
            raise ValueError(f"{bad_codes} stock codes were not standardized")

        cur.execute("SELECT COUNT(*) FROM clean_online_retail WHERE country = 'EIRE'")
        expected_ireland = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM transformed_online_retail WHERE country = 'Ireland'")
        ireland = cur.fetchone()[0]
        if ireland != expected_ireland:
            raise ValueError(f"expected {expected_ireland} Ireland rows, got {ireland}")

        cur.execute("SELECT COUNT(*) FROM clean_online_retail WHERE country = 'RSA'")
        expected_sa = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM transformed_online_retail WHERE country = 'South Africa'")
        south_africa = cur.fetchone()[0]
        if south_africa != expected_sa:
            raise ValueError(f"expected {expected_sa} South Africa rows, got {south_africa}")

        print(f"Transformed rows:    {total}")
        print(f"Ireland rows:        {ireland}")
        print(f"South Africa rows:   {south_africa}")