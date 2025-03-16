from typing_extensions import Annotated
from fastapi import Depends

from .get import get_current_user
from .websocket import get_user_from_websocket
from src.infrastructure.database import User


CurrentUser = Annotated[User, Depends(get_current_user)]
CurrentUserFromWebsocket = Annotated[User, Depends(get_user_from_websocket)]