"""
NOTE - A recursive function is a function that calls itself. The only thing that change is its input.
There are two most important things in recursion: 1. A base case -> This is case where the 
function end. 2. The changing input-> This is obvious.

"""


def count_down(num: int) -> str:
    """3, 2, 1"""
    if num <= 0:
        return "All Done"
    else:
        print(num)
        num -= 1
        return count_down(num=num)
