class TestPromptBuilder:
    """Build prompts for AI-generated pytest tests."""

    @staticmethod
    def build_test_prompt(
        python_code: str,
    ) -> str:
         """Build the LLM prompt for generating pytest tests."""
        
         return f"""
You are a Senior Python Test Engineer.

Generate production-quality pytest unit tests for the following Databricks Bronze ingestion pipeline.

Requirements:

- Use pytest.
- Mock all external HTTP requests.
- Mock Databricks and Spark dependencies.
- Test the successful ingestion path.
- Test invalid input/schema validation.
- Test retry behaviour.
- Test error handling.
- Return ONLY valid Python code.
- Do not include explanations or Markdown.

Pipeline:

{python_code}
"""