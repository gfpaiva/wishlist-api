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
        wishlist = Wishlist.select().where(Wishlist.id == id)
        return wishlist.get() if wishlist else None

    def find_by_user_id(
        self,
        user_id,
    ):
        wishlists = Wishlist.select(
            Wishlist.id,
            Wishlist.title,
            Wishlist.description
        ).where(Wishlist.user == user_id)
        return wishlists

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
