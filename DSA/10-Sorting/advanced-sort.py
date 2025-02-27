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

    # If there are remaining elements in the any list, add them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def quick_sort(arr: list) -> list:
    """
    Sorts an array using the Quick Sort algorithm.
    Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array
    and partitioning the other elements into two sub-arrays, according to whether they are less than/equal to or
    greater than the pivot. The sub-arrays are then sorted recursively.
    Args:
        arr (list): The list of elements to be sorted.
    Returns:
        list: A new list containing the sorted elements.
    Algorithm:
        1. If the array has one or no elements, it is already sorted. Return the array.
        2. Choose the last element of the array as the pivot.
        3. Partition the array into two sub-arrays:
            - left: Elements less than or equal to the pivot.
            - right: Elements greater than the pivot.
        4. Recursively apply the same process to the left and right sub-arrays.
        5. Combine the sorted left sub-array, the pivot, and the sorted right sub-array to get the final sorted array.
    """

    if len(arr) <= 1:  # Base case: If the array has one or no elements, it's sorted.
        return arr
    pivot = arr[-1]  # Choose the last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    return (
        quick_sort(left) + [pivot] + quick_sort(right)
    )  # Recursively sort and combine


def pivot(arr: list, pivot_index: int, end_index: int):
    """
    This function takes an array and a pivot index, and rearranges the elements in the array such that
    all elements less than the pivot are on the left of the pivot and all elements greater than the pivot
    are on the right. It returns the final position of the pivot element.
    Args:
        arr (list): The list of elements to be sorted.
        pivot_index (int): The index of the pivot element.
        end_index (int): The index of the last element in the array segment to be considered.
    Returns:
        int: The final index position of the pivot element after partitioning.
    Algorithm:
    1. Initialize swap_index to pivot_index.
    2. Iterate over the array from pivot_index + 1 to end_index.
    3. For each element, if it is less than the pivot element, increment swap_index and swap the current element with the element at swap_index.
    4. After the loop, swap the pivot element with the element at swap_index.
    5. Return the swap_index as the final position of the pivot element.
    """

    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    arr[pivot_index], arr[swap_index] = arr[swap_index], arr[pivot_index]
    return swap_index


def quick_sort_again(arr: list, left: int, right: int):
    """
    Sorts an array in place using the Quick Sort algorithm.
    Args:
        arr (list): The list of elements to be sorted.
        left (int): The starting index of the segment of the list to be sorted.
        right (int): The ending index of the segment of the list to be sorted.
    Returns:
        list: The sorted list.
    Algorithm:
        1. If the left index is less than the right index, proceed with sorting.
        2. Partition the array segment and get the pivot index.
        3. Recursively apply the same process to the left and right segments of the array divided by the pivot.
    Explanation:
        - The function uses a divide-and-conquer approach to sort the array.
        - The pivot function is used to partition the array such that elements less than the pivot are on the left,
          and elements greater than the pivot are on the right.
        - The function then recursively sorts the left and right segments of the array.
    """

    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_again(arr, left, pivot_index - 1)
        quick_sort_again(arr, pivot_index + 1, right)
    return arr


# Example usage for merge sort:
arr = [3, 7, 8, 5, 1, 2, 4, 3, -2]
sorted_arr = merge_sort(arr)
print("Using merge sort: ", sorted_arr)

# Example usage for quick sort:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Using quick sort: ", sorted_arr)


# Example using quick sort pt.2
arr = [4, 6, 1, 7, 3, 2, 5]
sorted_arr = quick_sort_again(arr, 0, len(arr) - 1)
print("Using quick sort again: ", sorted_arr)
