from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_perform_addition():
    payload = {"batchid": "id0101", "payload": [[1, 2], [3, 4]]}
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["status"] == "complete"
    assert isinstance(data["response"], list)
    assert len(data["response"]) == 2
    assert "started_at" in data
    assert "completed_at" in data
