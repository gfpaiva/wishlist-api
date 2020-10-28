from playhouse.shortcuts import model_to_dict

from src.domains.users.repository.users_repository import UsersRepository
from src.domains.users.model.user import User


class DBUsersRepository(UsersRepository):
    def find_all(
        self,
    ):
        users = User.select().dicts()
        return [user for user in users]

    def find_by_id(
        self,
        id: str,
    ):
        user = User.select().where(User.id == id)
        return model_to_dict(user.get()) if user else None

    def find_by_email(
        self,
        email: str,
    ):
        user = User.select().where(User.email == email)
        return model_to_dict(user.get()) if user else None

    def create(
        self,
        name: str,
        email: str,
    ):
        new_user = User(name=name, email=email)
        new_user.save()
        return model_to_dict(new_user)

    def update(
        self,
        id,
        name,
        email,
    ):
        user = User.get_by_id(id)

        if name:
            user.name = name
        if email:
            user.email = email

        user.save()
        return model_to_dict(user)

    def delete(
        self,
        id,
    ):
        user = User.get_by_id(id)
        User.delete().where(User.id == id).execute()
        return model_to_dict(user)
