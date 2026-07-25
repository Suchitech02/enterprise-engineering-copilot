from copilot.prompts.gold_prompt_builder import (
    GoldPromptBuilder,
)


def test_build_gold_prompt() -> None:
    """Test building a Gold generation prompt."""

    prompt = GoldPromptBuilder.build_prompt(
        silver_code="print('silver')",
        business_requirements="Calculate daily sales",
        target_table="gold.sales",
    )

    assert "print('silver')" in prompt

    assert "Calculate daily sales" in prompt

    assert "gold.sales" in prompt

    assert "## SUMMARY" in prompt

    assert "## PYTHON_CODE" in prompt

    assert "## SQL_CODE" in prompt

    assert "## KPIS" in prompt

    assert "## AGGREGATIONS" in prompt

    assert "## ASSUMPTIONS" in prompt
