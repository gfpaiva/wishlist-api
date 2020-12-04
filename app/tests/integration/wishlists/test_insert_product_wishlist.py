import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user
from tests.integration.fixtures.wishlist import wishlist
from tests.integration.fixtures.product import (
    product,
    product_id,
)

client = TestClient(app)


def test_insert_product(token, wishlist):
    response = client.post(
        f'/wishlist/{wishlist}/product/{product_id}',
        headers={'Authorization': token},
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['products'][0]['id'] == product_id
    )


def test_not_insert_product_for_invalid_wishlist(token):
    response = client.post(
        f'/wishlist/{uuid.uuid4()}/product/{product_id}',
        headers={'Authorization': token},
    )

    assert response.status_code == 404


def test_not_insert_duplicated_product(token, wishlist, product):
    response = client.post(
        f'/wishlist/{wishlist}/product/{product_id}',
        headers={'Authorization': token},
    )

    assert response.status_code == 409


def test_create_wishlist_validation(token):
    response = client.post(
        f'/wishlist/invalid-uuid/product/{product_id}',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
