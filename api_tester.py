import fire
import requests
import environ

env = environ.Env(
    API_HOST = (str,"https://pem-api.herokuapp.com"),
    RESOURCE_URI = (str,"/"),
    USERNAME = (str,"admin"),
    PASSWORD = (str,"Pass@123"),
)
environ.Env.read_env()

class ApiTester:

    """CLI for testing API"""

    def __init__(self, host=env.str("API_HOST")):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api

        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"username": env.str("USERNAME"), "password": env.str("PASSWORD")}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens

    def get_teachers(self):
        """get list of all resources from api
        Usage: python api_tester.py get_teachers

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/teachers"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_schools(self):
        """get list of all resources from api
        Usage: python api_tester.py get_schools

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/schools"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_evaluations(self):
        """get list of all resources from api
        Usage: python api_tester.py get_evaluations

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/evaluations"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_one_evaluation(self):
        """get list of the resources for the given id from api
        Usage: python api_tester.py get_one_evaluations

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/evaluations/1"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_goals(self):
        """get list of all resources from api
        Usage: python api_tester.py get_goals

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/goals"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_one_goal(self):
        """get list of the resources for the given id from api
        Usage: python api_tester.py get_one_goals

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/goals/1"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_assesments(self):
        """get list of all resources from api
        Usage: python api_tester.py get_assesments

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/assesments"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_one_assesment(self):
        """get list of the resources for the given id from api
        Usage: python api_tester.py get_one_assesment

        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/assesments/1"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def create_assessment(self):
        """creates a resource in api

        Usage:
        python api_tester.py create_assessment

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/assesments/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            "indicator": "testing",
            "first evaluation": "NA",
            "final evaluation": "NA",
            "score":"20",
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

    def create_evaluation(self):
        """creates a resource in api

        Usage:
        python api_tester.py create_evaluation

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/evaluations/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            "evaluated": False,
            "academic_year": "NA",
            "created by": "NA",
            "status":"20",
            "max score": 20,
            "score":"18",
            "school":2,
            "user":2
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

    def create_goal(self):
        """creates a resource in api

        Usage:
        python api_tester.py create_goal

        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/goals/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
            "goal": "test",
            "goal_result": "",
            "max score": 20,
            "score":"18",
            "evaluation":3,
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

if __name__ == "__main__":
    fire.Fire(ApiTester)

