"""Password correct length."""


def is_correct_length(password: str) -> bool:
    """Check password correct length.

    Args = password(str), Password to check.
    Returns bool: True if password is correct length, False if not.
    """
    return 8 <= len(password) <= 64
