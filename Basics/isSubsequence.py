"""
Write a function that takes in two string. The function should then compair 
the order of the two strings if the order of the two string are the same 
should return true else it should return false. 

For example: {'abc', 'adbc'} = true 
             {'hello', 'hello world'} = true
             {'abc', 'acb'} = false   
"""

def isSubsequence(first_str: str, second_str: str) -> bool: 
    if len(first_str) == 0 or len(second_str) == 0:
        print("this")
        return False
    # pointers
    pointer1 = 0
    # we need to check the order only in the second string
    for char in second_str:
        # check if the first string char matches the second string if so
        # continue by increating the pointer1 by 1. then check the second 
        # condition if the point1 is not equal to the len of first string
        # then continue the loop.  

        if first_str[pointer1] == char:
            pointer1 += 1
            if pointer1 == len(first_str):
                return True

    return False


