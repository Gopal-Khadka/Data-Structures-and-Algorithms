class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        # Transfer all elements from stack1 to stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        # Add the new element to the bottom of stack1
        self.stack1.append(value)

        # Transfer all elements back from stack2 to stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()

    def peek(self):
        # Note that position of front and rear is exchanged
        if self.is_empty():
            return None
        return self.stack1[-1]

    def print_queue(self):
        print(self.stack1[::-1])

    def is_empty(self):
        return len(self.stack1) == 0


# Create a new queue
q = MyQueue()


# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.print_queue()

# Output the front of the queue
print("Front of the queue:", q.peek())
q.dequeue()
q.dequeue()

q.print_queue()
print("Front of the queue:", q.peek())
q.dequeue()

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())
