class Node:
    # node for BST
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
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

    def insert(self, value):
        """
        Inserts a value into the Binary Search Tree (BST).
        Args:
            value: The value to be inserted into the BST.
        Returns:
            bool: True if the value was successfully inserted, False if the value already exists in the BST.
        Pseudo Code:
        1. Create a new node with the given value.
        2. If the BST is empty (root is None):
            a. Set the root to the new node.
            b. Return True.
        3. Initialize a temporary node (temp) to the root for traversal.
        4. While True:
            a. If the value of the new node is equal to the value of the temp node:
                i. Return False (duplicate value).
            b. If the value of the new node is less than the value of the temp node:
                i. If the left child of the temp node is None:
                    - Set the left child of the temp node to the new node.
                    - Return True.
                ii. Otherwise, set temp to the left child of the temp node.
            c. If the value of the new node is greater than the value of the temp node:
                i. If the right child of the temp node is None:
                    - Set the right child of the temp node to the new node.
                    - Return True.
                ii. Otherwise, set temp to the right child of the temp node.
        """

        new_node = Node(value)
        if self.root is None:  # if there is no node in BST
            self.root = new_node
            return True
        temp = self.root  # start with root node for traversal

        while True:
            if (
                new_node.value == temp.value
            ):  # check if given value is equal to value of the node i.e duplicate nodes
                return False
            if new_node.value < temp.value:  # go left
                if temp.left is None:  # check if the left spot is already open
                    temp.left = new_node
                    return True
                temp = temp.left  # assign left node as temp if spot not open
            else:  # go right
                if temp.right is None:
                    temp.right = new_node  # check if the right spot is already open
                    return True
                temp = temp.right  # assign right node as temp if spot not open

    def contains(self, value):
        """
        Check if the tree contains a specific value.
        Args:
            value: The value to search for in the tree.
        Returns:
            bool: True if the value is found in the tree, False otherwise.
        Pseudocode:
        1. Start at the root of the tree.
        2. While the current node is not None:
            a. If the current node's value is equal to the target value:
                i. Return True.
            b. If the target value is less than the current node's value:
                i. Move to the left child of the current node.
            c. If the target value is greater than the current node's value:
                i. Move to the right child of the current node.
        3. If the loop ends without finding the value, return False.
        """
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def dfs_in_order(self):
        result = []

        def traverse(node: Node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return result

    def is_valid_bst(self):
        """
        Checks if the binary tree is a valid Binary Search Tree (BST).
        A binary tree is a BST if:
        - All nodes in the left subtree have values less than the node's value
        - All nodes in the right subtree have values greater than the node's value
        - Both left and right subtrees are also BSTs
        Logic:
        1. Gets inorder traversal of tree which gives sorted array for valid BST
        2. Checks if array is strictly increasing (each element greater than previous)
        3. Returns False if any violation found, True if entire array is valid
        Returns:
            bool: True if tree is valid BST, False otherwise
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n) for storing inorder traversal array
        """

        sorted_values = self.dfs_in_order()
        for i in range(1, len(sorted_values)):
            if sorted_values[i - 1] >= sorted_values[i]:
                return False
        return True


bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(3)
bst.insert(5)

bst.print_tree()
print(bst.is_valid_bst())
