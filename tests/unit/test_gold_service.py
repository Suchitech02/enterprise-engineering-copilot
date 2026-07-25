from collections.abc import Iterator

from copilot.llm.base import BaseLLMClient
from copilot.models.gold import (
    GoldGenerationRequest,
)
from copilot.services.gold_service import GoldService


class FakeLLM(BaseLLMClient):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return """
## SUMMARY

Gold pipeline

## PYTHON_CODE

```python
print("gold")
```

## SQL_CODE

```sql
SELECT * FROM gold.sales;
```

## KPIS

1. Total Sales
2. Average Order Value

## AGGREGATIONS

1. Daily Sales
2. Monthly Sales

## ASSUMPTIONS

1. Silver data is validated.
"""

    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        yield self.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )


def test_generate_gold_pipeline() -> None:
    service = GoldService(
        llm=FakeLLM(),
    )

    request = GoldGenerationRequest(
        silver_code="print('silver')",
        business_requirements="Calculate sales KPIs",
        target_table="gold.sales",
    )

    response = service.generate(request)

    assert response.summary == "Gold pipeline"

    assert response.python_code == 'print("gold")'

    assert response.sql_code == ("SELECT * FROM gold.sales;")

    assert response.kpis == [
        "Total Sales",
        "Average Order Value",
    ]

    assert response.aggregations == [
        "Daily Sales",
        "Monthly Sales",
    ]

    assert response.assumptions == [
        "Silver data is validated.",
    ]


def test_gold_service_uses_factory(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "copilot.services.gold_service.get_llm",
        lambda: FakeLLM(),
    )

    service = GoldService()

    assert isinstance(
        service.llm,
        FakeLLM,
    )
