"""Capitalize and replace letters in string."""


def modify_string(phrase: str) -> str:
    """
    Return a modified version of the string with certain letters capitalized and replaced.

    First letter of the string must be capitalized.
    All occurrences of the letters: a,e,i,o,u must be capitalized.
    """
    if len(phrase) == 0:
        return phrase
    phrase = phrase[0].upper() + phrase[1:]
    for letter in "aeiou":
        phrase = phrase.replace(letter, letter.upper())
    return phrase
