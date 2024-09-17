"""
Write a function which returns the nth number in the fibonacci sequence. 

"""


def fib(num: int) -> int:
    """
    gives fibonacci numbers
    """
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fib(num=num - 1) + fib(num=num - 2)
