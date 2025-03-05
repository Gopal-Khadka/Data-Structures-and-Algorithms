from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Check if array of strings is sorted according to alien dictionary order.
        Algorithm:
        1. Create a dictionary mapping each character in alien order to its index position
        2. Compare adjacent words pairwise
        3. For each pair of words:
            - Compare characters at same positions until either word ends
            - If first word character has lower alien order - move to next word pair
            - If first word character has higher alien order - array is not sorted
            - If matching characters but first word longer - array is not sorted
        4. Return True if all pairs are sorted according to alien order
        Args:
             words (List[str]): List of words to check if sorted
             order (str): String defining the alien alphabet ordering
        Returns:
             bool: True if words are sorted according to alien dictionary, False otherwise
        Time Complexity: O(M) where M is total characters in all words
        Space Complexity: O(1) as order length is fixed at 26 characters
        Example:
             >>> isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
             True
             >>> isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
             False
        """

        alien_order = {char: idx for idx, char in enumerate(order)}

        for i in range(len(words) - 1):  # Loop from 2nd to last element
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                # loop in range of minimum length betn both words
                # useful for words with same prefix i.e [app, apple,...]
                if alien_order[word1[j]] < alien_order[word2[j]]:
                    # if first word char has lower alien order, move to next char
                    break
                elif alien_order[word1[j]] > alien_order[word2[j]]:
                    # # if first word char has higher alien order, it is not sorted lexographically
                    return False
            # If word1 is a prefix of word2 but word1 is longer, it's invalid
            if len(word1) > len(word2) and word1[: len(word2)] == word2:
                # if both words have same prefix but prev word is longer
                # that means it is not sorted lexographically
                # for eg: ["word","world","row"] (here, "wor" is same.)
                return False
        return True


sol = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
result = sol.isAlienSorted(words, order)
print(result)


words = ["kuvp", "q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
result = sol.isAlienSorted(words, order)
print(result)
