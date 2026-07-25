from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.gold import GoldGenerationResponse

client = TestClient(app)


@patch("copilot.api.routes.gold.service")
def test_gold_endpoint(
    mock_service,
) -> None:
    mock_service.generate.return_value = GoldGenerationResponse(
        summary="Gold pipeline",
        python_code='print("gold")',
        sql_code="SELECT * FROM gold.sales;",
        kpis=[
            "Total Sales",
        ],
        aggregations=[
            "Daily Sales",
        ],
        assumptions=[
            "Silver data is validated.",
        ],
    )

    response = client.post(
        "/gold",
        json={
            "silver_code": "print('silver')",
            "business_requirements": "Calculate sales KPIs",
            "target_table": "gold.sales",
        },
    )

    assert response.status_code == 200

    assert response.json()["summary"] == "Gold pipeline"

    assert response.json()["kpis"] == [
        "Total Sales",
    ]
