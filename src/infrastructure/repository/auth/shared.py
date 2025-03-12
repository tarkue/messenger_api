from .restore_token import forget, get
from src.infrastructure.database import User


async def update_password_by_restore_token(
    token: str,
    password: str
): 
    rp = await get(token)
    await User.update(rp.username, {
        "password": password
    })
    await forget(token)
