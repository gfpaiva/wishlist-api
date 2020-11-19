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


class ListWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
        wishlists_produts_repository: WishlistsProductsRepository,
        products_repository: ProductsRepository,
    ):
        self.wishlists_repository = wishlists_repository
        self.wishlists_produts_repository = wishlists_produts_repository
        self.products_repository = products_repository

    def run(
        self,
        id,
    ):
        """
        Service for list single wishlist.
        Chekcs if wishlist exists.
        If wishlist has products take products data
        from products_repository (external service) and append on return data
        """
        wishlist = self.wishlists_repository.find_by_id(id)

        if not wishlist:
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {id} does not exists'
            )

        products = (self.wishlists_produts_repository
                    .find_products_by_wishlist_id(id))

        if products:
            wishlist.products = []

            for product in products:
                product_data = self.products_repository.find_by_id(
                    product.product_id
                )
                wishlist.products.append(product_data)

        return wishlist
