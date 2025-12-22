"""Odd sums of consecutive elements."""


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """
    Return list of odd sums of consecutive elements.

    Consider all consecutive elements in the input list. Return a list of all the odd sums of consecutive elements.

    odd_sums_of_consecutive_elements([1, 2, 3, 5]) => [3, 5]
    odd_sums_of_consecutive_elements([8, 10]) => []
    odd_sums_of_consecutive_elements([9]) => []
    odd_sums_of_consecutive_elements([11, 8]) => [19]

    :param nums:
    :return:
    """
    result = []
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum % 2 == 1:
            result.append(current_sum)
    return result


if __name__ == "__main__":
    print(odd_sums_of_consecutive_elements([1, 2, 3, 5]))  # [3, 5]
    print(odd_sums_of_consecutive_elements([11, 8]))  # [19]
