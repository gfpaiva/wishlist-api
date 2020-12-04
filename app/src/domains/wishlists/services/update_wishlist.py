import logging

from src.domains.wishlists.model.wishlist import Wishlist
from src.domains.wishlists.repository.wishlists_repository import (
    WishlistsRepository
)
from src.exceptions.wishlist_exception import WishlistException

logger = logging.getLogger(__name__)


class UpdateWishlist:
    def __init__(
        self,
        wishlists_repository: WishlistsRepository,
    ):
        self.wishlists_repository = wishlists_repository

    def run(
        self,
        wishlist_id: str,
        title: str,
        description: str,
    ) -> Wishlist:
        """
        Service for update wishlist details.
        Checks required fields and if wishlist exists
        """
        logger.info(
            f'Updating wishlist <{wishlist_id}> \
            with <{title}> - <{description}>'
        )

        if not title and not description:
            logger.exception(
                f'Wishlist <{wishlist_id}> did not provide \
                title or description'
            )
            raise WishlistException(
                status_code=400,
                detail='You must provide title or description'
            )

        wishlist = self.wishlists_repository.find_by_id(wishlist_id)

        if not wishlist:
            logger.exception(
                f'Wishlist <{wishlist_id}> not found'
            )
            raise WishlistException(
                status_code=404,
                detail=f'Wishlist {wishlist_id} does not exists'
            )

        wishlist = self.wishlists_repository.update(
            wishlist_id=wishlist_id,
            title=title,
            description=description,
        )
        return wishlist
