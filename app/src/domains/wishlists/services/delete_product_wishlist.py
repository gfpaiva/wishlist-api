import logging

from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.domains.wishlists.repository.wishlists_products_repository import (
    WishlistsProductsRepository
)
from src.exceptions.wishlist_exception import WishlistException

logger = logging.getLogger(__name__)


class DeleteProductWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
        wishlists_products_repository: WishlistsProductsRepository,
    ):
        self.wishlists_repository = wishlists_repository
        self.wishlists_products_repository = wishlists_products_repository

    def run(
        self,
        wishlist_id: str,
        product_id: str,
    ) -> bool:
        """
        Service for remove product from wishlist
        Cehcks if wishlist and product exists
        """
        logger.info(
            f'Deleting product {product_id} \
            for wishlist {wishlist_id}'
        )

        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            logger.exception(
                f'Wishlist {wishlist_id} not found'
            )
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        product = (self.wishlists_products_repository
                   .find_products_by_product_id(
                       wishlist_id=wishlist_id,
                       product_id=product_id,
                   ))

        if not product:
            logger.exception(
                f'Product {product_id} not found \
                in wishlist {wishlist_id}'
            )
            raise WishlistException(
                status_code=404,
                detail=f'Product {product_id} does not exists in wishlist'
            )

        self.wishlists_products_repository.delete_product(
            wishlist_id=wishlist_id,
            product_id=product_id,
        )
        return True
