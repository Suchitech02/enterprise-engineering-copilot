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
You are a Principal Enterprise Data Engineer.

Generate a production-ready Databricks Bronze ingestion pipeline.

Requirements

- Use Medallion Architecture
- Python 3.11+
- Databricks Runtime 17+
- Unity Catalog
- Enterprise coding standards
- Retry strategy
- Logging
- Schema enforcement
- Data quality checks
- Configuration driven design

API Information

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

IMPORTANT

Return your answer using EXACTLY the following headings.

## SUMMARY

Provide a concise explanation.

## PYTHON_CODE

Return only the Python implementation.

## SQL_CODE

Return SQL required for Bronze tables.

## FOLDER_STRUCTURE

Show the recommended project structure.

## QUALITY_RULES

List the recommended quality rules.

## ASSUMPTIONS

List any assumptions you made.

Do not skip any section.
Do not invent extra headings.
"""

    @staticmethod
    def build_chat_prompt(
        history: list[dict[str, str]],
    ) -> str:
        """Build a conversational prompt from the message history."""

        conversation = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in history
        )

        return f"""
    You are Enterprise Engineering Copilot.

    Continue the following conversation naturally.

    {conversation}
    """