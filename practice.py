def common_in_list(list1: list, list2: list):
    for item1 in list1:
        if item1 in list2:
            return True
    return False


def common_in_arr(arr1: list, arr2: list):
    # total time complexity: O(m+n)
    common_dict = {}
    for item1 in arr1:  # runs len(arr1) times i.e O(m)
        common_dict[item1] = False

    for item2 in arr2:  # runs len(arr2) times i.e O(n)
        if item2 in common_dict.keys():  # constat lookup i.e O(1)
            return True
    return False


list1 = [1, 2, 9, 15, 21]
list2 = [2, 3, 5, 7, 11]
print(common_in_list(list1, list2))
