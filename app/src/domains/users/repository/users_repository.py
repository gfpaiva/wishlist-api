import abc
from typing import Optional, List

from src.domains.users.model.user import User


class UsersRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_all(
        self,
    ) -> List[User]:
        """
        Find all users and return it on list
        """
        pass

    @abc.abstractclassmethod
    def find_by_id(
        self,
        user_id: str,
    ) -> User:
        """
        Find single user by given id(uuid)
        """
        pass

    @abc.abstractclassmethod
    def find_by_email(
        self,
        email: str,
    ) -> User:
        """
        Find single user by given email string
        """
        pass

    @abc.abstractclassmethod
    def create(
        self,
        name: str,
        email: str,
    ) -> User:
        """
        Create new user. Required fields name and email
        """
        pass

    @abc.abstractclassmethod
    def update(
        self,
        user_id: str,
        name: Optional[str],
        email: Optional[str],
    ) -> User:
        """
        Update user by given id(uuid)
        """
        pass

    @abc.abstractclassmethod
    def delete(
        self,
        user_id: str,
    ) -> bool:
        """
        Delete user by given id(uuid)
        """
        pass
