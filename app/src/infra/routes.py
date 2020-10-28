from src.infra.server import app


@app.get('/')
def root():
    return 'OK'


from src.domains.users.routes import *  # noqa # isort:skip
from src.domains.wishlists.routes import *  # noqa # isort:skip
