def isPalendrone(input: str) -> bool:
    reverse_str: str = ""

    def reverser(input: str) -> str:
        nonlocal reverse_str
        if len(input) == 0:
            return reverse_str
        else:
            last_letter = input[len(input) - 1]
            reverse_str = reverse_str + last_letter
            return reverser(input=input[:-1])

    reversed_str = reverser(input=input)
    return input == reversed_str
