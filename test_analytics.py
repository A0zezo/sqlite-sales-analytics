import sqlite3
import analytics
from build_db import build


def setup_module(_):
    build("test.db", n=100)


def test_category_revenue_sums_to_total():
    total = sqlite3.connect("test.db").execute("SELECT SUM(qty*price) FROM sales").fetchone()[0]
    assert abs(analytics.run("revenue_by_category", "test.db").revenue.sum() - total) < 1


def test_top_products_sorted():
    r = analytics.run("top_products", "test.db").revenue.tolist()
    assert r == sorted(r, reverse=True) and len(r) == 3


def test_cumulative_ends_at_total():
    r = analytics.run("running_total", "test.db")
    assert abs(r.cumulative.iloc[-1] - r.revenue.sum()) < 1
