import debugpy
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.version import __version__

app = FastAPI(redoc_url=None, root_path="/api/v1")


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

from src.infra.routes import *  # noqa # isort:skip

debugpy.listen(('0.0.0.0', 5678))
