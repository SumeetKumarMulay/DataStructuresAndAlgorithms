"""
Write a function that accepts a list of strings and capitalizes the first 
letter of everyword in the array and returns a new array with the updated 
strings. 
"""


def capitalize_first(input_arr: list[str]) -> list[str]:
    """
    only capitalizes the first letters.
    """
    new_arr = []

    def helper(ip: list[str]) -> list[str]:
        nonlocal new_arr
        if len(ip) == 0:
            return new_arr
        else:
            updated = ip[0].capitalize()
            new_arr.append(updated)
            return helper(ip=ip[1:])

    return helper(ip=input_arr)
