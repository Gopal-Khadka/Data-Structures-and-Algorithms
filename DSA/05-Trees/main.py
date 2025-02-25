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

    # TODO: Construct this function
    def remove(self, value):
        """
        Removes a node with the specified value from the tree.
        Algorithm:
        1. If the tree is empty, return None.
        2. Find the node to be removed and its parent node.
        3. If the node to be removed has no children, simply remove it.
        4. If the node to be removed has one child, replace it with its child.
        5. If the node to be removed has two children:
           a. Find the in-order successor (smallest node in the right subtree).
           b. Replace the value of the node to be removed with the in-order successor's value.
           c. Recursively remove the in-order successor.
        6. Return the updated tree.
        Args:
            value (int): The value to be removed from the tree.
        Returns:
            None
        """

        pass


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(3)
    bst.insert(5)

    print(bst.contains(0))
    bst.print_tree()
