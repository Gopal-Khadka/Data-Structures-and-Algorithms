class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        self.height = 0
        self.top = None
        if value is not None:
            new_node = StackNode(value)
            self.top: StackNode = new_node
            self.height += 1

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


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value=None):
        self.stack1 = Stack()
        self.stack2 = Stack()
        if value is not None:
            self.stack1.push(value)
            self.length = self.stack1.height

    def print_queue(self):
        self.stack1.print_stack()

    def enqueue_using_stacks(self, value):
        """
        Enqueues a value into a queue implemented using two stacks.
        This method implements queue's enqueue operation using two stacks (stack1 and stack2).
        The implementation follows these steps:
        1. Transfers all elements from stack1 to stack2
        2. Pushes the new value to the now-empty stack1
        3. Transfers all elements back from stack2 to stack1
        This ensures that the oldest elements remain at the top of stack1,
        maintaining FIFO (First In First Out) queue behavior.
        Args:
            value: The value to be added to the queue
        Time Complexity: O(n) where n is the number of elements in the queue
        Space Complexity: O(n) for storing elements in the stacks
        """

        # All elements are stored in stack1
        # All elements are transferred to stack2
        while self.stack1.height > 0:
            node = self.stack1.pop()
            self.stack2.push(node.value)

        # Append new element to the empty stack1
        self.stack1.push(value)

        # All elements are now stored in stack2
        # All elements are transferred back to stack1
        while self.stack2.height > 0:
            node = self.stack2.pop()
            self.stack1.push(node.value)


q = Queue()
q.enqueue_using_stacks(1)
q.enqueue_using_stacks(2)
q.enqueue_using_stacks(3)
q.enqueue_using_stacks(4)
q.enqueue_using_stacks(5)
q.print_queue()
