"""Min block."""


def min_block(s: str) -> int:
    """
    Given a string, return the length of the smallest "block" in the string.

    A block is a run of adjacent chars that are the same.
    """
    if len(s) == 0:
        return 0

    block_lengths = []
    current_block_length = 1
    for position in range(1, len(s)):
        if s[position] == s[position - 1]:
            current_block_length += 1
        else:
            block_lengths.append(current_block_length)
            current_block_length = 1
    block_lengths.append(current_block_length)
    return min(block_lengths)


if __name__ == '__main__':
    print(min_block("abc"))  # 1
    print(min_block("aabc"))  # 1
    print(min_block("aabbcccc"))  # 2
    print(min_block("aaaaa"))  # 5
