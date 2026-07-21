from copilot.prompts.prompt_builder import PromptBuilder


def test_build_bronze_prompt_contains_sections():
    prompt = PromptBuilder.build_bronze_prompt(
        api_name="Customer API",
        endpoint="https://api.company.com/customers",
        authentication="OAuth2",
        description="Returns customer master data",
        sample_response={
            "customerId": 1001,
            "customerName": "Alice",
        },
    )

    assert "## SUMMARY" in prompt
    assert "## PYTHON_CODE" in prompt
    assert "## SQL_CODE" in prompt
    assert "## FOLDER_STRUCTURE" in prompt
    assert "## QUALITY_RULES" in prompt
    assert "## ASSUMPTIONS" in prompt

def test_build_rag_prompt() -> None:
    """Test building a RAG prompt."""

    prompt = PromptBuilder.build_rag_prompt(
        question="What is Delta Live Tables?",
        documents=[
            "Delta Live Tables simplifies ETL pipelines.",
            "It supports declarative data pipelines.",
        ],
    )

    assert "What is Delta Live Tables?" in prompt
    assert "Delta Live Tables simplifies ETL pipelines." in prompt
    assert "It supports declarative data pipelines." in prompt
