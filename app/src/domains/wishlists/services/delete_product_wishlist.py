from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.domains.wishlists.repository.wishlists_products_repository import (
    WishlistsProductsRepository
)
from src.exceptions.wishlist_exception import WishlistException


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
        wishlist_id,
        product_id,
    ):
        """
        Service for remove product from wishlist
        Cehcks if wishlist and product exists
        """
        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        product = (self.wishlists_products_repository
                   .find_by_products_by_product_id(
                       wishlist_id=wishlist_id,
                       product_id=product_id,
                   ))

        if not product:
            raise WishlistException(
                status_code=404,
                detail=f'Product {product_id} does not exists in wishlist'
            )

        self.wishlists_products_repository.delete_product(
            wishlist_id=wishlist_id,
            product_id=product_id,
        )
        return True
