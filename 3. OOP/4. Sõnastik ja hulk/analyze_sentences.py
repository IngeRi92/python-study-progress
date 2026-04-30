"""Analyze sentences."""


def analyze_sentences(sentence1: str, sentence2: str) -> tuple:
    """
    Analyzes two sentences to find common and unique words using sets.

    Examples:
    analyze_sentences("hello world python", "hello java python") => ({'world'}, {'hello', 'python'}, {'java'})
    analyze_sentences("a b c", "b c d") => ({'a'}, {'b', 'c'}, {'d'})
    analyze_sentences("", "x y") => (set(), set(), {'x', 'y'})

    :param sentence1: The first input sentence. Example: "hello world python"
    :param sentence2: The second input sentence. Example: "hello java python"
    :return: A tuple of three sets:
        - unique_to_sentence1: A set of words that are unique to sentence1.
        - common_words: A set of words that appear in both sentences.
        - unique_to_sentence2: A set of words that are unique to sentence2.
        Example: ({'world'}, {'hello', 'python'}, {'java'})
    """
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())
    unique_to_sentence1 = set1 - set2
    common_words = set1 & set2
    unique_to_sentence2 = set2 - set1
    return unique_to_sentence1, common_words, unique_to_sentence2


if __name__ == '__main__':
    print(analyze_sentences("hello world python", "hello java python"))  # ({'world'}, {'hello', 'python'}, {'java'})
    print(analyze_sentences("a b c", "b c d"))  # ({'a'}, {'b', 'c'}, {'d'})
    print(analyze_sentences("", "x y"))  # (set(), set(), {'x', 'y'})
    print(analyze_sentences("apple orange banana", "banana grape apple"))  # ({'orange'}, {'apple', 'banana'}, {'grape'})
    print(analyze_sentences("one two three", "four five six"))  # ({'one', 'two', 'three'}, set(), {'four', 'five', 'six'})
