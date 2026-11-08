import os 
from datetime import datetime
from pathlib import Path 

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")
REPORT = PROJECT_ROOT / "docs" / "query_plans.md"

conn_params = dict(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

MATERIALIZED_VIEW = """
    DROP MATERIALIZED VIEW IF EXISTS mv_monthly_revenue;
    CREATE MATERIALIZED VIEW mv_monthly_revenue AS
    SELECT DATE_TRUNC('month', f.invoice_date)::date AS month,
            f.country,
            SUM(f.line_total) AS revenue
    FROM fact_sales f
    WHERE NOT f.is_cancelled
    GROUP BY 1, 2;
    CREATE UNIQUE INDEX ON mv_monthly_revenue (month, country);

"""

QUERIES = {
    "Revenue by product category": """
        SELECT p.category, SUM(f.line_total) AS revenue
        FROM fact_sales f
        JOIN dim_product p USING (product_key)
        WHERE NOT f.is_cancelled
        GROUP BY p.category

""", 
    "Top 10 customers by revenue": """
        SELECT c.customer_id, SUM(f.line_total) AS revenue
        FROM fact_sales f
        JOIN dim_customer c USING (customer_key)
        GROUP BY c.customer_id
        ORDER BY revenue DESC
        LIMIT 10
""",
    "One month of sales (June 2011)": """
        SELECT SUM(line_total) AS revenue
        FROM fact_sales 
        WHERE invoice_date >= '2011-06-01' AND invoice_date < '2011-07-01'
    """,
    "One customer's orders (point lookup)": """
        SELECT COUNT(*) FROM fact_sales WHERE customer_key = 100
    """,
    "One product's sales (point lookup)": """
        SELECT COUNT(*) FROM fact_sales WHERE product_key = 1
    """,
    "One day's sales (point lookup)": """
        SELECT COUNT(*) FROM fact_sales WHERE date_key = 100
    """,
    "Monthly revenue by country, from the fact table": """
        SELECT DATE_TRUNC('month', invoice_date)::date AS month, country, SUM(line_total) AS revenue
        FROM fact_sales
        WHERE NOT is_cancelled
        GROUP BY 1, 2
    """,
    "Monthly revenue by country, from the materialized view": """
        SELECT month, country, revenue
        FROM mv_monthly_revenue
        WHERE country = 'United Kingdom'
    """,
}

def explain(cur, query):
    cur.execute("EXPLAIN ANALYZE "+ query)
    return "\n".join(row[0] for row in cur.fetchall())

def main():
    lines = [
        "# Query plans",
        "",
        f"Generated {datetime.now():%Y-%m-%d %H:%M:%S} by `scripts/performance.py`.",
        "",
        "Each query is run twice: with index scans allowed, and with index scans turned off. "
        "The second run shows what the planner does without the indexes.",
        "",
    ]

    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(MATERIALIZED_VIEW)

            for title, query in QUERIES.items():
                cur.execute("RESET enable_indexscan; RESET enable_bitmapscan;")
                with_indexes = explain(cur, query)

                cur.execute("SET enable_indexscan = off; SET enable_bitmapscan = off;")
                without_indexes = explain(cur, query)
                cur.execute("RESET enable_indexscan; RESET enable_bitmapscan;")

                lines += [
                    f"## {title}", "",
                    "With indexes:", "```", with_indexes, "```", "",
                    "Index scans turned off:", "```", without_indexes, "```", "",
                ]

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()