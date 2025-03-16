__all__ = ("routers",)

from .auth import router as auth_router
from .message import router as message_router
from .user import router as user_router
from .updates import router as updates_router


routers = (
    auth_router, 
    message_router, 
    user_router, 
    updates_router
)
