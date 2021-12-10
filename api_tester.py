import fire
import requests

API_HOST = "https://pem-api.herokuapp.com"
RESOURCE_URI = "/"
USERNAME = "admin"
PASSWORD = "Pass@123"


class ApiTester:

    """CLI for testing API"""

    def __init__(self, host=API_HOST):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api

        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"username": USERNAME, "password": PASSWORD}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens


if __name__ == "__main__":
    fire.Fire(ApiTester)