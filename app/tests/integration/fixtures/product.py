import pytest
from fastapi.testclient import TestClient

from src.infra.server import app

client = TestClient(app)

product_id = 'eaefc867-10a6-3a5e-947d-43a984964fcf'
product_b_id = '1b3780e9-6fe4-8070-e485-9c28099b610b'


@pytest.fixture
def product(token, wishlist):
    response = client.post(
        f'/wishlist/{wishlist}/product/{product_id}',
        headers={'Authorization': token},
    )

    return product_id


@pytest.fixture
def product_b(token, wishlist):
    response = client.post(
        f'/wishlist/{wishlist}/product/{product_b_id}',
        headers={'Authorization': token},
    )

    return product_b_id
