from typing import List
import uuid

from src.domains.wishlists.model.wishlist import Wishlist
from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)


class FakeWishlistsRepository(WishlistsRepository):
    def __init__(self):
        self.wishlists: List[Wishlist] = []

    def find_by_id(
        self,
        id,
    ):
        return next(
            (wishlist for wishlist in self.wishlists if wishlist.id == id),
            None,
        )

    def find_by_user_id(
        self,
        user_id,
    ):
        return next(
            (wishlist
                for wishlist in self.wishlists if wishlist.user == user_id
             ),
            None,
        )

    def create(
        self,
        user_id,
        title,
        description,
    ):
        wishlist = Wishlist(
            id=uuid.uuid4(),
            user_id=user_id,
            title=title,
            description=description
        )
        self.wishlists.append(wishlist)
        return wishlist

    def update(
        self,
        id,
        title,
        description,
    ):
        find_wishlist = None

        for wishlist in self.wishlists:
            if wishlist.id == id:
                if title:
                    wishlist.title = title
                if description:
                    wishlist.description = description
            find_wishlist = wishlist

        return find_wishlist

    def delete(
        self,
        id,
    ):
        self.wishlists = [
            wishlist for wishlist in self.wishlists if not (wishlist.id == id)
        ]
        return True
