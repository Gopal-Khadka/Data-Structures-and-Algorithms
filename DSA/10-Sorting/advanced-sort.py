def merge_sort(arr: list):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    Merge sort is a divide-and-conquer algorithm that works as follows:
    1. Divide the unsorted list into two approximately equal halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves to produce the sorted list.
    Args:
        arr (list): The list of elements to be sorted.
    Returns:
        list: A new list containing all elements from the input list in ascending order.
    Example:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """

    # Base case: if the array has 1 or no elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into one sorted list.
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both lists and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left list, add them to the merged list
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # If there are remaining elements in the right list, add them to the merged list
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


arr = [3, 7, 8, 5, 1, 2, 4, 3, -2]
print(merge_sort(arr))
