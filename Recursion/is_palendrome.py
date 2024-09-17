"""
Write a function that checks if the string is a palendrone
"""

def is_palendrone(input_arr: str) -> bool:
    """
    checks by reversing the string and compairing it to itself. 
    """
    reverse_str: str = ""

    def reverser(input_arr: str) -> str:
        nonlocal reverse_str
        if len(input_arr) == 0:
            return reverse_str
        else:
            last_letter = input_arr[len(input_arr) - 1]
            reverse_str = reverse_str + last_letter
            return reverser(input_arr=input_arr[:-1])

    reversed_str = reverser(input_arr=input_arr)
    return input_arr == reversed_str
