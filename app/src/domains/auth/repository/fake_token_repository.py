from src.domains.auth.repository.token_repository import TokenRepository


class FakeTokenRepository(TokenRepository):
    def encode(
        self,
        data,
    ):
        return data['sub']

    def decode(
        self,
        token,
    ):
        pass
