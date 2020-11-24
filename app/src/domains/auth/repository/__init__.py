from os import getenv
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.domains.auth.model.auth import Auth
from src.domains.auth.repository.auths_repository import AuthsRepository
from src.domains.auth.repository.hash_repository import HashRepository
from src.domains.auth.repository.token_repository import TokenRepository
from src.exceptions.credentials_exception import CredentialsException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class DBAuthsRepository(AuthsRepository):
    def find_by_username(
        self,
        username,
    ):
        auth = Auth.select().where(Auth.username == username)
        return auth.get() if auth else None


class PasslibRepository(HashRepository):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def verify(
        self,
        plain,
        hashed,
    ):
        return self.pwd_context.verify(plain, hashed)

    def hash(
        self,
        plain,
    ):
        return self.pwd_context.hash(plain)


class JWTRepository(TokenRepository):
    def __init__(self):
        self.secret_key = getenv('JWT_SECRET', '')
        self.algorithm = 'HS256'
        self.access_token_expire_minutes = 30

    def encode(
        self,
        data,
    ):
        expires_delta = timedelta(minutes=self.access_token_expire_minutes)
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(
            to_encode, self.secret_key,
            algorithm=self.algorithm,
        )
        return encoded_jwt

    def decode(
        self,
        token: str = Depends(oauth2_scheme),
    ):
        credentials_exception = CredentialsException(
            status_code=401,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
            )
            username = payload.get('sub')

            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        return payload
