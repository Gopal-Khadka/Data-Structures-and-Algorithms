class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None


class LinkedList:
    def __init__(self, value):
        """Create new node with given value"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head  # assign head as first node
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next  # assign next value as new node
        print(", ".join(values))

    def append(self, value):
        """Add the node with given value to end of the list and return boolean"""
        new_node = Node(value)
        if self.head is not None:  # or check if length == 0
            # for non-empty list to insert next item
            self.tail.next = new_node
            self.tail = new_node
        else:
            # for empty list to insert first item
            self.head = new_node
            self.tail = new_node
        # self.tail = new_node
        self.length += 1
        return True

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

    def reverse_between(self, m: int, n: int):

        # If the linked list is empty or m==n , then return None.
        if not self.head or m == n:
            return None

        # create a dummy node and connect it to the head.
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # move prev to the node at position m.
        for _ in range(m):
            prev = prev.next

        # set current to the next node of prev.
        current = prev.next

        # Reverse the linked list from position m to n.
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        # update the head of the linked list with the next node of the dummy.
        self.head = dummy.next

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


arr = LinkedList(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)

arr.print_list()

arr.reverse_btn(1, 6)

arr.print_list()
