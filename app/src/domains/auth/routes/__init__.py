from fastapi import (
    APIRouter,
    Depends
)
from fastapi.security import OAuth2PasswordRequestForm

from src.infra.server_responses import unauthorized

from src.domains.auth.model.token import Token
from src.domains.auth.repository import (
    DBAuthsRepository,
    PasslibRepository,
    JWTRepository,
)
from src.domains.auth.services.login import Login

auths_repository = DBAuthsRepository()
hash_repository = PasslibRepository()
token_repository = JWTRepository()
login_service = Login(
    auths_repository=auths_repository,
    hash_repository=hash_repository,
    token_repository=token_repository,
)

auth_router = APIRouter()


@auth_router.post(
    '/token',
    response_model=Token,
    responses=unauthorized,
    tags=['auth'],
)
def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login user and return new bearer token
    """
    access_token = login_service.run(
        username=form_data.username,
        password=form_data.password,
    )

    return {
        'token_type': 'bearer',
        'access_token': access_token,
    }
