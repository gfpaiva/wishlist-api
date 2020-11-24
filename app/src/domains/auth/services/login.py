from src.domains.auth.repository.auths_repository import AuthsRepository
from src.domains.auth.repository.hash_repository import HashRepository
from src.domains.auth.repository.token_repository import TokenRepository
from src.exceptions.credentials_exception import CredentialsException


class Login:
    def __init__(
        self,
        auths_repository: AuthsRepository,
        hash_repository: HashRepository,
        token_repository: TokenRepository,
    ):
        self.auths_repository = auths_repository
        self.hash_repository = hash_repository
        self.token_repository = token_repository

    def run(
        self,
        username,
        password,
    ) -> str:
        """
        Service for login user and get a token
        Checks if username auth exists and if password matches
        """
        if not username or not password:
            raise CredentialsException(
                status_code=400,
                detail='You must provide username and password'
            )

        auth = self.auths_repository.find_by_username(username=username)
        credentials_exception = CredentialsException(
            status_code=401,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        if not auth:
            raise credentials_exception

        if not self.hash_repository.verify(
            plain=password,
            hashed=auth.password,
        ):
            raise credentials_exception

        data = {
            'sub': auth.username,
        }
        token = self.token_repository.encode(data)

        return token
