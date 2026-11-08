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
            DROP TABLE IF EXISTS clean_online_retail;
            DROP TABLE IF EXISTS rejected_rows;

            CREATE TABLE clean_online_retail (
                invoice_no               TEXT,
                stock_code               TEXT,
                description              TEXT,
                quantity                 TEXT,
                invoice_date             TEXT,
                unit_price               TEXT,
                customer_id              TEXT,
                country                  TEXT,
                is_cancelled             BOOLEAN,
                has_nonpositive_quantity BOOLEAN, 
                loaded_at                TIMESTAMP

            );

            CREATE TABLE rejected_rows (
                LIKE raw_online_retail,
                reason      TEXT,
                rejected_at TIMESTAMP DEFAULT now()
            
            );

            CREATE TEMP TABLE deduped AS 
            SELECT DISTINCT ON (invoice_no, stock_code, description, quantity,
                                invoice_date, unit_price, customer_id, country) *
            FROM raw_online_retail
            ORDER BY invoice_no, stock_code, description, quantity,
                     invoice_date, unit_price, customer_id, country, loaded_at;

        """)

        cur.execute("""
            INSERT INTO rejected_rows
            SELECT d.*,
                   CASE WHEN d.unit_price::numeric < 0
                        THEN 'negative_unit_price'
                        ELSE 'zero_unit_price' END,
                    now()
            FROM deduped d
            WHERE d.unit_price::numeric <=0;
        """)

        cur.execute("""
            INSERT INTO clean_online_retail
            SELECT invoice_no,
                   stock_code, 
                   COALESCE(NULLIF(description, ''), 'UNKNOWN'),
                   quantity,
                   invoice_date,
                   unit_price,
                   customer_id,
                   country,
                   invoice_no LIKE 'C%',
                   quantity::numeric <= 0,
                   loaded_at
            FROM deduped
            WHERE unit_price::numeric > 0;

        """)

        cur.execute("""
            SELECT
                (SELECT COUNT(*) FROM raw_online_retail),
                (SELECT COUNT(*) FROM deduped),
                (SELECT COUNT(*) FROM rejected_rows),
                (SELECT COUNT(*) FROM clean_online_retail)
        """)
        raw, deduped, rejected, clean = cur.fetchone()

        if deduped != clean + rejected:
            raise ValueError(f"Reconciliation failed: {deduped} != {clean} + {rejected}")

        print(f"Raw rows:   {raw}")
        print(f"Duplicates removed:   {raw - deduped}")
        print(f"Rejected (price):  {rejected}")
        print(f"Clean rows:   {clean}")