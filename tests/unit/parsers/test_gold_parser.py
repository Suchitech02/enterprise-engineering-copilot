from copilot.parsers.gold_parser import GoldParser


def test_parse_gold_response() -> None:
    answer = """
## SUMMARY

Gold pipeline

## PYTHON_CODE

```python
print("gold")
```

## SQL_CODE

```sql
SELECT * FROM gold.sales;
```

## KPIS

1. Total Sales
2. Average Order Value

## AGGREGATIONS

1. Daily Sales
2. Monthly Sales

## ASSUMPTIONS

1. Silver data is validated.
"""

    response = GoldParser.parse(answer)

    assert response.summary == "Gold pipeline"

    assert response.python_code == 'print("gold")'

    assert response.sql_code == ("SELECT * FROM gold.sales;")

    assert response.kpis == [
        "Total Sales",
        "Average Order Value",
    ]

    assert response.aggregations == [
        "Daily Sales",
        "Monthly Sales",
    ]

    assert response.assumptions == [
        "Silver data is validated.",
    ]
