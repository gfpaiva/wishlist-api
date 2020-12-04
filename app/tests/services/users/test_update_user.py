import uuid
import pytest

from src.domains.users.services.create_user import CreateUser
from src.domains.users.services.update_user import UpdateUser
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.user_exception import UserException

users_repository = FakeUsersRepository()


@pytest.fixture
def update_user():
    users_repository.users = []
    create_user_service = CreateUser(users_repository)
    update_user_service = UpdateUser(users_repository)

    created_user = create_user_service.run(name='test', email='test@test.com')

    return (update_user_service, created_user)


def test_should_update_and_return_user(update_user):
    update_user_service, created_user = update_user
    user = update_user_service.run(
        user_id=created_user.id,
        name='test2',
        email='test2@test.com',
    )

    assert user.name == 'test2' and user.email == 'test2@test.com'


def test_should_not_update_user_and_raise_for_invalid_data(
    update_user,
):
    with pytest.raises(UserException):
        update_user_service, created_user = update_user
        update_user_service.run(
            user_id=created_user.id,
            name=None,
            email=None,
        )


def test_should_not_update_user_and_raise_for_invalid_user_id(
    update_user,
):
    with pytest.raises(UserException):
        update_user_service = update_user[0]
        update_user_service.run(
            user_id=uuid.uuid4(),
            name='test2',
            email='test2@test.com',
        )


def test_should_not_update_user_and_raise_for_email_alredy_in_repository(
    update_user,
):
    create_user_service = CreateUser(users_repository)
    create_user_service.run(
        name='test3',
        email='test3@test.com',
    )

    with pytest.raises(UserException):
        update_user_service, created_user = update_user
        update_user_service.run(
            user_id=created_user.id,
            name='test3',
            email='test3@test.com',
        )
