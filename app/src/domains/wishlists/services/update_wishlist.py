from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.exceptions.wishlist_exception import WishlistException


class UpdateWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
    ):
        self.wishlists_repository = wishlists_repository

    def run(
        self,
        id,
        title,
        description,
    ):
        """
        Service for update wishlist details.
        Checks required fields and if wishlist exists
        """
        if not title and not description:
            raise WishlistException(
                status_code=400,
                detail='You must provide title or description'
            )

        wishlist = self.wishlists_repository.find_by_id(id)

        if not wishlist:
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {id} does not exists'
            )

        wishlist = self.wishlists_repository.update(
            id=id,
            title=title,
            description=description,
        )
        return wishlist
