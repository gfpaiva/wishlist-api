import pytest
from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)


@pytest.fixture
def wishlist(token, user):
    response = client.post(
        f'/user/{user}/wishlist',
        headers={'Authorization': token},
        json={
            'title': 'Title',
            'description': 'Description'
        },
    )

    wishlist = response.json()
    wishlist_id = wishlist['id']

    return wishlist_id
