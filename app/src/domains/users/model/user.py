from typing import Optional
from peewee import (
    Model,
    CharField,
)
from pydantic import (
    BaseModel,
    EmailStr,
    UUID4,
)

from src.infra.db import db


class User(Model):
    """
    Model for user in database. With fields id, name and email
    """
    id = CharField(primary_key=True, null=False)
    name = CharField(null=False)
    email = CharField(null=False, unique=True)

    class Meta:
        table_name = 'users'
        database = db


class UserRequestBody(BaseModel):
    """
    Schema for http post request json body
    """
    name: str
    email: EmailStr


class UserUpdateRequestBody(BaseModel):
    """
    Schema for http patch request json body
    """
    name: Optional[str]
    email: Optional[EmailStr]


class UserResponse(BaseModel):
    """
    Schema for single user http response
    """
    id: UUID4
    name: str
    email: EmailStr
