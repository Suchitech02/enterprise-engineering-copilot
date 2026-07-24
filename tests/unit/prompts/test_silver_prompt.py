from copilot.prompts.silver_prompt_builder import SilverPromptBuilder


def test_build_prompt() -> None:
    prompt = SilverPromptBuilder.build_prompt(
        bronze_code="print('bronze')",
        business_rules="Remove duplicates",
        target_table="silver.customer",
    )

    assert "Remove duplicates" in prompt
    assert "silver.customer" in prompt
    assert "print('bronze')" in prompt
    assert "## SUMMARY" in prompt
    assert "## PYTHON_CODE" in prompt
    assert "## SQL_CODE" in prompt
