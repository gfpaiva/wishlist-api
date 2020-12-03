from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException


class DeleteUser:
    def __init__(
        self,
        users_repository: UsersRepository,
    ):
        self.users_repository = users_repository

    def run(
        self,
        id: str,
    ) -> bool:
        """
        Service for delete user by given id using users_repository.
        Checks if user exists before delete it.
        """
        user = self.users_repository.find_by_id(id)

        if not user:
            raise UserException(
                status_code=404,
                detail=f'User {id} does not exists'
            )

        self.users_repository.delete(id)
        return True
