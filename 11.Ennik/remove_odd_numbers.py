"""Remove odd numbers."""


def remove_odd_numbers(numbers: tuple) -> tuple:
    """
    Return a tuple where all the odd numbers are removed from the tuple received as input.

    The order of the elements should remain the same.

    remove_odd_numbers((1, 2, 3)) => (2, )
    remove_odd_numbers((1, 5, 3)) => ()
    remove_odd_numbers((2, 4, 6)) => (2, 4, 6)
    """
    new_tuple = ()
    for number in numbers:
        if number % 2 == 0:
            new_tuple += (number,)
    return new_tuple


if __name__ == "__main__":
    print(remove_odd_numbers((1, 2, 3)))  # => (2, )
    print(remove_odd_numbers((1, 5, 3)))  # => ()
    print(remove_odd_numbers((2, 4, 6)))  # => (2, 4, 6)
