from copilot.generator.project_generator import ProjectGenerator
from copilot.models.bronze import (
    BronzeGenerationRequest,
    BronzeGenerationResponse,
)


def test_generate_project_files():
    request = BronzeGenerationRequest(
        api_name="Customer API",
        endpoint="https://api.company.com/customers",
        authentication="OAuth2",
        description="Returns customer master data",
        sample_response={"customerId": 1},
    )

    response = BronzeGenerationResponse(
        summary="Customer API",
        python_code='print("hello")',
        sql_code="SELECT 1;",
        folder_structure="src/",
        quality_rules=["Rule One", "Rule Two"],
        assumptions=["Assumption One"],
    )

    generated_test = """import pytest

def test_example():
    assert True
"""

    files = ProjectGenerator.generate_files(
        request=request,
        response=response,
        generated_test=generated_test,
    )

    pipeline_name = (
        request.api_name.strip()
        .lower()
        .replace(" api", "")
        .replace(" ", "_")
    )

    # ------------------------------------------------------------------
    # Generated files
    # ------------------------------------------------------------------
    assert f"{pipeline_name}/README.md" in files
    assert f"{pipeline_name}/pyproject.toml" in files
    assert f"{pipeline_name}/requirements.txt" in files
    assert f"{pipeline_name}/.gitignore" in files
    assert f"{pipeline_name}/.github/workflows/ci.yml" in files

    assert f"{pipeline_name}/src/{pipeline_name}_ingestion.py" in files
    assert f"{pipeline_name}/tests/test_{pipeline_name}_ingestion.py" in files
    assert f"{pipeline_name}/sql/bronze_table.sql" in files
    assert f"{pipeline_name}/config/config.yaml" in files
    assert f"{pipeline_name}/config/quality_rules.txt" in files
    assert f"{pipeline_name}/config/assumptions.txt" in files

    # ------------------------------------------------------------------
    # README
    # ------------------------------------------------------------------
    readme = files[f"{pipeline_name}/README.md"]

    assert "Customer API" in readme
    assert "https://api.company.com/customers" in readme
    assert "OAuth2" in readme
    assert "Returns customer master data" in readme
    assert ".github/workflows/ci.yml" in readme

    # ------------------------------------------------------------------
    # Generated Python code
    # ------------------------------------------------------------------
    assert (
        files[f"{pipeline_name}/src/{pipeline_name}_ingestion.py"]
        == 'print("hello")'
    )

    # ------------------------------------------------------------------
    # Generated SQL
    # ------------------------------------------------------------------
    assert (
        files[f"{pipeline_name}/sql/bronze_table.sql"]
        == "SELECT 1;"
    )

    # ------------------------------------------------------------------
    # Config
    # ------------------------------------------------------------------
    config = files[f"{pipeline_name}/config/config.yaml"]

    assert "Customer API" in config
    assert "https://api.company.com/customers" in config
    assert "OAuth2" in config
    assert "api:" in config
    assert "bronze:" in config
    assert "retry:" in config

    # ------------------------------------------------------------------
    # pyproject.toml
    # ------------------------------------------------------------------
    pyproject = files[f"{pipeline_name}/pyproject.toml"]

    assert "[project]" in pyproject
    assert f'name = "{pipeline_name}"' in pyproject
    assert 'version = "0.1.0"' in pyproject
    assert "pytest" in pyproject

    # ------------------------------------------------------------------
    # Requirements
    # ------------------------------------------------------------------
    requirements = files[f"{pipeline_name}/requirements.txt"]

    assert "requests" in requirements
    assert "pydantic" in requirements
    assert "tenacity" in requirements
    assert "pyspark" in requirements
    assert "delta-spark" in requirements
    assert "databricks-sdk" in requirements
    assert "pytest" in requirements

    # ------------------------------------------------------------------
    # .gitignore
    # ------------------------------------------------------------------
    gitignore = files[f"{pipeline_name}/.gitignore"]

    assert "__pycache__/" in gitignore
    assert ".venv/" in gitignore
    assert ".pytest_cache/" in gitignore
    assert ".env" in gitignore

    # ------------------------------------------------------------------
    # GitHub Actions
    # ------------------------------------------------------------------
    ci_workflow_path = (
        f"{pipeline_name}/.github/workflows/ci.yml"
    )

    assert ci_workflow_path in files

    ci_workflow = files[ci_workflow_path]

    assert "name: CI" in ci_workflow
    assert "actions/checkout" in ci_workflow
    assert "actions/setup-python" in ci_workflow
    assert 'python-version: "3.11"' in ci_workflow
    assert "pip install -r requirements.txt" in ci_workflow
    assert "Run tests" in ci_workflow
    assert "pytest" in ci_workflow

    # ------------------------------------------------------------------
    # Generated tests
    # ------------------------------------------------------------------
    test_file = files[
        f"{pipeline_name}/tests/test_{pipeline_name}_ingestion.py"
    ]

    assert test_file == generated_test
    assert "import pytest" in test_file
    assert "test_example" in test_file
    assert "assert True" in test_file

    # ------------------------------------------------------------------
    # Supporting files
    # ------------------------------------------------------------------
    quality_rules = files[
        f"{pipeline_name}/config/quality_rules.txt"
    ]

    assumptions = files[
        f"{pipeline_name}/config/assumptions.txt"
    ]

    assert "Rule One" in quality_rules
    assert "Rule Two" in quality_rules
    assert "Assumption One" in assumptions