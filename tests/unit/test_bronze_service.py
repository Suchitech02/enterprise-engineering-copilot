from copilot.models.bronze import BronzeGenerationRequest
from copilot.services.bronze_service import BronzeService


class FakeLLM:
    def generate(self, prompt: str) -> str:
        return """
## SUMMARY

Test Summary

## PYTHON_CODE

print("hello")

## SQL_CODE

SELECT 1;

## FOLDER_STRUCTURE

src/

## QUALITY_RULES

1. Rule One

2. Rule Two

## ASSUMPTIONS

1. Assumption One
"""


def test_generate_bronze_pipeline():
    service = BronzeService(llm=FakeLLM())

    request = BronzeGenerationRequest(
        api_name="Customer API",
        endpoint="https://api.company.com/customers",
        authentication="OAuth2",
        description="Customer endpoint",
        sample_response={"customerId": 1},
    )

    response = service.generate(request)

    assert response.summary == "Test Summary"
    assert response.python_code == 'print("hello")'
    assert response.sql_code == "SELECT 1;"
    assert response.folder_structure == "src/"
    assert response.quality_rules == [
        "Rule One",
        "Rule Two",
    ]
    assert response.assumptions == [
        "Assumption One",
    ]

def test_bronze_service_uses_factory(monkeypatch):
    monkeypatch.setattr(
        "copilot.services.bronze_service.get_llm",
        lambda: FakeLLM(),
    )

    service = BronzeService()

    assert isinstance(service.llm, FakeLLM)