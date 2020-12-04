import pytest

from src.domains.users.model.user import User
from src.domains.wishlists.model.wishlist import Wishlist
from src.domains.wishlists.model.wishlist_product import WishlistProduct


@pytest.fixture(autouse=True)
def clear():
    User.delete().execute()
    Wishlist.delete().execute()
    WishlistProduct.delete().execute()
