"""Eat candy."""


def eat_candy(candy: int, is_diet: bool, christmas_time: bool) -> int:
    """
    Return how much candy will be left after eating candy.

    On a regular day you would eat 10 candy.
    If it's christmas time, you eat double the amount of normal eating amount.
    If you are on a diet, you eat 5 less than you would otherwise.
    Remember to always leave 1 candy left (never eat all).

    Examples:
    eat_candy(10, False, False) => 1
    eat_candy(100, True, False) => 95

    :param candy: The amount of candy in the beginning.
    :param is_diet: Whether you are on a diet.
    :param christmas_time: Whether it's christmas time.
    :return: The amount of candy after eating.
    """
    if candy <= 0:
        return 0
    if christmas_time:
        eat_ammount = 20
    else:
        eat_ammount = 10
    if is_diet:
        eat_ammount -= 5
    return max(candy - eat_ammount, 1)


if __name__ == "__main__":
    print(eat_candy(10, False, False))  # 1
    print(eat_candy(100, True, False))  # 95
    print(eat_candy(100, False, True))  # 80
    print(eat_candy(0, False, False))  # 0
