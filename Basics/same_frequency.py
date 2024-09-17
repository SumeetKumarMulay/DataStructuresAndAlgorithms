"""
write a function that accepts two positive integers. Find out if the two numbers have the same
frequency of digits. 
"""


def count_str(value: str):
    """just a small break down of the below function"""
    if not value:
        return 0
    else:
        return 1 + count_str(value[1:])


def same_frequency(value1: int, value2: int) -> bool:
    """checks if same frequency"""
    str_value1 = str(value1)
    str_value2 = str(value2)

    no_value1 = count_str(str_value1)
    no_value2 = count_str(str_value2)

    if no_value1 == no_value2:
        return True
    else:
        return False
    