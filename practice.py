def subarray_sum(nums: list[int], target: int):
    """
    Find a contiguous subarray that sums up to the target value.
    This function uses a cumulative sum approach with a hash map to find a subarray
    whose elements sum up to the target value. It runs in O(n) time complexity.
    Args:
        nums (list[int]): A list of integers to search through
        target (int): The target sum to find
    Returns:
        list[int]: A list containing two indices [i, j] where the subarray nums[i+1:j+1]
                  sums to the target value. Returns an empty list if no such subarray exists.
    Example:
        >>> subarray_sum([1, 2, 3, 4], 6)
        [0, 2]  # because nums[1:3] = [2, 3] sums to 6
        >>> subarray_sum([1, 4, 20, 3, 10, 5], 33)
        [2, 4]  # because nums[3:5] = [3, 10, 20] sums to 33
        >>> subarray_sum([1, 2, 3], 10)
        []      # no subarray sums to 10
    Note:
        - The function uses a cumulative sum dictionary to track running sums
        - The key in dict is cumulative_sum and value is the index
        - Time Complexity: O(n) where n is length of input list
        - Space Complexity: O(n) for storing the cumulative sums
    """

    cumulative_sum_dict = {0: -1}
    cumulative_sum = 0

    for idx, num in enumerate(nums):
        cumulative_sum += num
        complement = cumulative_sum - target
        if complement in cumulative_sum_dict:
            return [cumulative_sum_dict[complement], idx]
        cumulative_sum_dict[cumulative_sum] = idx

    return []


nums = [1, 2, 3, 4, 5]

# cum_sum/key           c = cum_sum - target        value/index
# 1 =1                  c= 0-9 = -8                 0
# 1+2 = 3               c= 3-9 = -6                 1
# 1+ 2+ 3 =6            c= 6-9 = -3                 2
# 1+ 2 + 3 + 4 = 10     c= 10-9 = 1                 3
# 1 + 2+ 3+ 4 + 5 = 15  c= 15-9 = 6                 4

# cumulative_sum_dict = {0: -1, 1: 0, 3: 1, 6: 2, 10: 3, 15: 4}
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]
