import abc


class TokenRepository(abc.ABC):
    @abc.abstractclassmethod
    def encode(
        self,
        data: dict,
    ) -> str:
        """
        Encode request data to valid token
        """
        pass

    @abc.abstractclassmethod
    def decode(
        self,
        token: str,
    ) -> dict:
        """
        Decode token and retur data as dict
        """
        pass
