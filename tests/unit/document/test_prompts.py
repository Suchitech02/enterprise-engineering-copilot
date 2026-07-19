from copilot.document.prompts import (
    SYSTEM_PROMPT,
    build_document_prompt,
)


def test_system_prompt_contains_json_instruction():
    assert "Return ONLY valid JSON." in SYSTEM_PROMPT


def test_system_prompt_contains_document_schema():
    assert '"summary"' in SYSTEM_PROMPT
    assert '"documented_code"' in SYSTEM_PROMPT
    assert '"changes"' in SYSTEM_PROMPT


def test_build_document_prompt_contains_language():
    prompt = build_document_prompt(
        "python",
        "print('hello')",
    )

    assert "Language:" in prompt
    assert "python" in prompt


def test_build_document_prompt_contains_code():
    code = "print('hello')"

    prompt = build_document_prompt(
        "python",
        code,
    )

    assert code in prompt


def test_build_document_prompt_contains_markdown():
    prompt = build_document_prompt(
        "python",
        "print('hello')",
    )

    assert "```python" in prompt
    assert "```" in prompt
