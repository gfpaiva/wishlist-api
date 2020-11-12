from typing import Optional
from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)
from pydantic import BaseModel

from src.infra.db import db
from src.domains.wishlists.model.wishlist import Wishlist


class WishlistProduct(Model):
    id = CharField(primary_key=True, null=False)
    wishlist = ForeignKeyField(
        Wishlist,
        column_name='wishlist_id',
        on_delete='CASCADE',
        null=False
    )
    product_id = CharField(null=False)

    class Meta:
        table_name = 'wishlists_products'
        database = db


# class WishlistRequestBody(BaseModel):
#     title: str
#     description: str


# class UserUpdateRequestBody(BaseModel):
#     name: Optional[str]
#     email: Optional[str]


# class UserResponseBody(BaseModel):
#     id: str
#     name: str
#     email: str
