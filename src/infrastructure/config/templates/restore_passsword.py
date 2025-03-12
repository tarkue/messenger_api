from jinja2 import Template


RESTORE_PASSWORD_TEMPLATE = Template(
    "./html/restore_password.html", 
    enable_async=True
)
