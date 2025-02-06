"""priorityqueue.py"""

import math
from typing import Any


class Node:
    """This is the node class which is used as an item in the priority queue class"""

    def __init__(self, value: Any, priority: int):
        self.value = value
        self.priority = priority


class PriorityQueue:
    """This is the priority queue class which is basically a min binary heap"""

    def __init__(self):
        self.values: list[Node] = []

    def enqueue(self, value: Node):
        """
        This adds values based on priority assigned to the nodes. Lowest Fist.
        Args:
            value (Node): The node value that needs to be inserted.

        Returns:
            PriorityQueue: Updated priority queue
        """
        self.values.append(value)
        index = len(self.values) - 1
        element = self.values[index]
        while index > 0:
            parent_index = math.floor((index - 1) / 2)
            parent_value = self.values[parent_index]
            if element.priority >= parent_value.priority:
                break
            self.values[parent_index] = element
            self.values[index] = parent_value
        return self

    def dequeue(self):
        """
        This function return the value with highest priority first. 

        Returns:
            Node: The value with high priority.
        """
        min_val = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = (2 * idx) + 1
            right_child_idx = (2 * idx) + 2
            left_child = None
            right_child = None
            swap = None
            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child.priority < element.priority:
                    swap = left_child_idx
            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((swap is None and right_child.priority < element.priority) or
                        (swap is not None and right_child.priority < left_child.priority)):
                    swap = right_child_idx
            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap
        return min_val
