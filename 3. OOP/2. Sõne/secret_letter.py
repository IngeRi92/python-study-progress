"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    Examples:
    secret_letter("sOMEteSTLETTer8") => True
    secret_letter("thisisNOTvaliD4") => False
    secret_letter("TOOMANYnumbers99") => False

    :param letter: secret letter
    :return: validation
    """
    upperase_count = 0
    lowercase_count = 0
    digit_sum = 0
    for char in letter:
        if char.isupper():
            upperase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_sum += int(char)

    rule1 = upperase_count > lowercase_count
    rule2 = digit_sum <= upperase_count
    rule3 = digit_sum >= lowercase_count

    return rule1 and rule2 and rule3


if __name__ == "__main__":
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
