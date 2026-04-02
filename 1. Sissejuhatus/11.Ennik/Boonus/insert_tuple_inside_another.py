"""Insert tuple inside another."""


def insert_tuple_inside_another(
    outer_tuple: tuple, position: int, inner_tuple: tuple
) -> tuple:
    """
    Insert inner_tuple inside outer_tuple at the given position.

    All the elements at the position and after the position are shifted to the right
    so that the whole inner_tuple fits at the position.

    The position is non-negative and its max value is the length of outer_tuple.
    If the position is the length of outer_tuple, the inner_tuple will be
    appended to the end of the outer_tuple.

    insert_tuple_inside_another((1, 2), 0, (3, 4)) => (3, 4, 1, 2)
    insert_tuple_inside_another((1, 2), 1, (3, 4)) => (1, 3, 4, 2)
    insert_tuple_inside_another((1, 2), 2, (3, 4)) => (1, 2, 3, 4)
    insert_tuple_inside_another((1, 2, 3), 1, (1, )) => (1, 1, 2, 3)
    """
    return outer_tuple[:position] + inner_tuple + outer_tuple[position:]


if __name__ == "main":
    print(insert_tuple_inside_another((1, 2), 0, (3, 4)))  # => (3, 4, 1, 2)
    print(insert_tuple_inside_another((1, 2), 1, (3, 4)))  # => (1, 3, 4, 2)
    print(insert_tuple_inside_another((1, 2), 2, (3, 4)))  # => (1, 2, 3, 4)
    print(insert_tuple_inside_another((1, 2, 3), 1, (1,)))  # => (1, 1, 2, 3)
