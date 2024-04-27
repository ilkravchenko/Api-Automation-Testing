import requests
import pytest
import json

test_registration_data = [
    ('YOUR_TOKEN', 'YOUR_LOGIN', 'YOUR_EMAIL', 'YOUR_PASSWORD', 200),
]


@pytest.mark.parametrize("token,login,email,password,expected", test_registration_data)
def test_registration(token, login, email, password, expected):
    url = "https://favqs.com/api/users/"

    data = {
        "user": {
            "login": login,
            "email": email,
            "password": password
        }
    }

    user_info = json.dumps(data)

    response = requests.post(url, data=user_info,
                             headers={"Authorization": f"Token token=\"{token}\"", "Content-Type": "application/json"})

    user_token = response.json()["User-Token"]
    print(user_token)

    assert response.status_code == expected

    headers = {"Authorization": f"Token token=\"{token}\"", 'User-Token': user_token}
    login_url = f"{url}{login}"
    response = requests.get(login_url, headers=headers)

    assert response.json()['login'] == login
    assert response.json()['account_details']['email'] == email
