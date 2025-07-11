from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_cities_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    data = response.json()
    assert data["country"] == "Spain"
    assert data["cities"] == ["Seville"]