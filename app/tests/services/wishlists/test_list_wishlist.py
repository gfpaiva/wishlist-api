import pytest

from src.domains.wishlists.services.list_wishlist import (
    ListWishlist
)
from src.domains.wishlists.repository.fake_wishlists_repository import (
    FakeWishlistsRepository
)
from src.domains.wishlists.repository.fake_wishlists_products_repository import (
    FakeWishlistsProductsRepository
)
from src.domains.products.repository.fake_products_repository import (
    FakeProductsRepository
)
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.wishlist_exception import WishlistException

wishlists_repository = FakeWishlistsRepository()
users_repository = FakeUsersRepository()
products_repository = FakeProductsRepository()
wishlists_products_repository = FakeWishlistsProductsRepository()


@pytest.fixture
def list_wishlist():
    wishlists_repository.wishlists = []
    users_repository.users = []
    wishlists_products_repository.wishlists_products = []

    created_user = users_repository.create(name='test', email='test@test.com')
    created_wishlist = wishlists_repository.create(
        user_id=created_user.id,
        title='title test',
        description='description test',
    )
    wishlists_products_repository.insert_product(
        wishlist_id=created_wishlist.id,
        product_id='958ec015-cfcf-258d-c6df-1721de0ab6ea',
    )
    list_wishlist_service = ListWishlist(
        wishlists_repository=wishlists_repository,
        wishlists_products_repository=wishlists_products_repository,
        products_repository=products_repository,
    )

    return list_wishlist_service, created_wishlist


def test_should_list_wishlist(
    list_wishlist,
):
    list_wishlist_service, created_wishlist = list_wishlist
    wishlist = list_wishlist_service.run(created_wishlist.id)

    assert (
        wishlist.id == created_wishlist.id and
        wishlist.title == 'title test' and
        wishlist.description == 'description test' and
        isinstance(wishlist.products, list) and
        len(wishlist.products) == 1 and
        wishlist.products[0].id == '958ec015-cfcf-258d-c6df-1721de0ab6ea'
    )


def test_should_not_list_wishlist_and_raise_for_invalid_wishlist_id(
    list_wishlist,
):
    with pytest.raises(WishlistException):
        list_wishlist_service = list_wishlist[0]
        list_wishlist_service.run('test-id')
