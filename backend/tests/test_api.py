from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_catalog_has_thirty_unique_skills():
    response = client.get("/api/v1/skills")
    assert response.status_code == 200
    skills = response.json()
    assert len(skills) == 30
    assert len({skill["id"] for skill in skills}) == 30
    assert {skill["status"] for skill in skills} == {"planned"}
