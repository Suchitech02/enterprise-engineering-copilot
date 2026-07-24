from copilot.services.test_generation_service import UnitTestGenerationService


class FakeLLM:
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return "import pytest"


def test_generate_pytest_tests():

    service = UnitTestGenerationService(
        llm=FakeLLM(),
    )

    result = service.generate(
        "print('hello')",
    )

    assert "pytest" in result
