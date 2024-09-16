"""
This is a naive approach to string. 
Write a function which accepts two strings. Find the number of times the second string appears
in the first one and return the count.
"""

"""
In this approach we have are going to look at each individual alphabet from both strings. if the 
squence of alphabets in the second matches the sequence of string in the first we increment match
by 1 else we continue till we have looped over the first string once. Once we have looped over we
return the match values. 

If there where same sequence of letters of the second string in the first one then match should be 
greater than 0. else it will be 0. The Time complexity should be o(n * M) considering the we loop over
the first string once and its lenght determines the time taken for the loop to finish. 
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


"""
In the second approach we are going to use a window and splice the first string and compaire that
with the second string. This should reduce code complexity and space complexity but time complexity 
remains the same i.e. o(n * M).

"""


def NaiveStringSearchV2(first_str: str, second_str: str) -> int:
    match = 0

    window_side_a = 0
    window_side_b = len(second_str)

    while window_side_b <= len(first_str):
        if second_str == first_str[window_side_a:window_side_b]:
            match += 1
            window_side_a += 1
            window_side_b += 1
        else:
            window_side_a += 1
            window_side_b += 1

    return match
