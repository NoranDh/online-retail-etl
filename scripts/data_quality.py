import os 
from datetime import datetime
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")
LOG_FILE = PROJECT_ROOT / "logs" / "data_quality.log"

conn_params = dict(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

# Runs after warehouse.py and checks the warehouse tables themselves.
# (name, query, rule, threshold): "min" means observed must be at least the threshold, "max" at most
CHECKS = [
    ("fact_rows", "SELECT COUNT(*) FROM fact_sales", "min", 500000),
    ("fact_rows_match_transformed",
     """SELECT ABS((SELECT COUNT(*) FROM fact_sales)
                - (SELECT COUNT(*) FROM transformed_online_retail))""",
     "max", 0),
    ("fact_missing_customer_pct",
     "SELECT 100.0 * COUNT(*) FILTER (WHERE customer_key IS NULL) / COUNT(*) FROM fact_sales",
     "max", 30.0),
    ("unknown_product_descriptions",
     "SELECT COUNT(*) FROM dim_product WHERE description = 'UNKNOWN'",
     "max", 50),
]

def main():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(""" 
                CREATE TABLE IF NOT EXISTS dq_results (
                    run_id      TEXT,
                    checked_at  TIMESTAMP DEFAULT now(),
                    check_name  TEXT,
                    observed    NUMERIC,
                    rule        TEXT,
                    threshold    NUMERIC,
                    status      TEXT
                )
    """)
            results = []
            for name, query, rule, threshold in CHECKS:
                cur.execute(query)
                observed = float(cur.fetchone()[0])
                ok =  observed >= threshold if rule == "min" else observed <= threshold 
                status = "PASS" if ok else "FAIL"
                results.append((name, observed, rule, threshold, status))
                cur.execute(
                    "INSERT INTO dq_results (run_id, check_name, observed, rule, threshold, status) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (run_id, name, observed, rule, threshold, status), 
                )

        LOG_FILE.parent.mkdir(exist_ok=True)
        with open(LOG_FILE, "a") as log:
            for name, observed, rule, threshold, status in results:
                line = f"{run_id} {status} {name} observed={observed} rule={rule} threshold={threshold}"
                log.write(line + "\n")
                print(line)

        failed = [r for r in results if r[4] == "FAIL"]
        if failed:
           
           raise SystemExit(f"{len(failed)} data quality check(s) failed")


if __name__ == "__main__":
    main()
        
