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
   