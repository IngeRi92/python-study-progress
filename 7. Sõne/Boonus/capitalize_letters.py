"""Capitalize letters in text."""


def capitalize_letters(text: str) -> str:
    """
    If a letter is present in given string in both lowercase and uppercase, capitalize all occurrences of the letter.

    Examples:
    capitalize_letters("") -> ""
    capitalize_letters("abbA") -> "AbbA"
    capitalize_letters("abBa") -> "aBBa"
    capitalize_letters("AbBa") -> "ABBA"
    capitalize_letters("AbbA") -> "AbbA
    capitalize_letters("abba") -> "abba"
    capitalize_letters("ABBA") -> "ABBA"

    :param text: given text
    :return: capitalized text
    """
    if not text:
        return text

    result = ""
    for char in text:
        if char.lower() in text and char.upper() in text:
            result += char.upper()
        else:
            result += char
    return result
