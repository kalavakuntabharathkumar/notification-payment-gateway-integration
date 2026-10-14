from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_mock_payment():
    r = client.post("/api/payments", json={"order_id":"ORD-1","amount":499})
    assert r.status_code == 200
    assert r.json()["status"] == "accepted"

def test_notification_queue():
    r = client.post("/api/notifications", json={"recipient":"+910000000000","message":"Hello","channel":"sms"})
    assert r.status_code == 200
    assert r.json()["status"] == "queued"
