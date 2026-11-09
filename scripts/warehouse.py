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
            DROP MATERIALIZED VIEW IF EXISTS mv_monthly_revenue;
            DROP TABLE IF EXISTS fact_sales;
            DROP TABLE IF EXISTS dim_product;
            DROP TABLE IF EXISTS dim_customer;
            DROP TABLE IF EXISTS dim_date;

            CREATE TABLE dim_date (
            date_key        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            full_date       DATE NOT NULL UNIQUE, 
            year            INTEGER NOT NULL,
            month           INTEGER NOT NULL, 
            day             INTEGER NOT NULL,
            weekday         TEXT NOT NULL
            );

            CREATE TABLE dim_customer (
                customer_key  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                customer_id   INTEGER NOT NULL UNIQUE
            );

            CREATE TABLE dim_product (
                product_key  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                stock_code   TEXT NOT NULL UNIQUE,
                description  TEXT NOT NULL,
                category     TEXT NOT NULL
            );

            INSERT INTO dim_date (full_date, year, month, day, weekday)
            SELECT
                d,
                EXTRACT(YEAR FROM d)::integer,
                EXTRACT(MONTH FROM d)::integer,
                EXTRACT(DAY FROM d)::integer,
                TRIM(TO_CHAR(d, 'Day'))
            FROM (SELECT DISTINCT invoice_date::date AS d FROM transformed_online_retail) dates
            ORDER BY d;

            INSERT INTO dim_customer (customer_id)
            SELECT DISTINCT customer_id
            FROM transformed_online_retail
            WHERE customer_id IS NOT NULL
            ORDER BY customer_id;

            INSERT INTO dim_product (stock_code, description, category)
            SELECT
                codes.stock_code,
                COALESCE(names.description, 'UNKNOWN'),
                CASE
                    WHEN codes.stock_code IN ('POST', 'DOT', 'C2', 'BANK CHARGES', 'AMAZONFEE', 'CRUK') THEN 'service_fee'
                    WHEN codes.stock_code IN ('M', 'D', 'S', 'B') THEN 'adjustment'
                    WHEN codes.stock_code LIKE 'GIFT%' THEN 'gift_voucher'
                    ELSE 'product'
                END
            FROM (SELECT DISTINCT stock_code FROM transformed_online_retail) codes
            LEFT JOIN (
                SELECT DISTINCT ON (stock_code) stock_code, description
                FROM transformed_online_retail
                WHERE description <> 'UNKNOWN' AND LOWER(description) <> 'ebay'
                ORDER BY stock_code, description
            ) names USING (stock_code)
            ORDER BY codes.stock_code;

""")
        cur.execute(""" 
            CREATE TABLE fact_sales (
                sales_key                INTEGER GENERATED ALWAYS AS IDENTITY,
                invoice_no               TEXT NOT NULL,
                invoice_date             TIMESTAMP NOT NULL,
                date_key                 INTEGER NOT NULL REFERENCES dim_date(date_key),
                customer_key             INTEGER REFERENCES dim_customer(customer_key),
                product_key              INTEGER NOT NULL REFERENCES dim_product(product_key),
                country                  TEXT NOT NULL,
                quantity                 INTEGER NOT NULL,
                unit_price               NUMERIC(10,2) NOT NULL,
                line_total               NUMERIC(12,2) NOT NULL,
                is_cancelled             BOOLEAN NOT NULL,
                has_nonpositive_quantity BOOLEAN NOT NULL,
                is_outlier               BOOLEAN NOT NULL,
                PRIMARY KEY (sales_key, invoice_date)
            ) PARTITION BY RANGE (invoice_date);

            DO $$
            DECLARE
                m DATE := (SELECT DATE_TRUNC('month', MIN(invoice_date))::date FROM transformed_online_retail);
                last_month DATE := (SELECT DATE_TRUNC('month', MAX(invoice_date))::date FROM transformed_online_retail);
            BEGIN
                WHILE m <= last_month LOOP
                    EXECUTE format(
                        'CREATE TABLE fact_sales_%s PARTITION OF fact_sales FOR VALUES FROM (%L) TO (%L)',
                        to_char(m, 'YYYY_MM'), m, m + INTERVAL '1 month'
                    );
                    m := m + INTERVAL '1 month';
                END LOOP;
            END $$;

            CREATE TABLE fact_sales_default PARTITION OF fact_sales DEFAULT;
            """)

        cur.execute("""
            INSERT INTO fact_sales (
                invoice_no, invoice_date, date_key, customer_key, product_key,
                country, quantity, unit_price, line_total, is_cancelled, has_nonpositive_quantity,
                is_outlier
            )
            SELECT
                t.invoice_no,
                t.invoice_date,
                d.date_key,
                c.customer_key,
                p.product_key,
                t.country,
                t.quantity,
                t.unit_price,
                t.quantity * t.unit_price,
                t.is_cancelled,
                t.has_nonpositive_quantity,
                t.is_outlier
            FROM transformed_online_retail t
            JOIN dim_date d ON d.full_date = t.invoice_date::date
            JOIN dim_product p ON p.stock_code = t.stock_code
            LEFT JOIN dim_customer c ON c.customer_id = t.customer_id;

            CREATE INDEX idx_fact_sales_product_key  ON fact_sales (product_key);
            CREATE INDEX idx_fact_sales_customer_key ON fact_sales (customer_key);
            CREATE INDEX idx_fact_sales_date_key     ON fact_sales (date_key);
     """)

        cur.execute("SELECT COUNT(*) FROM fact_sales")
        fact_rows = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM transformed_online_retail")
        source_rows = cur.fetchone()[0]
        if fact_rows != source_rows:
            raise ValueError(f"expected {source_rows} fact rows, got {fact_rows}")

        print(f"Warehouse loaded: {fact_rows} sales rows")

        