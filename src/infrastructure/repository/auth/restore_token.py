__all__ = ("exists", "remember")

from typing import Dict, Literal


async def remember(
    credentials: Dict[Literal['username']], 
    restore_key: str
) -> None: ...


async def exists(restore_key: str) -> bool: ...