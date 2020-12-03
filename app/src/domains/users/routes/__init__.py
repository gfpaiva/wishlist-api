from uuid import UUID
from typing import List
from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

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

user_router = APIRouter()


@user_router.get(
    '/user',
    response_model=List[UserResponse],
    tags=['user'],
)
def list_users():
    """
    List all users
    """
    users = users_repository.find_all()
    return [user for user in users.dicts()]


@user_router.post(
    '/user',
    response_model=UserResponse,
    tags=['user'],
)
def create_user(user: UserRequestBody):
    """
    Create a new user
    """
    new_user = create_user_service.run(name=user.name, email=user.email)
    return model_to_dict(new_user)


@user_router.get(
    '/user/{id}',
    response_model=UserResponse,
    tags=['user'],
)
def show_user(user_id: UUID):
    """
    Show specific user by given id(uuid)
    """
    user = users_repository.find_by_id(user_id)
    if not user:
        raise UserException(
            status_code=404,
            detail=f'User {user_id} does not exists'
        )
    return model_to_dict(user)


@user_router.patch(
    '/user/{id}',
    response_model=UserResponse,
    tags=['user'],
)
def update_user(user_id: UUID, user: UserUpdateRequestBody):
    """
    Update specific user by given id(uuid).
    Can update one or both fields user/email
    """
    updated_user = update_user_service.run(
        user_id=user_id,
        name=user.name,
        email=user.email,
    )
    return model_to_dict(updated_user)


@user_router.delete(
    '/user/{id}',
    status_code=204,
    tags=['user'],
)
def delete_user(user_id: UUID):
    """
    Delete specific user by given id(uuid).
    """
    delete_user_service.run(user_id)
    return
