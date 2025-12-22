"""Generate string with random length."""

import random


def generate_string_with_random_length(threshold: float) -> str:
    """
    Generate a string of "-" symbols until random numbers is below threshold.

    Use random.random() to generate a random float.
    If the random number is below threshold, add "-" to the result.
    If the random number is greater or equal to the threshold, stop the loop.

    generate_string_with_random_length(0.9) => "-----" (result can vary greatly)
    generate_string_with_random_length(0.5) => "-" (usually contains 0-1 hyphens)

    :param threshold: the threshold under which number generation halts
    :return: A string of "-" continuously repeated until the threshold is hit.
    """
    result = ""
    while random.random() < threshold:
        result += "-"
    return result
