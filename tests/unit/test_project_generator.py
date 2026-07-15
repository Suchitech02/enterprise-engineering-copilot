from copilot.generator.project_generator import ProjectGenerator
from copilot.models.bronze import BronzeGenerationResponse


def test_generate_project_files():

    response = BronzeGenerationResponse(
        summary="Customer API",
        python_code='print("hello")',
        sql_code="SELECT 1;",
        folder_structure="src/",
        quality_rules=["Rule One", "Rule Two"],
        assumptions=["Assumption One"],
    )

    files = ProjectGenerator.generate_files(response)

    assert "customer_ingestion.py" in files
    assert "bronze_table.sql" in files
    assert "README.md" in files
    assert "quality_rules.txt" in files
    assert "assumptions.txt" in files

    assert files["customer_ingestion.py"] == 'print("hello")'
    assert files["bronze_table.sql"] == "SELECT 1;"