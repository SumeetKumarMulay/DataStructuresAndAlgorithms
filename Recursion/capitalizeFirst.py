"""
Write a function that accepts a list of strings and capitalizes the first 
letter of everyword in the array and returns a new array with the updated 
strings. 
"""

def capitalizeFirst(input: list[str]) -> list[str]:
    newArr = []

    def helper(ip: list[str]) -> list[str]:
        nonlocal newArr 
        if len(ip) == 0:
            return newArr
        else:
            updated = ip[0].capitalize()
            newArr.append(updated)
            return helper(ip=ip[1:]) 
    
    return helper(ip=input)
            