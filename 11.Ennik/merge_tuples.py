"""Merge tuples."""


def merge_tuples(a: tuple, b: tuple) -> tuple:
    """
    Merge two tuples by adding b elements after a elements.

    merge_tuples((1, 2), (3, 4)) => (1, 2, 3, 4)
    merge_tuples((1, ), (3, )) => (1, 3)
    merge_tuples((1, 2, 3), (1, 2)) => (1, 2, 3, 1, 2)
    """
    return a + b


if __name__ == "__main__":
    print(merge_tuples((1, 2), (3, 4)))  # => (1, 2, 3, 4)
    print(merge_tuples((1,), (3,)))  # => (1, 3)
    print(merge_tuples((1, 2, 3), (1, 2)))  # => (1, 2, 3, 1, 2)
