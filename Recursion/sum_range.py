"""
Where a function which accepts a number and then all the number before it to until 1. 
So, for example: if number 4 is provided then number 4, 3, 2, 1 are added and the sum is 
returned. 
"""

def sum_range(num: int) -> int:
    # this is the base case
    if num == 1:
        return 1
    else:
        # change the input by reducing number input by one
        return num + sum_range(num - 1)
