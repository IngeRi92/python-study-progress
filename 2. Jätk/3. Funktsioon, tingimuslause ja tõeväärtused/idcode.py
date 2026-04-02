"""ID code."""


def is_valid_gender_number(gender_number: int) -> bool:
    """Check if given value is correct for gender number in ID code."""
    return 1 <= gender_number <= 6


def get_gender(gender_number: int) -> str:
    """Define gender based on gender number in ID code."""
    if gender_number % 2 == 0:
        return "female"
    else:
        return "male"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    return 0 <= year_number <= 99


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    return 1 <= month_number <= 12


def is_valid_serial_number(serial_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    return 1 <= serial_number <= 999


def is_leap_year(year_number: int) -> bool:
    """Check if given year is a leap year."""
    if year_number % 400 == 0:
        return True
    elif year_number % 100 == 0:
        return False
    elif (year_number % 4 == 0) and (year_number % 100 != 0):
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    if gender_number in [1, 2]:
        return 1800 + year_number
    elif gender_number in [3, 4]:
        return 1900 + year_number
    elif gender_number in [5, 6]:
        return 2000 + year_number


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    if not is_valid_serial_number(birth_number):
        return "Wrong input!"
    elif 1 <= birth_number <= 10:
        return "Kuressaare"
    elif 11 <= birth_number <= 20:
        return "Tartu"
    elif 21 <= birth_number <= 220:
        return "Tallinn"
    elif 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    elif 271 <= birth_number <= 370:
        return "Tartu"
    elif 371 <= birth_number <= 420:
        return "Narva"
    elif 421 <= birth_number <= 470:
        return "Pärnu"
    elif 471 <= birth_number <= 710:
        return "Tallinn"
    else:
        return "undefined"


if __name__ == '__main__':
    print("\nGender number:")
    # for i in range(9):
    #    print(f"{i} {is_valid_gender_number(i)}")
    # 0 -> False
    # 1...6 -> True
    # 7...8 -> False

    print("\nGet gender:")
    # print(get_gender(2))  # -> "female"
    # print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_serial_number(0))  # -> False
    print(is_valid_serial_number(1))  # -> True
    print(is_valid_serial_number(850))  # -> True

    print("\nLeap year:")
    # print(is_leap_year(1804))  # -> True
    # print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
