"""Remove sixes."""


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where the entries where the value was divisible by 6, are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without entries where the value would be divisible by six.
    """
    result_dict = {}
    for key, value in six_dict.items():
        if value % 6 != 0:
            result_dict[key] = value
    return result_dict


if __name__ == '__main__':
    print(remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}))  # => {"a": 4, "b": 8}
    print(remove_sixes({}))  # => {}
    print(remove_sixes({"a": 6, "b": 6, "c": 7, "d": 6}))  # => {"c": 7}
