"""Is letter in a word."""


def is_letter_in_word(letter: str, word: str) -> bool:
    """
    If the word contains the letter return True, else return False.

    is_letter_in_word("a", "car") => True
    is_letter_in_word("b", "car") => False

    :param letter: given letter.
    :param word: given word.
    :return: True or False depending on whether the letter is in the word.
    """
    if letter in word:
        return True
    else:
        return False
