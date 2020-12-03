import pytest

from src.domains.wishlists.services.update_wishlist import UpdateWishlist
from src.domains.wishlists.repository.fake_wishlists_repository import (
    FakeWishlistsRepository
)
from src.domains.users.repository.fake_users_repository import (
    FakeUsersRepository
)
from src.exceptions.wishlist_exception import WishlistException

users_repository = FakeUsersRepository()
wishlists_repository = FakeWishlistsRepository()


@pytest.fixture
def update_wishlist():
    users_repository.users = []
    wishlists_repository.wishlists = []
    update_wishlist_service = UpdateWishlist(
        wishlists_repository=wishlists_repository
    )

    created_user = users_repository.create(name='test', email='test@test.com')
    created_wishlist = wishlists_repository.create(
        user_id=created_user.id,
        title='title test',
        description='description test',
    )

    return (update_wishlist_service, created_wishlist)


def test_should_update_and_return_wishlist(update_wishlist):
    update_wishlist_service, created_wishlist = update_wishlist
    wishlist = update_wishlist_service.run(
        wishlist_id=created_wishlist.id,
        title='title test2',
        description='description test2',
    )

    assert (
        wishlist.title == 'title test2'
        and wishlist.description == 'description test2'
    )


def test_should_not_update_wishlist_and_raise_for_invalid_data(
    update_wishlist,
):
    with pytest.raises(WishlistException):
        update_wishlist_service, created_wishlist = update_wishlist
        update_wishlist_service.run(
            wishlist_id=created_wishlist.id,
            title=None,
            description=None,
        )


def test_should_not_update_wishlist_and_raise_for_invalid_wishlist_id(
    update_wishlist,
):
    with pytest.raises(WishlistException):
        update_wishlist_service = update_wishlist[0]
        update_wishlist_service.run(
            wishlist_id='test-id',
            title='title test2',
            description='description test2',
        )
