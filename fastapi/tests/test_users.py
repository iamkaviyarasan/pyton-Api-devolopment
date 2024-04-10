from app import schemas
from .database import client, session 
import pytest
from jose import jwt
from app.config import settings


@pytest.fixture
def test_user(client):
    user_data = {"email":"gkavi@gmail.com","password":"kavi"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user







# def test_root(client,session):
#     res = client.get("/")
#     print(res.json().get('Hello'))
#     assert res.json().get('Hello') == 'wecome to my api...'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email":"kavi@gmail.com", "password":"XXXXXXX"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "kavi@gmail.com"
    assert res.status_code == 201

def test_login_user(client,test_user):
        res = client.post("/login",data={test_user['email'], test_user['password']})
        login_res = schemas.Token(**res.json())
        payload = jwt.decode(login_res.access_token,settings.secret_key, algorithms=[settings.algorithm])
    
        id= payload.get("user_id")
        assert id == test_user['id']
        assert login_res.token_type == "bearer"
        assert res.status_code == 200

