"""Analytics queries over sales.db returned as pandas DataFrames."""
import sqlite3
import pandas as pd

QUERIES = {
    "revenue_by_category": "SELECT category, ROUND(SUM(qty*price),2) AS revenue, SUM(qty) AS units FROM sales GROUP BY category ORDER BY revenue DESC",
    "top_products": "SELECT product, ROUND(SUM(qty*price),2) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 3",
    "monthly_revenue": "SELECT substr(day,1,7) AS month, ROUND(SUM(qty*price),2) AS revenue FROM sales GROUP BY month ORDER BY month",
    "running_total": "WITH m AS (SELECT substr(day,1,7) AS month, SUM(qty*price) AS r FROM sales GROUP BY month) SELECT month, ROUND(r,2) AS revenue, ROUND(SUM(r) OVER (ORDER BY month),2) AS cumulative FROM m",
}


def run(name, db="sales.db"):
    with sqlite3.connect(db) as con:
        return pd.read_sql_query(QUERIES[name], con)


if __name__ == "__main__":
    for n in QUERIES:
        print(f"## {n}\n{run(n).to_string(index=False)}\n")
