import logging

from src.domains.wishlists.model.wishlist import Wishlist
from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.domains.wishlists.repository.wishlists_products_repository import (
    WishlistsProductsRepository
)
from src.domains.products.repository.products_repository import (
    ProductsRepository
)
from src.exceptions.wishlist_exception import WishlistException

logger = logging.getLogger(__name__)


class ListWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
        wishlists_products_repository: WishlistsProductsRepository,
        products_repository: ProductsRepository,
    ):
        self.wishlists_repository = wishlists_repository
        self.wishlists_products_repository = wishlists_products_repository
        self.products_repository = products_repository

    def run(
        self,
        wishlist_id: str,
    ) -> Wishlist:
        """
        Service for list single wishlist.
        Chekcs if wishlist exists.
        If wishlist has products take products data
        from products_repository (external service) and append on return data
        """
        logger.info(f'Linsting wishlist <{wishlist_id}>')

        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            logger.exception(
                f'Wishlist <{wishlist_id}> not found'
            )
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        products = (self.wishlists_products_repository
                    .find_products_by_wishlist_id(wishlist_id))

        if products:
            wishlist.products = []

            for product in products:
                product_data = self.products_repository.find_by_id(
                    product.product_id
                )
                wishlist.products.append(product_data)

        return wishlist
