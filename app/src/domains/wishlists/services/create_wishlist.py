from src.domains.users.repository.users_repository import UsersRepository
from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.exceptions.wishlist_exception import WishlistException


class CreateWishlist:
    def __init__(
        self,
        wishlists_repository,
        users_repository,
    ):
        self.wishlists_repository: WishlistsRepository = wishlists_repository
        self.users_repository: UsersRepository = users_repository

    def run(
        self,
        user_id,
        title,
        description,
    ):
        if not title:
            raise WishlistException(
                status_code=400,
                detail='You must provide any title'
            )

        user = self.users_repository.find_by_id(user_id)

        if not user:
            raise WishlistException(
                status_code=404,
                detail=f'User {user_id} does not exists'
            )

        wishlist = self.wishlists_repository.create(
            user_id=user_id,
            title=title,
            description=description
        )
        return wishlist