from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.dab import DABGenerationResponse

client = TestClient(app)


@patch("copilot.api.routes.dab.service")
def test_dab_endpoint(
    mock_service,
) -> None:
    mock_service.generate.return_value = DABGenerationResponse(
        summary="Databricks Asset Bundle",
        databricks_yml="bundle:",
        jobs_yml="resources:",
        pipelines_yml="resources:",
        variables_yml="variables:",
        targets_yml="targets:",
        folder_structure="resources/",
        assumptions=[
            "Unity Catalog is enabled.",
        ],
    )

    response = client.post(
        "/dab",
        json={
            "project_name": "enterprise-engineering-copilot",
            "catalog": "main",
            "schema_name": "engineering",
            "bronze_pipeline": "bronze.py",
            "silver_pipeline": "silver.py",
            "gold_pipeline": "gold.py",
            "environment": "dev",
        },
    )

    assert response.status_code == 200

    assert response.json()["summary"] == ("Databricks Asset Bundle")

    assert response.json()["databricks_yml"] == "bundle:"

    assert response.json()["jobs_yml"] == "resources:"
