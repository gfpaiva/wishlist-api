from src.infra.server import app


@app.get('/')
async def root():
    return 'OK'

from src.domains.users.routes import *  # noqa # isort:skip
