
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)



def create_event():
    response = client.post("/events/", json={"title": "Test Event", "location": "Online", "date": "2025-06-25"})
    assert response.status_code == 200
    return response.json()


def test_create_event():
    event= create_event()
    assert event["title"] == "Test Event"
    assert event["is_open"] is True
    assert "id" in event


def test_get_event():
    event = create_event()
    event_id = event["id"]
    response = client.get(f"/events/{event_id}")
    assert response.status_code == 200
    assert response.json()["id"] == event_id

def test_update_event():
    event = create_event()
    event_id = event["id"]
    response = client.put(f"/events/{event_id}", json={
        "title": "Updated Event",
        "location": "Lagos",
        "date": "2025-06-25"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Event"

def test_delete_event():
    event = create_event()
    event_id=event["id"]
    response = client.delete(f"/events/{event_id}")
    assert response.status_code == 200
    assert response.json()["id"] == event_id


def test_close_event():
    event = create_event()
    event_id = event["id"]
    response = client.post(f"/events/{event_id}/close")
    assert response.status_code == 200
    assert response.json()["is_open"] is False
