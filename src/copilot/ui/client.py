import requests


class CopilotClient:
    """Client for communicating with the Copilot API."""

    BASE_URL = "http://127.0.0.1:8000"

    def generate_bronze(
        self,
        api_name: str,
        endpoint: str,
        authentication: str,
        description: str,
        sample_response: dict,
    ) -> dict:

        response = requests.post(
            f"{self.BASE_URL}/bronze/generate",
            json={
                "api_name": api_name,
                "endpoint": endpoint,
                "authentication": authentication,
                "description": description,
                "sample_response": sample_response,
            },
            timeout=300,
        )

        response.raise_for_status()

        return response.json()
