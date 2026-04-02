"""Capitalize first letter of a string."""


def capitalize_first_letter(string_with_low: str) -> str:
    """Return the same string with the first letter capitalized."""
    return string_with_low[0].upper() + string_with_low[1:]
