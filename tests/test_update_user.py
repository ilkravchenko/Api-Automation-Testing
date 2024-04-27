import requests
import pytest
import json

test_update_data = [
    ('YOUR_TOKEN', 'YOUR_USER_TOKEN', 'YOUR_LOGIN', 'YOUR_NEW_EMAIL', 'YOUR_NEW_LOGIN', 200)
]


@pytest.mark.parametrize("token,user_token,login,new_email,new_login,expected", test_update_data)
def test_update_user(token, user_token, login, new_email, new_login, expected):
    login_url = f"https://favqs.com/api/users/{login}"
    headers = {"Authorization": f"Token token=\"{token}\"", 'User-Token': user_token,
               "Content-Type": "application/json"}

    data = {
        "user": {
            "login": new_login,
            "email": new_email,
        }
    }

    user_info = json.dumps(data)

    response = requests.put(login_url, data=user_info, headers=headers)

    assert response.status_code == expected

    login_url = f"https://favqs.com/api/users/{new_login}"
    response = requests.get(login_url, headers=headers)

    assert response.json()['login'] == new_login
    assert response.json()['account_details']['email'] == new_email
