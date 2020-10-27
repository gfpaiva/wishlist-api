from src.domains.users.repository.users_repository import UsersRepository
from src.exceptions.user_exception import UserException


class UpdateUser:
    def __init__(self, users_repository):
        self.users_repository: UsersRepository = users_repository

    def run(
        self,
        id,
        name,
        email,
    ):
        if not name and not email:
            raise UserException(
                status_code=400,
                detail='You must provide name or email'
            )

        user = self.users_repository.find_by_id(id)

        if not user:
            raise UserException(
                status_code=404,
                detail=f'User {id} does not exists'
            )

        if email and email != user['email']:
            find_email = self.users_repository.find_by_email(email)

            if find_email:
                raise UserException(
                    status_code=400,
                    detail=f'User with email {email} alredy exists'
                )

        user = self.users_repository.update(id=id, name=name, email=email)
        return user
