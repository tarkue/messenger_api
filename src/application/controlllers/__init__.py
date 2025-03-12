__all__ = ("routers",)

from .auth import router as auth_router
from .message import router as message_router
from .user import router as user_router


routers = (auth_router, message_router, user_router)
