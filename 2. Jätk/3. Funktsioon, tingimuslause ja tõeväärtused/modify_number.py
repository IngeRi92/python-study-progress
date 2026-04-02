"""Modify number."""


def modify_number(x):
    """Modify number based on given conditions.

    If x is 0, return 0.
    If x is divisible by 2 and 5 , multiply x by 100.
    If x is divisible by 5, multiply x by 2.
    If x is divisible by 2, multiply x by 3.
    Otherwise, return x plus 10.
    """
    if x == 0:
        return 0
    elif (x % 2 == 0) and (x % 5 == 0):
        return x * 100
    elif x % 5 == 0:
        return x * 2
    elif x % 2 == 0:
        return x * 3
    else:
        return x + 10
