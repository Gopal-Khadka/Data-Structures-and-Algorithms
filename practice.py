def remove_duplicates(arr: list[int]):
    return list(set(arr))

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
print(remove_duplicates(my_list))
