"""
Write a function which returns the nth number in the fibonacci sequence. 

"""


def fib(num: int) -> int:
    """
    gives fibonacci numbers
    """
    if num <= 2:
        return 1
    return fib(num=num - 1) + fib(num=num - 2)


def fib_memo(num: int, memo: dict = None):
    """
    This is a simple fib function which uses the concept of memoization where calculated values
    are stored in a simple list called memo and num represent the n in fib(n).
    Args:
        num (int): This the n in fib(n)
        memo (list, optional): This is a memo

    Returns:
        int.
    """
    if memo is None:
        memo = {}
    if num in memo:
        return memo[num]
    if num <= 2:
        return 1
    result = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
    memo[num] = result
    return result


def fib_tabulation(num: int):
    """
    This function calculates fib sequence using the tabulation method.
    Stack does not overflow in this method but it is also fast. 
    Args:
        num (int): number you want to use.

    Returns:
        int
    """
    if num <= 2:
        return 1
    fib_nums = [0, 1, 1]
    for i in range(3, num + 1):
        res = fib_nums[i - 1] + fib_nums[i - 2]
        fib_nums.append(res)
    return fib_nums[num]
