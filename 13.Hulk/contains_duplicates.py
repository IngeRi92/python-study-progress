"""Contains duplicates."""


def contains_duplicates(input_list: list) -> bool:
    """
    Return whether the list contains duplicate elements.

    No loops required.

    contains_duplicates([1, 2, 3]) => False
    contains_duplicates([1, 2, 1]) => True
    contains_duplicates([1, 1]) => True
    contains_duplicates([1]) => False
    contains_duplicates([]) => False
    """
    return len(input_list) != len(set(input_list))


if __name__ == "__main__":
    # run this file to test the function
    print(contains_duplicates([1, 2, 3]))  # False
    print(contains_duplicates([1, 2, 1]))  # True
    print(contains_duplicates([1, 1]))  # True
