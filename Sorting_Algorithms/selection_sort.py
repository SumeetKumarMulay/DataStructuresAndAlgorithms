"""
Implement a algorithm which should sort a list of unsorted integers with minimum 
number of swaps possible.
"""


def selection_sort(values: list[int]) -> list[int]:
    """
    The function returns a sorted array.

    Args:
        values (list[int]): This should be unsorted values.

    Returns:
        list[int]: This a sorted list of values. 
    """
    for i in range(len(values)):
        lowest_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[lowest_index]:
                lowest_index = j
        if i is not lowest_index:
            temp = values[i]
            values[i] = values[lowest_index]
            values[lowest_index] = temp
    return values
