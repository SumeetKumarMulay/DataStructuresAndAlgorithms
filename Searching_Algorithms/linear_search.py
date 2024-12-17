"""
Write a function that accepts an array and a value. Then go through the entire array and see if
there is an item in the array which is equal to the values provided. If this is the cause then
return the index else return -1. 
"""


def linear_search(array: list, values) -> int:
    """This is a linear search function which is the most basic. We just go through the
    complete array and compair.
    """
    index_count = 0

    def helper(ip_arr: list, value):
        nonlocal index_count
        if len(ip_arr) == 0:
            return -1
        if ip_arr[0] == value:
            return index_count
        else:
            index_count += 1
            return helper(ip_arr=ip_arr[1:], value=value)

    return helper(ip_arr=array, value=values)
