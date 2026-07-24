class SilverPromptBuilder:
    """Prompt builder for Silver pipeline generation."""

    @staticmethod
    def build_prompt(
        bronze_code: str,
        business_rules: str,
        target_table: str,
    ) -> str:
        return f"""
You are an expert Databricks Data Engineer.

Generate a production-ready Silver layer pipeline.

Requirements:

- Read the Bronze dataset.
- Apply the required business transformations.
- Improve data quality.
- Remove duplicate records when appropriate.
- Handle null values appropriately.
- Produce clean PySpark code.
- Produce equivalent SQL when possible.

Business Rules:
{business_rules}

Target Table:
{target_table}

Bronze Pipeline:
{bronze_code}

Return your answer using EXACTLY this structure:

## SUMMARY

...

## PYTHON_CODE

```python```

...

## SQL_CODE

```SQL```

...
"""
