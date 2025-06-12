from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_speakers():
    response = client.get("/speakers/")
    assert response.status_code == 200
    assert len(response.json()) == 3
