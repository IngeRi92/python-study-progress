"""Print table."""


def print_line():
    """
    Print a line of minus symbols.

    This function will be called out in print_table function below.
    """
    print("-" * 10)


def print_table():
    """
    Print a table with your name and hobby in it.

    The format of the table is as follows:
    First there is a line of - symbols.
    Then there is line of your name.
    The third line is again the line of - symbols.
    Then comes your hobby.
    The last line is again the line of - symbols.

    The width of the table is up to you (depends on your name and/or hobby).
    Use previous function print_line() to get the three lines.
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
    print_line()
    print("| " + " Inge " + " |")
    print_line()
    print("| " + "gaming" + " |")
    print_line()


if __name__ == "__main__":
    print_table()
