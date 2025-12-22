"""Count of letters."""


def count_of_letters(word: str) -> int:
    """
    Return the count of ascii letters in the string.

    Lower and upper case letters are treated as one.

    count_of_letters("Hello!") => 4
    count_of_letters("HELLO") => 4
    count_of_letters("HellohELLO") => 4
    count_of_letters("12345") => 0
    """
    word_lower = word.lower()
    letters = set()
    for char in word_lower:
        if char.isalpha():
            letters.add(char)
    return len(letters)


if __name__ == "__main__":
    print(count_of_letters("Hello!"))  # 4
    print(count_of_letters("HELLO"))  # 4
    print(count_of_letters("HellohELLO"))  # 4
    print(count_of_letters("12345"))  # 0
