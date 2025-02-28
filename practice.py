class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


arr = LinkedList(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
print(arr.find_middle_node().value)
