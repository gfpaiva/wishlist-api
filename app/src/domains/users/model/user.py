from peewee import (
    Model,
    CharField,
    UUIDField,
)
from pydantic import BaseModel

from src.infra.db import db


class User(Model):
    id = UUIDField()
    name = CharField()
    email = CharField()

    class Meta:
        table_name = 'users'
        database = db


class UserRequestBody(BaseModel):
    name: str
    email: str
