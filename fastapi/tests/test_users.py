from app import schemas
import pytest
from jose import jwt
from app.config import settings









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
        res = client.post("/login",data={ "username":test_user['email'],"password": test_user['password']})
        print(res.json())
        print("aaaaaaaaaaa")
        login_res = schemas.Token(**res.json())
        payload = jwt.decode(login_res.access_token,settings.secret_key, algorithms=[settings.algorithm])
    
        id= payload.get("user_id")
        assert id == test_user['id']
        assert login_res.token_type == "bearer"
        assert res.status_code == 200
@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail.com', 'password123', 403),
    ('gkavi@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password1234', 422),
    ('kavi@gmail.com', None, 422)
])
def test_incorrect_login(client, test_user,email,password,status_code):
        res = client.post("/login", data={ "username":email, "password":password})
        assert res.status_code == status_code
        # assert res.json().get("detail") == "Invalid Credentials"

