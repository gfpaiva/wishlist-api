from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException


class DeleteUser:
    def __init__(self, users_repository):
        self.users_repository: UsersRepository = users_repository

    def run(
        self,
        id,
    ):
        user = self.users_repository.find_by_id(id)

        if not user:
            raise UserException(
                status_code=404,
                detail=f'User {id} does not exists'
            )

        user = self.users_repository.delete(id)
        return True
