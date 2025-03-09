from .jinja_email import JinjaEmail


class EmailSender:
    @staticmethod
    async def send(email: JinjaEmail): ...