class UserNotFoundError(Exception):
    def __init__(self):
        super().__init__("User not found.")