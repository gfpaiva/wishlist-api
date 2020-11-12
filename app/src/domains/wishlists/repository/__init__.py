from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.domains.wishlists.repository.wishlists_products_repository import (
    WishlistsProductsRepository
)

from src.domains.wishlists.model.wishlist import Wishlist
from src.domains.wishlists.model.wishlist_product import WishlistProduct


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
        wishlist = Wishlist.get_by_id(id)

        if title:
            wishlist.title = title
        if description:
            wishlist.description = description

        wishlist.save()
        return wishlist

    def delete(
        self,
        id,
    ):
        Wishlist.delete().where(
            Wishlist.id == id
        ).execute()
        return True


class DBWishlistsProductsRepository(WishlistsProductsRepository):
    def find_by_products_by_wishlist_id(
        self,
        wishlist_id: str,
    ):
        products = WishlistProduct.select().where(
            WishlistProduct.wishlist == wishlist_id
        )
        return products

    def insert_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> WishlistProduct:
        new_product = WishlistProduct(
            wishlist_id=wishlist_id,
            product_id=product_id
        )
        new_product.save()
        return new_product

    def delete_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> bool:
        WishlistProduct.delete().where(
            WishlistProduct.product_id == product_id
        ).execute()
        return True
