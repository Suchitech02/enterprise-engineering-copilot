from copilot.generator.project_generator import ProjectGenerator
from copilot.models.bronze import BronzeGenerationRequest, BronzeGenerationResponse


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

    files = ProjectGenerator.generate_files(
        request, 
        response,
    )

    assert "customer_ingestion.py" in files
    assert "bronze_table.sql" in files
    assert "README.md" in files
    assert "quality_rules.txt" in files
    assert "assumptions.txt" in files
    assert "Customer API" in files["README.md"]
    assert "https://api.company.com/customers" in files["README.md"]
    assert "OAuth2" in files["README.md"]
    assert "Returns customer master data" in files["README.md"]

    assert files["customer_ingestion.py"] == 'print("hello")'
    assert files["bronze_table.sql"] == "SELECT 1;"