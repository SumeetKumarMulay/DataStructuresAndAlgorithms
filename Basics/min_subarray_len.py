"""
Write a function called minsub_arrayLen which accepts two parameter an array of positive integer
The function should return the min lenght of a contigeous sub_array of which the sum is greate 
or equal to integers passed into the function. If there isnt one Return 0
"""


def sum_rec(input_list: list[int]):
    """a recursive sum function"""
    if not input_list:
        return 0
    else:
        return input_list[0] + sum_rec(input_list=input_list[1:])


def min_sub_array_len(input_list: list[int], value: int) -> int:
    """
    NOTE - The problem with this approach is that it is not efficient. o(n)^2
    """
    window_size = 0

    if len(input_list) == 0:
        return 0

    while window_size < len(input_list):
        window_side_a = 0
        window_side_b = window_size + 1
        for v in input_list:
            sub_list = input_list[window_side_a:window_side_b]
            sum_arr = sum_rec(input_list=sub_list)
            if sum_arr >= value:
                return len(sub_list)
            else:
                window_side_a += 1
                window_side_b += 1
        window_size += 1
    return 0
