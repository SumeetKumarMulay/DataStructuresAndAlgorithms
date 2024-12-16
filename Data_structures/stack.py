"""
This is a stack implementation using linked list data structure. The stacks are build on the LIFO 
principle
"""

from typing import Union, Any


class Node:
    """This is the data structure in which the data is store."""

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None


class Stack:
    """This is the stack data structure with all its methods."""

    def __init__(self):
        self.first: Union[Node, None] = None
        self.last: Union[Node, None] = None
        self.size: int = 0

    def push(self, value) -> int:
        """
        This function added values into the stack and return the size of the stack.
        Args:
            value (Any): value that needs to be stored inside the stack.

        Returns:
            int: The size of the stack.
        """
        new_node: Node = Node(value)
        if self.first is None and self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            current_first = self.first
            self.first = new_node
            new_node.next = current_first
        self.size += 1
        return self.size

    def pop(self) -> Any:
        """
        This function returns the first values stored in the node. 
        Returns:
            Any: The first value stored in the stack and can be of "Any" Type.
        """
        if self.first is None:
            return None
        return_node = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = return_node.next
            self.size -= 1
        return return_node.value
