class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = StackNode(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """
        Pushes a value onto the top of the stack.
        Args:
            value: The value to be pushed onto the stack.
        Returns:
            bool: True if the value was successfully pushed onto the stack.
        """

        new_node = StackNode(value)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        """
        Removes and returns the top element of the stack.
        Returns:
            Node: The node that was removed from the top of the stack.
            None: If the stack is empty.
        """

        if self.height <= 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

    def size(self):
        return self.height

    def empty(self):
        return self.height == 0

    def top(self):
        return self.top


def stack_ops():
    stack = Stack(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print("Popped:", stack.pop().value)

    stack.print_stack()
    print("Height:", stack.height)


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = QueueNode(value)
        self.front = new_node
        self.rear = new_node
        self.length = 1

    def print_queue(self):
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """
        Adds a new node with the given value to the end of the queue.
        Parameters:
        value (any): The value to be added to the queue.
        Returns:
        bool: True if the node is successfully added to the queue.
        """

        new_node = QueueNode(value)
        if self.length == 0:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.length += 1
        return True

    def dequeue(self):
        """
        Removes and returns the front element from the queue.
        If the queue is empty, returns None. If the queue has only one element,
        sets both the front and rear of the queue to None. Otherwise, updates
        the front to the next element in the queue and detaches the removed element.
        Returns:
            The removed element from the front of the queue, or None if the queue is empty.
        """

        if self.length == 0:
            return None
        temp = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = temp.next
            temp.next = None
        self.length -= 1
        return temp


def queue_ops():
    q = Queue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.print_queue()

    print("Length:", q.length)


if __name__ == "__main__":
    # stack_ops()
    queue_ops()
