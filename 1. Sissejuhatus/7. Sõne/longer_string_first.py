"""Longer string first."""


def longer_string_first(first_string: str, second_string: str) -> str:
    """Return longer string in front and the shorter string after that."""
    if len(first_string) >= len(second_string):
        return first_string + second_string
    else:
        return second_string + first_string
