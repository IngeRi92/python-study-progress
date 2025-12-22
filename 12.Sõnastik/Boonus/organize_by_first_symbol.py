"""Organize by first symbols."""


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where the key is a character and the value is a list of words starting with this character.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting character and corresponding words in order of appearance.
    """
    result = {}
    for string in strings:
        if string:
            first_char = string[0]
            if first_char not in result:
                result[first_char] = []
            result[first_char].append(string)
    return result


if __name__ == '__main__':
    print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))
    # => {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}
    print(organise_by_first_symbol([""]))  # => {}
    print(organise_by_first_symbol(["a", "ab", "abcd"]))  # => {'a': ["a", "ab", "abcd"]}
