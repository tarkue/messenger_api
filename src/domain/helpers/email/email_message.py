from jinja2 import Template


class EmailMessage:
    def __init__(
        self, 
        template: Template, 
        email: str = None,
        subject: str = None
    ) -> None:
        self.__data = {}
        self.__template = template
        self.__email = email
        self.__subject = subject
        

    async def render(self):
        return await self.__template.render_async(**self.__data)
    

    @property
    def subject(self):
        return self.__subject
    

    @property
    def email(self):
        return self.__email