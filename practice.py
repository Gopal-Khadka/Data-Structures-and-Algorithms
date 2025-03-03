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

    def pop(self):
        """Remove last node and return the node"""
        # The traversal to find the second-to-last node in pop() is a linear operation.
        # You may want to consider optimizations like maintaining a pointer to the second-to-last node.

        # check if the list is empty
        if self.length == 0:
            return None

        temp = self.head
        # check if list has only 1 item
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = self.head
            while temp.next is not None:
                prev_node = temp
                temp = temp.next
            self.tail = prev_node  # point tail to second last node
            self.tail.next = None  # point next of present tail to None
        self.length -= 1
        return temp

    def prepend(self, value):
        """Add the given value node in the beginning of the linked list"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Pop the first node of the list and return the node"""
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """Returns the value at given index of the linked list"""
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """Set the given value at the given index node"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert the value at given index of the list"""
        if index > self.length or index < 0:
            return None

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)  # get previous node i.e. node at (index-1)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        """ "Remove the node at given index and return boolean"""
        if index < 0 or index >= self.length:
            return None

        if index == 0:  # for first node
            return self.pop_first()
        if index == self.length - 1:  # for last node
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next  # get node at given index
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

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


ll = LinkedList(1)
ll.append(5)
ll.append(-3)
ll.append(25)
ll.append(10)

print("Before Sorting: ", end="")
ll.print_list()
ll.bubble_sort()
print(ll.tail.value)
print("After Sorting: ", end="")
ll.print_list()
