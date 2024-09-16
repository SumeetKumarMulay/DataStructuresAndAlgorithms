"""
Write a function that accepts an array and a value. Then go through the entire array and see if
there is an item in the array which is equal to the values provided. If this is the cause then
return the index else return -1. 
"""


def LinearSearch(array: list, values) -> int:
    index_count = 0

    def helper(ipArr: list, value):
        nonlocal index_count
        if len(ipArr) == 0:
            return -1
        if ipArr[0] == value:
            return index_count
        else:
            index_count += 1
            return helper(ipArr=ipArr[1:], value=value)

    return helper(ipArr=array, value=values)
