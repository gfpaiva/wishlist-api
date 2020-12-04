import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_create_wishlist(token, user):
    response = client.post(
        f'/user/{user}/wishlist',
        headers={'Authorization': token},
        json={
            'title': 'Title',
            'description': 'Description'
        },
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['title'] == 'Title' and
        response_json['description'] == 'Description'
    )


def test_not_create_wishlist_for_invalid_user(token):
    response = client.post(
        f'/user/{uuid.uuid4()}/wishlist',
        headers={'Authorization': token},
        json={
            'title': 'Title',
            'description': 'Description'
        },
    )

    assert response.status_code == 404


def test_create_wishlist_validation(token, user):
    response = client.post(
        f'/user/{user}/wishlist',
        headers={'Authorization': token},
        json={
            'description': 'Description'
        },
    )

    assert response.status_code == 422
