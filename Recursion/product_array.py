"""
Write a function which accepts an array and returns the product of the array.
for example: [1, 2, 3] = 6
"""

def product_array(input: list[int]) -> int: 
    if len(input) == 0:
        return 1 
    else: 
        return input[0] * product_array(input=input[1:])