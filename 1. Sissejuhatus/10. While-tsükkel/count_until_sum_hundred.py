"""Count until a hundred."""


def count_until_sum_hundred(number: int) -> int:
    """
    Count the number of times a given number must be added to reach or exceed 100.

    Starting from zero, the function repeatedly adds the given number until the sum reaches at least 100 (inclusive).
    It then returns the number of iterations required.

    :param number: The integer value to be added repeatedly.
    :return: The number of iterations needed to reach or exceed 100.
    """
    current_sum = 0
    iterations = 0
    while current_sum < 100:
        current_sum += number
        iterations += 1
    return iterations


if __name__ == "__main__":
    print(count_until_sum_hundred(1))  # 100
    print(count_until_sum_hundred(49))  # 3
    print(count_until_sum_hundred(50))  # 2
