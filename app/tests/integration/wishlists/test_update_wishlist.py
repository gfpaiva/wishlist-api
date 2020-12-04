import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user
from tests.integration.fixtures.wishlist import wishlist

client = TestClient(app)


def test_update_wishlist_by_id(token, wishlist):
    data = client.patch(
        f'/wishlist/{wishlist}',
        headers={'Authorization': token},
        json={
            'title': 'Changed Title',
            'description': 'changed description'
        },
    )

    data_json = data.json()

    assert (
        data.status_code == 200 and
        data_json['id'] == wishlist and
        data_json['title'] == 'Changed Title' and
        data_json['description'] == 'changed description'
    )

    title = client.patch(
        f'/wishlist/{wishlist}',
        headers={'Authorization': token},
        json={
            'title': 'Another Title'
        }
    )

    title_json = title.json()

    assert (
        title.status_code == 200 and
        title_json['id'] == wishlist and
        title_json['title'] == 'Another Title' and
        title_json['description'] == 'changed description'
    )

    description = client.patch(
        f'/wishlist/{wishlist}',
        headers={'Authorization': token},
        json={
            'description': 'another description'
        }
    )

    description_json = description.json()

    assert (
        description.status_code == 200 and
        description_json['id'] == wishlist and
        description_json['title'] == 'Another Title' and
        description_json['description'] == 'another description'
    )


def test_not_update_for_invalid_id(token):
    response = client.patch(
        f'/wishlist/{uuid.uuid4()}',
        headers={'Authorization': token},
        json={
            'title': 'Changed Title',
            'description': 'changed description'
        },
    )

    assert response.status_code == 404


def test_update_wishlist_validation(token, wishlist):
    without_data = client.patch(
        f'/wishlist/{wishlist}',
        headers={'Authorization': token}
    )

    assert without_data.status_code == 422
