from uuid import uuid4


def generate_restore_token() -> str:
    return uuid4().hex