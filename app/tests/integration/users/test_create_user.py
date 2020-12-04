from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_list_users(token):
    response = client.get(
        '/user',
        headers={'Authorization': token},
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        isinstance(response_json, list)
    )


def test_create_user(token):
    response = client.post(
        '/user',
        headers={'Authorization': token},
        json={
            'name': 'Test',
            'email': 'test@test.com',
        },
    )

    response_json = response.json()

    assert (
        response.status_code == 200 and
        response_json['name'] == 'Test' and
        response_json['email'] == 'test@test.com'
    )


def test_not_create_existent_user(token, user):
    response = client.post(
        '/user',
        headers={'Authorization': token},
        json={
            'name': 'John Doe',
            'email': 'john@doe.com',
        },
    )

    assert response.status_code == 409


def test_create_user_validation(token):
    without_data = client.post(
        '/user',
        headers={'Authorization': token},
        json={
            'name': '',
            'email': '',
        },
    )

    assert without_data.status_code == 422

    invalid_email = client.post(
        '/user',
        headers={'Authorization': token},
        json={
            'name': 'Test',
            'email': 'test-invalid-mail',
        },
    )

    assert invalid_email.status_code == 422
