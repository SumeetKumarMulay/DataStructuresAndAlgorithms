"""
Write a function called stringifyNumbers which accepts an object, converts all the numbers in 
the object to string and leaves everything else as is. It is import to note that the structure 
of the object should be preserved.

"""

def stringifyNumbers(input: dict) -> dict: 
    def helper(ip: dict) -> dict:
        newObj = {}
        for values in ip:
            if isinstance(ip[values], dict) and type(ip[values]) != list: 
                newObj[values] = helper(ip=ip[values])
            elif isinstance(ip[values], int):
                newObj[values] = str(ip[values])
            else: 
                newObj[values] = ip[values]
        return newObj

    return helper(ip=input)
