import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_show_user_by_id(token, user):
    response = client.get(
        f'/user/{user}',
        headers={'Authorization': token},
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['id'] == user and
        response_json['name'] == 'John Doe' and
        response_json['email'] == 'john@doe.com'
    )


def test_not_found_for_invalid_id(token):
    response = client.get(
        f'/user/{uuid.uuid4()}',
        headers={'Authorization': token},
    )

    assert response.status_code == 404


def test_show_user_validation(token):
    response = client.get(
        '/user/invalid-uuid',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
