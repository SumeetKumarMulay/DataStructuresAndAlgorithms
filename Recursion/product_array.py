"""
Write a function which accepts an array and returns the product of the array.
for example: [1, 2, 3] = 6
"""


def product_array(input_arr: list[int]) -> int:
    """
    products all values in the array
    """
    if len(input_arr) == 0:
        return 1
    else:
        return input_arr[0] * product_array(input_arr=input_arr[1:])
