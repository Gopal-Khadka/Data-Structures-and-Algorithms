def two_sum(nums: list[int], target: int):
    # Returns the list of two numbers whose sum equals the target.
    num_map = {}
    for num in nums:
        complement = target - num
        if complement in num_map:
            return [complement, num]
        num_map[num] = complement
    return []


def two_sum_indices(nums: list[int], target: int):
    """
    Find indices of two numbers in a list that sum up to the target value.
    This function implements the two-sum problem using a hash map approach with O(n) time complexity.
    Args:
        nums (list[int]): List of integers to search through
        target (int): Target sum to find
    Returns:
        list[int]: List containing indices of two numbers that sum to target.
                   Returns empty list if no solution exists.
    Examples:
        >>> two_sum_indices([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum_indices([3, 2, 4], 6)
        [1, 2]
        >>> two_sum_indices([3, 3], 6)
        [0, 1]
    """

    num_map = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], idx]
        num_map[num] = idx
    return []


# my_dict = {2: 0, 6: 1, 7: 2, 8: 3}
# ==> [my_dict[2] = 0, i = 2]

# [2,6,7,8] target = 9
# two_nums = [?, ?]
# two_nums[0] + two_nums[1] = 9

# 9 - 2 = 7
# 9-6 = 3
# 9-7 = 2
# 9-8 = 1
lst = [2, 6, 7, 8]
print(two_sum_indices(lst, 9))  # [0, 2] i.e lst[0] + lst[2]


print(two_sum_indices([2, 7, 11, 15], 9))  # [0,1]
print(two_sum_indices([3, 2, 4], 6))  # [0,1, 2]
print(two_sum_indices([3, 3], 6))  # [0,1 ]
print(two_sum_indices([1, 2, 3, 4, 5], 10))  # []
print(two_sum_indices([1, 2, 3, 4, 5], 7))  # [2,3]
print(two_sum_indices([1, 2, 3, 4, 5], 3))  # [0,1]
print(two_sum_indices([], 0))  # []
