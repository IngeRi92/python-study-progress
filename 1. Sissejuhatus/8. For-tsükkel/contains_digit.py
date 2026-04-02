"""Contains digit."""


def contains_digit(some_string: str) -> bool:
    """
    Check if a given string contains at least one digit.

    :parm some_string: given string
    :return: Return True if the input string contains a digit, False otherwise.
    """
    for char in some_string:
        if char.isdigit():
            return True
    return False
