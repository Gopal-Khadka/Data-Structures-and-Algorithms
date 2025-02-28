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


arr = LinkedList(1)
arr.append(2)
arr.append(1)
arr.append(3)
arr.append(4)

arr.print_list()
print("Using set: ")
arr.remove_duplicates()
arr.print_list()


lst = LinkedList(1)
lst.append(2)
lst.append(4)
lst.append(3)
lst.append(4)


lst.print_list()
print("Using no extra DS: ")
lst.remove_duplicates_again()
lst.print_list()
