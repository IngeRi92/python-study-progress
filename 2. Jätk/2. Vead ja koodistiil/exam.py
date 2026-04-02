"""Docstring."""


def list_of_digits_and_chars(num_and_char: list) -> str:
    """Find digits and chars.

    You need to find letters and numbers in separate lists from the list.
    The list of numbers should include numbers larger than two digits with a balance of 9 greater than 5.
    The list of stars must not include large stars or 3-letter strings. Return a string consisting of the sum of the numbers and the added string.
    """
    dig_list = []
    char_list = []
    for i in num_and_char:
        if i.isdigit() and len(i) > 1:
            if int(i) % 9 >= 5:
                dig_list.append(int(i))
        elif i.isalpha() and len(i) != 3 and not i.isupper():
            char_list.append(i)
    letters = "".join(char_list)
    return f"{sum(dig_list)} {letters}"


if __name__ == "__main__":
    print(
        list_of_digits_and_chars(
            [
                "9",
                "AEL",
                "25",
                "5",
                "k",
                "+",
                "15",
                "ae",
                "17",
                "abr",
                "l",
                "?",
                "01",
                "k",
                "0",
                "i",
                "9098",
                "r",
                "j",
                "778",
                "ak",
                "905",
            ]
        )
    )  # 10660 kaelkirjak
