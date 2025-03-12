from fastapi.exceptions import HTTPException
from fastapi import status


class IncorrectCredentialsError(HTTPException):
   def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect username or password.", 
            headers={"WWW-Authenticate": "Bearer"}
        )
