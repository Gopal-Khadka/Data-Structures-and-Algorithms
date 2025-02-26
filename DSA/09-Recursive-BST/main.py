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


bst = BinarySearchTree()


# bst.r_insert(52)
# bst.r_insert(27)
# bst.r_insert(82)

bst.r_insert(47)
bst.r_insert(21)
bst.r_insert(76)
bst.r_insert(18)
bst.r_insert(27)
bst.r_insert(52)
bst.r_insert(82)

# print("BST contains 27: ", end="")
# print(bst.r_contains(27))

# print("BST contains 50: ", end="")
# print(bst.r_contains(50))

print("Before deletion:")
bst.print_tree()

bst.delete_node(47)
print("---------------------")

print("After deletion:")
bst.print_tree()