import uuid
from typing import List
from fastapi import HTTPException

from src.infra.server import app
from src.domains.users.services.create_user import CreateUser
from src.domains.users.repository import DBUsersRepository
from src.domains.users.model.user import (
    UserRequestBody,
    UserResponseBody,
)

users_repository = DBUsersRepository()
create_user_service = CreateUser(users_repository)


@app.get('/user', response_model=List[UserResponseBody])
def list_users():
    return users_repository.find_all()


@app.get('/user/{id}', response_model=UserResponseBody)
def show_user(id: uuid.UUID):
    id = str(id)
    user = users_repository.find_by_id(id)
    print('user', user)
    if user:
        return user
    else:
        raise HTTPException(
            status_code=404
        )


@app.post('/user')
def create_user(user: UserRequestBody):
    new_user = create_user_service.run(name=user.name, email=user.email)
    return new_user
