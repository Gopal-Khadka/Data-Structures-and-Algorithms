def bubble_sort(lst: list):
    """
    Sorts a list of elements in ascending order using the bubble sort algorithm.

    Args:
        lst (list): The list of elements to be sorted.

    Returns:
        lst(list): Sorted list.

    Algorithm:
    1. For each element in the list (i from 0 to length of list - 1):
       a. For each element in the list up to the unsorted portion (j from 0 to length of list - i - 1):
          i. If the current element is greater than the next element:
             1. Swap the current element with the next element
    """

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swappping the items
    return lst


def selection_sort(my_list: list):
    """
    Sorts a list in ascending order using the selection sort algorithm.
    The selection sort algorithm divides the input list into two parts:
    the sublist of items already sorted, which is built up from left to right at the front (left) of the list,
    and the sublist of items remaining to be sorted that occupy the rest of the list.
    Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
    The algorithm proceeds by finding the smallest element in the unsorted sublist,
    exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order),
    and moving the sublist boundaries one element to the right.
    Args:
        my_list (list): The list of elements to be sorted.
    Returns:
        list: The sorted list in ascending order.
    Pseudocode:
    1. For each element in the list (except the last one):
        a. Assume the current element is the minimum.
        b. For each of the remaining elements:
            i. If the element is smaller than the current minimum, update the minimum.
        c. Swap the current element with the minimum element found in the remaining elements if "min_index" changed
    2. Return the sorted list.
    """

    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:  # no swapping (i.e no change in value of min_index)
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


def insertion_sort(my_list: list):
    """
    Sorts a list of elements using the insertion sort algorithm.
    Args:
        my_list (list): A list of elements to be sorted.
    Returns:
        list: The sorted list.
    Pseudocode:
    1. Iterate over the list starting from the second element (index 1).
    2. For each element, compare it with the elements before it.
    3. Swap the element with the previous elements until it is in the correct position.
    4. Continue this process until the entire list is sorted.
    """

    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
    return my_list


def insertion_sort_again(my_list: list):
    """
    Sorts a list of elements using the insertion sort algorithm.
    Args:
        my_list (list): The list of elements to be sorted.
    Returns:
        list: The sorted list.
    Algorithm:
        1. Iterate from the second element to the end of the list.
        2. For each element, store it in a temporary variable.
        3. Compare the temporary variable with the elements before it.
        4. Shift the elements one position to the right until the correct position for the temporary variable is found.
        5. Place the temporary variable in its correct position.
        6. Repeat until the entire list is sorted.
    Example:
        >>> insertion_sort_again([4, 2, 7, 1, 3])
        [1, 2, 3, 4, 7]
    """

    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


lst = [-2, 2, 1, 4, 7, 3, 2]
# lst = ["A", "C", "B"]
# selection_sort(lst)
# bubble_sort(lst)
insertion_sort(lst)
print(lst)
