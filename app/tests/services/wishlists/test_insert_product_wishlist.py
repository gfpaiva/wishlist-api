import pytest

from src.domains.wishlists.services.insert_product_wishlist import (
    InsertProductWishlist
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
def insert_product():
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
    insert_product_wishlist_service = InsertProductWishlist(
        wishlists_repository=wishlists_repository,
        wishlists_products_repository=wishlists_products_repository,
        products_repository=products_repository,
    )

    return (insert_product_wishlist_service, created_wishlist)


def test_should_insert_product_into_wishlist_and_return_wishlist(
    insert_product,
):
    insert_product_wishlist_service, created_wishlist = insert_product
    wishlist = insert_product_wishlist_service.run(
        wishlist_id=created_wishlist.id,
        product_id='1bf0f365-fbdd-4e21-9786-da459d78dd1f',
    )

    assert (
        isinstance(wishlist.products, list) and
        len(wishlist.products) == 1 and
        wishlist.products[0].id == '1bf0f365-fbdd-4e21-9786-da459d78dd1f'
    )


def test_should_not_insert_product_and_raise_for_invalid_wishlist_id(
    insert_product,
):
    with pytest.raises(WishlistException):
        insert_product_wishlist_service = insert_product[0]
        insert_product_wishlist_service.run(
            wishlist_id='test-id',
            product_id='1bf0f365-fbdd-4e21-9786-da459d78dd1f',
        )


def test_should_not_insert_product_and_raise_for_invalid_product_id(
    insert_product,
):
    with pytest.raises(WishlistException):
        insert_product_wishlist_service, created_wishlist = insert_product
        insert_product_wishlist_service.run(
            wishlist_id=created_wishlist.id,
            product_id='test-id',
        )


def test_should_not_insert_product_and_raise_for_duplicated_product_id(
    insert_product,
):
    with pytest.raises(WishlistException):
        insert_product_wishlist_service, created_wishlist = insert_product
        insert_product_wishlist_service.run(
            wishlist_id=created_wishlist.id,
            product_id='958ec015-cfcf-258d-c6df-1721de0ab6ea',
        )
