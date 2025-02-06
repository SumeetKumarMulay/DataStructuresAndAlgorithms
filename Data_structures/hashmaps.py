"""hashmaps"""


import json
from typing import Any


def simple_hash(key: str, length: int) -> int:
    """
    This is a simple hash function. IT has linear time complexity
    Args:
        key (str): String you want to convert
        length (int): Length of the array you want to store it at

    Returns:
        int: The hashed value.
    """
    total = 0
    for alp in key:
        value = ord(alp[0]) - 96
        total = (total + value) % length
    return total


def simple_improved_hash(key: str, length: int) -> int:
    """
    Here we are limiting the length of the key and using a prime number to 
    limit the collision that can happen.
    Args:
        key (str): String you want to convert.
        length (int): Length of the array

    Returns:
        int: The hashed value.
    """
    total = 0
    prime_number = 27
    for i in range(min(len(key), 100)):
        char = key[i]
        value = ord(char[0]) - 96
        total = (total * prime_number + value) % length
    return total


class HashMaps:
    """
    This is hashmaps data structure.
    """

    def __init__(self, size: int = 10):
        self.keymap = [[] for i in range(size)]

    def _hash(self, key: str) -> int:
        """
        Here we are limiting the length of the key and using a prime number to 
        limit the collision.
        Args:
            key (str): String you want to convert.
            length (int): Length of the array

        Returns:
            int: The hashed value.
        """
        total = 0
        prime_number = 31
        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char[0]) - 96
            total = (total * prime_number + value) % len(self.keymap)
        return total

    def set(self, key: str, value: Any):
        """
        This function sets the key value pair into a map.
        We are using separate chaining to store values into
        the map. 

        If same keys is use value is updated or overwritten.

        Args:
            key (str): User defined key
            value (Any): Value that needs to be store.
        """
        index = self._hash(key)
        index_val = self.keymap[index]
        if len(index_val) > 0:
            for i in range(len(index_val)):
                if index_val[i][0] == key:
                    index_val[i][1] = value
                    return self

        self.keymap[index].append([key, value])
        return self

    def get(self, key: str):
        """
        This function gets values stored in the hashmap.  
        Args:
            key (str): Key of the value you want to retrieve. 

        Returns:
            Any: value
        """
        index = self._hash(key)
        index_val = self.keymap[index]
        if len(index_val) == 0:
            return None
        if len(index_val) == 1:
            return index_val[0]
        for i in range(len(index_val)):
            if index_val[i][0] is key:
                return index_val[i][1]
        return None

    def values(self):
        """
        This function gets all the values in the hash map.
        return only 1 unique occurrence of a value. 

        Returns:
            list: of all the values. 
        """
        values_arr = []
        for i in range(len(self.keymap)):
            if len(self.keymap[i]) > 0:
                for j in range(len(self.keymap[i])):
                    if self.keymap[i][j][1] not in values_arr:
                        values_arr.append(self.keymap[i][j][1])

        return values_arr

    def keys(self):
        """
        This function gets all the key in the hash map.
        return only 1 unique occurrence of a key. 

        Returns:
            list: of all the keys. 
        """
        values_arr = []
        for i in range(len(self.keymap)):
            if len(self.keymap[i]) > 0:
                for j in range(len(self.keymap[i])):
                    if self.keymap[i][j][0] not in values_arr:
                        values_arr.append(self.keymap[i][j][0])

        return values_arr
