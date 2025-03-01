def first_non_repeating_char(string: str):
    """Find the first non-repeating character in a string.
    This function takes a string input and returns the first character that appears exactly
    once in the string. If no such character exists, returns None.
    Args:
        string (str): The input string to search for non-repeating characters
    Returns:
        str or None: The first non-repeating character if one exists, None otherwise
    Example:
        >>> first_non_repeating_char("abcab")
        'c'
        >>> first_non_repeating_char("abcabc")
        None
        >>> first_non_repeating_char("aabbcc")
        None
    """

    char_counts = {}
    for letter in string:
        char_counts[letter] = char_counts.get(letter, 0) + 1

    for char in char_counts:
        if char_counts[char] == 1:
            return char

    return None


print(first_non_repeating_char("hheelloo"))  # None
print(first_non_repeating_char("hello"))  # h
print(first_non_repeating_char("leetcode"))  # l
