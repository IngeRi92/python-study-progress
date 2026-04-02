"""Slice of string."""


def slice_of_string(string: str, first_index: int, second_index: int) -> str:
    """Return the substring between indexes (both inclusive)."""
    return string[first_index : second_index + 1]
