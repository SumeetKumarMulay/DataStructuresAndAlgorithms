"""
Find the factorial of a given number. 
for example: 2! = 2 * 1 = 2
"""


def factorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num * factorial(num=num - 1)

