__all__ = ("find_by_credentials", "exists", "create")

from bcrypt import checkpw

from src.infrastructure.errors.auth import IncorrectCredentialsError
from src.infrastructure.database import User


async def find_by_credentials(credentials: User) -> User:
    password_checker = lambda password: checkpw(
        credentials.password.encode(), 
        password.encode()
    )
    user = await User.first(username=credentials.username)

    if not user.check_password(password_checker):
        raise IncorrectCredentialsError()
    
    return user


async def exists(username: str) -> bool:
    return await User.exists(username)


async def create(credentials: User) -> User:
    return await User.create(**credentials.model_dump())


