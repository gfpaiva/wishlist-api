import logging

from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException

logger = logging.getLogger(__name__)


class DeleteUser:
    def __init__(
        self,
        users_repository: UsersRepository,
    ):
        self.users_repository = users_repository

    def run(
        self,
        user_id: str,
    ) -> bool:
        """
        Service for delete user by given id using users_repository.
        Checks if user exists before delete it.
        """
        logger.info(f'Deleting user <{user_id}>')

        user = self.users_repository.find_by_id(user_id)

        if not user:
            logger.exception(
                f'User <{user_id}> not found'
            )
            raise UserException(
                status_code=404,
                detail=f'User {user_id} does not exists'
            )

        self.users_repository.delete(user_id)
        return True
