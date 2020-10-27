from typing import Optional
from peewee import (
    Model,
    CharField,
)
from pydantic import BaseModel

from src.infra.db import db


class User(Model):
    id = CharField()
    name = CharField()
    email = CharField()

    class Meta:
        table_name = 'users'
        database = db


class UserRequestBody(BaseModel):
    name: str
    email: str


class UserUpdateRequestBody(BaseModel):
    name: Optional[str]
    email: Optional[str]


class UserResponseBody(BaseModel):
    id: str
    name: str
    email: str
