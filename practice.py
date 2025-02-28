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


arr = LinkedList(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)

arr.print_list()
k = 1
print(f"{k}-th node from end: ", arr.kth_node_from_end(k).value)
