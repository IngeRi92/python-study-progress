"""Unique chars counter."""


def count_unique_characters(words: list[str]) -> dict:
    """
    Count the number of unique characters in each word from a list of words.

    Examples:
    count_unique_characters(["apple", "banana", "pear"]) => {"apple": 4, "banana": 3, "pear": 4}
    count_unique_characters(["hello", "world", "python"]) => {"hello": 4, "world": 5, "python": 6}
    count_unique_characters(["a", "bb", "ccc"]) => {"a": 1, "b": 1, "c": 1}

    :param words: A list of words. Example: ["apple", "banana", "pear"]
    :return: A dictionary with words as keys and the count of unique characters as values.
             Example: {"apple": 4, "banana": 3, "pear": 4}
    """
    result = {}
    for word in words:
        result[word] = len(set(word))
    return result


if __name__ == '__main__':
    print(count_unique_characters(["apple", "banana", "pear"]))  # {'apple': 4, 'banana': 3, 'pear': 4}
    print(count_unique_characters(["hello", "world", "python"]))  # {'hello': 4, 'world': 5, 'python': 6}
    print(count_unique_characters(["a", "bb", "ccc"]))  # {'a': 1, 'bb': 1, 'ccc': 1}
    print(count_unique_characters(["test", "example", "unique"]))  # {'test': 3, 'example': 6, 'unique': 6}
    print(count_unique_characters(["abc", "aabbcc", "xyz"]))  # {'abc': 3, 'aabbcc': 3, 'xyz': 3}
