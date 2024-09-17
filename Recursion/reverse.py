"""
Write a function called reverse, it accpets a string and reverses it. 
Example: "Sumeet" = "teemuS"
"""


def reverse(input_arr: str) -> str:
    """reverses a given string."""
    reverse_str = ""

    def reverser(input_arr: str, reverse_str: str):
        if len(input_arr) == 0:
            return reverse_str
        else:
            last_letter = input_arr[len(input_arr) - 1]
            reverse_str = reverse_str + last_letter
            return reverser(input_arr=input_arr[:-1], reverse_str=reverse_str)

    return reverser(input_arr=input_arr, reverse_str=reverse_str)
