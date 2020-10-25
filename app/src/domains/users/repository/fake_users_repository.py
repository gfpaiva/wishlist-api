from typing import List
import uuid

from src.domains.users.model.user import User
from src.domains.users.repository.users_repository import UsersRepository


class FakeUsersRepository(UsersRepository):
    def __init__(self):
        self.users: List[User] = []

    def find_all(self):
        return self.users

    def create(
        self,
        name,
        email,
    ):
        user = User(id=uuid.uuid4(), name=name, email=email)
        self.users.append(user)

        return user

    def find_by_id(
        self,
        id,
    ):
        pass

    def find_by_email(
        self,
        email,
    ):
        return next(
            (user for user in self.users if user.email == email),
            None,
        )

    def update(
        self,
        id,
        name,
        email,
    ):
        pass
