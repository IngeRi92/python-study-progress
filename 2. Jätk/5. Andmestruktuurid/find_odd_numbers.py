"""Find odd numbers."""


def find_odd_numbers(set_a: set, set_b: set) -> set:
    """
    Given two set, return a set containing the odd numbers that are in set_a or in st_b, but not in both.

    find_odd_numbers({1, 2, 3}, {3, 4, 5}) -> {1, 5}
    """
    result = set()
    for num in set_a:
        if num % 2 == 1 and num not in set_b:
            result.add(num)
    for num in set_b:
        if num % 2 == 1 and num not in set_a:
            result.add(num)
    return result
