from pydantic import BaseModel


class Token(BaseModel):
    """
    Schema for single token response
    """
    access_token: str
    token_type: str
