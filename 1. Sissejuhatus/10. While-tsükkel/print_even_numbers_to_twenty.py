"""Print even numbers."""


def print_even_numbers_to_twenty():
    """Print even numbers starting from 2 up to 20."""
    number = 2
    while number <= 20:
        print(number)
        number += 2


if __name__ == "__main__":
    print_even_numbers_to_twenty()  # 2 4 6 8 10 12 14 16 18 20
