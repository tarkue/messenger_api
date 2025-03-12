from fastapi import APIRouter
from uuid import UUID4

from src.domain.dto import message as DTO

from aiogram import Bot

router = APIRouter(
    prefix="/message",
    tags=["message"],
)


@router.get("/")
async def get_all_chats(
    limit: int = 10,
    offset: int = 0,
    search: str = "",
): ...


@router.get("/{chat_id}")
async def get_messages_in_chat(chat_id: UUID4): ...


@router.post("/")
def create_message(dto: DTO.CreateMessageDTO): ...