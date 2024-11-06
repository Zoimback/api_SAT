# tests/test_endpoints.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Item 1",
        "description": "A sample item",
        "price": 10.0,
        "tax": 1.5
    }

def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_create_item():
    item_data = {
        "name": "New Item",
        "description": "A new item",
        "price": 20.0,
        "tax": 2.0
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data
