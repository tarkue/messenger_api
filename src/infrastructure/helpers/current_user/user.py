from typing_extensions import Annotated
from fastapi import Depends

from .get import get_current_user
from src.infrastructure.database import User


CurrentUser = Annotated[User, Depends(get_current_user)]
