"""
Write a function called reverse, it accpets a string and reverses it. 
Example: "Sumeet" = "teemuS"
"""

def reverse(input:str) -> str:
    reverse_str = ""
    def reverser(input: str, reverse_str: str):
        if len(input) == 0:
            return reverse_str
        else:
            last_letter = input[len(input) - 1]
            reverse_str = reverse_str + last_letter
            return reverser(input=input[:-1], reverse_str=reverse_str)
    
    return reverser(input=input, reverse_str=reverse_str)
