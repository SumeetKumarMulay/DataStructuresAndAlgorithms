"""
Write a function called nestedEven. The function should look at object which may contain other
objects, list or str it should then add only the even number to and return the sum of all even 
numbers in that list.
"""


def nestedEven(input: dict) -> int:
    op = 0

    def helper(ip: dict) -> int:
        nonlocal op
        for values in ip:
            if isinstance(ip[values], dict):
                helper(ip=ip[values])
            elif isinstance(ip[values], int) and ip[values] % 2 == 0:
                op += ip[values]
        return op

    return helper(ip=input)
