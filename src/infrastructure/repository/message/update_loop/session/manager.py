from uuid import UUID
from typing import List

from .session import UpdateSession
from src.infrastructure.database.models.message import Message


class SessionsManager:
    def __init__(self):
        self.__sessions: List[UpdateSession] = []


    async def put(self, message: Message):
        for session in self.__sessions:
            await session.put(message)


    def create_session(self) -> UUID:
        session = UpdateSession()
        self.__sessions.append(session)
        return session.id


    def remove(self, session_id: UUID):
        session = self[session_id]
        self.__sessions.remove(session)


    def __getitem__(self, session_id: UUID) -> UpdateSession:
        filtered = filter(lambda x: x.id == session_id, self.__sessions)
        return next(filtered)
    