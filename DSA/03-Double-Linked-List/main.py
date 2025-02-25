class Node:
    def __init__(self, value):
        self.value = value
        self.prev: Node = None
        self.next: Node = None


class DoublyLinkedList:
    def __init__(self, value):
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
        new_node = Node(value)
        if self.head is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the double linked list.
        Parameters:
        index (int): The position at which the new node should be inserted. Must be between 0 and the current length of the list.
        value (Any): The value to be stored in the new node.
        Returns:
        bool: True if the insertion is successful, None if the index is out of bounds.
        """

        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after

        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the node at the specified index from the double linked list.

        Parameters:
        index (int): The position of the node to be removed. Must be within the range [0, length-1].

        Returns:
        Node: The removed node if the index is valid, otherwise None.

        Notes:
        - If the index is 0, the first node is removed.
        - If the index is length-1, the last node is removed.
        - For other valid indices, the node at the specified index is removed and the list is updated accordingly.
        """
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


if __name__ == "__main__":
    lst = DoublyLinkedList(1)

    lst.append(2)
    lst.append(3)

    lst.append(4)
    lst.pop()

    lst.prepend(0)

    lst.prepend(-1)
    # lst.pop_first()

    lst.set_value(3, 2.5)

    lst.insert(2, 0.75)
    lst.insert(2, 0.5)

    lst.remove(4)
    lst.print_list()
    print("Length: ", lst.length)
