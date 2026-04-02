"""Set basic."""


def create_set_from_numbers(a: int, b: int, c: int) -> set:
    """
    Create set from three integers.

    create_set_from_numbers(1, 2, 3) => {1, 2, 3}
    create_set_from_numbers(1, 2, 1) => {1, 2}
    create_set_from_numbers(1, 1, 1) => {1}
    """
    return {a, b, c}


def convert_list_to_set(list_a: list) -> set:
    """
    Take a list, convert it to a set and return it.

    convert_list_to_set([1, 2, 3, 1]) => {1, 2, 3}
    convert_list_to_set([1, 2, 3, 4]) => {1, 2, 3, 4}

    :param list_a: given list
    :return: set made from given list.
    """
    return set(list_a)


def count_unique_elements(input_list: list) -> int:
    """
    Count unique elements in the list.

    Hint: set only has unique elements.

    Hint: no loop required

    count_unique_elements([1, 2, 3]) => 3
    count_unique_elements([1, 1, 1]) => 1
    count_unique_elements([]) => 0
    """
    return len(set(input_list))


def remove_sixes(set_a: set) -> set:
    """
    Take a set of numbers and remove the number six from it if its there, return the set without sixes.

    remove_sixes({1, 2, 3, 4, 5, 6, 7, 8, 9}) => {1, 2, 3, 4, 5, 7, 8, 9}
    remove_sixes({1, 5, 7}) => {1, 5, 7}

    :param set_a: given set
    :return: set without sixes.
    """
    set_a.discard(6)
    return set_a


if __name__ == "__main__":
    # run this file to test the function
    print(create_set_from_numbers(1, 2, 3))  # {1, 2, 3}
    print(create_set_from_numbers(1, 2, 1))  # {1, 2}

    print(convert_list_to_set([1, 2, 3, 1]))  # {1, 2, 3}
    print(convert_list_to_set([1, 2, 3, 4]))  # {1, 2, 3, 4}

    print(count_unique_elements([1, 2, 3]))  # 3
    print(count_unique_elements([1, 2, 1]))  # 2

    print(remove_sixes({1, 2, 3, 4, 5, 6, 7, 8, 9}))  # {1, 2, 3, 4, 5, 7, 8, 9}
    print(remove_sixes({1, 5, 7}))  # {1, 5, 7}
