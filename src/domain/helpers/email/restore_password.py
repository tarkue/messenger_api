from .email_message import EmailMessage
from jinja2 import Template

restore_password_email_template = Template("restore_password.html", enable_async=True)

class RestorePasswordEmail(EmailMessage):
    def __init__(self, email: str, restore_token: str) -> None:
        super().__init__(
            template=restore_password_email_template,
            email=email,
            subject="Restore password"
        )
        self.__data["restore_token"] = restore_token

    @property
    def restore_token(self):
        return self.__restore_token