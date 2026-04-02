"""Add one to numbers in the set."""


def add_one_to_numbers_in_set(set_a: set) -> set:
    """
    Take a set of integers and increment each integer by one, return new set.

    add_one_to_numbers_in_set({1, 2, 3}) => {2, 3, 4}
    add_one_to_numbers_in_set({-10, 0, 10}) => {-9, 1, 11}

    :param set_a: given set
    :return: new set where all elements have been incremented by one.
    """
    return {x + 1 for x in set_a}


if __name__ == '__main__':
    # run this file to test the function
    print(add_one_to_numbers_in_set({1, 2, 3}))  # => {2, 3, 4}
    print(add_one_to_numbers_in_set({-10, 0, 10}))  # => {-9, 1, 11}
