import logging

from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.exceptions.wishlist_exception import WishlistException

logger = logging.getLogger(__name__)


class DeleteWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
    ):
        self.wishlists_repository = wishlists_repository

    def run(
        self,
        wishlist_id: str,
    ) -> bool:
        """
        Service for delete wishlist by given id
        Checks if wishlist exists
        """
        logger.info(f'Deleting wishlist <{wishlist_id}>')

        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            logger.exception(
                f'Wishlist <{wishlist_id}> not found'
            )
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        self.wishlists_repository.delete(wishlist_id)
        return True
