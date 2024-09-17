"""
Write a function called recursive range which accepts an input_arr and adds all the number from 0 
to the input_arr number. Return a sum 

"""


def recursive_range(num: int) -> int:
    """
    return sum
    """
    if num == 0:
        return 0
    else:
        return num + recursive_range(num=num - 1)
