"""Min and max."""


def tuple_min_and_max(tuple1: tuple, tuple2: tuple) -> int:
    """
    Return the sum of the smallest and largest elements from both tuples.

    Given two tuples containing integers.
    If both tuples are empty, it returns 0.

    Args:
    tuple1 (tuple): A tuple of integers.
    tuple2 (tuple): A tuple of integers.

    Returns:
    int: The sum of the smallest and largest elements from both tuples.
    Returns 0 if both tuples are empty.
    """
    if not tuple1 and not tuple2:
        return 0
    combined = tuple1 + tuple2
    return min(combined) + max(combined)


if __name__ == "__main__":
    print(tuple_min_and_max((), ()))  # => 0
    print(tuple_min_and_max((1, 2), (3, 4)))  # => 5
