"""This is the doublylinkedlist data structure"""
from typing import Union


class Node:
    """This class represents the node structure of a doubly linked list class"""

    def __init__(self, value):
        self.value = value
        self.next_node: Union[Node, None] = None
        self.previous_node: Union[Node, None] = None


class DoublyLinkedList:
    """This is a doublylinkedclass and all its methods"""

    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None
        self.length: int = 0

    def push(self, value):
        """The function pushes new data into the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """The functin pops the last node on the list and returns it."""
        if self.length == 0:
            return None
        current_tail = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = current_tail.previous_node
            current_tail.previous_node = None
            self.tail.next_node = None
        self.length -= 1
        return current_tail

    def shift(self):
        """The function pops the head of the list and returns it."""
        if self.length == 0:
            return None
        current_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current_head.next_node
            self.head.previous_node = None
            current_head.next_node = None
        self.length -= 1
        return current_head

    def unshift(self, value):
        """This function add a new value to the head of the list."""
        new_node = Node(value)
        if self.length == 0:
            return self.push(value)
        else:
            old_head = self.head
            old_head.previous_node = new_node
            new_node.next_node = old_head
            self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        """This function gets the node at the index provided"""
        if (self.length == 0 or index < 0 or index > self.length):
            return None
        half_way = self.length // 2
        if index <= half_way:
            current = self.head
            c_idx = 0
            while c_idx != index:
                current = current.next_node
                c_idx += 1
        if index > half_way:
            current = self.tail
            c_idx = self.length - 1
            while c_idx != index:
                current = current.previous_node
                c_idx -= 1
        return current

    def set(self, index, value):
        """This function updates a value at a given index."""
        update_node = self.get(index)
        if update_node is None:
            return False
        update_node.value = value
        return True

    def insert(self, index, value):
        "This function inserts a new node at a given index."
        if (index < 0 or index >= self.length):
            return False
        if index == 0:
            return bool(self.unshift(value))
        if index == self.length:
            return bool(self.push(value))
        pre_node = self.get(index - 1)
        post_node = pre_node.next_node
        new_node = Node(value)
        pre_node.next_node = new_node
        new_node.previous_node = pre_node
        post_node.previous_node = new_node
        new_node.next_node = post_node
        self.length += 1
        return True

    def remove(self, index):
        """This function remove node at a given index"""
        if (index < 0 or index >= self.length):
            return False
        if index == 0:
            return bool(self.shift())
        if index == self.length - 1:
            return bool(self.pop())
        remove_node = self.get(index)
        before_node = remove_node.previous_node
        after_node = remove_node.next_node
        before_node.next_node = after_node
        after_node.previous_node = before_node
        remove_node.previous_node = None
        remove_node.next_node = None
        self.length -= 1
        return remove_node

    def print_fw(self):
        """this function prints the values going forward"""
        current = self.head
        while current:
            print(current.value)
            current = current.next_node

    def print_bw(self):
        """This function prints the values going backward"""
        current = self.tail
        while current:
            print(current.value)
            current = current.previous_node
