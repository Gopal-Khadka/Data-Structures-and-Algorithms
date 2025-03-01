def group_anagrams(words: list[str]):
    """
    Group anagrams from a list of strings.
    This function takes a list of strings and groups anagrams together. Two strings are considered
    anagrams if they contain the same characters with the same frequencies, regardless of order.
    Args:
        words (list[str]): A list of strings to be grouped into anagrams.
    Returns:
        list[list[str]]: A list of lists, where each inner list contains strings that are anagrams
        of each other.
    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    Time Complexity:
        O(n * k * log(k)) where n is the number of words and k is the maximum length of a word
        due to sorting each word.
    Space Complexity:
        O(n) where n is the total number of characters across all words.
    """

    my_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in my_dict:
            my_dict[sorted_word].append(word)
        else:
            my_dict[sorted_word] = [word]

    return list(my_dict.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
