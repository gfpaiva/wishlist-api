import pytest

from src.domains.wishlists.services.delete_product_wishlist import (
    DeleteProductWishlist
)
from src.domains.wishlists.repository.fake_wishlists_repository import (
    FakeWishlistsRepository
)
from src.domains.wishlists.repository.fake_wishlists_products_repository import (
    FakeWishlistsProductsRepository
)
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.wishlist_exception import WishlistException

wishlists_repository = FakeWishlistsRepository()
users_repository = FakeUsersRepository()
wishlists_products_repository = FakeWishlistsProductsRepository()


@pytest.fixture
def delete_product():
    wishlists_repository.wishlists = []
    users_repository.users = []
    wishlists_products_repository.wishlists_products = []

    created_user = users_repository.create(name='test', email='test@test.com')
    created_wishlist = wishlists_repository.create(
        user_id=created_user.id,
        title='title test',
        description='description test',
    )
    created_wishlist_product = wishlists_products_repository.insert_product(
        wishlist_id=created_wishlist.id,
        product_id='958ec015-cfcf-258d-c6df-1721de0ab6ea',
    )
    delete_product_wishlist_service = DeleteProductWishlist(
        wishlists_repository=wishlists_repository,
        wishlists_products_repository=wishlists_products_repository,
    )

    return delete_product_wishlist_service, created_wishlist_product


def test_should_delete_product_product_from_wishlist(
    delete_product,
):
    delete_product_wishlist_service, created_wishlist_product = delete_product
    deleted = delete_product_wishlist_service.run(
        wishlist_id=created_wishlist_product.wishlist_id,
        product_id=created_wishlist_product.product_id,
    )

    assert deleted is True


def test_should_not_delete_product_and_raise_for_invalid_wishlist_id(
    delete_product,
):
    with pytest.raises(WishlistException):
        (
            delete_product_wishlist_service,
            created_wishlist_product,
        ) = delete_product
        delete_product_wishlist_service.run(
            wishlist_id='test-id',
            product_id=created_wishlist_product.product_id,
        )


def test_should_not_delete_product_and_raise_for_invalid_product_id(
    delete_product,
):
    with pytest.raises(WishlistException):
        (
            delete_product_wishlist_service,
            created_wishlist_product,
        ) = delete_product
        delete_product_wishlist_service.run(
            wishlist_id=created_wishlist_product.wishlist_id,
            product_id='test-id',
        )
