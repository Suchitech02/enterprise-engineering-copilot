class GoldPromptBuilder:
    """Build Prompts for Gold Pipeline generation."""

    @staticmethod
    def build_prompt(
        silver_code: str,
        business_requirements: str,
        target_table: str,
    ) -> str:
        """Build a prompt for generating a gold pipeline."""

        return f"""
You are a Principal Enterprise Data Engineer.

Generate a production-ready Databricks Gold pipeline.

Requirements

- Databricks Runtime 17+
- Python 3.12+
- Unity Catalog
- Delta Lake
- Medallion Architecture
- Enterprise coding standards
- Optimized Spark transformations
- Business-ready reporting tables
- Maintainable and scalable code

Input Silver Pipeline

{silver_code}

Business Requirements

{business_requirements}

Target Table

{target_table}

IMPORTANT

Return your answer using EXACTLY the following headings.

## SUMMARY

Provide a concise explanation.

## PYTHON_CODE

Return only the Python implementation.

## SQL_CODE

Return SQL required for the Gold table.

## KPIS

List the business KPIs created.

## AGGREGATIONS

List the aggregations performed.

## ASSUMPTIONS

List any assumptions you made.

Do not skip any section.
Do not invent extra headings.
"""
