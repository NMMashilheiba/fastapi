import re
from jose import jwt
import pytest
from app import schemas
from app.config import settings

def test_root(client):
    res = client.get("/"    )
    print(res.json())
    assert res.json().get('message') == 'Welcome to Mashilheiba dockerized fastAPI!!!'
    assert res.status_code == 200

def test_user_create(client):
    res = client.post("/users/", json={"email": "testing@gmail.com", "password": "password123" })
    # print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "testing@gmail.com"
    assert res.status_code == 201

def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wronfemail@gmail.com', 'wrongPassword', 403),
    ('wronfemail@gmail.com', 'password123', 403),
    ('mashil@gmail.com', 'wrongpassword', 403),
    (None, 'wrongpassword', 422),
    ('mashil@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    # print (res.json())
    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"