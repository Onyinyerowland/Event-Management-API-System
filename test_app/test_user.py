import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def test_create_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert data["is_active"] is True
    assert "id" in data
    return data

def test_get_user(test_create_user):
    user_id = test_create_user["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_update_user(test_create_user):
    user_id = test_create_user["id"]
    response = client.put(f"/users/{user_id}", json={"name": "Updated Name", "email": "updated@example.com"})
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == "Updated Name"
    assert updated["email"] == "updated@example.com"



def test_delete_user():
    response = client.post("/users/", json={"name": "Temp", "email": "temp@example.com"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200



def test_deactivate_user():
    response = client.post("/users/", json={"name": "Inactive User", "email": "inactive@example.com"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = client.post(f"/users/{user_id}/deactivate")
    assert response.status_code == 200
    assert response.json()["is_active"] is False
