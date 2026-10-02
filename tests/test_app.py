from app import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_add_endpoint():
    client = app.test_client()

    response = client.get("/add/3/4")

    assert response.status_code == 200
    assert response.get_json() == {"result": 7}