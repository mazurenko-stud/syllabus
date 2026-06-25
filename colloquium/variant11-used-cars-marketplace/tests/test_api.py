from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_contains_student_id():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 11
    assert data["status"] == "running"


def test_get_cars_returns_variant_11_ids():
    response = client.get("/cars")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 11
    assert data["count"] == 3
    assert data["cars"][0]["id"] == 1101


def test_create_test_drive():
    response = client.post(
        "/test-drives",
        json={
            "car_id": 1101,
            "buyer_name": "Test Buyer",
            "preferred_date": "2026-06-25"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 11
    assert data["status"] == "created"
    assert data["test_drive"]["car_id"] == 1101
