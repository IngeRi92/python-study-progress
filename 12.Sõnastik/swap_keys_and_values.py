"""Swap keys and values."""


def swap_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been swapped.

    swap_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been swapped.
    """
    swapped_dict = {}
    for key, value in exchange_dict.items():
        swapped_dict[value] = key
    return swapped_dict


if __name__ == '__main__':
    print(swap_keys_and_values({"a": "b", "c": "d"}))  # => {"b": "a", "d": "c"}
    print(swap_keys_and_values({"Ago": "Luberg"}))  # => {"Luberg" : "Ago"}
    print(swap_keys_and_values({"Sass": "Alexander", "number": 37}))  # => {"Alexander" : "Sass", 37 : "number"}
