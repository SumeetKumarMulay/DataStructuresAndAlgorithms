"""
NOTE - A recursive function is a function that calls itself. The only thing that change is its input.
There are two most important things in recursion: 1. A base case -> This is case where the 
function end. 2. The changing input-> This is obvious.

"""

def countDown(num: int)-> str:
    if num <= 0:
        return "All Done"
    else:
        print(num)
        num -= 1
        return countDown(num=num)
    