# sqlite-sales-analytics

SQL analytics with SQLite and pandas: revenue by category, top products, monthly revenue and a running total using a window function. `build_db.py` generates a seeded synthetic sales table (400 rows).

## Run

```bash
pip install -r requirements.txt
python build_db.py
python analytics.py
pytest
```

## Output (reproduced)

```
$ python3 analytics.py
## revenue_by_category
   category  revenue  units
Electronics 272100.0    369
  Furniture  67280.0    370
 Stationery   1341.0    375

## top_products
product  revenue
 Laptop 152100.0
  Phone 120000.0
   Desk  44000.0

## monthly_revenue
  month  revenue
2026-01  56155.0
2026-02  45579.0
2026-03  66238.0
2026-04  53654.0
2026-05  53605.0
2026-06  65490.0

## running_total
  month  revenue  cumulative
2026-01  56155.0     56155.0
2026-02  45579.0    101734.0
2026-03  66238.0    167972.0
2026-04  53654.0    221626.0
2026-05  53605.0    275231.0
2026-06  65490.0    340721.0

$ pytest -q
3 passed in 0.20s
```

## Limits

- Data is synthetic and randomly generated, so the numbers say nothing about real sales. Window functions need SQLite 3.25 or newer.
