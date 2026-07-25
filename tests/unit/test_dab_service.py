from collections.abc import Iterator

from copilot.llm.base import BaseLLMClient
from copilot.models.dab import DABGenerationRequest
from copilot.services.dab_service import DABService


class FakeLLM(BaseLLMClient):
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return """
## SUMMARY

Databricks Asset Bundle

## DATABRICKS_YML

```yaml
bundle:
  name: enterprise-engineering-copilot
```

## JOBS_YML

```yaml
resources:
  jobs:
```

## PIPELINES_YML

```yaml
resources:
  pipelines:
```

## VARIABLES_YML

```yaml
variables:
  catalog:
```

## TARGETS_YML

```yaml
targets:
  dev:
```

## FOLDER_STRUCTURE

resources/
jobs.yml
pipelines.yml
variables.yml
targets.yml

## ASSUMPTIONS

1. Unity Catalog is enabled.
2. Databricks Runtime 17+ is available.
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


def test_generate_dab() -> None:
    service = DABService(
        llm=FakeLLM(),
    )

    request = DABGenerationRequest(
        project_name="enterprise-engineering-copilot",
        catalog="main",
        schema_name="engineering",
        bronze_pipeline="bronze.py",
        silver_pipeline="silver.py",
        gold_pipeline="gold.py",
        environment="dev",
    )

    response = service.generate(request)

    assert response.summary == "Databricks Asset Bundle"

    assert response.databricks_yml.startswith("bundle:")

    assert response.jobs_yml.startswith("resources:")

    assert response.pipelines_yml.startswith("resources:")

    assert response.variables_yml.startswith("variables:")

    assert response.targets_yml.startswith("targets:")

    assert "resources/" in response.folder_structure

    assert response.assumptions == [
        "Unity Catalog is enabled.",
        "Databricks Runtime 17+ is available.",
    ]


def test_dab_service_uses_factory(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "copilot.services.dab_service.get_llm",
        lambda: FakeLLM(),
    )

    service = DABService()

    assert isinstance(
        service.llm,
        FakeLLM,
    )
