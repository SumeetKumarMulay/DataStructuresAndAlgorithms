"""This is the queues data structure"""

from typing import Union, Any


class Node:
    """This is the node structure which contains all the values saved in the queues"""

    def __init__(self, value):
        self.value: Any = value
        self.next: Union[Node, None] = None


class Queues:
    """This is the queues data structure and all its methods"""

    def __init__(self):
        self.first: Union[Node, None] = None
        self.last: Union[Node, None] = None
        self.size: int = 0

    def enqueue(self, value) -> int:
        """
        This function add values to the queues
        Args:
            value (_type_): This is the data you want to put into the queues.

        Returns:
            int: The size of the queue.
        """
        new_node = Node(value)
        if self.last is None and self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self.size

    def dequeue(self) -> Any:
        """
        This return the values from start of queues
        Returns:
            Any: This values stored starting from the first node.
        """
        if self.first is None:
            return None
        current_first = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = current_first.next
        self.size -= 1
        return current_first.value
