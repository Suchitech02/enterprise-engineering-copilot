from copilot.parsers.silver_parser import SilverParser


def test_parse_silver_response() -> None:
    answer = """
## SUMMARY

Silver pipeline

## PYTHON_CODE

```python
print("silver")

## SQL_CODE

```sql
SELECT * FROM silver.customer;
```

## TRANSFORMATIONS


1. Remove duplicates
2. Standardize names


## QUALITY_RULES

1. customer_id must be unique


## ASSUMPTIONS

1. Bronze data is valid

"""

    response = SilverParser.parse(answer)

    assert response.summary == "Silver pipeline"
    assert response.python_code == 'print("silver")'
    assert response.sql_code == "SELECT * FROM silver.customer;"
    assert response.transformations == [
        "Remove duplicates",
        "Standardize names",
    ]
    assert response.quality_rules == [
        "customer_id must be unique",
    ]
    assert response.assumptions == [
        "Bronze data is valid",
    ]
