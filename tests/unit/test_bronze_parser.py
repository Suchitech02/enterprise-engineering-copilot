from copilot.parsers.bronze_parser import BronzeParser


def test_parse_bronze_response():
    response = """
## SUMMARY

Sample summary

## PYTHON_CODE

print("hello")

## SQL_CODE

SELECT 1;

## FOLDER_STRUCTURE

src/

## QUALITY_RULES

1. Rule one
2. Rule two

## ASSUMPTIONS

1. Assumption one
2. Assumption two
"""

    result = BronzeParser.parse(response)

    assert result.summary == "Sample summary"

    assert result.python_code == 'print("hello")'

    assert result.sql_code == "SELECT 1;"

    assert result.folder_structure == "src/"

    assert result.quality_rules == [
        "Rule one",
        "Rule two",
    ]

    assert result.assumptions == [
        "Assumption one",
        "Assumption two",
    ]
