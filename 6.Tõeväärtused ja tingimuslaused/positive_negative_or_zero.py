"""Positive, negative or zero."""


def positive_negative_or_zero(num_a: int) -> str:
    """
    Return "positive", "negative", or "zero" depending on the given integer.

    positive_negative_or_zero(12) => "positive"
    positive_negative_or_zero(-12) => "negative"
    positive_negative_or_zero(0) => "zero"

    :param num_a: given integer
    :return: "positive", "negative", or "zero" depending on the given integer.
    """
    if num_a > 0:
        return "positive"
    elif num_a < 0:
        return "negative"
    else:
        return "zero"
