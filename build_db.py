"""Create a synthetic sales database (seeded) in sales.db."""
import random
import sqlite3
from datetime import date, timedelta

rng = random.Random(0)
PRODUCTS = [("Laptop", "Electronics", 900), ("Phone", "Electronics", 600), ("Desk", "Furniture", 250),
            ("Chair", "Furniture", 120), ("Notebook", "Stationery", 5), ("Pen", "Stationery", 2)]


def build(path="sales.db", n=400):
    con = sqlite3.connect(path)
    con.executescript("DROP TABLE IF EXISTS sales; CREATE TABLE sales(id INTEGER PRIMARY KEY, day TEXT, product TEXT, category TEXT, qty INT, price REAL);")
    d0 = date(2026, 1, 1)
    rows = []
    for i in range(n):
        p = rng.choice(PRODUCTS)
        rows.append((i, (d0 + timedelta(days=rng.randrange(180))).isoformat(), p[0], p[1], rng.randint(1, 5), p[2]))
    con.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?)", rows)
    con.commit()
    return con


if __name__ == "__main__":
    build()
