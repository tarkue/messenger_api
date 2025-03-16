from uuid import UUID
from typing import Dict, AsyncGenerator, AsyncIterator
from asyncio import sleep, Queue

from src.infrastructure.database.models.message import Message


class UpdateLoop:
    def __init__(self):
        self.__subscribers: Dict[UUID, Queue] = {}


    async def emit(self, user_id: UUID, message: Message):
        self.__create_queue_if_not_exists(user_id)
        await self.__subscribers[id].put(message)


    async def subscribe(self, user_id: UUID) -> AsyncIterator[Message]:
        self.__create_queue_if_not_exists(user_id)
        loop = await self.__loop(user_id)
        return iter(loop)
    

    async def unsubscribe(self, user_id: UUID):
        del self.__subscribers[user_id]
    

    async def __loop(self, user_id: UUID) -> AsyncGenerator[None, Message]:
        while True:
            if self.__subscribers[user_id].empty():
                await sleep(1)
            else:
                message = await self.__subscribers[user_id].get()
                yield message

    
    def __create_queue_if_not_exists(self, user_id: UUID):
        if user_id not in self.__subscribers:
            self.__subscribers[user_id] = Queue()
