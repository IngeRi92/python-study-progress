"""Swap edge elements."""


def swap_edge_elements(elements: list) -> list:
    """
    Return a list where the first and last element of the initial list are swapped.

    swap_edge_elements([1, 2, 3]) => [3, 2, 1]
    swap_edge_elements([1, 2]) => [2, 1]
    swap_edge_elements([1, 2, 1, 4]) => [4, 2, 1, 1]
    swap_edge_elements(["foo", "bar", "pub"]) => ["pub", "bar", "foo"]

    """
    elements[0], elements[-1] = elements[-1], elements[0]
    return elements
