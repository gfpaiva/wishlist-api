from peewee import (
    Model,
    CharField,
)

from src.infra.db import db


class Auth(Model):
    """
    Model for user/app authentication in database. With fields id, username
    and password
    """
    id = CharField(primary_key=True, null=False)
    username = CharField(null=False, unique=True)
    password = CharField(null=False)

    class Meta:
        table_name = 'auths'
        database = db
