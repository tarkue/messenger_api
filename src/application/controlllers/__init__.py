__all__ = ("routers",)

from .auth import router as auth_router
from .chat import router as chat_router
from .user import router as user_router


routers = (auth_router, chat_router, user_router)
