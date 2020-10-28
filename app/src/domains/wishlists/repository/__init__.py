from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.domains.wishlists.model.wishlist import Wishlist


class DBWishlistsRepository(WishlistsRepository):
    def find_all(
        self,
    ):
        wishlists = Wishlist.select()
        return wishlists

    def find_by_id(
        self,
        id,
    ):
        pass

    def create(
        self,
        user_id,
        title,
        description,
    ):
        new_wishlist = Wishlist(
            user_id=user_id,
            title=title,
            description=description
        )
        new_wishlist.save()
        return new_wishlist

    def update(
        self,
        id,
        title,
        description,
    ):
        pass

    def delete(
        self,
        id,
    ):
        pass
