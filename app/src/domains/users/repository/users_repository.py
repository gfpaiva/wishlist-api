import abc
from typing import Optional, List

from src.domains.users.model.user import User


class UsersRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_all(
        self,
    ) -> List[User]:
        pass

    @abc.abstractclassmethod
    def find_by_id(
        self,
        id: str,
    ) -> User:
        pass

    @abc.abstractclassmethod
    def find_by_email(
        self,
        email: str,
    ) -> User:
        pass

    @abc.abstractclassmethod
    def create(
        self,
        name: str,
        email: str,
    ) -> User:
        pass

    @abc.abstractclassmethod
    def update(
        self,
        id: str,
        name: Optional[str],
        email: Optional[str],
    ) -> User:
        pass
