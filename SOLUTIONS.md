# Practicing LeetCode Questions

- [Practicing LeetCode Questions](#practicing-leetcode-questions)
  - [List of Questions](#list-of-questions)
    - [Linked Lists](#linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Hash Tables (Dictionaries)](#hash-tables-dictionaries)
    - [Sets](#sets)
    - [Sorting Algorithms for Linked Lists](#sorting-algorithms-for-linked-lists)
    - [Binary Search Trees (BST)](#binary-search-trees-bst)
    - [List Manipulation](#list-manipulation)
  - [Questions and Solutions](#questions-and-solutions)

## List of Questions

### Linked Lists

- **Finding the Middle Node:** Uses slow and fast pointers to locate the middle node in a linked list without knowing the length.
  - The `slow` pointer moves one step at a time.
  - The `fast` pointer moves two steps at a time.
  - When the `fast` pointer reaches the end, the `slow` pointer is at the middle node.
- **Detecting a Loop:** Employs Floyd's cycle-finding algorithm ("tortoise and hare") to efficiently detect loops in a linked list.
  - Uses `slow` and `fast` pointers.
  - If the pointers meet, a loop exists.
  - If the `fast` pointer reaches the end, no loop exists.
- **Removing Duplicates:** Removes duplicate values from a singly linked list in-place.
  - Optimal O(n) solution uses a Set to keep track of values.
  - O(n^2) solution iterates through the list without additional data structures.
- **Finding the Kth Node From the End:** Locates the Kth node from the end of a linked list without using the length attribute.
  - Uses `slow` and `fast` pointers, with the `fast` pointer starting k nodes ahead.
  - If the fast pointer reaches the end before moving k nodes, the list is too short.
- **Reversing a Sublist:** Reverses the nodes in a singly linked list from index m to n (inclusive) in one pass and in-place.
- **Partitioning a List:** Partitions a linked list such that nodes with values less than x come before nodes with values greater than or equal to x, preserving the original relative order.
  - Uses two dummy nodes to create two new linked lists.
  - One list contains nodes less than x, and the other contains nodes greater than or equal to x.
- **Swapping First and Last Nodes in a Doubly Linked List:** Swaps the values of the first and last nodes.
  - If the list is empty or has only one node, no action is taken.
- **Reversing a Doubly Linked List:** Reverses the order of nodes in a doubly linked list by swapping `prev` and `next` pointers.
- **Palindrome Check for Doubly Linked List:** Determines whether a doubly linked list reads the same forwards and backward.
  - Uses two pointers, one starting from the head and the other from the tail.
- **Swapping Pairs in a Doubly Linked List:** Swaps the values of adjacent nodes.
  - Uses a dummy node to simplify head pointer manipulation.

### Stacks

- **Stack Implementation with a List:** Implements a stack using a Python list.
  - The constructor initializes an empty list.
- **Push Operation:** Adds a value to the top of the stack (end of the list).
- **Pop Operation:** Removes and returns the top value from the stack (last element of the list).
- **Parentheses Balance Check:** Checks if a string of parentheses is balanced using a stack.
  - Push opening parentheses onto the stack.
  - Pop when encountering a closing parenthesis; returns `False` if the stack is empty or the popped value doesn't match.
- **String Reversal:** Uses a stack to reverse a string.
  - Push each character onto the stack, then pop to create the reversed string.
- **Stack Sorting:** Sorts a stack in ascending order using one additional stack.
  - Elements are temporarily moved between the original and additional stacks to achieve sorting.

### Queues

- **Queue Implementation with Stacks:** Implements a queue using two stacks.
  - **Enqueue:** Adds an element to the back of the queue.
  - **Dequeue:** Removes an element from the front of the queue.

### Hash Tables (Dictionaries)

- **Common Item Detection:** Checks if two lists have at least one common item.
  - Uses a dictionary to store elements from the first list for O(1) lookup.
- **Duplicate Finding:** Finds all duplicates in an array of integers.
  - Uses a hash table to count the occurrences of each number.
- **First Non-Repeating Character:** Finds the first non-repeating character in a string.
  - Uses a dictionary to count character frequencies.
- **Anagram Grouping:** Groups anagrams in an array of strings.
  - Uses a dictionary to store anagrams, with the sorted string as the key.
- **Two Sum Problem:** Finds the indices of two numbers in an array that add up to a target.
  - Uses a hash table to store numbers and their indices for quick lookup.
- **Subarray Sum:** Finds the indices of a contiguous subarray that adds up to a target sum.
  - Uses a hash table to store running sums and their indices.

### Sets

- **Duplicate Removal:** Removes duplicates from a list using a set.
  - Leverages the property that sets only contain unique elements.
- **Unique Character Check:** Checks if all characters in a string are unique.
  - Uses a set to track seen characters.
- **Pair Finding:** Finds pairs of numbers (one from each of two arrays) that sum to a target value.
  - Uses a set for efficient lookup.
- **Longest Consecutive Sequence:** Finds the length of the longest consecutive sequence in an unsorted array of integers.
  - Uses a set to optimize runtime.

### Sorting Algorithms for Linked Lists

- **Bubble Sort:** Sorts a linked list in ascending order by repeatedly comparing and swapping adjacent elements.
- **Selection Sort:** Sorts a linked list by repeatedly finding the smallest element and swapping it with the first element in the unsorted part of the list.
- **Insertion Sort:** Sorts a linked list by inserting each element into its correct position in the sorted part of the list.
- **Merge Sort:** Merges two sorted linked lists into one sorted list.

### Binary Search Trees (BST)

- **BST Validation:** Checks whether a binary search tree is a valid BST.
  - Uses in-order traversal to ensure nodes are in ascending order.
- **Kth Smallest Node:** Finds the kth smallest element in a BST.
  - Can be solved iteratively using a stack or recursively.

### List Manipulation

- **Find Max Min:** Finds the maximum and minimum values in a list.
- **Find Longest String:** Finds the longest string in a list of strings.
- **Remove Duplicates:** Removes duplicates from a sorted list in-place.
- **Max Profit:** Calculates the maximum profit that can be made by buying and selling stock at the right time.
- **Rotate:** Rotates a list to the right by k steps.

## Questions and Solutions

**Note:** Refer to `practice.py` file in specific commit for specific complete solution

1. Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.

   ```python
    def find_middle_node(self):
        """
        Finds the middle node in a linked list using the two-pointer (slow and fast) technique.
        The function uses two pointers moving at different speeds:
        - slow pointer moves one step at a time
        - fast pointer moves two steps at a time
        When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
        For odd number of nodes, returns the exact middle node.
        For even number of nodes, returns the first of the two middle nodes.
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) as only two pointers are used
        Returns:
            Node: The middle node of the linked list
                  Returns None if list is empty
        Example:
            For list: 1->2->3->4->5, returns node containing 3
            For list: 1->2->3->4, returns node containing 2
        """

        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

   ```

2. Write a method called has_loop that is part of the linked list class.

   - The method should be able to detect if there is a cycle or loop present in the linked list.
   - The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

```python
  def has_loop(self):
      """
      Detects if there's a loop in a linked list using Floyd's Cycle-Finding Algorithm.
      The algorithm uses two pointers, 'slow' and 'fast', moving at different speeds
      through the linked list. The 'slow' pointer moves one step at a time while the
      'fast' pointer moves two steps. If there's a loop, the pointers will eventually
      meet.
      Returns:
          bool: True if a loop is detected, False otherwise
      Time Complexity: O(n) where n is the number of nodes in the linked list
      Space Complexity: O(1) as only two pointers are used regardless of list size
      Example:
          >>> linked_list = LinkedList()
          >>> linked_list.append(1)
          >>> linked_list.append(2)
          >>> linked_list.append(3)
          >>> # Create a loop by connecting last node to second node
          >>> linked_list.tail.next = linked_list.head.next
          >>> linked_list.has_loop()
          True
      """

      slow = self.head
      fast = self.head

      while fast is not None and fast.next is not None:
          slow = slow.next
          fast = fast.next.next

          if slow == fast:
              return True
      return False

```
3. You are given a singly linked list that contains integer values, where some of these values may be duplicated.

   - Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.

   - Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.

   - You can implement the remove_duplicates() method in two different ways:

     1. Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.

      ```python
      def remove_duplicates(self):
           """
           Remove duplicate nodes from a linked list.
           This method removes duplicate nodes from the linked list by maintaining a set of
           seen values. It traverses the list once, removing subsequent occurrences of values
           that have already been encountered.
           Time Complexity: O(n) where n is the number of nodes in the linked list
           Space Complexity: O(n) to store the set of unique values
           Example:
               Before: 1 -> 2 -> 2 -> 3 -> 1 -> 4
               After:  1 -> 2 -> 3 -> 4
           Returns:
               None. The list is modified in place.
           Note:
               - The method modifies the original linked list
               - The first occurrence of each value is kept
               - The length of the list is updated accordingly
           """

           values = set()
           previous: Node = None
           current = self.head

           while current is not None:
               if current.value in values:
                   previous.next = (
                       current.next
                   )  # breaks the list chain(remove the element) if value already in the set
                   self.length -= 1
               else:
                   values.add(current.value)
                   previous = current  # updates "previous" if values is added to set

               current = current.next  # moves current to the next node

      ```
     2. Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.
      ```python
      def remove_duplicates_again(self):
          """
          Remove duplicate nodes from a linked list without using additional data structures.
          This method uses a nested loop approach where for each node, it checks all subsequent
          nodes for duplicates and removes them.

          Time Complexity: O(n^2) where n is the number of nodes in the linked list
          Space Complexity: O(1) as no extra space is needed

          Example:
              Before: 1 -> 2 -> 4 -> 3 -> 4
              After:  1 -> 2 -> 4 -> 3

          Note:
              - The method modifies the original linked list
              - The first occurrence of each value is kept
              - More computationally intensive than using a set, but uses no extra space
              - The length of the list is updated accordingly
          """
          current = self.head  # iterates all items of the list
          while current is not None:
              runner = current  # starts from current to the last item
              while runner.next is not None:
                  if runner.next.value == current.value:
                      # breaks the chain of element if duplicate found
                      runner.next = runner.next.next
                      self.length -= 1
                  else:
                      # moves the runner to the next element if no duplicate
                      runner = runner.next
              current = current.next
      ```

4. Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.
   ```python
     def kth_node_from_end(self, k: int):
           """
           Find the kth node from the end of a linked list using the two-pointer technique.
           This method uses two pointers (fast and slow) to find the kth node from the end
           in a single traversal. The fast pointer moves k steps ahead first, then both
           pointers move until fast reaches the end, making slow point to the kth node
           from the end.
           Args:
               k (int): The position from the end to find (0-based indexing)
           Returns:
               Node: The kth node from the end of the linked list
                     Returns None if k is greater than the length of the list
           Examples:
               >>> ll = LinkedList(1)
               >>> ll.append(2)
               >>> ll.append(3)
               >>> ll.append(4)
               >>> ll.append(5)
               >>> ll.print_list()
               1, 2, 3, 4, 5
               >>> node = ll.kth_node_from_end(1)
               >>> node.value
               4
           Time Complexity: O(n) where n is the length of the linked list
           Space Complexity: O(1) as only two pointers are used
           """

           fast = self.head
           slow = self.head

           for _ in range(k):
               if fast is None:
                   return None
               fast = fast.next

           while fast.next is not None:
               slow = slow.next
               fast = fast.next
           return slow
   ```

5. You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.
  ```python
  def reverse_btn(self, start: int, end: int):
        """
        Reverses a portion of the linked list between given positions `start` and `end` (inclusive).

        This method performs an **in-place** reversal of nodes from position `start` to `end`.
        The positions are **1-indexed**, meaning the first node is at position `1`.

        Args:
            start (int): The starting position of reversal (1-based index)
            end (int): The ending position of reversal (1-based index)

        Returns:
            None. The linked list is modified in place.

        Example:
            Given the linked list: 1 -> 2 -> 3 -> 4 -> 5
            Calling reverse_btn(start=2, end=4) results in: 1 -> 4 -> 3 -> 2 -> 5

        Notes:
            - If the list is empty (`self.head is None`) or if `start == end`, no modification is needed.
            - A **dummy node** is used to handle edge cases where the reversal includes the head node.
            - The reversal is performed in **one pass** with **O(n) time complexity**.
            - The space complexity is **O(1)**, as the reversal is done in place.
        """

        # Edge case: If the list is empty or no reversal is needed
        if not self.head or start == end:
            return

        # Step 1: Create a dummy node to simplify edge cases where `start = 1`
        dummy = Node(0)  # Dummy node does not hold any real value
        dummy.next = self.head  # Connect dummy node to the head
        leftPre = dummy  # This will eventually point to the node before `start`

        # Step 2: Move `leftPre` to the node **before** `start`
        for _ in range(start - 1):
            leftPre = leftPre.next  # Move forward

        # Now `leftPre` is the (start-1)th node, and `current_node` is the `start`th node
        current_node = leftPre.next
        reverse_tail = current_node  # The `start`th node will become the tail of the reversed section

        # Step 3: Reverse the sublist from `start` to `end`
        prev = (
            None  # `prev` will eventually become the new head of the reversed section
        )
        for _ in range(end - start + 1):
            next = current_node.next  # Save the next node
            current_node.next = prev  # Reverse the pointer
            prev = current_node  # Move `prev` forward
            current_node = next  # Move `current_node` forward

        # Step 4: Connect the reversed portion back to the original list
        leftPre.next = (
            prev  # Connect the (start-1)th node to the new head of the reversed section
        )
        reverse_tail.next = current_node  # Connect the tail of the reversed section to the remaining list

        # Step 5: Update `self.head` if `start == 1` (i.e., head was part of the reversed portion)
        self.head = dummy.next
  ```

6. Swap the values of the first and last node of LL. Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.
  ```python
  def swap_first_last(self):
        """
        Swaps the values of the first and last nodes in a linked list.
        The function performs an in-place swap of values between the head and tail nodes.
        No nodes are actually moved - only their values are exchanged.
        Returns:
            None if list is empty or has only one node
            Otherwise modifies the list in-place by swapping head and tail values
        Example:
            For list: 1 -> 2 -> 3 -> 4
            After swap: 4 -> 2 -> 3 -> 1
        Notes:
            - Does not modify the list if it's empty or has only one node
            - Maintains the same node references, only swaps values
        """

        if not self.head or self.head == self.tail:
            return None
        self.head.value, self.tail.value = self.tail.value, self.head.value

  ```
7. You are given a class MyQueue which implements a queue using two stacks. Your task is to implement the enqueue method which should add an element to the back of the queue.

- To achieve this, you can use the two stacks stack1 and stack2. Initially, all elements are stored in stack1 and stack2 is empty. In order to add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.

- Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

  ```python
  def enqueue_using_stacks(self, value):
        """
        Enqueues a value into a queue implemented using two stacks.
        This method implements queue's enqueue operation using two stacks (stack1 and stack2).
        The implementation follows these steps:
        1. Transfers all elements from stack1 to stack2
        2. Pushes the new value to the now-empty stack1
        3. Transfers all elements back from stack2 to stack1
        This ensures that the oldest elements remain at the top of stack1,
        maintaining FIFO (First In First Out) queue behavior.
        Args:
            value: The value to be added to the queue
        Time Complexity: O(n) where n is the number of elements in the queue
        Space Complexity: O(n) for storing elements in the stacks
        """

        # All elements are stored in stack1
        # All elements are transferred to stack2
        while self.stack1.height > 0:
            node = self.stack1.pop()
            self.stack2.push(node.value)

        # Append new element to the empty stack1
        self.stack1.push(value)

        # All elements are now stored in stack2
        # All elements are transferred back to stack1
        while self.stack2.height > 0:
            node = self.stack2.pop()
            self.stack1.push(node.value)
  ```

8. You have been tasked with implementing a queue data structure using two stacks in Python, and you need to write the dequeue method.The dequeue method should remove and return the first element in the queue.

  ```python
  def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()
  ```

9. Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise. Use a dictionary to solve the problem that creates an O(n) time complexity.

  ```python
  def common_in_list(arr1: list, arr2: list):
    # total time complexity: O(m+n)
    common_dict = {}
    for item1 in arr1:  # runs len(arr1) times i.e O(m)
        common_dict[item1] = False

    for item2 in arr2:  # runs len(arr2) times i.e O(n)
        if item2 in common_dict.keys():  # constat lookup i.e O(1)
            return True
    return False

  ```
10. Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
  ```python
  def find_duplicates(nums):
    # create an empty hash table
    num_counts = {}
 
    # iterate through each number in the array
    for num in nums:
        # add the number to the hash table or increment its count if it's already in the hash table
        num_counts[num] = num_counts.get(num, 0) + 1
 
    # create a list of the numbers that appear more than once in the input array
    duplicates = [num for num, count in num_counts.items() if count > 1]
 
    # return the list of duplicates
    return duplicates
  ```

11. Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

  ```python
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
  ```
12. You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams. (**Group Anagrams**)
```python
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
```

13.  Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target. (**Two Sum**)
```python
def two_sum_indices(nums: list[int], target: int):
"""
Find indices of two numbers in a list that sum up to the target value.
This function implements the two-sum problem using a hash map approach with O(n) time complexity.
Args:
   nums (list[int]): List of integers to search through
   target (int): Target sum to find
Returns:
   list[int]: List containing indices of two numbers that sum to target.
              Returns empty list if no solution exists.
Examples:
   >>> two_sum_indices([2, 7, 11, 15], 9)
   [0, 1]
   >>> two_sum_indices([3, 2, 4], 6)
   [1, 2]
   >>> two_sum_indices([3, 3], 6)
   [0, 1]
"""

num_map = {}
for idx, num in enumerate(nums):
   complement = target - num
   if complement in num_map:
       return [num_map[complement], idx]
   num_map[num] = idx
return []
```

14. Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).(**Subarray Sum**)
```python
def subarray_sum(nums: list[int], target: int):
    """
    Find a contiguous subarray that sums up to the target value.
    This function uses a cumulative sum approach with a hash map to find a subarray
    whose elements sum up to the target value. It runs in O(n) time complexity.
    Args:
        nums (list[int]): A list of integers to search through
        target (int): The target sum to find
    Returns:
        list[int]: A list containing two indices [i, j] where the subarray nums[i+1:j+1]
                  sums to the target value. Returns an empty list if no such subarray exists.
    Example:
        >>> subarray_sum([1, 2, 3, 4], 6)
        [0, 2]  # because nums[1:3] = [2, 3] sums to 6
        >>> subarray_sum([1, 4, 20, 3, 10, 5], 33)
        [2, 4]  # because nums[3:5] = [3, 10, 20] sums to 33
        >>> subarray_sum([1, 2, 3], 10)
        []      # no subarray sums to 10
    Note:
        - The function uses a cumulative sum dictionary to track running sums
        - The key in dict is cumulative_sum and value is the index
        - Time Complexity: O(n) where n is length of input list
        - Space Complexity: O(n) for storing the cumulative sums
    """

    cumulative_sum_dict = {0: -1}
    cumulative_sum = 0

    for idx, num in enumerate(nums):
        cumulative_sum += num
        complement = cumulative_sum - target
        if complement in cumulative_sum_dict:
            return [cumulative_sum_dict[complement], idx]
        cumulative_sum_dict[cumulative_sum] = idx

    return []
```
15. You have been given a list `my_list` with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.
- You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.
- Your function should not modify the original list, instead, it should create a new list with unique values and return it.
```python
def remove_duplicates(arr: list[int]):
    return list(set(arr))
```
16. Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.
```python
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
```
17. You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target. (**Find Pairs**)
```python
def find_pairs_using_set(arr1: list[int], arr2: list[int], target: int):
    """
    Find all pairs of numbers from two arrays that sum up to a target value.
    This function uses a set-based approach to efficiently find pairs of numbers
    from arr1 and arr2 whose sum equals the target value. By converting arr2 to
    a set, we achieve O(1) lookup time for each complement check.
    Args:
        arr1 (list[int]): First input array of integers
        arr2 (list[int]): Second input array of integers
        target (int): Target sum value to find pairs for
    Returns:
        list[tuple[int, int]]: List of tuples containing pairs (x,y) where
            x is from arr1, y is from arr2, and x + y = target
    Example:
        >>> find_pairs_using_set([1, 2, 3], [4, 5, 6], 7)
        [(1, 6), (2, 5), (3, 4)]
    Time Complexity: O(n) where n is length of arr1
    Space Complexity: O(m) where m is length of arr2 (for the set)
    """

    pairs = []
    arr2_set = set(arr2)
    for num in arr1:
        complement = target - num
        if complement in arr2_set:
            pairs.append((num, complement))
    return pairs
```
18. Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element). (**Set: Longest Consecutive Sequence**)  

**Method 1**  

- First, the function creates a set called num_set that contains all the elements of nums. Creating a set from the array allows the function to check whether an element is in the array in constant time, which optimizes the runtime of the solution.

- The function initializes the variable longest_sequence to zero, which will be updated as the function finds longer sequences.

- Next, the function loops through each number in the nums array. For each number, it checks if the previous number is not in num_set, which means the current number is the start of a new sequence. If the previous number is not in num_set, the function initializes a variable current_num to the current number and a variable current_sequence to 1, since the current number is the first element of a new sequence.

- The function then loops through the remaining elements of the sequence, incrementing the current_num and current_sequence variables for each element that is one more than the previous element. This loop stops when the next element is not in num_set, which means the sequence has ended.

- Once the loop has ended, the function updates the longest_sequence variable to the maximum of its current value and the current_sequence value, since current_sequence represents the length of the sequence that has just been found.

- Finally, the function returns the longest_sequence.

```python
def longest_consecutive_sequence(nums):
    # Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0
    
    # Loop through the numbers in the nums array
    for num in nums:
        # Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            # Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

```

**Method 2**
```python
def longest_consecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an unsorted array of integers.
    This function takes an array of integers and returns the length of the longest
    consecutive elements sequence. A consecutive sequence is a sequence of integers
    where each element is exactly one more than the previous element.


    Args:
        nums (list[int]): An unsorted array of integers.
    Returns:
        int: Length of the longest consecutive sequence found in the array.
    Examples:
        >>> longest_consecutive([100,4,200,1,3,2])
        4  # The consecutive sequence is [1,2,3,4]
        >>> longest_consecutive([0,3,7,2,5,8,4,6,0,1])
        9  # The consecutive sequence is [0,1,2,3,4,5,6,7,8]
        >>> longest_consecutive([])
        0  # Empty array returns 0
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1) as we only use constant extra space

    """

    if not nums:
        return 0
    nums.sort()

    longest_sequence = 1  # Track overall longest sequence
    current_length = 1  # Track current sequence length

    for idx in range(1, len(nums)):
        if nums[idx] == nums[idx - 1] + 1:  # Found consecutive number
            current_length += 1
        elif (
            nums[idx] != nums[idx - 1]
        ):  # Sequence break but not duplicates consecutively
            longest_sequence = max(longest_sequence, current_length)
            current_length = 1
    return max(
        longest_sequence, current_length
    )  # for cases where longest_sequence ends at last.
```

19. Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the bubble sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list. (**Bubble Sort of LL**)

```python
def bubble_sort(self):
    """
    Sorts the linked list using bubble sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Algorithm:
    1. If list has less than 2 nodes, return as it's already sorted
    2. Use two pointers: current and next_node
    3. Traverse list repeatedly, swapping adjacent values if they're out of order
    4. Track sorted portion with sorted_until pointer
    5. Continue until no more swaps are needed
    6. Update tail pointer to last node
    """

    # Check if the list has less than 2 elements
    if self.length < 2:
    return

    # Initialize the sorted_until pointer to None
    sorted_until = None  # Initially, last node points to None
    count = 0

    # Continue sorting until sorted_until reaches the second node
    # sorted_until starts from previous sorted_until to second node (decrementing in index)
    while sorted_until != self.head.next:
    # Initialize current pointer to head of the list
    current = self.head

    # Iterate through unsorted portion of the list until sorted_until
    while current.next != sorted_until:
        next_node = current.next

        # Swap current and next_node values if current is greater
        if current.value > next_node.value:
            current.value, next_node.value = next_node.value, current.value

        # Move current pointer to next node
        current = current.next

    # Update sorted_until pointer to the last node processed
    sorted_until = current
```

20.  Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the selection sort algorithm. (**Selection Sort of LL**)

21. Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm. (**Insertion Sort of LL**)

22. Write merge() method that takes in another LinkedList as an input and merges it with the current LinkedList. The elements in both lists are assumed to be in ascending order, but the input lists themselves do not need to be sorted. (**Merge Two Sorted LL**)

23. You are tasked with writing a method called is_valid_bst in the BinarySearchTree class that checks whether a binary search tree is a valid binary search tree. (**Validate BST**)
```python 
def dfs_in_order(self):
        result = []

        def traverse(node: Node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return result

    def is_valid_bst(self):
        """
        Checks if the binary tree is a valid Binary Search Tree (BST).
        A binary tree is a BST if:
        - All nodes in the left subtree have values less than the node's value
        - All nodes in the right subtree have values greater than the node's value 
        - Both left and right subtrees are also BSTs
        Logic:
        1. Gets inorder traversal of tree which gives sorted array for valid BST
        2. Checks if array is strictly increasing (each element greater than previous)
        3. Returns False if any violation found, True if entire array is valid
        Returns:
            bool: True if tree is valid BST, False otherwise
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n) for storing inorder traversal array
        """

        sorted_values = self.dfs_in_order()
        for i in range(1, len(sorted_values)):
            if sorted_values[i - 1] >= sorted_values[i]:
                return False
        return True
```

24. Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3. (**BST: Kth Smallest Node**)

```python

```
