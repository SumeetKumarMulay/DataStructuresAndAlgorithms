"""
Write a function called stringifyNumbers which accepts an object, converts all the numbers in 
the object to string and leaves everything else as is. It is import to note that the structure 
of the object should be preserved.

"""


def stringify_numbers(input_arr: dict) -> dict:
    """
    Stringify objects
    """

    def helper(ip: dict) -> dict:
        new_obj = {}
        for values in ip:
            if isinstance(ip[values], dict) and not isinstance(ip[values], list):
                new_obj[values] = helper(ip=ip[values])
            elif isinstance(ip[values], int):
                new_obj[values] = str(ip[values])
            else:
                new_obj[values] = ip[values]
        return new_obj

    return helper(ip=input_arr)
