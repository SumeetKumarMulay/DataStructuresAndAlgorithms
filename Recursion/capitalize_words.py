"""
Write a function which accepts a list of string and capitalizes all the words in the list and 
returns a new list.
"""


def capitalize_words(input_arr: list[str]) -> list[str]:
    """
    basicially does .touppercase from JS.
    """
    new_arr = []

    def helper(ip: list[str]) -> list[str]:
        nonlocal new_arr
        if len(ip) == 0:
            return new_arr
        else:
            updated = ip[0].upper()
            new_arr.append(updated)
            return helper(ip[1:])

    return helper(ip=input_arr)
