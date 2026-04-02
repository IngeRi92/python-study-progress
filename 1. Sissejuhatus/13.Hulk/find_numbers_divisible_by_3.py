"""Find numbers divisible by 3."""


def find_numbers_divisible_by_3(numbers: list) -> set:
    """
    Return a set of numbers from the input list which are divisible by 3.

    Numbers are between 0 and 1000 (inclusive).

    Hint: this function can be done without a loop.
    As we know the limit of numbers, we can create
    a set of all the numbers in the range which are
    divisible by 3.
    Hint: use range().

    find_numbers_divisible_by_3([1, 2, 3]) => {3}
    find_numbers_divisible_by_3([3, 2, 3, 12]) => {3, 12}
    """
    divisible_by_3 = set(range(0, 1001, 3))
    return set(numbers) & divisible_by_3


if __name__ == '__main__':
    # run this file to test the function
    print(find_numbers_divisible_by_3([1, 2, 3]))  # {3}
    print(find_numbers_divisible_by_3([3, 2, 3, 12, 36]))  # {3, 12, 36}
