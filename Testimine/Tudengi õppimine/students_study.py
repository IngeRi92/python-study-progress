"""Students study."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 1 <= time <= 4:
        return False
    elif 5 <= time <= 17:
        return coffee_needed
    elif 18 <= time <= 24:
        return True
    else:
        return False
