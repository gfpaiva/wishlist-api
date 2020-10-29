from typing import List
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict

from src.infra.server import app
from src.domains.users.repository import DBUsersRepository
from src.domains.wishlists.repository import DBWishlistsRepository
from src.domains.wishlists.services.create_wishlist import CreateWishlist
from src.domains.wishlists.model.wishlist import WishlistRequestBody
from src.exceptions.wishlist_exception import WishlistException

wishlists_repository = DBWishlistsRepository()
users_repository = DBUsersRepository()
create_wishlist_service = CreateWishlist(
    wishlists_repository=wishlists_repository,
    users_repository=users_repository
)


@app.get('/wishlist')
def list_wishlists():
    wishlists = wishlists_repository.find_all()
    return [wishlist for wishlist in wishlists.dicts()]


@app.get('/wishlist/{id}')
def show_wishlist(id: str):
    wishlist = wishlists_repository.find_by_id(id)
    return model_to_dict(wishlist)


@app.get('/user/{user_id}/wishlist')
def show_user_wishlists(user_id: str):
    user = users_repository.find_by_id(user_id)

    if not user:
        raise WishlistException(
            status_code=404,
            detail=f'User {user_id} does not exists'
        )

    wishlists = wishlists_repository.find_by_user_id(user_id)
    return [wishlist for wishlist in wishlists.dicts()]


@app.post('/user/{user_id}/wishlist')
def create_wishlist(user_id: str, wishlist: WishlistRequestBody):
    new_wishlist = create_wishlist_service.run(
        user_id=user_id,
        title=wishlist.title,
        description=wishlist.description,
    )
    return model_to_dict(new_wishlist)
