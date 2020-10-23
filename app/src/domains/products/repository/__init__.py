import requests
from fastapi import HTTPException

from src.domains.products.model.product import Product
from src.domains.products.repository.products_repository import (
    ProductsRepository
)

BASE_URL = 'http://challenge-api.luizalabs.com'


class APIProductsRepository(ProductsRepository):
    def find_by_page(
        self,
        page='1'
    ):
        res = requests.get(f'{BASE_URL}/api/product/?page={page}')
        data = res.json()
        products = data['products']

        if data:
            return [
                Product(
                    id=product['id'],
                    title=product['title'],
                    price=product['price'],
                    image=product['image'],
                    brand=product['brand'],
                    review_score=product.get('reviewScore', None),
                ) for product in products
            ]

        return None

    def find_by_id(
        self,
        id: str,
    ):
        res = requests.get(f'{BASE_URL}/api/product/{id}/')
        product = res.json()

        try:
            res.raise_for_status()

            if product:
                return Product(
                    id=product['id'],
                    title=product['title'],
                    price=product['price'],
                    image=product['image'],
                    brand=product['brand'],
                    review_score=product.get('reviewScore', None),
                )
        except requests.exceptions.HTTPError as e:
            raise HTTPException(
                status_code=res.status_code,
                detail=e.strerror
            )
        except KeyError:
            raise HTTPException(
                status_code=500,
            )
