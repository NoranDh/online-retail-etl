import os

import psycopg
from dotenv import load_dotenv
from pathlib import Path



PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail.csv"

load_dotenv(PROJECT_ROOT / ".env")


conn_params = dict(
    host = os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),

)

with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cur:

        cur.execute("""
            DROP TABLE IF EXISTS raw_online_retail;
            CREATE TABLE raw_online_retail (
                invoice_no   TEXT,
                stock_code   TEXT,
                description  TEXT,
                quantity     TEXT,
                invoice_date TEXT,
                unit_price   TEXT,
                customer_id  TEXT,
                country      TEXT,
                loaded_at    TIMESTAMP DEFAULT now()
            );

"""
        )

# Bulk load with COPY 

        copy_sql = """
    COPY raw_online_retail (invoice_no, stock_code, description, quantity,
                            invoice_date, unit_price, customer_id, country)
    FROM STDIN WITH (FORMAT csv, HEADER true)

"""

        with open(CSV_PATH, "rb") as f:
            with cur.copy(copy_sql) as copy:
                for chunk in iter(lambda: f.read(65536), b""):
                 copy.write(chunk)

# Count the rows 

        cur.execute("SELECT COUNT(*) FROM raw_online_retail;")
        print("Rows loaded:", cur.fetchone()[0])