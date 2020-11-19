from typing import Optional, List
from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)
from pydantic import BaseModel

from src.infra.db import db
from src.domains.users.model.user import (
    User,
    UserResponse,
)
from src.domains.products.model.product import (
    Product,
    ProductResponse,
)


class Wishlist(Model):
    """
    Model for wishlist in database. With fields id, title, description
    and user as relationship with User model
    """
    id = CharField(primary_key=True, null=False)
    title = CharField(null=False)
    description = CharField()
    user = ForeignKeyField(
        User,
        column_name='user_id',
        on_delete='CASCADE'
    )
    products: Optional[List[Product]] = []

    class Meta:
        table_name = 'wishlists'
        database = db


class WishlistRequestBody(BaseModel):
    """
    Schema for http post request json body
    """
    title: str
    description: Optional[str]


class WishlistUpdateRequestBody(BaseModel):
    """
    Schema for http patch request json body
    """
    title: Optional[str]
    description: Optional[str]


class WishlistResponse(BaseModel):
    """
    Schema for single wishlist http response
    """
    id: str
    title: str
    description: str


class WishlistUserResponse(BaseModel):
    """
    Schema for single wishlist with user data http response
    """
    title: str
    description: str
    user: UserResponse


class WishlistProductsResponse(BaseModel):
    """
    Schema for single wishlist with user and products data http response
    """
    title: str
    description: str
    user: UserResponse
    products: List[ProductResponse]
