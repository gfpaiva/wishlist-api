import abc

from src.domains.auth.model.auth import Auth


class AuthsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_username(
        self,
        username: str,
    ) -> Auth:
        """
        Find single auth by given username
        """
        pass
