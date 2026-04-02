"""Are strings the same length."""


def are_strings_same_length(str_a: str, str_b: str) -> bool:
    """
    Return True if the two given strings are of equal length, else return False.

    are_strings_same_length("aa", "bb") => True
    are_strings_same_length("a", "bbb") => False

    :param str_b: first string
    :param str_a: second string
    :return: True or False depending on whether the two given strings are of equal length.
    """
    if len(str_a) == len(str_b):
        return True
    else:
        return False
