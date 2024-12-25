# Data Structures and Algorithms in Python

This repository provides a detailed overview and implementation of common **Data Structures and Algorithms (DSA)** in Python. Each section includes explanations, Python code examples, and real-life analogies to help understand these concepts better.

---

## Table of Contents

- [Big O Notation](#big-o-notation)
- [Linked Lists](#linked-lists)
- [Double Linked Lists](#double-linked-lists)
- [Stacks and Queues](#stacks-and-queues)
- [Trees](#trees)
- [Hashtables](#hashtables)
- [Graphs](#graphs)
- [Recursion](#recursion)
- [Recursive BST](#recursive-bst)
- [Sorting](#sorting)
- [Tree Traversal](#tree-traversal)

---

## Big O Notation

**Big O notation** is used to describe the efficiency of an algorithm in terms of time and space. It helps us understand the worst-case scenario for an algorithm's performance.

### Common Big O Complexities:
- **O(1)**: Constant time - The operation takes the same amount of time, no matter the input size.
- **O(n)**: Linear time - The operation scales linearly with the input size.
- **O(n²)**: Quadratic time - The operation scales with the square of the input size.
- **O(log n)**: Logarithmic time - The operation time decreases as input size grows.

### Example:

```python
# O(1) - Constant time complexity
def constant_time_example(arr):
    return arr[0]

# O(n) - Linear time complexity
def linear_time_example(arr):
    for i in arr:
        print(i)
```

---

## Linked Lists

A **linked list** is a linear data structure where each element is a separate object. Each element (node) contains data and a reference to the next node in the sequence.

### Real-Life Example:
Think of a train where each car (node) is linked to the next one. The train can move, add or remove cars easily without affecting the entire structure.

### Code Example:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
```

---

## Double Linked Lists

A **double linked list** is similar to a linked list, but each node has two pointers: one pointing to the next node and one pointing to the previous node.

### Real-Life Example:
Imagine a train where you can travel in both directions, either forwards or backwards.

### Code Example:

```python
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
```

---

## Stacks and Queues

- **Stack**: A linear data structure where elements are added and removed in a **Last In, First Out (LIFO)** order.
- **Queue**: A linear data structure where elements are added and removed in a **First In, First Out (FIFO)** order.

### Real-Life Examples:
- **Stack**: A stack of plates where you can only add or remove plates from the top.
- **Queue**: A queue at a bank where the first person in line is the first to be served.

### Code Example:

```python
# Stack implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop() if self.stack else None

# Queue implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
```

---

## Trees

A **tree** is a hierarchical data structure with nodes connected by edges. The topmost node is called the **root**, and each node has zero or more children.

### Real-Life Example:
A family tree is a classic example where one node (person) can have multiple child nodes (children).

### Code Example:

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = new_node
                return
            queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            queue.append(node.right)
```

---

## Hashtables

A **hashtable** is a data structure that maps keys to values using a hash function. It allows fast access to values using the key.

### Real-Life Example:
Think of a dictionary where each word (key) is mapped to its meaning (value).

### Code Example:

```python
class Hashtable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)
```

---

## Graphs

A **graph** is a collection of nodes (vertices) and edges that connect pairs of nodes. Graphs can be **directed** or **undirected** and are used to model relationships in networks.

### Real-Life Example:
A social network is a graph where each person is a node, and friendships are edges between nodes.

### Code Example:

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")
```

---

## Recursion

**Recursion** is a technique where a function calls itself to solve smaller instances of the same problem.

### Real-Life Example:
Think of a Russian doll set. Each doll contains a smaller one, and the process repeats until the smallest doll is reached.

### Code Example:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

---

## Recursive BST

A **Binary Search Tree (BST)** is a tree where each node has at most two children, and the left child is smaller than the parent, while the right child is larger.

### Code Example:

```python
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = BSTNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = BSTNode(data)
```

---

## Sorting

Sorting algorithms arrange elements in a specified order (usually ascending or descending). Common sorting algorithms include **Bubble Sort**, **Merge Sort**, **Quick Sort**, and **Insertion Sort**.

### Code Example (Bubble Sort):

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

---

## Tree Traversal

**Tree Traversal** refers to visiting all the nodes in a tree in a specific order. The common tree traversal methods are **Pre-order**, **In-order**, **Post-order**, and **Level-order**.

### Code Example (In-order Traversal):

```python
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)
```

