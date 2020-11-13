from typing import Optional, List
from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)
from pydantic import BaseModel

from src.infra.db import db
from src.domains.users.model.user import User
from src.domains.products.model.product import Product


class Wishlist(Model):
    id = CharField(primary_key=True, null=False)
    title = CharField(null=False)
    description = CharField()
    user = ForeignKeyField(
        User,
        column_name='user_id',
        on_delete='CASCADE'
    )
    products: List[Product] = []

    class Meta:
        table_name = 'wishlists'
        database = db


class WishlistRequestBody(BaseModel):
    title: str
    description: str


# class UserUpdateRequestBody(BaseModel):
#     name: Optional[str]
#     email: Optional[str]


# class UserResponseBody(BaseModel):
#     id: str
#     name: str
#     email: str
