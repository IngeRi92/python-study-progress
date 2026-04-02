"""Make hola string."""


def hola_string(count: int) -> str:
    """
    Make hola string.

    print(hola_string(3)) => "holaholahola"
    print(hola_string(0)) => ""

    :param count: number of times to repeat
    :return: The string "hola" repeated `count` times.
    """
    result = ""
    for i in range(count):
        result += "hola"
    return result
