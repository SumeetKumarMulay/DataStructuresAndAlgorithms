"""
Write an function which accepts a list of integers and then sorts it from lowest to highest. 
The values should "bubble up" to the top. 
"""


def bubble_sort(input: list[int]) -> list[int]:
    """
    Sorts a given array from the smallet to the larges value.

    Args:
        input (list[int]): input array

    Returns:
        list[int]: input list.
    """

    for i in range(len(input)):
        for j in range(0, len(input) - i - 1):
            if input[j] > input[j + 1]:
                temp = input[j]
                input[j] = input[j + 1]
                input[j + 1] = temp

    return input


def bubble_sort_v2(input: list[int]) -> list[int]:
    """
    The logic is same as above but written using recursion. 

    Args:
        input (list[int]): The list which needs to be sorted.

    Returns:
        list[int]: returns a sorted list.
    """
    count = len(input) - 1
    pointer_1 = 0

    def compaier_loop(inp: list[int]) -> list[int]:
        nonlocal pointer_1
        if pointer_1 == len(inp):
            pointer_1 = 0
            return inp

        if pointer_1 < len(inp) - 1:
            if inp[pointer_1] > inp[pointer_1 + 1]:
                temp = inp[pointer_1]
                inp[pointer_1] = inp[pointer_1 + 1]
                inp[pointer_1 + 1] = temp

        pointer_1 += 1
        return compaier_loop(inp=inp)

    def looper(ip: list[int]) -> list[int]:
        nonlocal count
        if count == 0:
            return ip

        count -= 1
        return looper(ip=compaier_loop(inp=ip))

    return looper(ip=input)
