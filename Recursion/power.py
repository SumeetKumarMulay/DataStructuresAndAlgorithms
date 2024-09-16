"""
Write a function called power. This function accepts two variable the first
is the base and the second is the exponent. The function should replicate the
function Math.pow(). 

Example power(2, 0) = 0
        power(2, 2) = 4
"""


def power(base: int, exponent: int) -> int:
    if exponent == 1:
        return base
    elif exponent < 0:
        return 1 / power(base=base, exponent=-exponent)
    else:
        exponent -= 1
        return base * power(base=base, exponent=exponent)
