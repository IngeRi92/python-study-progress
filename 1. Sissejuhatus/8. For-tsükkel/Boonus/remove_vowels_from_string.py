"""Remove vowels from a string."""


def remove_vowels_from_string(original_string: str) -> str:
    """
    Return the given string without vowels.

    print(remove_vowels_from_string("tere-tere")) => tr-tr
    print(remove_vowels_from_string("hklmn")) => hklmn
    print(remove_vowels_from_string("aauuiii")) => ""

    :param original_string: the original string
    :return: The processed string without vowels.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in original_string:
        if char not in vowels:
            result += char
    return result
