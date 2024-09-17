"""
Write a function that takes a list of intergers. The function should find a list 
of two values who's some is zero and put them into another list and return it. If there 
are not values in the list who's sum is equal to zero then the function should return 
undefined. 
"""


def sum_zero(input_arr: list) -> list[int]:
    """the standard sorting method is list o(n) so the function is o(n)"""
    sorted_input = sorted(input_arr) if input_arr else []
    if sorted_input:
        pointer_left: int = 0
        pointer_right: int = len(sorted_input) - 1
        check_sum = sorted_input[pointer_left] + sorted_input[pointer_right]
        if check_sum == 0:
            return [sorted_input[pointer_left], sorted_input[pointer_right]]
        elif check_sum > 0:
            sorted_input.pop(pointer_right)
            return sum_zero(input_arr=sorted_input)
        elif check_sum < 0:
            sorted_input.pop(pointer_left)
            return sum_zero(input_arr=sorted_input)
        else:
            return None
    else:
        return None


result = sum_zero(
    input_arr=[
        -56,
        32,
        -27,
        78,
        -92,
        3,
        45,
        -17,
        -63,
        71,
        -84,
        25,
        -5,
        97,
        -32,
        66,
        -42,
        15,
        -75,
        89,
        28,
        -10,
        54,
        -67,
        41,
        93,
        -22,
        -8,
        7,
        -52,
        61,
        -37,
        23,
        -98,
        47,
        -1,
        82,
        -4,
        57,
        -73,
        38,
        -24,
        13,
        -94,
        53,
        -68,
        43,
        95,
        -26,
        -9,
        6,
        -51,
        60,
        -36,
        22,
        -99,
        48,
        -2,
        83,
        -5,
        58,
        -74,
        39,
        -25,
        14,
        -96,
        55,
        -69,
        44,
        96,
        -27,
        -11,
        8,
        -50,
        59,
        -35,
        21,
        -100,
        49,
        -3,
        84,
        -54,
        62,
        -38,
        24,
        -97,
        56,
        -70,
        40,
        91,
        -28,
        -12,
        9,
        -49,
        58,
        -34,
        20,
    ]
)
