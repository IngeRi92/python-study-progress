"""Create tuple from two numbers."""


def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    """
    Create a tuple.

    If the values of a and b are the same, then return a tuple with one element.
    If the values are different, return a tuple of a and b (in that order).

    create_tuple_from_two_numbers(1, 2) => (1, 2)
    create_tuple_from_two_numbers(1, 1) => (1,)
    """
    if a == b:
        return (a,)
    return (a, b)


if __name__ == "__main__":
    print(create_tuple_from_two_numbers(1, 2))  # => (1, 2)
    print(create_tuple_from_two_numbers(1, 1))  # => (1, )
