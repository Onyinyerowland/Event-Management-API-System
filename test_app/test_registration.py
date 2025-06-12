from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_registration_flow():

    user_resp = client.post("/users/", json={"name": "Attendee", "email": "attend@example.com"})
    user_id = user_resp.json()["id"]


    event_resp = client.post("/events/", json={"title": "Reg Event", "location": "Virtual", "date": "2025-11-11"})
    event_id = event_resp.json()["id"]


    reg_resp = client.post("/registrations/", json={"user_id": user_id, "event_id": event_id})
    assert reg_resp.status_code == 200
    reg_id = reg_resp.json()["id"]


    reg_dup = client.post("/registrations/", json={"user_id": user_id, "event_id": event_id})
    assert reg_dup.status_code == 400


    attend_resp = client.post(f"/registrations/{reg_id}/attend")
    assert attend_resp.status_code == 200
    assert attend_resp.json()["attended"] is True


    reg_list = client.get(f"/registrations/user/{user_id}")
    assert reg_list.status_code == 200
    assert len(reg_list.json()) == 1


    attended = client.get("/registrations/attendees")
    assert user_id in attended.json()
