import abc
from typing import List

from src.domains.wishlists.model.wishlist_product import WishlistProduct


class WishlistsProductsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_products_by_wishlist_id(
        self,
        wishlist_id: str,
    ) -> List[WishlistProduct]:
        pass

    @abc.abstractclassmethod
    def insert_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> WishlistProduct:
        pass

    @abc.abstractclassmethod
    def delete_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> bool:
        pass
