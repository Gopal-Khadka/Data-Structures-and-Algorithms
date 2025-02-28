class Node:
    # node for BST
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # Implementation of BST using recursion
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.root = new_node
        else:
            self.root = None

    def print_tree(self):
        """
        Prints the Binary Search Tree (BST) in a structured format.
        """

        def _print_tree(node, level=0):
            if node is not None:
                _print_tree(node.right, level + 1)
                print(" " * 4 * level + "->", node.value)
                _print_tree(node.left, level + 1)

        _print_tree(self.root)

    def __r_contains(self, current_node: Node | None, value):
        """
        Recursively checks if a value exists in the binary search tree.
        Args:
            current_node (Node | None): The current node being checked.
            value: The value to search for in the tree.
        Returns:
            bool: True if the value is found, False otherwise.
        Pseudocode:
        1. If current_node is None, return False (base case).
        2. If value is equal to current_node.value, return True.
        3. If value is less than current_node.value, recursively call __r_contains on the left child.
        4. If value is greater than current_node.value, recursively call __r_contains on the right child.
        """

        if current_node == None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node | None, value):
        """
        Recursively inserts a value into the Binary Search Tree (BST).
        Args:
            current_node (Node | None): The current node in the BST where the value is to be inserted.
            value: The value to be inserted into the BST.
        Returns:
            Node: The node after insertion.
        Pseudocode:
        1. If current_node is None:
            a. Create and return a new Node with the given value.
        2. If value is less than current_node.value:
            a. Recursively call __r_insert on the left child of current_node.
            b. Assign the result to current_node.left.
        3. If value is greater than current_node.value:
            a. Recursively call __r_insert on the right child of current_node.
            b. Assign the result to current_node.right.
        4. Return the current_node.
        """

        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        # if BST is empty
        if self.root == None:
            self.root = Node(value)
        # if BST is not empty (Note that this code doesn't run for empty BST)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        """
        Find the minimum value in a Binary Search Tree (BST).
        This function traverses the left subtree of the given node to find the node
        with the smallest value, as the smallest value in a BST is always located
        in the leftmost node.
        Args:
            current_node (TreeNode): The root node of the BST or subtree.
        Returns:
            int: The value of the leftmost (minimum) node in the BST.
        """

        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node: Node | None, value):
        """
        Deletes a node with the given value from the binary search tree.
        Args:
            current_node (Node | None): The current node in the tree.
            value: The value to be deleted from the tree.
        Returns:
            Node | None: The new root of the subtree after deletion.
        Pseudocode:
        1. If current_node is None, return None (base case).
        2. If value is less than current_node.value, recursively call __delete_node on the left subtree.
        3. If value is greater than current_node.value, recursively call __delete_node on the right subtree.
        4. If value is equal to current_node.value:
            a. If current_node is a leaf node (no children), return None.
            b. If current_node has only a right child, replace current_node with its right child.
            c. If current_node has only a left child, replace current_node with its left child.
            d. If current_node has both children:
                i. Find the minimum value in the right subtree.
                ii. Replace current_node's value with the minimum value.
                iii. Recursively call __delete_node on the right subtree to delete the node with the minimum value.
        5. Return the current_node.
        """

        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:  # Main code to delete the node
            if (
                current_node.left == None and current_node.right == None
            ):  # current node is a leaf node(no child)
                return None
            elif current_node.left == None:  # node has only right child
                current_node = current_node.right
            elif current_node.right == None:  # node has only left child
                current_node = current_node.left
            else:  # Node has both right and left child
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    def BFS(self):
        """
        Performs a Breadth-First Search (BFS) traversal of the binary tree.
        BFS explores all nodes at the present depth before moving on to nodes at the next depth level.
        The traversal uses a queue data structure to track nodes to visit.
        Returns:
            list: A list containing the values of all nodes in the tree in BFS order,
                  visiting each level from left to right before moving to the next level.
        Time Complexity: O(n) where n is the number of nodes in the tree
        Space Complexity: O(w) where w is the maximum width of the tree
        Example:
            If tree is:
             -   2
             -  / \\
             - 1   3
            - BFS() returns [2, 1, 3]
        """

        current_node = self.root
        queue: list[Node] = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        """
        Performs a Depth-First Search (DFS) Pre-order traversal on the binary tree.
        Pre-order traversal visits nodes in the following order:
        1. Root node
        2. Left subtree
        3. Right subtree
        Returns:
            list: A list containing node values in pre-order traversal order.
        Example:
            For a tree:
            -     1
            -    / \\
            -   2   3
            - / \\
            - 4   5
            - Returns: [1, 2, 4, 5, 3]
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree due to recursion stack
        """

        results = []
        current_node = self.root

        def traverse(current_node: Node):
            """
            Performs a pre-order traversal of a binary tree.
            This recursive function visits the current node first, then traverses the left subtree,
            and finally traverses the right subtree. The values of visited nodes are stored in
            the results list.
            Args:
                current_node (Node): The current node being processed in the traversal.
                                    Must be of type Node with attributes: value, left, right.
            Note:
                - This is a helper function used internally for tree traversal
                - The results list must be defined in the outer scope
                - Assumes Node class has value, left, and right attributes
            """

            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(current_node)
        return results

    def dfs_in_order(self):
        results = []
        current_node = self.root

        def traverse(current_node: Node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(current_node)
        return results

    def dfs_post_order(self):
        results = []
        current_node = self.root

        def traverse(current_node: Node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(current_node)
        return results


bst = BinarySearchTree()

bst.r_insert(10)
bst.r_insert(5)
bst.r_insert(15)
bst.r_insert(3)
bst.r_insert(7)
bst.r_insert(20)

print("Printing Tree...",end="\n\n")
bst.print_tree()
print("----------")
# print(bst.BFS())
print("Pre order DFS traversal: ", bst.dfs_pre_order())
print("In order DFS traversal: ", bst.dfs_in_order())
print("Post order DFS traversal: ", bst.dfs_post_order())
