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
        user_id,
    ):
        return next(
            (user for user in self.users if user.id == user_id), None
        )

    def find_by_email(
        self,
        email,
    ):
        return next(
            (user for user in self.users if user.email == email), None
        )

    def update(
        self,
        user_id,
        name,
        email,
    ):
        find_user = None

        for user in self.users:
            if user.id == user_id:
                if name:
                    user.name = name
                if email:
                    user.email = email
            find_user = user

        return find_user

    def delete(
        self,
        user_id,
    ):
        self.users = [user for user in self.users if not (user.id == user_id)]
        return True
