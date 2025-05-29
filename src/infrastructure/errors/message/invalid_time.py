from fastapi import status
from fastapi.exceptions import HTTPException


class InvalidTimeError(HTTPException):
   def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"createdAt is not valid."
        )
