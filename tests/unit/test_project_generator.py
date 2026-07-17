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

    # Generated files
    assert "customer_ingestion.py" in files
    assert "test_customer_ingestion.py" in files
    assert "bronze_table.sql" in files
    assert "README.md" in files
    assert "config.yaml" in files
    assert "requirements.txt" in files
    assert ".gitignore" in files
    assert "quality_rules.txt" in files
    assert "assumptions.txt" in files

    # README
    readme = files["README.md"]

    assert "Customer API" in readme
    assert "https://api.company.com/customers" in readme
    assert "OAuth2" in readme
    assert "Returns customer master data" in readme

    # Generated code
    assert files["customer_ingestion.py"] == 'print("hello")'
    assert files["bronze_table.sql"] == "SELECT 1;"

    # Config
    config = files["config.yaml"]

    assert "Customer API" in config
    assert "https://api.company.com/customers" in config
    assert "OAuth2" in config
    assert "api:" in config
    assert "bronze:" in config
    assert "retry:" in config

    # Requirements
    requirements = files["requirements.txt"]

    assert "requests" in requirements
    assert "pydantic" in requirements
    assert "pyspark" in requirements
    assert "delta-spark" in requirements
    assert "streamlit" in requirements
    assert "fastapi" in requirements

    # Gitignore
    gitignore = files[".gitignore"]

    assert "__pycache__/" in gitignore
    assert ".venv/" in gitignore
    assert ".pytest_cache/" in gitignore
    assert ".env" in gitignore

    # Generated test
    test_file = files["test_customer_ingestion.py"]

    assert test_file == generated_test
    assert "import pytest" in test_file
    assert "test_example" in test_file
    assert "assert True" in test_file