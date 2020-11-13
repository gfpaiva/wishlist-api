from typing import List
from playhouse.shortcuts import model_to_dict

from src.infra.server import app
from src.domains.users.repository import DBUsersRepository
from src.domains.users.services.create_user import CreateUser
from src.domains.users.services.update_user import UpdateUser
from src.domains.users.services.delete_user import DeleteUser
from src.domains.users.model.user import (
    UserRequestBody,
    UserResponse,
    UserUpdateRequestBody,
)
from src.exceptions.user_exception import UserException

users_repository = DBUsersRepository()
create_user_service = CreateUser(users_repository)
update_user_service = UpdateUser(users_repository)
delete_user_service = DeleteUser(users_repository)


@app.get(
    '/user',
    response_model=List[UserResponse],
)
def list_users():
    """
    List all users
    """
    users = users_repository.find_all()
    return [user for user in users.dicts()]


@app.post(
    '/user',
    response_model=UserResponse,
)
def create_user(user: UserRequestBody):
    """
    Create a new user
    """
    new_user = create_user_service.run(name=user.name, email=user.email)
    return model_to_dict(new_user)


@app.get(
    '/user/{id}',
    response_model=UserResponse,
)
def show_user(id: str):
    """
    Show specific user by given id(uuid)
    """
    user = users_repository.find_by_id(id)
    if not user:
        raise UserException(
            status_code=404,
            detail=f'User {id} does not exists'
        )
    return model_to_dict(user)


@app.patch(
    '/user/{id}',
    response_model=UserResponse,
)
def update_user(id: str, user: UserUpdateRequestBody):
    """
    Update specific user by given id(uuid).
    Can update one or both fields user/email
    """
    updated_user = update_user_service.run(
        id=id,
        name=user.name,
        email=user.email,
    )
    return model_to_dict(updated_user)


@app.delete(
    '/user/{id}',
    status_code=204,
)
def delete_user(id: str):
    """
    Delete specific user by given id(uuid).
    """
    delete_user_service.run(id)
    return
