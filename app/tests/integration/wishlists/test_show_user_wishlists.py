import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_show_wishlist_by_user_id(token, user):
    response = client.get(
        f'/user/{user}/wishlist',
        headers={'Authorization': token},
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        isinstance(response_json, list)
    )


def test_not_found_wishlists_for_invalid_id(token):
    response = client.get(
        f'/user/{uuid.uuid4()}/wishlist',
        headers={'Authorization': token},
    )

    assert response.status_code == 404


def test_show_user_validation(token):
    response = client.get(
        f'/user/invalid-uuid/wishlist',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
