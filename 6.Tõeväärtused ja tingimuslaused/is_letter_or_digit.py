"""Is letter or digit."""


def is_letter_or_digit(symbol: str) -> str:
    """
    Return "letter" if given symbol is a letter, "digit" if given symbol is a digit, and "other" if it's neither.

    is_letter_or_digit("a") => "letter"
    is_letter_or_digit("1") => "digit"
    is_letter_or_digit("?") => "other"

    :param symbol: symbol
    :return: Either "letter", "digit", or "other".
    """
    if symbol.isalpha():
        return "letter"
    elif symbol.isdigit():
        return "digit"
    else:
        return "other"
