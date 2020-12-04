import uuid
import pytest

from src.domains.wishlists.services.create_wishlist import CreateWishlist
from src.domains.wishlists.repository.fake_wishlists_repository import (
    FakeWishlistsRepository
)
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.wishlist_exception import WishlistException

users_repository = FakeUsersRepository()


@pytest.fixture
def create_wishlist():
    users_repository.users = []
    create_wishlist_service = CreateWishlist(
        wishlists_repository=FakeWishlistsRepository(),
        users_repository=users_repository,
    )

    created_user = users_repository.create(name='test', email='test@test.com')

    return (create_wishlist_service, created_user)


def test_should_create_and_return_new_wishlist(create_wishlist):
    create_wishlist_service, created_user = create_wishlist
    wishlist = create_wishlist_service.run(
        user_id=created_user.id,
        title='title test',
        description='description test'
    )
    create_wishlist_service.run(
        user_id=created_user.id,
        title='title test',
        description='description test'
    )

    assert (
        isinstance(wishlist.id, uuid.UUID) and
        wishlist.title == 'title test' and
        wishlist.description == 'description test'
    )


def test_should_not_create_wishlist_and_raise_for_invalid_data(
    create_wishlist
):
    create_wishlist_service, created_user = create_wishlist
    with pytest.raises(WishlistException):
        create_wishlist_service.run(
            user_id=created_user.id,
            title=None,
            description='description test'
        )


def test_should_not_create_wishlist_and_raise_for_non_existing_user(
    create_wishlist
):
    create_wishlist_service = create_wishlist[0]
    with pytest.raises(WishlistException):
        create_wishlist_service.run(
            user_id='test-id',
            title='title test',
            description='description test'
        )
