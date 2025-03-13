from pydantic import BaseModel


class ChatOut(BaseModel):
    id: str
    name: str
    last_message: str
    new_messages: int