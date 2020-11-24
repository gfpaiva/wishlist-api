import abc


class HashRepository(abc.ABC):
    @abc.abstractclassmethod
    def verify(
        self,
        plain: str,
        hashed: str,
    ) -> bool:
        """
        Verify if hashed password matches with plain text
        """
        pass

    @abc.abstractclassmethod
    def hash(
        self,
        plain: str,
    ) -> str:
        """
        Return hashed plain text
        """
        pass
