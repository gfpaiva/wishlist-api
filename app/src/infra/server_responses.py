from pydantic import (
    BaseModel,
    EmailStr,
    UUID4,
)


class Conflict(BaseModel):
    detail: str


class NotFound(BaseModel):
    detail: str


class Unauthorized(BaseModel):
    detail: str


conflict = {409: {"model": Conflict}}
not_found = {404: {"model": NotFound}}
unauthorized = {401: {"model": Unauthorized}}
