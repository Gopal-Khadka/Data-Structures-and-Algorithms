def longest_consecutive_sequence(nums):
    # Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0

    # Loop through the numbers in the nums array
    for num in nums:
        # Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence


def longest_consecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an unsorted array of integers.
    This function takes an array of integers and returns the length of the longest
    consecutive elements sequence. A consecutive sequence is a sequence of integers
    where each element is exactly one more than the previous element.


    Args:
        nums (list[int]): An unsorted array of integers.
    Returns:
        int: Length of the longest consecutive sequence found in the array.
    Examples:
        >>> longest_consecutive([100,4,200,1,3,2])
        4  # The consecutive sequence is [1,2,3,4]
        >>> longest_consecutive([0,3,7,2,5,8,4,6,0,1])
        9  # The consecutive sequence is [0,1,2,3,4,5,6,7,8]
        >>> longest_consecutive([])
        0  # Empty array returns 0
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1) as we only use constant extra space

    """

    if not nums:
        return 0
    nums.sort()

    longest_sequence = 1  # Track overall longest sequence
    current_length = 1  # Track current sequence length

    for idx in range(1, len(nums)):
        if nums[idx] == nums[idx - 1] + 1:  # Found consecutive number
            current_length += 1
        elif (
            nums[idx] != nums[idx - 1]
        ):  # Sequence break but not duplicates consecutively
            longest_sequence = max(longest_sequence, current_length)
            current_length = 1
    return max(
        longest_sequence, current_length
    )  # for cases where longest_sequence ends at last.


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))
# Output: 4


nums = [-2, -1, 4, 1, 3, 2, 5]
print(longest_consecutive(nums))
# Output: 5
