from jinja2 import Template


class JinjaEmail:
    def __init__(self, template: Template):
        self.__template = template
        self.__data = {}
        self.__subject = None


    def render(self):
        return self.__template.render_async(**self.__data)
    
    
    @property
    def subject(self):
        return self.__subject