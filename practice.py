def find_pairs(arr1: list[int], arr2: list[int], target: int):
    """Find pairs of numbers from two arrays that sum up to a target value.
    This function takes two lists of integers and a target sum, then returns all pairs
    (one number from each list) that add up to the target.

    Method: Brute Force
    - Uses nested loops to check all possible combinations of numbers from both arrays
    - Time Complexity: O(n*m) where n and m are lengths of arr1 and arr2 respectively
    - Space Complexity: O(k) where k is the number of pairs found

    Args:
        arr1 (list[int]): First list of integers to search through
        arr2 (list[int]): Second list of integers to search through
        target (int): The target sum to find pairs for

    Returns:
        list[tuple[int, int]]: A list of tuples, where each tuple contains a pair of numbers
                              (one from arr1 and one from arr2) that sum to target

    Examples:
        >>> find_pairs([1, 2, 3], [4, 5, 6], 7)
        [(1, 6), (2, 5), (3, 4)]
        >>> find_pairs([1, 2], [3, 4], 10)
        []
    """

    results = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 + num2 == target:
                results.append((num1, num2))
    return results


def find_pairs_using_set(arr1: list[int], arr2: list[int], target: int):
    """
    Find all pairs of numbers from two arrays that sum up to a target value.
    This function uses a set-based approach to efficiently find pairs of numbers
    from arr1 and arr2 whose sum equals the target value. By converting arr2 to
    a set, we achieve O(1) lookup time for each complement check.
    Args:
        arr1 (list[int]): First input array of integers
        arr2 (list[int]): Second input array of integers
        target (int): Target sum value to find pairs for
    Returns:
        list[tuple[int, int]]: List of tuples containing pairs (x,y) where
            x is from arr1, y is from arr2, and x + y = target
    Example:
        >>> find_pairs_using_set([1, 2, 3], [4, 5, 6], 7)
        [(1, 6), (2, 5), (3, 4)]
    Time Complexity: O(n) where n is length of arr1
    Space Complexity: O(m) where m is length of arr2 (for the set)
    """

    pairs = []
    arr2_set = set(arr2)
    for num in arr1:
        complement = target - num
        if complement in arr2_set:
            pairs.append((num, complement))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)
# Output: [(1, 6), (3, 4), (5, 2)]


pairs = find_pairs_using_set(arr1, arr2, target)
print(pairs)
# Output: [(1, 6), (3, 4), (5, 2)]
