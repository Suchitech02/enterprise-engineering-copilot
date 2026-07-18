from copilot.explain.prompts import (
    SYSTEM_PROMPT,
    build_explain_prompt,
)


def test_system_prompt_contains_json_instruction():
    assert "Return ONLY valid JSON." in SYSTEM_PROMPT


def test_system_prompt_contains_explanation_schema():
    assert '"summary"' in SYSTEM_PROMPT
    assert '"explanation"' in SYSTEM_PROMPT


def test_build_explain_prompt_contains_language():
    prompt = build_explain_prompt(
        "python",
        "print('hello')",
    )

    assert "Language:" in prompt
    assert "python" in prompt


def test_build_explain_prompt_contains_code():
    code = "print('hello')"

    prompt = build_explain_prompt(
        "python",
        code,
    )

    assert code in prompt


def test_build_explain_prompt_contains_markdown():
    prompt = build_explain_prompt(
        "python",
        "print('hello')",
    )

    assert "```python" in prompt
    assert "```" in prompt
