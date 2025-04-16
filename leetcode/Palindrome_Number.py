"""Link: {https://leetcode.com/problems/palindrome-number/description/}"""


def is_palindrome(x: int) -> bool:
    """t"""
    x = str(x)
    i = 0
    j = len(x) - 1

    while i < j:
        print([x[i], x[j]])
        if x[i] != x[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
