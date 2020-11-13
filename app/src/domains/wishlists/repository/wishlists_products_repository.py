import abc
from typing import List

from src.domains.wishlists.model.wishlist_product import WishlistProduct


class WishlistsProductsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_products_by_wishlist_id(
        self,
        wishlist_id: str,
    ) -> List[WishlistProduct]:
        """
        Find all products for given wishlist_id(uuid) and return it on list
        """
        pass

    @abc.abstractclassmethod
    def find_by_products_by_product_id(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> WishlistProduct:
        """
        Find product for given wishlist_id(uuid) and product_id(uuid)
        """
        pass

    @abc.abstractclassmethod
    def insert_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> WishlistProduct:
        """
        Create wishlist product. Required fields wishlist_id and product_id
        """
        pass

    @abc.abstractclassmethod
    def delete_product(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> bool:
        """
        Delete wishlist product by given id(uuid)
        """
        pass
