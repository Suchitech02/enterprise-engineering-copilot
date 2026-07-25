from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.silver import (
    SilverGenerationResponse,
)

client = TestClient(app)


@patch("copilot.api.routes.silver.service")
def test_silver_endpoint(
    mock_service,
) -> None:
    mock_service.generate.return_value = SilverGenerationResponse(
        summary="Silver pipeline",
        python_code='print("silver")',
        sql_code="SELECT 1;",
        transformations=[
            "Remove duplicates",
        ],
        quality_rules=[
            "customer_id unique",
        ],
        assumptions=[
            "Bronze data valid",
        ],
    )

    response = client.post(
        "/silver",
        json={
            "bronze_code": "print('bronze')",
            "business_rule": "Remove duplicates",
            "target_table": "silver.customer",
        },
    )

    assert response.status_code == 200

    assert response.json()["summary"] == "Silver pipeline"
