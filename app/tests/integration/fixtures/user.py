import pytest
from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)


@pytest.fixture
def user(token):
    response = client.post(
        '/user',
        headers={'Authorization': token},
        json={
            'name': 'John Doe',
            'email': 'john@doe.com',
        },
    )

    user = response.json()
    user_id = user['id']

    return user_id
