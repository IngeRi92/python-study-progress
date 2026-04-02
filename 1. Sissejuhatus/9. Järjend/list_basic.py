"""List basic."""


def create_list_of_elements(a: int, b: int) -> list:
    """
    Return a list of the two elements a and b (in that order).

    create_list_of_two_elements(1, 2) => [1, 2]
    create_list_of_two_elements(81, 72) => [81, 72]
    """
    return [a, b]


def create_new_list_with_added_number(numbers: list, number: int) -> list:
    """
    Return a new list with the number added to it.

    Do not modify the existing list.
    add_element_into_list([1, 2, 3], 4) => [1, 2, 3, 4]
    """
    return numbers + [number]


def create_repeated_list(elements: list, repetition: int) -> list:
    """
    Create a list where the initial list's elements are repeated the amount of times given as the second argument .

    create_repeated_list([1, 2], 2) => [1, 2, 1, 2]
    create_repeated_list([1], 5) => [1, 1, 1, 1, 1]
    create_repeated_list([1, 2], 0) => []
    """
    return elements * repetition


def reverse_list(elements: list) -> list:
    """
    Return reversed list.

    reverse_list([1, 2, 3]) => [3, 2, 1]
    reverse_list(["a", "b"]) => ["b", "a"]
    """
    return elements[::-1]


if __name__ == "__main__":
    print(create_list_of_elements(1, 2))  # => [1, 2]
    print(create_list_of_elements(101, 23))  # => [101, 23]
    print(create_list_of_elements(56, 98))  # => [56, 98]
    print(create_new_list_with_added_number([1, 2, 3], 4))  # => [1, 2, 3, 4]
    print(
        create_new_list_with_added_number([66, 83, 13, 44], 25)
    )  # => [66, 83, 13, 44, 25]
    print(create_new_list_with_added_number([6, 10], 1))  # => [6, 10, 1]
    print(create_repeated_list([1, 2], 2))  # => [1, 2, 1, 2]
    print(create_repeated_list([1], 5))  # => [1, 1, 1, 1, 1]
    print(create_repeated_list([1, 2], 0))  # => []
    print(reverse_list([1, 2, 3]))  # => [3, 2, 1]
    print(reverse_list(["a", "b"]))  # => ["b", "a"]
