"""
This is a naive approach to string. 
Write a function which accepts two strings. Find the number of times the second string appears
in the first one and return the count.
"""


def NaiveStringSearchV1(first_str: str, second_str: str) -> int:
    match = 0

    pointer1 = 0
    pointer2 = 0

    length_second_str = len(second_str) - 1
    length_first_str = len(first_str) - 1

    while pointer1 <= length_first_str:
        if pointer2 <= length_second_str:
            if first_str[pointer1] == second_str[pointer2]:
                if pointer2 == length_second_str:
                    match += 1
                    pointer2 = 0
                    pointer1 += 1
                else:
                    pointer1 += 1
                    pointer2 += 1
            else:
                pointer1 += 1
                pointer2 += 1
        else:
            pointer2 = 0
    return match

def NaiveStringSearchV2(first_str: str, second_str: str) -> int: 
    match = 0

    window_side_a = 0
    window_side_b = len(second_str)

    while window_side_b <= len(first_str):
        if second_str == first_str[window_side_a: window_side_b]: 
            match += 1
            window_side_a += 1
            window_side_b += 1
        else: 
            window_side_a += 1
            window_side_b += 1

    return match
