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


arr = LinkedList(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)


arr.tail.next = arr.head.next
print(arr.has_loop())
