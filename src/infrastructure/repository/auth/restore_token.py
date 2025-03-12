__all__ = ("exists", "remember", "forget")

from src.infrastructure.redis import RestorePassword


async def remember(username: str, token: str) -> None:
    rp = RestorePassword(
        username=username,
        token=token
    )
    rp.save()


async def forget(token: str) -> None:
    RestorePassword.delete(token)


async def exists(token: str) -> bool:
    query = RestorePassword.find(
        RestorePassword.token == token
    )
    return query.count() > 0


async def get(token: str) -> RestorePassword:
    return RestorePassword.get(token)
