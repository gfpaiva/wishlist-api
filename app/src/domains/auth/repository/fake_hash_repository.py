from src.domains.auth.repository.hash_repository import HashRepository


class FakeHashRepository(HashRepository):
    def verify(
        self,
        plain,
        hashed,
    ):
        return plain == hashed

    def hash(
        self,
        plain,
    ):
        return plain
