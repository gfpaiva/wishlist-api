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
        return User.get_by_id(id)

    def find_by_email(
        self,
        email: str,
    ):
        return User.select().where(User.email == email)

    def create(
        self,
        name: str,
        email: str,
    ):
        new_user = User(name=name, email=email)
        new_user.save()
        return new_user.__data__

    def update(
        self,
        name,
        email,
    ):
        pass
