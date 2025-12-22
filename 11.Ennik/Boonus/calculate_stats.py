"""Calculate statistics."""


def calculate_stats(*numbers):
    """
    Calculate statistics from a given set of numbers and return a tuple.

    Tuple containing: (smallest number, largest number, average value, total sum).

    Args:
    *numbers: A variable number of numerical arguments (integers or floats).

    Returns:
    tuple: A tuple containing:
        - smallest number (int or float),
        - largest number (int or float),
        - average value (float),
        - total sum (int or float).

    If no numbers are provided, returns None.
    """
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    return (smallest, largest, average, total_sum)


if __name__ == "__main__":
    print(calculate_stats(5, 12, 3, 8, 20))  # => (3, 20, 9.6, 48)
