import uuid
import pytest

from src.domains.users.services.create_user import CreateUser
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.user_exception import UserException


@pytest.fixture
def create_user_service():
    return CreateUser(FakeUsersRepository())


def test_should_create_and_return_new_user(create_user_service):
    user = create_user_service.run(name='test', email='test@test.com')

    assert (
        isinstance(user.id, uuid.UUID) and
        user.name == 'test' and user.email == 'test@test.com'
    )


def test_should_not_create_user_and_raise_for_invalid_data(
    create_user_service
):
    with pytest.raises(UserException):
        create_user_service.run(name=None, email=None)


def test_should_not_create_users_with_same_email(create_user_service):
    with pytest.raises(UserException):
        create_user_service.run(name='test', email='test@test.com')
        create_user_service.run(name='test', email='test@test.com')
