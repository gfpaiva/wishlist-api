import abc
from typing import Optional, List

from src.domains.wishlists.model.wishlist import Wishlist


class WishlistsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_all(
        self,
    ) -> List[Wishlist]:
        pass

    @abc.abstractclassmethod
    def find_by_id(
        self,
        id: str,
    ) -> Wishlist:
        pass

    @abc.abstractclassmethod
    def create(
        self,
        user_id: str,
        title: str,
        description: str,
    ) -> Wishlist:
        pass

    @abc.abstractclassmethod
    def update(
        self,
        id: str,
        title: Optional[str],
        description: Optional[str],
    ) -> Wishlist:
        pass

    @abc.abstractclassmethod
    def delete(
        self,
        id: str,
    ) -> bool:
        pass
