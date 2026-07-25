from copilot.parsers.dab_parser import DABParser


def test_parse_dab_response() -> None:
    answer = """
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

    response = DABParser.parse(answer)

    assert response.summary == "Databricks Asset Bundle"

    assert response.databricks_yml == ("bundle:\n  name: enterprise-engineering-copilot")

    assert response.jobs_yml == ("resources:\n  jobs:")

    assert response.pipelines_yml == ("resources:\n  pipelines:")

    assert response.variables_yml == ("variables:\n  catalog:")

    assert response.targets_yml == ("targets:\n  dev:")

    assert response.folder_structure == (
        "resources/\njobs.yml\npipelines.yml\nvariables.yml\ntargets.yml"
    )

    assert response.assumptions == [
        "Unity Catalog is enabled.",
        "Databricks Runtime 17+ is available.",
    ]
