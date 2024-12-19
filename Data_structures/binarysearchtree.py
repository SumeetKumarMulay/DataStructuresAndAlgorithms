"""

This is a binary search tree data structure. Like a tree it has roots and nodes however, 
unlike a normal tree its is a binary tree which mean each root can only have two nodes attached
to it. Furthermore, this is a binary search tree which means it is sorted this means that 
any values greater than the root are stored to the right side of the tree and any values 
less than are stored in the left side.

"""

from typing import Union, Any


class Node:
    """This is the node class and contains the data that needs to be stored inside the tree."""

    def __init__(self, value):
        self.value: Any = value
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None


class BinarySearchTree:
    """This is the Binary Search tree with all its data structures."""

    def __init__(self):
        self.root: Union[Node, None] = None

    def insert(self, value):
        """
        This inserts a value into a binary search tree using while loop

        Args:
            value (Any): any value to be inserted 

        Returns:
            self: Binary Search tree
        """
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return self
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                current_node = current_node.right
            if value == current_node.value:
                return self

    def insert_rec(self, value):
        """
        This function inserts a values in a binary search tree
        Args:
            value (Any): value to be stored

        Returns:
            _type_: _description_
        """
        new_node = Node(value)

        def _loop(node: Node):
            nonlocal new_node
            if new_node.value == node.value:
                return self
            # go right
            if new_node.value > node.value:
                if node.right is None:
                    node.right = new_node
                else:
                    _loop(node.right)
            # go left
            elif new_node.value < node.value:
                if node.left is None:
                    node.left = new_node
                else:
                    _loop(node.left)

        if self.root is None:
            self.root = new_node
        else:
            _loop(self.root)
        return self

    def contains(self, value) -> bool:
        """
        This function finds a value in a BST.
        Args:
            value (Any): Data you are looking for

        Returns:
            bool: True if the value exist else false 
        """
        if self.root is None:
            return False
        current_node = self.root
        while True:
            if value == current_node.value:
                return True
            if value < current_node.value:
                if current_node.left is None:
                    return False
                current_node = current_node.left
            if value > current_node.value:
                if current_node.right is None:
                    return False
                current_node = current_node.right

    def breath_first_search(self) -> list:
        """
        This function does a breath fist search of the tree.
        Returns:
            list: list of all the values in the tree.
        """
        final_list = []
        if self.root is None:
            return final_list

        queue: list[Node] = []
        queue.append(self.root)
        while len(queue) != 0:
            current_node = queue[0]
            queue.pop(0)
            final_list.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return final_list

    def inorder(self, node: Node):
        """This function is used to print binary tree"""
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)
