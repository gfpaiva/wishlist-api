from typing import List
import uuid

from src.domains.wishlists.repository.wishlists_products_repository import (
    WishlistsProductsRepository
)
from src.domains.wishlists.model.wishlist_product import WishlistProduct


class FakeWishlistsProductsRepository(WishlistsProductsRepository):
    def __init__(self):
        self.wishlists_products: List[WishlistProduct] = []

    def find_products_by_wishlist_id(
        self,
        wishlist_id,
    ):
        products = []
        for product in self.wishlists_products:
            if product.wishlist_id == wishlist_id:
                products.append(product)
        return products

    def find_products_by_product_id(
        self,
        wishlist_id,
        product_id,
    ):
        return next(
            (product
                for product in self.wishlists_products
                if product.wishlist_id == wishlist_id
                and product.product_id == product_id
             ),
            None,
        )

    def insert_product(
        self,
        wishlist_id,
        product_id,
    ):
        product = WishlistProduct(
            id=uuid.uuid4(),
            wishlist_id=wishlist_id,
            product_id=product_id,
        )
        self.wishlists_products.append(product)
        return product

    def delete_product(
        self,
        wishlist_id,
        product_id,
    ):
        self.wishlists_products = [
            (product
                for product in self.wishlists_products
                if not product.wishlist == wishlist_id
                and not product.product_id == product_id
             )
        ]
        return True
