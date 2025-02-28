# Practicing LeetCode Questions

## List of Questions

### Linked Lists

*   **Finding the Middle Node:** Uses slow and fast pointers to locate the middle node in a linked list without knowing the length.
    *   The `slow` pointer moves one step at a time.
    *   The `fast` pointer moves two steps at a time.
    *   When the `fast` pointer reaches the end, the `slow` pointer is at the middle node.
*   **Detecting a Loop:** Employs Floyd's cycle-finding algorithm ("tortoise and hare") to efficiently detect loops in a linked list.
    *   Uses `slow` and `fast` pointers.
    *   If the pointers meet, a loop exists.
    *   If the `fast` pointer reaches the end, no loop exists.
*   **Removing Duplicates:** Removes duplicate values from a singly linked list in-place.
    *   Optimal O(n) solution uses a Set to keep track of values.
    *   O(n^2) solution iterates through the list without additional data structures.
*   **Finding the Kth Node From the End:** Locates the Kth node from the end of a linked list without using the length attribute.
    *   Uses `slow` and `fast` pointers, with the `fast` pointer starting k nodes ahead.
    *   If the fast pointer reaches the end before moving k nodes, the list is too short.
*   **Reversing a Sublist:** Reverses the nodes in a singly linked list from index m to n (inclusive) in one pass and in-place.
*   **Partitioning a List:** Partitions a linked list such that nodes with values less than x come before nodes with values greater than or equal to x, preserving the original relative order.
    *   Uses two dummy nodes to create two new linked lists.
    *   One list contains nodes less than x, and the other contains nodes greater than or equal to x.
*   **Swapping First and Last Nodes in a Doubly Linked List:** Swaps the values of the first and last nodes.
    *   If the list is empty or has only one node, no action is taken.
*   **Reversing a Doubly Linked List:** Reverses the order of nodes in a doubly linked list by swapping `prev` and `next` pointers.
*   **Palindrome Check for Doubly Linked List:** Determines whether a doubly linked list reads the same forwards and backward.
    *   Uses two pointers, one starting from the head and the other from the tail.
*   **Swapping Pairs in a Doubly Linked List:** Swaps the values of adjacent nodes.
    *   Uses a dummy node to simplify head pointer manipulation.

### Stacks

*   **Stack Implementation with a List:** Implements a stack using a Python list.
    *   The constructor initializes an empty list.
*   **Push Operation:** Adds a value to the top of the stack (end of the list).
*   **Pop Operation:** Removes and returns the top value from the stack (last element of the list).
*   **Parentheses Balance Check:** Checks if a string of parentheses is balanced using a stack.
    *   Push opening parentheses onto the stack.
    *   Pop when encountering a closing parenthesis; returns `False` if the stack is empty or the popped value doesn't match.
*   **String Reversal:** Uses a stack to reverse a string.
    *   Push each character onto the stack, then pop to create the reversed string.
*   **Stack Sorting:** Sorts a stack in ascending order using one additional stack.
    *   Elements are temporarily moved between the original and additional stacks to achieve sorting.

### Queues

*   **Queue Implementation with Stacks:** Implements a queue using two stacks.
    *   **Enqueue:** Adds an element to the back of the queue.
    *   **Dequeue:** Removes an element from the front of the queue.

### Hash Tables (Dictionaries)

*   **Common Item Detection:** Checks if two lists have at least one common item.
    *   Uses a dictionary to store elements from the first list for O(1) lookup.
*   **Duplicate Finding:** Finds all duplicates in an array of integers.
    *   Uses a hash table to count the occurrences of each number.
*   **First Non-Repeating Character:** Finds the first non-repeating character in a string.
    *   Uses a dictionary to count character frequencies.
*   **Anagram Grouping:** Groups anagrams in an array of strings.
    *   Uses a dictionary to store anagrams, with the sorted string as the key.
*   **Two Sum Problem:** Finds the indices of two numbers in an array that add up to a target.
    *   Uses a hash table to store numbers and their indices for quick lookup.
*   **Subarray Sum:** Finds the indices of a contiguous subarray that adds up to a target sum.
    *   Uses a hash table to store running sums and their indices.

### Sets

*   **Duplicate Removal:** Removes duplicates from a list using a set.
    *   Leverages the property that sets only contain unique elements.
*   **Unique Character Check:** Checks if all characters in a string are unique.
    *   Uses a set to track seen characters.
*   **Pair Finding:** Finds pairs of numbers (one from each of two arrays) that sum to a target value.
    *   Uses a set for efficient lookup.
*   **Longest Consecutive Sequence:** Finds the length of the longest consecutive sequence in an unsorted array of integers.
    *   Uses a set to optimize runtime.

### Sorting Algorithms for Linked Lists

*   **Bubble Sort:** Sorts a linked list in ascending order by repeatedly comparing and swapping adjacent elements.
*   **Selection Sort:** Sorts a linked list by repeatedly finding the smallest element and swapping it with the first element in the unsorted part of the list.
*   **Insertion Sort:** Sorts a linked list by inserting each element into its correct position in the sorted part of the list.
*   **Merge Sort:** Merges two sorted linked lists into one sorted list.

### Binary Search Trees (BST)

*   **BST Validation:** Checks whether a binary search tree is a valid BST.
    *   Uses in-order traversal to ensure nodes are in ascending order.
*   **Kth Smallest Node:** Finds the kth smallest element in a BST.
    *   Can be solved iteratively using a stack or recursively.

### List Manipulation

*   **Find Max Min:** Finds the maximum and minimum values in a list.
*   **Find Longest String:** Finds the longest string in a list of strings.
*   **Remove Duplicates:** Removes duplicates from a sorted list in-place.
*   **Max Profit:** Calculates the maximum profit that can be made by buying and selling stock at the right time.
*   **Rotate:** Rotates a list to the right by k steps.

## Questions and Solutions
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