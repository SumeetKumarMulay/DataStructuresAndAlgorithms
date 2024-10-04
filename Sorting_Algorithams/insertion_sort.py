"""
Write a function which accepts a list of values. Should then form a sorted list on one side
as the function iterates through the list.     
"""


def insertion_sort(values: list[int]) -> list[int]: 
    """
    This function returns a sorted list of values.

    Args:
        values (list[int]): input list. 

    Returns:
        list[int]: Returns a list of sorted list of values.
    """
    n = len(values)
    if n <= 1:
        return values

    for j in range(1, n):
        current_value = values[j]
        i = j - 1
        #print(f"arr start: {values}")
        #print(f"current values: {current_value}, i: {i}")
        while i >= 0 and current_value < values[i]:
            values[i+1] = values[i]
            i -= 1
            #print(f"arr before: {values}, i {i}, current_value: {current_value}")
        values[i + 1] = current_value
        #print(f"arr after: {values}")

    return values
