import pytest

from src.domains.wishlists.services.delete_wishlist import DeleteWishlist
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
def delete_wishlist():
    users_repository.users = []
    wishlists_repository.wishlists = []
    delete_wishlist_service = DeleteWishlist(
        wishlists_repository=wishlists_repository
    )

    created_user = users_repository.create(name='test', email='test@test.com')
    created_wishlist = wishlists_repository.create(
        user_id=created_user.id,
        title='title test',
        description='description test',
    )

    return (delete_wishlist_service, created_wishlist)


def test_should_delete_wishlist(delete_wishlist):
    delete_wishlist_service, created_wishlist = delete_wishlist
    deleted = delete_wishlist_service.run(created_wishlist.id)

    assert deleted is True


def test_should_not_delete_wishlist_and_raise_for_invalid_wishlist_id(
    delete_wishlist,
):
    with pytest.raises(WishlistException):
        delete_wishlist_service = delete_wishlist[0]
        delete_wishlist_service.run('test-id')
