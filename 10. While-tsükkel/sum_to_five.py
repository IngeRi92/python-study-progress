"""Sum to five."""


def sum_to_five() -> int:
    """Return sum from 1 to 5."""
    total_sum = 0
    number = 1
    while number <= 5:
        total_sum += number
        number += 1
    return total_sum


if __name__ == "__main__":
    print(sum_to_five())  # 15
