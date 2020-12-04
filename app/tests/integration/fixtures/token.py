import pytest
from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)


@pytest.fixture
def token():
    response = client.post(
        '/token',
        data={
            'username': 'wishlist',
            'password': 'wishlist',
        },
    )

    response_json = response.json()

    return f'Bearer {response_json["access_token"]}'
