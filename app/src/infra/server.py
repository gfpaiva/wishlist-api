import debugpy
from fastapi import (
    FastAPI,
    Depends,
)

from fastapi.openapi.utils import get_openapi

from src.domains.auth.repository import JWTRepository
from src.infra.routes import root_router
from src.domains.auth.routes import auth_router
from src.domains.users.routes import user_router
from src.domains.wishlists.routes import wishlist_router

from src.version import __version__

token_repository = JWTRepository()

app = FastAPI(redoc_url=None, root_path="/api/v1")
app.include_router(root_router)
app.include_router(auth_router)
app.include_router(
    user_router,
    dependencies=[Depends(token_repository.decode)],
)
app.include_router(
    wishlist_router,
    dependencies=[Depends(token_repository.decode)],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Wishlist API",
        version=__version__,
        description="This is the docs from wishlist api",
        routes=app.routes,
        servers=[
            {
                "url": "/api/v1"
            }
        ]
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

debugpy.listen(('0.0.0.0', 5678))
