from fastapi.testclient import TestClient

from copilot.main import app

client = TestClient(app)


def test_generate_endpoint():
    response = client.post(
        "/generate",
        json={
            "prompt": "Say hello",
        },
    )

    assert response.status_code == 200
    assert "response" in response.json()

def test_generate_stream_endpoint():
    response = client.post(
        "/generate/stream",
        json={
            "prompt": "Say hello",
        },
    )

    assert response.status_code == 200
    assert response.text != ""