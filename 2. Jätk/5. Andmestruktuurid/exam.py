"""Sum the first half of even numbers."""


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.

    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    sum_length = (len(even_numbers) + 1) // 2
    return sum(even_numbers[:sum_length])
