import uuid
from fastapi.testclient import TestClient

from src.infra.server import app

from tests.integration.fixtures.clear import clear
from tests.integration.fixtures.token import token
from tests.integration.fixtures.user import user

client = TestClient(app)


def test_update_user_by_id(token, user):
    data = client.patch(
        f'/user/{user}',
        headers={'Authorization': token},
        json={
            'name': 'Tom Doe',
            'email': 'tom@doe.com'
        },
    )

    data_json = data.json()

    assert (
        data.status_code == 200 and
        data_json['id'] == user and
        data_json['name'] == 'Tom Doe' and
        data_json['email'] == 'tom@doe.com'
    )

    name = client.patch(
        f'/user/{user}',
        headers={'Authorization': token},
        json={
            'name': 'Harry Doe'
        }
    )

    name_json = name.json()

    assert (
        name.status_code == 200 and
        name_json['id'] == user and
        name_json['name'] == 'Harry Doe' and
        name_json['email'] == 'tom@doe.com'
    )

    email = client.patch(
        f'/user/{user}',
        headers={'Authorization': token},
        json={
            'email': 'harry@doe.com'
        }
    )

    email_json = email.json()

    assert (
        email.status_code == 200 and
        email_json['id'] == user and
        email_json['name'] == 'Harry Doe' and
        email_json['email'] == 'harry@doe.com'
    )


def test_not_update_for_invalid_id(token):
    response = client.patch(
        f'/user/{uuid.uuid4()}',
        headers={'Authorization': token},
        json={
            'name': 'Tom Doe',
            'email': 'tom@doe.com'
        },
    )

    assert response.status_code == 404


def test_update_user_validation(token, user):
    without_data = client.patch(
        f'/user/{user}',
        headers={'Authorization': token}
    )

    assert without_data.status_code == 422

    invalid_email = client.patch(
        f'/user/{user}',
        headers={'Authorization': token},
        json={
            'name': 'Tom Doe',
            'email': 'test-invalid-mail',
        },
    )

    assert invalid_email.status_code == 422
