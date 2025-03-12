from fastapi.exceptions import HTTPException
from fastapi import status


class UserAlreadyExistsError(HTTPException):
   def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"User already exists."
        )
