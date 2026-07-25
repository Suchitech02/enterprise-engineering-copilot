class DABPromptBuilder:
    """Build prompts for Databricks Asset Bundle generation."""

    @staticmethod
    def build_prompt(
        project_name: str,
        catalog: str,
        schema_name: str,
        bronze_pipeline: str,
        silver_pipeline: str,
        gold_pipeline: str,
        environment: str,
    ) -> str:
        """Build a prompt for generating a Databricks Asset Bundle."""

        return f"""
You are a Principal Databricks Architect.

Generate a production-ready Databricks Asset Bundle (DAB).

Requirements

- Databricks Asset Bundles
- Databricks Runtime 17+
- Unity Catalog
- Medallion Architecture
- Enterprise coding standards
- Environment-specific deployment
- Reusable configuration
- CI/CD ready
- Production-ready structure

Project Name

{project_name}

Catalog

{catalog}

Schema

{schema_name}

Environment

{environment}

Bronze Pipeline

{bronze_pipeline}

Silver Pipeline

{silver_pipeline}

Gold Pipeline

{gold_pipeline}

IMPORTANT

Return your answer using EXACTLY the following headings.

## SUMMARY

Provide a concise explanation.

## DATABRICKS_YML

Return the main databricks.yml file.

## JOBS_YML

Return the jobs.yml configuration.

## PIPELINES_YML

Return the pipelines.yml configuration.

## VARIABLES_YML

Return the variables.yml configuration.

## TARGETS_YML

Return the targets.yml configuration.

## FOLDER_STRUCTURE

Show the recommended bundle structure.

## ASSUMPTIONS

List any assumptions you made.

Do not skip any section.
Do not invent extra headings.
"""
