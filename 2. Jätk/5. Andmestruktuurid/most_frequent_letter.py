"""Find the most frequent letter in a string."""


def most_frequent_letter(string):
    """
    Return the most frequent letter in a string.

    There can be symbols and letters in a string. Symbols are not counted.
    """
    letter_counts = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    most_common_letter = ""
    highest_count = 0
    for letter in letter_counts:
        if letter_counts[letter] > highest_count:
            highest_count = letter_counts[letter]
            most_common_letter = letter
    return most_common_letter
