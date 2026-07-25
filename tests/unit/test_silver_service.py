from collections.abc import Iterator

from copilot.llm.base import BaseLLMClient
from copilot.models.silver import (
    SilverGenerationRequest,
)
from copilot.services.silver_service import SilverService


class FakeLLM(BaseLLMClient):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return """
## SUMMARY

Silver pipeline

## PYTHON_CODE

```python
print("silver")
```

## SQL_CODE

```sql
SELECT * FROM silver.customer;
```

## TRANSFORMATIONS


1. Remove duplicates
2. Standardize names


## QUALITY_RULES

1. customer_id must be unique


## ASSUMPTIONS

1. Bronze data is valid

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


def test_generate_silver_pipeline() -> None:
    service = SilverService(
        llm=FakeLLM(),
    )

    request = SilverGenerationRequest(
        bronze_code="print('bronze')",
        business_rule="Remove duplicates",
        target_table="silver.customer",
    )

    response = service.generate(request)

    assert response.summary == "Silver pipeline"

    assert response.python_code == 'print("silver")'

    assert response.sql_code == ("SELECT * FROM silver.customer;")

    assert response.transformations == [
        "Remove duplicates",
        "Standardize names",
    ]

    assert response.quality_rules == [
        "customer_id must be unique",
    ]

    assert response.assumptions == [
        "Bronze data is valid",
    ]


def test_silver_service_uses_factory(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "copilot.services.silver_service.get_llm",
        lambda: FakeLLM(),
    )

    service = SilverService()

    assert isinstance(
        service.llm,
        FakeLLM,
    )
