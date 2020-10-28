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
        return user.__dict__['__data__']

    def find_by_id(
        self,
        id,
    ):
        return next(
            (user.__dict__['__data__']
             for user in self.users if user.id == id),
            None,
        )

    def find_by_email(
        self,
        email,
    ):
        return next(
            (user.__dict__['__data__']
             for user in self.users if user.email == email),
            None,
        )

    def update(
        self,
        id,
        name,
        email,
    ):
        find_user = None

        for user in self.users:
            if user.id == id:
                if name:
                    user.name = name
                if email:
                    user.email = email
            find_user = user

        return find_user.__dict__['__data__']

    def delete(
        self,
        id,
    ):
        self.users = [user for user in self.users if not (user.id == id)]
        return True
