from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)


def test_get_token():
    response = client.post(
        '/token',
        data={
            'username': 'wishlist',
            'password': 'wishlist',
        }
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['token_type'] == 'bearer' and
        isinstance(response_json['access_token'], str)
    )


def test_get_token_wrong_password():
    response = client.post(
        '/token',
        data={
            'username': 'test',
            'password': 'test',
        }
    )
    assert response.status_code == 401


def test_get_token_field_validator():
    response = client.post(
        '/token',
        data={
            'username': '',
            'password': '',
        }
    )
    assert response.status_code == 422
