"""
Write a function which accepts a list of string and capitalizes all the words in the list and 
returns a new list.
"""

def capitalizeWords(input: list[str]) -> list[str]: 
    newArr = []
    def helper(ip: list[str]) -> list[str]: 
        nonlocal newArr
        if len(ip) == 0: 
            return newArr
        else:
            updated = ip[0].upper()
            newArr.append(updated)
            return helper(ip[1:])
    
    return helper(ip=input)