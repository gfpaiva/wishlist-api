import logging

from src.domains.users.model.user import User
from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException

logger = logging.getLogger(__name__)


class UpdateUser:
    def __init__(
        self,
        users_repository: UsersRepository,
    ):
        self.users_repository = users_repository

    def run(
        self,
        user_id: str,
        name: str,
        email: str,
    ) -> User:
        """
        Service for update user by given id using users_repository.
        Checks required fields and if is updating user email,
        checks if the new one alredy exists before update it.
        """
        logger.info(
            f'Updating user <{user_id}> with <{name}> - <{email}>'
        )

        if not name and not email:
            logger.exception(
                f'User <{user_id}> did not provide name or email'
            )
            raise UserException(
                status_code=400,
                detail='You must provide name or email'
            )

        user = self.users_repository.find_by_id(user_id)

        if not user:
            logger.exception(
                f'User <{user_id}> not found'
            )
            raise UserException(
                status_code=404,
                detail=f'User {user_id} does not exists'
            )

        if email and email != user.email:
            find_email = self.users_repository.find_by_email(email)

            if find_email:
                logger.exception(
                    f'User with <{email}> alredy exists'
                )
                raise UserException(
                    status_code=409,
                    detail=f'User with email {email} alredy exists'
                )

        user = self.users_repository.update(
            user_id=user_id,
            name=name,
            email=email
        )
        return user
