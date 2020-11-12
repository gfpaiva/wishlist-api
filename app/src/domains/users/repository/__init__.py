from src.domains.users.repository.users_repository import UsersRepository
from src.domains.users.model.user import User


class DBUsersRepository(UsersRepository):
    def find_all(
        self,
    ):
        users = User.select().dicts()
        return users

    def find_by_id(
        self,
        id: str,
    ):
        user = User.select().where(User.id == id)
        return user.get() if user else None

    def find_by_email(
        self,
        email: str,
    ):
        user = User.select().where(User.email == email)
        return user.get() if user else None

    def create(
        self,
        name: str,
        email: str,
    ):
        new_user = User(name=name, email=email)
        new_user.save()
        return new_user

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
        return user

    def delete(
        self,
        id,
    ):
        User.delete().where(User.id == id).execute()
        return True
