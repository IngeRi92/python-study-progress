"""Asking age from a user."""


def asking_age_from_user(age_limit: int) -> int:
    """
    Ask user age.

    You have to ask the user their age using input("What is your age?").
    You have to repeat this process until a correct age is entered.
    The age is correct if:
    - it is greater or equal to the age_limit; and
    - it is less or equal to 100.

    If the user enters a wrong age, the user gets a warning.
    The question is repeated until a correct age is entered.
    The function returns the correct age as an integer.

    Warning is printed out:
    - age < age_limit: Too young!
    - age > 100: Too old!

    An example (with age_limit 18):
    What is your age? 10
    Too young!
    What is your age? 101
    Too old!
    What is your age? 21
    (function returns 21)

    :param age_limit: The age limit.
    :return: A correct age given by the user.
    """
    while True:
        age = int(input("What is your age? "))
        if age < age_limit:
            print("Too young!")
        elif age > 100:
            print("Too old!")
        else:
            return age
