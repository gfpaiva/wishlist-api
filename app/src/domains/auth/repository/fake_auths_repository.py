from typing import List

from src.domains.auth.repository.auths_repository import AuthsRepository
from src.domains.auth.model.auth import Auth


class FakeAuthsRepository(AuthsRepository):
    def __init__(self, auths=[]):
        self.auths: List[Auth] = auths

    def find_by_username(
        self,
        username,
    ):
        return next(
            (auth for auth in self.auths if auth.username == username), None
        )
