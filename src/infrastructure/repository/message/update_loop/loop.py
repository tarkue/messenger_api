from uuid import UUID
from typing import Dict, AsyncGenerator, AsyncIterator
from asyncio import sleep

from .session import SessionsManager
from src.infrastructure.database.models.message import Message



class UpdateLoop:
    def __init__(self):
        self.__subscribers: Dict[UUID, SessionsManager] = {}


    async def emit(self, user_id: UUID, message: Message):
        if user_id in self.__subscribers:
            await self.__subscribers[user_id].put(message)

    
    def subscribe(self, user_id: UUID) -> UUID:
        session_id = self.__create_if_not_exists(user_id)
        return session_id
    

    def unsubscribe(self, user_id: UUID, session_id: UUID):
        self.__subscribers[user_id].remove(session_id)
    

    def loop(self, user_id: UUID, session_id: UUID) -> AsyncIterator[Message]:
        return self.__loop(user_id, session_id)

    async def __loop(
        self, 
        user_id: UUID, 
        session_id: UUID
    ) -> AsyncGenerator[None, Message]:
        session = self.__subscribers[user_id][session_id]
        while True:
            if session.empty():
                await sleep(1)
            else:
                message = await session.get()
                yield message

    
    def __create_if_not_exists(self, user_id: UUID) -> UUID:
        if user_id not in self.__subscribers:
            self.__subscribers[user_id] = SessionsManager()

        session_id = self.__subscribers[user_id].create_session()
        return session_id