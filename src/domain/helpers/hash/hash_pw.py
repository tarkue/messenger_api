from bcrypt import gensalt, hashpw


def hash_password(password: str) -> str:
    salt = gensalt()
    return hashpw(password.encode(), salt).decode()

