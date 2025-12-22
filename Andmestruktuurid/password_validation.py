"""Password validation."""


def is_correct_length(password: str) -> bool:
    """
    Check if the password's length is within the valid range.

    The password should have a length between 8 and 64 symbols.
    :param password: Password to be checked
    :return: True if the password's length is within the valid range, False otherwise
    """
    return 8 <= len(password) <= 64


def includes_uppercase(password: str) -> bool:
    """
    Check if the password contains at least one uppercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one uppercase letter, False otherwise
    """
    for char in password:
        if char.isupper():
            return True
    return False


def includes_lowercase(password: str) -> bool:
    """
    Check if the password contains at least one lowercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one lowercase letter, False otherwise
    """
    for char in password:
        if char.islower():
            return True
    return False


def includes_number(password: str) -> bool:
    """
    Check if the password contains at least one numeric digit.

    :param password: Password to be checked
    :return: True if the password contains at least one numeric digit, False otherwise
    """
    for char in password:
        if char.isdigit():
            return True
    return False


if __name__ == "__main__":
    print("\nPassword has at least one uppercase letter validation:")
    print(includes_uppercase("Defwefwevwe"))  # -> True
    print(includes_uppercase("e/¤!fwe64fwevw"))  # -> False

    print("\nPassword has at least one lowercase letter validation:")
    print(includes_lowercase("dJOWE821%&/"))  # -> True
    print(includes_lowercase("ÖJOWE821%&/"))  # -> False

    print("\nPassword has at least one number validation:")
    print(includes_number("dJOWE8%&/"))  # -> True
    print(includes_number("ÖJOWE%&/"))  # -> False
