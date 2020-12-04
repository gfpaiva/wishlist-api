from uuid import UUID
from dataclasses import asdict
from typing import List
from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from src.infra.server_responses import (
    not_found,
    conflict,
)

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
    wishlists_products_repository=wishlists_products_repository,
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
    wishlists_products_repository=wishlists_products_repository,
    products_repository=products_repository
)
delete_product_wishlist_service = DeleteProductWishlist(
    wishlists_repository=wishlists_repository,
    wishlists_products_repository=wishlists_products_repository,
)

wishlist_router = APIRouter()


@wishlist_router.get(
    '/wishlist/{wishlist_id}',
    response_model=WishlistProductsResponse,
    responses=not_found,
    tags=['wishlist'],
)
def show_wishlist(wishlist_id: UUID):
    """
    Show specific wishlist by given id(uuid).
    Return complete data with user and product details
    """
    wishlist = list_wishlist_service.run(wishlist_id)
    wishlist_dict = model_to_dict(wishlist)
    products_dict = [asdict(product) for product in wishlist.products]
    wishlist_dict['products'] = products_dict

    return wishlist_dict


@wishlist_router.patch(
    '/wishlist/{wishlist_id}',
    response_model=WishlistUserResponse,
    responses=not_found,
    tags=['wishlist'],
)
def update_wishlist(wishlist_id: UUID, wishlist: WishlistUpdateRequestBody):
    """
    Update specific wishlist by given id(uuid).
    Can update one or both fields title/description
    """
    updated_wishlist = update_wishlist_service.run(
        wishlist_id=wishlist_id,
        title=wishlist.title,
        description=wishlist.description,
    )
    return model_to_dict(updated_wishlist)


@wishlist_router.delete(
    '/wishlist/{wishlist_id}',
    status_code=204,
    responses=not_found,
    tags=['wishlist'],
)
def delete_wishlist(wishlist_id: UUID):
    """
    Delete specific wishlist by given id(uuid).
    """
    delete_wishlist_service.run(wishlist_id)
    return


@wishlist_router.post(
    '/wishlist/{wishlist_id}/product/{product_id}',
    response_model=WishlistProductsResponse,
    responses={**not_found, **conflict},
    tags=['wishlist'],
)
def insert_product_wishlist(wishlist_id: UUID, product_id: str):
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
    products_dict = [asdict(product) for product in wishlist.products]
    wishlist_dict['products'] = products_dict

    return wishlist_dict


@wishlist_router.delete(
    '/wishlist/{wishlist_id}/product/{product_id}',
    status_code=204,
    responses=not_found,
    tags=['wishlist'],
)
def delete_product_wishlist(wishlist_id: UUID, product_id: str):
    """
    Remove product from specific wishlist by given product_id(uuid)
    and wishlist_id(uuid).
    """
    delete_product_wishlist_service.run(
        wishlist_id=wishlist_id,
        product_id=product_id,
    )
    return


@wishlist_router.get(
    '/user/{user_id}/wishlist',
    response_model=List[WishlistResponse],
    responses=not_found,
    tags=['user', 'wishlist'],
)
def show_user_wishlists(user_id: UUID):
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


@wishlist_router.post(
    '/user/{user_id}/wishlist',
    response_model=WishlistUserResponse,
    responses=not_found,
    tags=['user', 'wishlist'],
)
def create_wishlist(user_id: UUID, wishlist: WishlistRequestBody):
    """
    Create a new wishlist for specific user
    """
    new_wishlist = create_wishlist_service.run(
        user_id=user_id,
        title=wishlist.title,
        description=wishlist.description,
    )
    return model_to_dict(new_wishlist)
