def has_unique_chars(string: str):
    """
    Check if a string contains all unique characters.
    This function determines whether all characters in the input string are unique,
    meaning no character appears more than once.
    Args:
        string (str): The input string to check for unique characters.
    Returns:
        bool: True if all characters in the string are unique, False otherwise.
    Example:
        >>> has_unique_chars("abc")
        True
        >>> has_unique_chars("abca")
        False
    """

    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True


str1 = "abcdefg"
print("For", str1, has_unique_chars(str1))
str2 = "hello"
print("For", str2, has_unique_chars(str2))
