import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user
from tests.integration.fixtures.wishlist import wishlist
from tests.integration.fixtures.product import (
    product,
    product_b,
)

client = TestClient(app)


def test_show_wishlist_by_user_id(
    token,
    wishlist,
    product,
    product_b,
):
    response = client.get(
        f'/wishlist/{wishlist}',
        headers={'Authorization': token},
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['title'] == 'Title' and
        response_json['user']['name'] == 'John Doe' and
        isinstance(response_json['products'], list) and
        len(response_json['products']) == 2
    )


def test_not_found_wishlists_for_invalid_id(token):
    response = client.get(
        f'/wishlist/{uuid.uuid4()}',
        headers={'Authorization': token},
    )

    assert response.status_code == 404


def test_show_user_validation(token):
    response = client.get(
        '/wishlist/invalid-uuid',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
