from peewee import (
    Model,
    CharField,
    ForeignKeyField,
)

from src.infra.db import db
from src.domains.wishlists.model.wishlist import Wishlist


class WishlistProduct(Model):
    """
    Model for wishlist products in database. With fields id, product_id
    and wishlist as relationship with Wishlist model
    """
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
