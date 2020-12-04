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


def test_delete_product_from_wishlist(token, wishlist, product):
    response = client.delete(
        f'/wishlist/{wishlist}/product/{product_id}',
        headers={'Authorization': token},
    )

    assert response.status_code == 204


def test_not_delete_for_invalid_id(token, wishlist, product):
    invalid_wishlist = client.delete(
        f'/wishlist/{uuid.uuid4()}/product/{product_id}',
        headers={'Authorization': token},
    )

    assert invalid_wishlist.status_code == 404

    invalid_product = client.delete(
        f'/wishlist/{wishlist}/product/{uuid.uuid4()}',
        headers={'Authorization': token},
    )

    assert invalid_product.status_code == 404


def test_show_wishlist_validation(token):
    response = client.delete(
        f'/wishlist/invalid-uuid/product/{product_id}',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
