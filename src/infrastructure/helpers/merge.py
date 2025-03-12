from typing import Iterable
from fastapi import APIRouter


def merge_routers(routers: Iterable[APIRouter]) -> APIRouter: 
    merged_router = APIRouter()

    for router in routers:
        merged_router.include_router(router)

    return merged_router
