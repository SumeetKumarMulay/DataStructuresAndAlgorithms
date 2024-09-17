"""
Write a function which accepts an object, it should then go through an object to check and see
if the values are of type string. If they are string it should then put it in a list. Once the 
function has collected all the strings in the object it should return the array 
"""


def collect_strings(input_arr: dict) -> list[str]:
    """
    collects string a returns an array
    """
    new_arr = []

    def helper(ip: dict) -> list[str]:
        nonlocal new_arr
        for keys in ip:
            if isinstance(ip[keys], dict):
                helper(ip=ip[keys])
            elif isinstance(ip[keys], str):
                new_arr.append(ip[keys])

        return new_arr

    return helper(ip=input_arr)
