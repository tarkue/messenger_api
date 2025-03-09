__all__ = ("find_by_credentials", "exists", "create")

from typing import Dict, Literal
from bcrypt import checkpw
from uuid import UUID

from src.infrastructure.errors.auth import UserNotFoundError
from src.infrastructure.database import User


async def find_by_credentials(
    credentials: Dict[Literal['username', 'password'], str]
) -> UUID:
    if not await exists(credentials["username"]):
        raise UserNotFoundError()
    
    check_pw = lambda password: checkpw(
        credentials["password"].encode(), 
        password.encode()
    )
    user = User.check_password(credentials, check_pw)

    if not user:
        raise UserNotFoundError()
    
    return user.id


async def exists(username: str) -> bool:
    return await User.exists(username)


async def create(
    credentials: Dict[Literal['name', 'username', 'password'], str]
) -> None:
    await User.create(**credentials)
