import abc
from typing import List, Optional

from src.domains.products.model.product import Product


class ProductsRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_page(
        self,
        page: Optional[str],
    ) -> List[Product]:
        """
        Find list of products with pagination. Auto starts with page '1'
        """
        pass

    @abc.abstractclassmethod
    def find_by_id(
        self,
        id: str,
    ) -> Product:
        """
        Find single product by given id(uuid)
        """
        pass
