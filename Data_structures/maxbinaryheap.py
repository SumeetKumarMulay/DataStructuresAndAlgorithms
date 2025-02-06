"""MaxBinaryHeap.py"""

import math


class MaxBinaryHeap:
    """This is the max binary heap class and contains only a list."""

    def __init__(self):
        self.values = []

    def insert(self, value: int):
        """
        This function adds a new value to the binary heap.
        Args:
            value (int): This is the new value that needs to be inserted.

        Returns:
            list: This is the new binary heap
        """
        self.values.append(value)
        index = len(self.values) - 1
        element = self.values[index]
        while index > 0:
            parent_index = math.floor((index - 1)/2)
            parent_value = self.values[parent_index]
            if element <= parent_value:
                break
            self.values[parent_index] = element
            self.values[index] = parent_value
            index = parent_index
        return self

    def extract_max(self):
        """
        This function return the top value in the heap and rearranges the heap
        to become a compact heap.
        Returns:
            int: Max Value
        """
        max_val = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            left_child = None
            right_child = None
            swap = None
            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child > element:
                    swap = left_child_idx
            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((swap is None and right_child > element) or
                        (swap is not None and right_child > left_child)
                        ):
                    swap = right_child_idx
            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

        return max_val
