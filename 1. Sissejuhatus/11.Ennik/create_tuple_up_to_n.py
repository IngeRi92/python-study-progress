"""Create tuple up to n."""


def create_tuple_up_to_n(n: int) -> tuple:
    """
    Create a tuple with numbers from 0 up to n (inclusive).

    If n < 0, return an empty tuple.

    create_tuple_up_to_n(2) => (0, 1, 2)
    create_tuple_up_to_n(0) => (0, )
    create_tuple_up_to_n(-10) => ()
    """
    if n < 0:
        return ()
    return tuple(range(n + 1))


if __name__ == '__main__':
    print(create_tuple_up_to_n(2))  # => (0, 1, 2)
    print(create_tuple_up_to_n(0))  # => (0, )
    print(create_tuple_up_to_n(-10))  # => ()
    print(create_tuple_up_to_n(5))  # => (0, 1, 2, 3, 4, 5)
