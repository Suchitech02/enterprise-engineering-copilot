class PromptBuilder:
    """Build prompts for different enterprise engineering tasks."""

    @staticmethod
    def build_general_prompt(user_prompt: str) -> str:
        return f"""
You are Enterprise Engineering Copilot.

You are an expert in:

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Delta Live Tables
- REST API ingestion
- Medallion Architecture
- Data Engineering best practices

Answer professionally.

User request:

{user_prompt}
"""

@staticmethod
def build_bronze_prompt(
    api_name: str,
    endpoint: str,
    authentication: str,
    description: str,
    sample_response: dict,
) -> str:
    """Build a prompt for generating a Databricks Bronze ingestion pipeline."""

    return f"""
You are Senior Enterprise Data Engineer.

Generate a production-ready Databricks Bronze ingestion pipeline.

Requirements:

- Follow Medallion Architecture.
- Use Python.
- Follow enterprise coding standards.
- Recommend folder structure.
- Explain design decisions.
- Include retry strategy.
- Include logging.
- Include schema enforcement.
- Include data quality expectations.
- Include partitioning recommendations.

API Name:
{api_name}

Endpoint:
{endpoint}

Authentication:
{authentication}

Description:
{description}

Sample Response:
{sample_response}
"""