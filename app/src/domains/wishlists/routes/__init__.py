from typing import List
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict

from src.infra.server import app
from src.domains.wishlists.repository import DBWishlistsRepository
from src.domains.wishlists.model.wishlist import WishlistRequestBody

wishlists_repository = DBWishlistsRepository()


@app.get('/wishlist')
def list_wishlists():
    wishlists = wishlists_repository.find_all()
    return [wishlist for wishlist in wishlists.dicts()]


@app.post('/user/{user_id}/wishlist')
def create_wishlist(user_id: str, wishlist: WishlistRequestBody):
    new_wishlist = wishlists_repository.create(
        user_id=user_id,
        title=wishlist.title,
        description=wishlist.description
    )
    return model_to_dict(new_wishlist)
