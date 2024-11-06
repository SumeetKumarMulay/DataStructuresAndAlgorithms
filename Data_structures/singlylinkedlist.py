"""This is the singly linked list datastucture"""
from typing import Union


class Node:
    """This is that node that contains data in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None


class SinglyLinkedList:
    """
    This is a singlylinked list data structure. This data structure is made of nodes 
    each node contains data and the next node. The structure itself keeps track of the 
    head tail and the length.
    """

    def __init__(self):
        self.tail: Union[Node, None] = None
        self.head: Union[Node, None] = None
        self.length: int = 0

    def push(self, value):
        """
        This function create a new node with the data provided and adds to the Singly linked
        list
        """
        new_data = Node(value=value)
        if self.head is None and self.tail is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next = new_data
            self.tail = new_data
        self.length += 1
        return self

    def pop(self):
        """This function removes the last node from the linked list."""
        if self.length == 0:
            return None
        current = self.head
        pre = current
        while current.next:
            pre = current
            current = current.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        """This function shifts the head by one place or removes a node from the top"""
        if self.length == 0:
            return None
        current_head = self.head
        new_head = current_head.next
        self.head = new_head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_head

    def unshift(self, value):
        """This function adds new node at the top of the list."""
        new_data = Node(value)
        if self.head is None:
            self.push(value)
            return self
        else:
            new_data.next = self.head
            self.head = new_data
        self.length += 1
        return self

    def get(self, index):
        """The function gets a node at a specific index."""
        if (index < 0 or index >= self.length):
            return None
        c_idx = index
        current = self.head
        while c_idx > 0:
            current = current.next
            c_idx -= 1
        return current

    def set(self, index, value):
        """This function sets the value at a specific position in the list."""
        update_node = self.get(index)
        if update_node is None:
            return False
        update_node.value = value
        return True

    def insert(self, index, value):
        """This function inserts a node at the specified index"""
        if (index < 0 or index > self.length):
            return False
        if index == self.length:
            return bool(self.push(value))
        if index == 0:
            return bool(self.unshift(value))
        previous_node = self.get(index - 1)
        new_node = Node(value=value)
        if previous_node is not None:
            temp_next = previous_node.next
            previous_node.next = new_node
            new_node.next = temp_next
            self.length += 1
            return True
        return False

    def remove(self, index):
        """This function removes a node at a specific position"""
        if (index < 0 or index > self.length):
            return False
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.shift()
        previous_node = self.get(index - 1)
        temp_nxt = previous_node.next
        previous_node.next = temp_nxt.next
        self.length -= 1
        return temp_nxt

    def reverse(self):
        """This function reverses a singly linked list"""
        if self.length == 0:
            return None

        node = self.head
        self.head, self.tail = self.tail, self.head
        previous_node = None
        for _ in range(self.length):
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node
        return self

    def print(self):
        """This function just prints all the values in the list"""
        current = self.head
        while current:
            print(current.value)
            current = current.next
