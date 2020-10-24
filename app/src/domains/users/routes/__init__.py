from src.infra.server import app
from src.domains.users.services.create_user import CreateUser
from src.domains.users.repository import DBUsersRepository
from src.domains.users.model.user import UserRequestBody

users_repository = DBUsersRepository()
create_user_service = CreateUser(users_repository)


@app.get('/user')
def show_users():
    return users_repository.find_all()


@app.post('/user')
def create_user(user: UserRequestBody):
    new_user = create_user_service.run(name=user.name, email=user.email)
    return new_user
