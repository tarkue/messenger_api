from .email_message import EmailMessage
from src.infrastructure.config import templates as html


class RestorePasswordEmail(EmailMessage):
    def __init__(self, email: str, restore_token: str) -> None:
        super().__init__(
            template=html.RESTORE_PASSWORD_TEMPLATE,
            email=email,
            subject="Restore password"
        )
        self.__data["restore_token"] = restore_token
