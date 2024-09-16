"""
Write a function which accepts an object, it should then go through an object to check and see
if the values are of type string. If they are string it should then put it in a list. Once the 
function has collected all the strings in the object it should return the array 
"""


def collectStrings(input: dict) -> list[str]:
    newArr = []
    
    def helper(ip: dict) -> list[str]: 
        nonlocal newArr
        for keys in ip:
            if isinstance(ip[keys], dict):
                helper(ip=ip[keys])
            elif isinstance(ip[keys], str):
                newArr.append(ip[keys])

        return newArr
    
    return helper(ip=input)