import logging

from src.domains.users.model.user import User
from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException

logger = logging.getLogger(__name__)


class CreateUser:
    def __init__(
        self,
        users_repository: UsersRepository,
    ):
        self.users_repository = users_repository

    def run(
        self,
        name: str,
        email: str,
    ) -> User:
        """
        Service for create new user using users_repository.
        Checks required fields
        and user email alredy exists before insert it.
        """
        logger.info(f'Creating user <{name}> - <{email}>')

        if not name or not email:
            logger.exception(
                'Did not provide name or email'
            )
            raise UserException(
                status_code=400,
                detail='You must provide name and email'
            )

        find_email = self.users_repository.find_by_email(email)

        if find_email:
            logger.exception(
                f'User with <{email}> alredy exists'
            )
            raise UserException(
                status_code=409,
                detail=f'User with email {email} alredy exists'
            )

        user = self.users_repository.create(name=name, email=email)
        return user
