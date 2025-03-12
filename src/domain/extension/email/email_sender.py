from aiosmtplib import SMTP
from email.mime.text import MIMEText

from .email_message import EmailMessage
from src.infrastructure.config import env


class EmailSender:
    client = SMTP(
        hostname=env.mail.host, 
        port=env.mail.port, 
        username=env.mail.username, 
        password=env.mail.password,
        use_tls=True, 
        validate_certs=False
    )

    @staticmethod
    async def send(email: EmailMessage) -> None:
        template = await email.render()
        await __class__.__send(email.email, email.subject, template)


    @staticmethod
    async def __send(email: str, subject: str, html_template) -> None:
        msg = MIMEText(html_template, "html")
        msg["Subject"] = subject
        msg["From"] = f"{env.app.title} <{env.mail.username}>"
        msg["To"] = email

        async with EmailSender.client as c:
            await c.send_message(msg)