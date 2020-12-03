import json
import requests

from fastapi import HTTPException

from src.infra.cache import redis
from src.domains.products.model.product import Product
from src.domains.products.repository.products_repository import (
    ProductsRepository
)


class APIProductsRepository(ProductsRepository):
    def __init__(self):
        self.BASE_URL = 'http://challenge-api.luizalabs.com'
        self.cache = redis
        self.cache_key_prefix = 'product-api/'

    def find_by_page(
        self,
        page='1'
    ):
        res = {}
        cache_key = f'{self.cache_key_prefix}page:{page}'
        res_cache = self.cache.get(cache_key)

        if res_cache:
            res_json = res_cache
        else:
            res = requests.get(f'{self.BASE_URL}/api/product/?page={page}')
            res_json = res.text
            self.cache.set(cache_key, res_json)

        data = json.loads(res_json)
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
        product_id: str,
    ):
        res = None
        cache_key = f'{self.cache_key_prefix}product:{product_id}'
        res_cache = self.cache.get(cache_key)

        if res_cache:
            res_json = res_cache
        else:
            res = requests.get(f'{self.BASE_URL}/api/product/{product_id}/')
            res_json = res.text
            self.cache.set(cache_key, res_json)

        product = json.loads(res_json)

        try:
            if not res_cache:
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
