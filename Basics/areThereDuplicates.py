from test_data.test_data import longList

"""
Write a function with accepts a variable number of arguments, and checks 
wether there are any duplicates amount them. And returns true if there are 
and returns false if there arn't. 
"""


def areThereDuplicates(input_list: list[any]) -> bool:
    pointer1 = 0
    pointer2 = 1
    if len(input_list) > 1:
        input_list.sort()
        if input_list[pointer1] != input_list[pointer2]:
            input_list.pop(pointer1)
            return areThereDuplicates(input_list=input_list)
        else:
            return True
    else:
        return False


