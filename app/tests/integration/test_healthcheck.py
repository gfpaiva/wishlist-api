from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)


def test_healthcheck():
    response = client.get('/')
    assert (
        response.status_code == 200 and
        response.text == '"OK"'
    )
