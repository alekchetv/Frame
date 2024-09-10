from fastapi.testclient import TestClient
from schemas import UserAuth
from main import app

Client = TestClient(app)


def test_login_user():
    response = Client.post("/auth/login")
    assert response.status_code == 422
    response = Client.post("/auth/login", json={
      "email": "user@example.com",
      "password": "string"
    })
    assert response.status_code == 200