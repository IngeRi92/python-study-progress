"""Calculate sum and difference."""


def calculate_sum_and_difference(a: int, b: int) -> tuple:
    """
    Return two values as a tuple: the sum of a and b and the difference of a and b.

    calculate_sum_and_difference(1, 2) => (3, -1)
    calculate_sum_and_difference(1, 1) => (2, 0)
    calculate_sum_and_difference(5, 1) => (6, 4)
    """
    return a + b, a - b


if __name__ == "__main__":
    print(calculate_sum_and_difference(1, 2))  # => (3, -1)
    print(calculate_sum_and_difference(0, 0))  # => (0, 0)
    print(calculate_sum_and_difference(6, 2))  # => (8, 4)
    print(calculate_sum_and_difference(0, 9))  # => (9, -9)
