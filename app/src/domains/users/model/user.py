from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class User:
    id: str
    name: str
    email: str


class UserRequestBody(BaseModel):
    name: str
    email: str
