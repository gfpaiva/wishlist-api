from fastapi import HTTPException


class CredentialsException(HTTPException):
    pass
