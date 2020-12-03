import abc
from typing import Optional, List

from src.domains.wishlists.model.wishlist import Wishlist


class WishlistsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_id(
        self,
        wishlist_id: str,
    ) -> Wishlist:
        """
        Find single wishlist by given id(uuid)
        """
        pass

    @abc.abstractclassmethod
    def find_by_user_id(
        self,
        user_id: str,
    ) -> List[Wishlist]:
        """
        Find all wishlists for given user_id(uuid) and return it on list
        """
        pass

    @abc.abstractclassmethod
    def create(
        self,
        user_id: str,
        title: str,
        description: str,
    ) -> Wishlist:
        """
        Create new user. Required field title and description
        """
        pass

    @abc.abstractclassmethod
    def update(
        self,
        wishlist_id: str,
        title: Optional[str],
        description: Optional[str],
    ) -> Wishlist:
        """
        Update wishlist by given id(uuid)
        """
        pass

    @abc.abstractclassmethod
    def delete(
        self,
        wishlist_id: str,
    ) -> bool:
        """
        Delete wishlist by given id(uuid)
        """
        pass
