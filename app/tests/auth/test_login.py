import pytest

from src.domains.auth.model.auth import Auth
from src.domains.auth.services.login import Login
from src.domains.auth.repository.fake_auths_repository import (
    FakeAuthsRepository
)
from src.domains.auth.repository.fake_hash_repository import (
    FakeHashRepository
)
from src.domains.auth.repository.fake_token_repository import (
    FakeTokenRepository
)
from src.exceptions.credentials_exception import CredentialsException


@pytest.fixture
def login_service():
    return Login(
        auths_repository=FakeAuthsRepository(
            [Auth(username='test', password='secret-password')]
        ),
        hash_repository=FakeHashRepository(),
        token_repository=FakeTokenRepository(),
    )


def test_should_login_properly_and_return_token(login_service):
    token = login_service.run(
        username='test',
        password='secret-password',
    )

    assert token == 'test'


def test_should_not_login_and_raise_for_invalid_data(
    login_service
):
    with pytest.raises(CredentialsException):
        login_service.run(username=None, password=None)

    with pytest.raises(CredentialsException):
        login_service.run(username='test', password=None)

    with pytest.raises(CredentialsException):
        login_service.run(username=None, password='')


def test_should_not_login_and_raise_for_non_existing_username(
    login_service
):
    with pytest.raises(CredentialsException):
        login_service.run(username='another', password='secret-password')


def test_should_not_login_and_raise_for_invalid_password(
    login_service
):
    with pytest.raises(CredentialsException):
        login_service.run(username='test', password='secret-wrong-password')
