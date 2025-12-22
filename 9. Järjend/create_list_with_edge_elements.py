"""Create list of edge elements."""


def create_list_with_edge_elements(elements: list) -> list:
    """
    Create a new list with 2 elements: the first and the last element of the list passed to the function.

    The initial list has at least one element.
    If the initial list has only one element, the same element is both the first and the last element.

    create_list_with_edge_elements([1, 2, 3]) => [1, 3]
    create_list_with_edge_elements([1]) => [1, 1]
    create_list_with_edge_elements(["a", "b"]) => ["a", "b"]
    create_list_with_edge_elements(["a", "b", "c", "d", "f"]) => ["a", "f"]
    """
    return [elements[0], elements[-1]]
