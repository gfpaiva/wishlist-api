import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_delete_user_by_id(token, user):
    response = client.delete(
        f'/user/{user}',
        headers={'Authorization': token},
    )

    assert response.status_code == 204


def test_not_delete_for_invalid_id(token):
    response = client.delete(
        f'/user/{uuid.uuid4()}',
        headers={'Authorization': token},
    )

    assert response.status_code == 404


def test_delete_user_validation(token):
    response = client.delete(
        '/user/invalid-uuid',
        headers={'Authorization': token},
    )

    assert response.status_code == 422
