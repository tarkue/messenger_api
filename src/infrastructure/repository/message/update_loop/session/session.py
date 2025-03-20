from asyncio import Queue
from uuid import UUID, uuid4

from src.infrastructure.database.models.message import Message


class UpdateSession: 
    def __init__(self):
        self.id: UUID = uuid4()
        self.queue: Queue = Queue()


    def __eq__(self, value):
        if isinstance(value, UUID):
            return self.user_id == value
        return self.id == self.id
    

    async def put(self, message: Message):
        await self.queue.put(message)


    def empty(self):
        return self.queue.empty()


    async def get(self):
        return await self.queue.get()
    