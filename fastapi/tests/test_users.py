from fastapi import Response
from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get('Hello'))
    assert res.json().get('Hello') == 'wecome to my api...'
    assert res.status_code == 200

def test_create_user():
    res = client.post("/users/", json={"email":"kavi@gmail.com", "password":"XXXXXXX"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "kavi@gmail.com"
    assert res.status_code == 201