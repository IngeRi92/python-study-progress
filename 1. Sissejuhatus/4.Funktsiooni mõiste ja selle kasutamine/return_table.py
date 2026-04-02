"""Get table string."""


def get_line() -> str:
    """
    Return a line (string) of minus symbols.

    This function will be called out in get_table function below.
    """
    return "-" * 10


def get_table() -> str:
    r"""
    Return a table (string) with your name and hobby in it.

    The format of the table is as follows:
    First there is a line of - symbols.
    Then there is line of your name.
    The third line is again the line of - symbols.
    Then comes your hobby.
    The last line is again the line of - symbols.

    Add new line symbol \n after every line.

    The width of the table is up to you (depends on your name and/or hobby).
    Use previous function get_line() to get the three lines.
    The second and the fourth line start and end with a pipe (|).

    For example:
    -----------
    | John    |
    -----------
    | running |
    -----------

    Note that the pipes have to align (the text inside doesn't have to align).

    Another example:
    ---------
    | Kim   |
    ---------
    |   box |
    ---------

    Name and hobby - both have to contain at least 3 letters.
    """
    name = " Inge "
    hobby = "gaming"
    table = ""
    table += get_line() + "\n"
    table += f"| {name} |\n"
    table += get_line() + "\n"
    table += f"| {hobby} |\n"
    table += get_line()
    return table


if __name__ == "__main__":
    print(get_table())
