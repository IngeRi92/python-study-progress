"""Add or subtract."""


def add_or_subtract(numbers):
    """
    Add or subtract.

    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    total = 0
    add = True
    for number in numbers:
        if number == 0:
            add = not add
        elif add:
            total += number
        else:
            total -= number
    return total
