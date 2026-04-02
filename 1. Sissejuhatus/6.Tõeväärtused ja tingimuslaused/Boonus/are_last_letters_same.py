"""Are last letters the same."""


def are_last_letters_same(str_a: str, str_b: str) -> bool:
    """
    Given two strings, return True if last symbols are the same and False if not.

    are_last_letters_same("car", "house") => False
    are_last_letters_same("bird", "card") => True

    :param str_a: first string.
    :param str_b: second string.
    :return: True if the last characters are equal, False otherwise.
    """
    if str_a[-1] == str_b[-1]:
        return True
    else:
        return False
