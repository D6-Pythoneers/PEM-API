import pytest
import requests


@pytest.fixture()
def get_user_token():
    token_url = f"https://pem-api.herokuapp.com/api/token/"

    response = requests.post(
        token_url,
        json={"username": "majed", "password": "Pass@123"},
    )

    data = response.json()
    tokens = data.get("access")
    return tokens


def test_schools(get_user_token):
    url = f"https://pem-api.herokuapp.com/schools/"
    token = get_user_token
    response = requests.get(
        url,
        headers={"Authorization": "Bearer " + token},
    )
    print(response.status_code)
    data = response.json()

    assert response.status_code == 200


def test_teachers(get_user_token):
    url = f"https://pem-api.herokuapp.com/teachers/"
    token = get_user_token
    response = requests.get(
        url,
        headers={"Authorization": "Bearer " + token},
    )
    print(response.status_code)
    data = response.json()

    assert response.status_code == 200


def test_evaluations(get_user_token):
    url = f"https://pem-api.herokuapp.com/evaluations/"
    token = get_user_token
    response = requests.get(
        url,
        headers={"Authorization": "Bearer " + token},
    )
    print(response.status_code)
    data = response.json()

    assert response.status_code == 200


def test_goals(get_user_token):
    url = f"https://pem-api.herokuapp.com/goals/"
    token = get_user_token
    response = requests.get(
        url,
        headers={"Authorization": "Bearer " + token},
    )
    print(response.status_code)
    data = response.json()

    assert response.status_code == 200


def test_assesments(get_user_token):
    url = f"https://pem-api.herokuapp.com/assesments/"
    token = get_user_token
    response = requests.get(
        url,
        headers={"Authorization": "Bearer " + token},
    )
    print(response.status_code)
    data = response.json()

    assert response.status_code == 200
