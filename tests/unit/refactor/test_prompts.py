from copilot.refactor.prompts import (
    SYSTEM_PROMPT,
    build_refactor_prompt,
)


def test_system_prompt_contains_json_instruction():
    assert "Return ONLY valid JSON." in SYSTEM_PROMPT


def test_system_prompt_contains_refactor_schema():
    assert '"summary"' in SYSTEM_PROMPT
    assert '"refactored_code"' in SYSTEM_PROMPT
    assert '"changes"' in SYSTEM_PROMPT


def test_build_refactor_prompt_contains_language():
    prompt = build_refactor_prompt(
        "python",
        "print('hello')",
    )

    assert "Language:" in prompt
    assert "python" in prompt


def test_build_refactor_prompt_contains_code():
    code = "print('hello')"

    prompt = build_refactor_prompt(
        "python",
        code,
    )

    assert code in prompt


def test_build_refactor_prompt_contains_markdown():
    prompt = build_refactor_prompt(
        "python",
        "print('hello')",
    )

    assert "```python" in prompt
    assert "```" in prompt
