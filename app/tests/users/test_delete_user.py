import uuid
import pytest

from src.domains.users.services.create_user import CreateUser
from src.domains.users.services.delete_user import DeleteUser
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.user_exception import UserException

users_repository = FakeUsersRepository()


@pytest.fixture
def delete_user():
    users_repository.users = []
    create_user_service = CreateUser(users_repository)
    delete_user_service = DeleteUser(users_repository)

    created_user = create_user_service.run(name='test', email='test@test.com')

    return (delete_user_service, created_user)


def test_should_delete_user(delete_user):
    delete_user_service, created_user = delete_user
    deleted = delete_user_service.run(id=created_user.id)

    assert deleted is True


def test_should_not_update_user_and_raise_for_invalid_user_id(
    delete_user,
):
    with pytest.raises(UserException):
        delete_user_service = delete_user[0]
        delete_user_service.run(id=uuid.uuid4())
