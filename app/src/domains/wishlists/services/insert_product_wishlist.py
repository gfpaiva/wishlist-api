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


class InsertProductWishlist:
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
        wishlist_id,
        product_id,
    ) -> Wishlist:
        """
        Service for insert products on wishlist.
        Checks if wishlist exists,
        if product alredy exists on wishlist (can't duplicate)
        and if product exists on products_repository (external service)
        """
        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        product = (self.wishlists_products_repository
                   .find_products_by_product_id(
                       wishlist_id=wishlist_id,
                       product_id=product_id,
                   ))

        if product:
            raise WishlistException(
                status_code=409,
                detail=f'Product {product_id} is alredy on Wishlist'
            )

        product_data = self.products_repository.find_by_id(product_id)

        if not product_data:
            raise WishlistException(
                status_code=404,
                detail=f'Product {product_id} does not exists'
            )

        self.wishlists_products_repository.insert_product(
            wishlist_id=wishlist_id,
            product_id=product_id,
        )

        wishlist.products = [product_data]

        return wishlist
