from typing import List
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict

from src.infra.server import app

from src.domains.users.repository import DBUsersRepository
from src.domains.wishlists.repository import (
    DBWishlistsRepository,
    DBWishlistsProductsRepository,
)
from src.domains.products.repository import APIProductsRepository

from src.domains.wishlists.services.create_wishlist import CreateWishlist
from src.domains.wishlists.services.list_wishlist import ListWishlist
from src.domains.wishlists.services.insert_product_wishlist import InsertProductWishlist

from src.domains.wishlists.model.wishlist import WishlistRequestBody
from src.exceptions.wishlist_exception import WishlistException

wishlists_repository = DBWishlistsRepository()
wishlists_products_repository = DBWishlistsProductsRepository()
users_repository = DBUsersRepository()
products_repository = APIProductsRepository()

create_wishlist_service = CreateWishlist(
    wishlists_repository=wishlists_repository,
    users_repository=users_repository
)
list_wishlist_service = ListWishlist(
    wishlists_repository=wishlists_repository,
    wishlists_produts_repository=wishlists_products_repository,
    products_repository=products_repository
)
insert_product_wishlist_service = InsertProductWishlist(
    wishlists_repository=wishlists_repository,
    wishlists_produts_repository=wishlists_products_repository,
    products_repository=products_repository
)


@app.get('/wishlist/{id}')
def show_wishlist(id: str):
    wishlist = list_wishlist_service.run(id)
    wishlist_dict = model_to_dict(wishlist)
    wishlist_dict['products'] = wishlist.products

    return wishlist_dict


@app.post('/wishlist/{wishlist_id}/product/{product_id}')
def insert_product_wishlist(wishlist_id: str, product_id: str):
    wishlist = insert_product_wishlist_service.run(
        wishlist_id=wishlist_id,
        product_id=product_id,
    )
    wishlist_dict = model_to_dict(wishlist)
    wishlist_dict['products'] = wishlist.products

    return wishlist_dict


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
