from typing import List
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
from src.domains.wishlists.services.update_wishlist import UpdateWishlist
from src.domains.wishlists.services.insert_product_wishlist import (
    InsertProductWishlist
)
from src.domains.wishlists.services.delete_wishlist import DeleteWishlist
from src.domains.wishlists.services.delete_product_wishlist import (
    DeleteProductWishlist
)

from src.domains.wishlists.model.wishlist import (
    WishlistRequestBody,
    WishlistUpdateRequestBody,
    WishlistResponse,
    WishlistUserResponse,
    WishlistProductsResponse,
)
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
update_wishlist_service = UpdateWishlist(
    wishlists_repository=wishlists_repository,
)
delete_wishlist_service = DeleteWishlist(
    wishlists_repository=wishlists_repository,
)
insert_product_wishlist_service = InsertProductWishlist(
    wishlists_repository=wishlists_repository,
    wishlists_produts_repository=wishlists_products_repository,
    products_repository=products_repository
)
delete_product_wishlist_service = DeleteProductWishlist(
    wishlists_repository=wishlists_repository,
    wishlists_products_repository=wishlists_products_repository,
)


@app.get(
    '/wishlist/{id}',
    response_model=WishlistProductsResponse,
)
def show_wishlist(id: str):
    """
    Show specific wishlist by given id(uuid).
    Return complete data with user and product details
    """
    wishlist = list_wishlist_service.run(id)
    wishlist_dict = model_to_dict(wishlist)
    wishlist_dict['products'] = wishlist.products

    return wishlist_dict


@app.patch(
    '/wishlist/{id}',
    response_model=WishlistUserResponse,
)
def update_wishlist(id: str, wishlist: WishlistUpdateRequestBody):
    """
    Update specific wishlist by given id(uuid).
    Can update one or both fields title/description
    """
    updated_wishlist = update_wishlist_service.run(
        id=id,
        title=wishlist.title,
        description=wishlist.description,
    )
    return model_to_dict(updated_wishlist)


@app.delete(
    '/wishlist/{id}',
    status_code=204,
)
def delete_wishlist(id: str):
    """
    Delete specific wishlist by given id(uuid).
    """
    delete_wishlist_service.run(id)
    return


@app.post(
    '/wishlist/{wishlist_id}/product/{product_id}',
    response_model=WishlistProductsResponse,
)
def insert_product_wishlist(wishlist_id: str, product_id: str):
    """
    Add one product into a specific wishlist by given product_id(uuid)
    and wishlist_id(uuid).
    A product can be added just once on each list
    """
    wishlist = insert_product_wishlist_service.run(
        wishlist_id=wishlist_id,
        product_id=product_id,
    )
    wishlist_dict = model_to_dict(wishlist)
    wishlist_dict['products'] = wishlist.products

    return wishlist_dict


@app.delete(
    '/wishlist/{wishlist_id}/product/{product_id}',
    status_code=204,
)
def delete_product_wishlist(wishlist_id: str, product_id: str):
    """
    Remove product from specific wishlist by given product_id(uuid)
    and wishlist_id(uuid).
    """
    delete_product_wishlist_service.run(
        wishlist_id=wishlist_id,
        product_id=product_id,
    )
    return


@app.get(
    '/user/{user_id}/wishlist',
    response_model=List[WishlistResponse],
)
def show_user_wishlists(user_id: str):
    """
    List all wishlists from specific user by given user_id(uuid).
    """
    user = users_repository.find_by_id(user_id)

    if not user:
        raise WishlistException(
            status_code=404,
            detail=f'User {user_id} does not exists'
        )

    wishlists = wishlists_repository.find_by_user_id(user_id)
    return [wishlist for wishlist in wishlists.dicts()]


@app.post(
    '/user/{user_id}/wishlist',
    response_model=WishlistUserResponse,
)
def create_wishlist(user_id: str, wishlist: WishlistRequestBody):
    """
    Create a new wishlist for specific user
    """
    new_wishlist = create_wishlist_service.run(
        user_id=user_id,
        title=wishlist.title,
        description=wishlist.description,
    )
    return model_to_dict(new_wishlist)
