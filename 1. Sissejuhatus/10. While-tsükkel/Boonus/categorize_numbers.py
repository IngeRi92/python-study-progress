"""Positive number, negative number and zero."""


def categorize_numbers(number: list) -> None:
    """
    Print out number and their respective category.

    Given list of numbers, print out each number's category.
    If number X is zero, then function prints 'X - Null'.
    If number X is bigger than zero, then function prints 'X - Positiivne arv'.
    If number X is less than zero, then function prints 'X - Negatiivne arv'.

    :param number: List of numbers, which to categorize.
    """
    i = 0
    while i < len(number):
        num = number[i]
        if num > 0:
            print(f"{num} - Positiivne arv")
        elif num < 0:
            print(f"{num} - Negatiivne arv")
        else:
            print(f"{num} - Null")
        i += 1


if __name__ == "__main__":
    print(categorize_numbers([1, -6, 0, 17]))
    """
    1 - Positiivne arv
    -6 - Negatiivne arv
    0 - Null
    17 - Positiivne arv
    """
