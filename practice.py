# Method 1
def duplicates(arr: list):
    my_dict = {}
    for item in arr:
        if item in my_dict.keys():
            my_dict[item] = True
        else:
            my_dict[item] = False
    return [key for key, val in my_dict.items() if val == True]


# Method 2
def duplicates_again(arr: list[int]):
    # arr = [1,2,3,3,4]
    # nums_count = {1:1, 2:1, 3: 2, 4:1}
    nums_count = {}
    for item in arr:
        nums_count[item] = nums_count.get(item, 0) + 1
    return [key for key, val in nums_count.items() if val > 1]


list1 = [1, 2, 3, 2, 9, 9, 15, 21, 15]
arr = [1, 2, 3, 4, 5]
print(duplicates_again(list1))
