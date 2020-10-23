from typing import List

from src.domains.products.model.product import Product
from src.domains.products.repository.products_repository import (
    ProductsRepository
)


class FakeProductsRepository(ProductsRepository):
    def __init__(self):
        example_product = Product(
            id='1',
            title='Product',
            price=100.0,
            image='example.jpg',
            brand='Brand',
            review_score=4.99
        )
        another_example_product = Product(
            id='2',
            title='Product 2',
            price=299.9,
            image='example-2.jpg',
            brand='Brand',
            review_score=5.0
        )

        self.products: List[Product] = [
            example_product,
            another_example_product,
        ]

    def find_by_page(
        self,
        page='1'
    ):
        return self.products

    def find_by_id(
        self,
        id: str,
    ) -> Product:
        return next(
            (product for product in self.products if product.id == id),
            None,
        )
